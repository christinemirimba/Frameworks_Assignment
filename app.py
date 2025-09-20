# Data Loading and Basic Exploration
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from wordcloud import WordCloud
import re
from collections import Counter

# Load and sample the data
@st.cache_data
def load_data():
    df = pd.read_csv('metadata.csv', low_memory=False)
    # Load only the first 5000 rows
    df = df.head(5000)  
    return df

df = load_data()

# Data Cleaning and Preparation
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year
df['abstract'] = df['abstract'].fillna('')
df['title'] = df['title'].fillna('')
df['journal'] = df['journal'].fillna('Unknown')
df['source_x'] = df['source_x'].fillna('Unknown')
df['abstract_word_count'] = df['abstract'].apply(lambda x: len(x.split()))

# Data Analysis and Visualization
def plot_publications_by_year(data):
    year_counts = data['year'].value_counts().sort_index()
    fig, ax = plt.subplots()
    ax.bar(year_counts.index, year_counts.values, color='skyblue')
    ax.set_title('Publications by Year')
    ax.set_xlabel('Year')
    ax.set_ylabel('Number of Papers')
    st.pyplot(fig)

def plot_top_journals(data):
    top_journals = data['journal'].value_counts().head(10)
    fig, ax = plt.subplots()
    sns.barplot(x=top_journals.values, y=top_journals.index, ax=ax, palette='viridis')
    ax.set_title('Top Journals Publishing COVID-19 Research')
    ax.set_xlabel('Number of Papers')
    st.pyplot(fig)

def plot_wordcloud(data):
    text = ' '.join(data['title'].dropna().tolist())
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

def plot_source_distribution(data):
    source_counts = data['source_x'].value_counts()
    fig, ax = plt.subplots()
    source_counts.plot(kind='bar', ax=ax, color='coral')
    ax.set_title('Distribution of Paper Counts by Source')
    ax.set_xlabel('Source')
    ax.set_ylabel('Number of Papers')
    st.pyplot(fig)

# Streamlit Application
st.set_page_config(page_title="CORD-19 Data Explorer", layout="wide")
st.title("CORD-19 Data Explorer")
st.write("Explore COVID-19 research metadata from the CORD-19 dataset")

# Interactive filters
year_range = st.slider("Select publication year range", 2019, 2022, (2020, 2021))
filtered_df = df[df['year'].between(year_range[0], year_range[1])]

# Show sample data
st.subheader("Sample of Filtered Data")
st.dataframe(filtered_df[['title', 'journal', 'year', 'source_x']].head())

# Visualizations
st.subheader("Publications Over Time")
plot_publications_by_year(filtered_df)

st.subheader("Top Journals")
plot_top_journals(filtered_df)

st.subheader("Word Cloud of Paper Titles")
plot_wordcloud(filtered_df)

st.subheader("Source Distribution")
plot_source_distribution(filtered_df)

# Reflection
st.markdown("### Reflection")
st.markdown("""
This application analyzes a sample of 5,000 COVID-19 research papers from the CORD-19 metadata.
We explored publication trends, journal contributions, and title keywords.

**Key insights:**
- A surge in publications during 2020 and 2021
- Top journals contributing to COVID-19 research
- Frequent keywords in paper titles

**Challenges:**
- Handling missing and inconsistent data
- Optimizing performance for large datasets
- Designing clear and informative visualizations

**Skills developed:**
- Data manipulation with pandas
- Visualization using matplotlib, seaborn, and wordcloud
- Building interactive dashboards with Streamlit
""")
