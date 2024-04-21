<h1 align="center" id="title">"LinkedInfluencers" Detector: Leveraging Influencers on LinkedIn for Online Course Promotion – A Project Overview</h1>

<p id="description">In this project, we explore the integration of influencer marketing strategies within the professional networking platform, LinkedIn. With the rapid expansion of digital marketing and the emergence of influencers as key promoters, we delve into the realm of "LinkedInfluencers" – influential users within the LinkedIn community. Our objective is to devise a model capable of detecting potential influencers and recommending domain-related online courses for them to promote.</p>

<ins>Two Central Research Questions</ins>:<br>
•	Does the user possess the attributes indicative of an influencer?<br>
•	If so, what online courses align with their domain expertise and interests?<br>

<ins>Key Objectives</ins>:<br>
•	Develop a predictive model to identify users with the potential to become "LinkedInfluencers."<br>
•	Propose a strategy for recommending online courses tailored to the expertise and interests of identified influencers.<br>

<ins>Significance</ins>:<br>
•	Enhance user engagement with online courses through targeted promotion by influencers.<br>
•	Potentially increase revenue streams for LinkedIn through enhanced course enrollments.<br>

This project serves as an exploration into the fusion of influencer marketing and LinkedIn platform. Through our findings and methodologies, we aim to provide insights and innovative approaches to digital marketing and user engagement for the marketers of the platform.

<h2>⭐UI</h2>
<p id="description">Our project extends beyond predictive modeling; we have built a streamlined user interface (UI) using Streamlit. This UI provides an intuitive platform for users to interact with our predictive model. Through the UI, users can input LinkedIn profiles, allowing the model to analyze their attributes and determine their potential as influencers. Furthermore, the UI offers personalized course recommendations based on the user's expertise and interests.</p>
Link to the app: https://linkedinfluencerdetector.streamlit.app/ <br>
You can use the small_df.csv as an input example to the app from our drive storage (link in the report).
<h3>🚀 Demo</h3>

![project mockup](https://github.com/maayan-aytek/linkedInfluencer_detector/assets/81248290/6bb08045-b492-4acd-99ea-955de5c8c3af)
<h2>🛠️ Installation Steps for running local</h2>

<p>1. Clone the GitHub repository:</p>

```
git clone https://github.com/maayan-aytek/linkedInfluencer_detector.git
```

<p>2. Install the required packages using pip:</p>

```
pip install -r requirements.txt
```

<p>3. Once all dependencies are installed you can run the Streamlit app:</p>

```
streamlit run app.py
```
<h2>💻The scraping process</h2>
<p id="description">As part of our project, we conducted extensive web scraping. We added two new features, the binary influencer label column and the number of connections feature, to the existing scraping code provided by BrightData. We utilized BrightData's scraping platform to create our scraper.<br>Within the scraper, we defined the output schema to include both features as numeric values and added the necessary code to access the relevant HTML tags. Once everything was set up, we uploaded a CSV file containing user URLs and ran the code.</p>
<p id="description">Overall, we generated three different scraped tables. The first table was created by simply uploading all the profile URLs without considering the consequences. Unfortunately, we only found four influencers out of 250,000 records. For the second and third tables, we approached the scraping process more strategically by inputting a sorted list of URLs based on the number of followers. The resulting data sets are as follows: .</p>

•	inital_scraped_data.csv: Contains approximately 250,000 records with only 4 influencers identified.<br>
•	9000_scraped_data.csv: Contains approximately 9,000 records with 40 identified influencers.<br>
•	8000_scraped_data.csv: Contains approximately 8,000 records with 3 identified influencer<br>

<h2>🔍The code files</h2>
<p>1. data_loading_and_EDA.ipynb- notebook for loading the scraped data and process it, preform EDA and eventually undersampling.</p> 
<p>2. oversampling.ipynb- notebook for preforming oversampling using gemini API.</p> 
<p>3. modeling.ipynb- notebook for model preparation and model selection.</p> 
<p>4. full_pipleline.py- script for inference. Preparing data for modeling and predict the probability for is_influencer.</p>
<p>4. app.py- streamlit app code.</p>

