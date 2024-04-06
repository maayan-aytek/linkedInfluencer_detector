<h1 align="center" id="title">"LinkedInfluencers" Detector: Leveraging Influencers on LinkedIn for Online Course Promotion – A Project Overview</h1>

<p id="description">In this project, we explore the integration of influencer marketing strategies within the professional networking platform, LinkedIn. With the rapid expansion of digital marketing and the emergence of influencers as key promoters, we delve into the realm of "LinkedInfluencers" – influential users within the LinkedIn community. Our objective is to devise a model capable of detecting potential influencers and recommending domain-related online courses for them to promote.

Two Central Research Questions:
•	Does the user possess the attributes indicative of an influencer?
•	If so, what online courses align with their domain expertise and interests?

Key Objectives:
•	Develop a predictive model to identify users with the potential to become "LinkedInfluencers."
•	Propose a strategy for recommending online courses tailored to the expertise and interests of identified influencers.
•	Enhance user engagement with online courses through targeted promotion by influencers.
•	Potentially increase revenue streams for LinkedIn through enhanced course enrollments.

This project serves as an exploration into the fusion of influencer marketing and LinkedIn platform. Through our findings and methodologies, we aim to provide insights and innovative approaches to digital marketing and user engagement for the marketers of the platform.

<h2>UI</h2>
<p id="description"> Our project equipped with a user interface built on Streamlit aims to predict potential LinkedInfluencers and recommend domain-specific online courses for them to endorse optimizing engagement and revenue.</p>
Link to the app: https://linkedinfluencerdetector.streamlit.app/
<h3>🚀 Demo</h3>

![project mockup](https://github.com/maayan-aytek/linkedInfluencer_detector/assets/81248290/6bb08045-b492-4acd-99ea-955de5c8c3af)
<h2>🛠️ Installation Steps:</h2>

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
<h2>Explanations about the files:</h2>
<p>1. data_loading_and_EDA.ipynb- notebook for loading the scraped data and process it, preform EDA and eventually undersampling</p> 
<p>2. oversampling.ipynb- notebook for preforming oversampling using gemini API</p> 
