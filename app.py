# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 09:35:22 2023

@author: barry
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 07:12:47 2023

@author: barry
"""

import time #for time loops
import numpy as np #probability functions
import pandas as pd
import plotly.express as px # interactive charts
import streamlit as st #web development


# Create a container for the chart
container = st.container()

# Define the CSS styles to center the heading
heading_style = """
    display: flex;
    justify-content: center;
    align-items: center;
"""

# Add the chart to the container with a centered heading
#with container:
    #st.write("# My Chart Heading", unsafe_allow_html=True, 
             #style=heading_style)
    #st.line_chart(my_data)


#read csv file from a url
dataset_url = "C:/Users/barry/.spyder-py3/test2/processed_cleveland_simple.csv"

@st.cache()

def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url)

df = get_data()


# dashboard title
st.title("Heart attack tracker")

# top-level filters
job_filter = st.selectbox("Select Age", pd.unique(df["age"]))

# creating a single-element container
placeholder = st.empty()

# dataframe filter
df = df[df["age"] == job_filter]

# near real-time / live feed simulation
for seconds in range(200):

    df["age_new"] = df["age"] * np.random.choice(range(1, 5))
    df["chol_new"] = df["chol"] * np.random.choice(range(1, 5))

    # creating KPIs
    avg_age = np.mean(df["age_new"])

    count_bldpress = int(
        df[(df["restbldpress"] == "restbldpress")]["restbldpress"].count()
        + np.random.choice(range(1, 30))
    )
    
    cholesterol= np.mean(df["chol_new"])

with placeholder.container():

      # create three columns
      kpi1, kpi2, kpi3 = st.columns(3)

      # fill in those three columns with respective metrics or KPIs
      kpi1.metric(
          label="Age ⏳",
          value=round(count_bldpress),
          delta=round(count_bldpress) - 10,
      )
      
      kpi2.metric(
          label="Cholesterol Levels ",
          value=int(cholesterol),
          delta=-10 + cholesterol,
      )
      
      kpi3.metric(
          label="Cholestorol Predictor",
          value=f" {round(cholesterol,2)} ",
          delta=-round( cholesterol/ count_bldpress) * 100,
      )

      # create two columns for charts
      fig_col1, fig_col2 = st.columns(2)
      # Add the chart to the container with a centered heading
      #with container:
          #st.write("# Life Expectancy", unsafe_allow_html=True, 
                   #style=heading_style)
          #st.line_chart(df)
      with fig_col1:
          st.markdown("### Life Expectancy")
          st.markdown("### *no change*")
          fig = px.density_heatmap(
              data_frame=df, y="age_new", x="restbldpress"
          )
          st.write(fig)
          
          with fig_col2:
           st.markdown("### Life Expectancy")
           st.markdown("### *with change*")
           fig2 = px.histogram(data_frame=df, x="age_new")
           st.write(fig2)

           st.markdown("### Detailed Data View")
           st.dataframe(df)
           time.sleep(1)



