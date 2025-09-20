# CORD-19 Data Explorer**

This project analyzes a sample of COVID-19 research papers from the CORD-19 metadata dataset. It includes data cleaning, exploration, visualization, and an interactive Streamlit dashboard.

## 📂 Project Structure**

week8/ │── app.py # Streamlit app 
       │── requirements.txt # Python dependencies 
       │── README.md # Project documentation

Code

> ⚠️ **Note:** The `metadata.csv` file is too large to include in this repository.  
> Please download it manually from [CORD-19 on Kaggle](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)  
> and place it inside the `week8/` folder before running the app.

## 🚀 Features**

- Load and sample metadata from COVID-19 research papers  
- Clean and prepare data for analysis  
- Visualize publication trends, top journals, and title keywords  
- Interactive filters for year range and data preview  
- Word cloud generation from paper titles  
- Streamlit app for sharing insights  

## 🛠️ Tools Used**

- Python 3.7+  
- pandas  
- matplotlib  
- seaborn  
- wordcloud  
- Streamlit  
- Jupyter Notebook  

## 📊 How to Run**

### 1. Clone the repository**
```bash
git clone https://github.com/your-username/Frameworks_Assignment.git
cd Frameworks_Assignment/week8

## 2. Create and activate a virtual environment
bash
python -m venv venv
venv\Scripts\activate  # Windows
****3. Install dependencies
bash
pip install -r requirements.txt
****4. Download the dataset
Go to CORD-19 on Kaggle

Download metadata.csv

Place it inside the week8/ folder

****5. Run the Streamlit app
bash
streamlit run app.py
## 🧠 Reflection
This project explored 5,000 COVID-19 research papers from the CORD-19 metadata. It involved handling missing data, extracting publication years, and visualizing key trends. The Streamlit app provides an interactive way to explore the dataset.

Skills Developed
Data manipulation with pandas

Visualization using matplotlib, seaborn, and wordcloud

Building interactive dashboards with Streamlit
