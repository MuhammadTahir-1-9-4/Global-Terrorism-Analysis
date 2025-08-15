import streamlit as st
import plotly.express as px
from preprocessor import load_and_clean_data # custom preprocessing function

# page configuration
st.set_page_config(
    page_title='Global Terrorism Analysis',
    page_icon = '💣',
    layout='wide'
)

# data loading
@st.cache_data(show_spinner=False)
def get_data():
    return load_and_clean_data()

df = get_data()

# Main Application
st.title("🌍 Global Terrorism Analysis Dashboard")
st.markdown("This dashboard provides an interactive analysis of global terrorism data from 1970 to 2017.")

# sidebar for user input
st.sidebar.header("Filter Options")
analysis_choice = st.sidebar.radio(
    "Choose Analysis Type",
    ('Overall Analysis', 'Country-wise Analysis', "Region-wise Analysis", "Year-wise Analysis")
)

# display data bsed on analysis choice
st.header(f"{analysis_choice}")

if analysis_choice == 'Overall Analysis':
    st.subheader("Key Metrics")
    total_attacks = len(df)
    total_casualities = int(df['Casualties'].sum())
    total_countries = df['Country'].nunique()

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Attacks", f"{total_attacks:,}")
    col2.metric("Total Casualties", f"{total_casualities:,}")
    col3.metric("Countries Affected", total_countries)

    st.subheader("Number of Attacks Over Time")
    attacks_over_time = df['Year'].value_counts().sort_index()
    fig = px.line(attacks_over_time, x=attacks_over_time.index, y=attacks_over_time.values,
                  labels={'x': 'Year', 'y': 'Number of Attacks'},
                  title="Annual Number of Terrorist Attacks Worldwide")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Top 10 Most Affected Countries")
    top_countries = df['Country'].value_counts().nlargest(10)
    fig2 = px.bar(top_countries, x=top_countries.index, y=top_countries.values,
                  labels={'x': 'Country', 'y': 'Number of Attacks'},
                  title='Top 10 Countries by Number of Attacks')
    st.plotly_chart(fig2, use_container_width=True)

elif analysis_choice == 'Country-wise Analysis':
    st.subheader("Explore Data by Country")
    # sort country list alphabetically
    country_list = sorted(df['Country'].unique())
    country = st.sidebar.selectbox(
        "Select a Country",
        country_list
    )

    country_df = df[df['Country'] == country]

    st.subheader(f"Attack Trends in {country}")
    country_attacks_over_time = country_df['Year'].value_counts().sort_index()
    fig = px.line(country_attacks_over_time, x=country_attacks_over_time.index, y=country_attacks_over_time.values,
                  labels={'x': 'Year', 'y': 'Number of Attacks'},
                  title=f'Annual Attacks in {country}')
    st.plotly_chart(fig, use_container_width=True)

    st.subheader(f"Most Common Attack Types in {country}")
    attack_types = country_df['AttackType'].value_counts().nlargest(5)
    fig2 = px.pie(values=attack_types.values,
                  names=attack_types.index,
                  title=f"Top 5 Attack Types in {country}")
    st.plotly_chart(fig2, use_container_width=True)

elif analysis_choice == 'Region-wise Analysis':
    st.subheader("Explore Data by Region")
    # sort region list alphabetically
    region_list = sorted(df['Region'].unique())
    region = st.sidebar.selectbox(
        "Select a Region",
        region_list
    )

    region_df = df[df['Region'] == region]

    st.subheader(f"Attack Trends in {region}")
    region_attacks_over_time = region_df['Year'].value_counts().sort_index()
    fig = px.area(region_attacks_over_time, x=region_attacks_over_time.index, y=region_attacks_over_time.values,
                 labels={'x':'Year', 'y':'Number of Attacks'},
                 title=f"Annual Attacks in {region}")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader(f"Most Affected Countries in {region}")
    region_country_counts = region_df['Country'].value_counts().nlargest(10)
    fig2 = px.bar(region_country_counts, y=region_country_counts.index, x=region_country_counts.values,
                  orientation='h',
                  labels={'y':'Country', 'x':'Number of Attacks'},
                  title=f"Top 10 Affected Countries in {region}")
    st.plotly_chart(fig2, use_container_width=True)
    

elif analysis_choice == 'Year-wise Analysis':
    st.subheader("Explore Data by Year")
    year = st.sidebar.slider(
        "Select a Year",
        int(df['Year'].min()),
        int(df['Year'].max()),
        int(df['Year'].min()) # default value
    )

    year_df = df[df['Year'] == year]

    st.subheader(f"Geographical Distribution of Attacks in {year}")
    # the map requires latitude and logitude, drop rows where these are missing for the selected year
    year_df_map = year_df.dropna(subset=['latitude', 'longitude'])
    if not year_df_map.empty:
        st.map(year_df_map)
    else:
        st.warnign(f"No attack data with geographical coordinates available for the year {year}.")

    st.subheader(f"Top 5 Regions by Number of Attacks in {year}")
    year_region_counts = year_df['Region'].value_counts().nlargest(5)
    fig = px.pie(values=year_region_counts.values, names=year_region_counts.index,
                 title=f"Attack Distribution by Region in {year}")
    st.plotly_chart(fig, use_container_width=True)