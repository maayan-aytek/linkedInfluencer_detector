import ast
import pickle
import numpy as np
import pandas as pd
import streamlit as st
import google.generativeai as genai
from streamlit_extras.row import row
from sentence_transformers import SentenceTransformer

st.set_page_config(
    page_title="Influencer Detection",
    page_icon="🔍",
    layout="wide",
)

# Load the models
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
gemini_model = genai.GenerativeModel('gemini-pro')

def parse_complex_column(text):
    try:
        return ast.literal_eval(text)
    except (SyntaxError, ValueError):
        return None
    

def get_sentence_embedding(text):
    embedding = embedding_model.encode(text, convert_to_tensor=False)
    return np.array(embedding)


def string_to_embedding_feature(df, col):
    """
    Convert string column to embedding vector 
    """
    df[col] = df[col].astype(str).fillna(" ") # fill missing values 
    df[f'{col}_embedding'] = df[col].apply(get_sentence_embedding)
    pickle_in = open(f"pca_trained_{col}.pickle", "rb")
    pca_loaded = pickle.load(pickle_in)
    df_pca = pca_loaded.transform(np.stack(df[f'{col}_embedding']))
    df_pca = pd.DataFrame(df_pca, columns=[f'{col}_pca_{i+1}' for i in range(df_pca.shape[1])]).reset_index(drop=True)
    return df_pca


def pre_process(df, used_features):
    """
    Prepare df for modeling- split into X (features) and y (labels)
    """
    numeric_features = used_features['numeric']
    X = df[numeric_features].reset_index(drop=True)
    for text_col in used_features['textual']:
        df_pca = string_to_embedding_feature(df, text_col)
        X = pd.concat([X, df_pca], axis=1)
    return X


def prepare_data_for_modeling(df):
    """
    Features preprocessing
    """
    df['education'] = df['education'].apply(parse_complex_column)
    df['experience'] = df['experience'].apply(parse_complex_column)
    df['posts'] = df['posts'].apply(parse_complex_column)
    df['education_count'] = df['education'].apply(lambda x: len(x) if isinstance(x, list) else None)
    df['experience_count'] = df['experience'].apply(lambda x: len(x) if isinstance(x, list) else None)
    df['posts_count'] = df['posts'].apply(lambda x: len(x) if isinstance(x, list) else None)
    df['followers'] = df['followers'].astype(float)
    used_features = {'numeric': ['followers', 'posts_count', 'experience_count', 'education_count'], 'textual': ['about', 'position', 'recommendations']}
    X = pre_process(df, used_features)
    return X 


def run_and_predict_influencers(df):
    """
    Predict influencer label
    """
    X = prepare_data_for_modeling(df)
    pickle_model = open("trained_model.pickle", "rb")
    model_loaded = pickle.load(pickle_model)
    predictions = model_loaded.predict(X)
    df['predicted_influencer'] = predictions
    df['is_influencer_probability'] = model_loaded.predict_proba(X)[:, 1]
    influencers = df[df['predicted_influencer'] == 1]
    return influencers

def user_row_to_string(user_row):
    # Initialize an empty string to accumulate the information
    user_string = ""
    
    # Iterate over all items in the row dictionary
    for key, value in user_row.items():
        # Check if the value is a dictionary or list and convert to string accordingly
        if isinstance(value, dict) or isinstance(value, list):
            value_str = str(value)
        else:
            # For NaN or None, set a placeholder
            value_str = str(value) if value is not None else "N/A"
        
        # Append the key and value to the user string with formatting
        user_string += f"{key}: {value_str}\n"
    
    # Return the compiled user string
    return user_string

def match_user_course_category(user):
    genai.configure(api_key="AIzaSyA2UCE2Vk2vsG9UxzWJuNnxfnVHActKmzI")
    courses = pd.read_csv("Course Count by Category.csv")["Sub Category"].to_list()
    user_as_string = user_row_to_string(user)
    user_name = user['id']
    text_prompt = f"based on the following user features: \n {user_as_string} \n , recommend the user: {user_name},  which one category of courses will be the most suitable for it to advertise as an influencer, from the following list: {courses}. Explain the choice. The output should look like this: category (in bold) and in the next row the explanation"
    response = gemini_model.generate_content(text_prompt)
    text = response.text.replace('•', '*')
    st.markdown(text)

def display_influencers(data):
    # Display the influencers
    data['is_influencer_probability'] = data['is_influencer_probability'].apply(lambda x: round(x*100, 3))
    data['is_influencer_probability'] = data['is_influencer_probability'].astype(str) + '%'
    init_row = row(1)
    col1, col2 = init_row.columns(2)
    with col1:
        st.markdown('### :robot_face: The system detected the following potential influencers:')
    with col2:
        st.markdown('### :bulb: The system recommends these course categories for the influencers:')
    st.markdown('---')
    for i in range(len(data)):
        row1 = row(1)
        col1, col2 = row1.columns(2)
        with col1:
            st.markdown(f'**Influencer ID**: {data.iloc[i]["id"]}')
            st.markdown(f'**Influencer URL**: {data.iloc[i]["url"]}')
            st.markdown(f'**Influencer Probability**: {data.iloc[i]["is_influencer_probability"]}')
        with col2:
            match_user_course_category(data.iloc[i])
        st.markdown('---')
    
def main():
    # Title with linkedin logo (Linkedin_icon_circle.svg.png). make the color like the linkedin logo
    st.markdown('<h1 style="text-align: center; color: #0077B5;">LinkedInfluencer Detector</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center;"><img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="linkedin logo" width="100" height="100"></p>', unsafe_allow_html=True)
    
    # Upload the CSV file
    # change the color of the text in the file_uploader to be white
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        
        # Create a button to run the model
        if st.button('Run Model'):
            predicted_data = run_and_predict_influencers(data)
            predicted_data = predicted_data.sort_values(by='is_influencer_probability', ascending=False)
            display_influencers(predicted_data)

# Run the app
if __name__ == '__main__':
    main()