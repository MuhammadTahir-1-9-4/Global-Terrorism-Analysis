# 💣 GTD-Insight: An Interactive Global Terrorism Analysis Dashboard

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)![Streamlit](https://img.shields.io/badge/Streamlit-1.48-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)![Pandas](https://img.shields.io/badge/Pandas-2.3-150458?style=for-the-badge&logo=pandas&logoColor=white)![Plotly](https://img.shields.io/badge/Plotly-6.32-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)

An interactive web application for analyzing the Global Terrorism Database (GTD). This dashboard provides a comprehensive interface to explore trends, patterns, and statistics of worldwide terrorism incidents from 1970 to 2017.

---

## ✨ Live Demo

### [**>> Try the live app here! <<**]([https://global-terrorism-analysis.streamlit.app/])


![GTD Insight Demo GIF](demo.gif)

---

## 🚀 Features

- **High-Level Metrics:** Instantly view key statistics like total attacks, casualties, and countries affected.
- **Dynamic Filtering:** Analyze data by specific Year, Region, or Country using interactive sidebar controls.
- **Temporal Analysis:** Visualize the frequency of attacks over time to identify key historical periods of activity.
- **Geographical Insights:** Explore the spatial distribution of attacks on an interactive world map, with points sized by casualty count.
- **Deep Dives:** Investigate country-specific trends, common attack types, and the most active terrorist groups.

---

## 🛠️ Tech Stack & Methodology

This project is an end-to-end demonstration of a data analysis workflow, from cleaning a large dataset to deploying an interactive web application.

- **Data Source:** The project utilizes the [Global Terrorism Database (GTD)](https://www.kaggle.com/datasets/START-UMD/gtd), a comprehensive open-source database of over 180,000 terrorist attacks.
- **Data Cleaning & Preprocessing:**
  - A dedicated preprocessing script was developed to handle the raw 155 MB dataset.
  - **Column Selection:** Out of 135 columns, only 15 relevant columns were selected to optimize performance.
  - **Data Consolidation:** A significant data quality issue was addressed by mapping historical country names (e.g., `West Germany (FRG)`, `Soviet Union`) and non-sovereign territories to their modern equivalents, reducing the unique country count from 205 to a more accurate 184.
  - **Feature Engineering:** A `Casualties` column was created by combining the `Killed` and `Wounded` columns.
- **Visualization & Frontend:**
  - The entire user interface is built with **Streamlit**, a Python framework for building data apps.
  - Interactive charts (line, bar, pie) and the world map are powered by **Plotly Express** for a rich user experience.
- **Deployment:**
  - The application is deployed on **Streamlit Cloud**, which is connected directly to this GitHub repository for continuous integration.

---

## 💻 Running the Project Locally

To run this project on your own machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/MuhammadTahir-1-9-4/Global-Terrorism-Analysis.git
    cd Global-Terrorism-Analysis
    ```

2.  **Set up a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```
    The application should now be running in your local web browser!

---

## 👤 Contact

Muhammad Tahir - [LinkedIn]([https://www.linkedin.com/in/muhammad-tahir-data/])