import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import numpy as np
import chart_studio.plotly as py
import chart_studio.tools as tls
import plotly.graph_objs as go
import plotly.express as px
import streamlit_option_menu as option_menu

with open("styles.css") as source_style:
    st.markdown(f"<style>{source_style.read()}</style>",
                unsafe_allow_html=True)


with st.sidebar:
  selected = option_menu.option_menu(menu_title="Main Menu", options=["Home", "EDA"])

if selected == "Home":
  st.markdown("""<div style="line-height: 1.4; letter-spacing: 0.3px"> PREDICTIVE ANALYTICS AND EARLY DISEASE DETECTION USING MACHINE LEARNING MODELS </div>""",
                unsafe_allow_html=True)
  
  st.markdown('\n')

  st.subheader('INTRODUCTION:')

  st.markdown('The World Health Organization (WHO) states that cardiovascular diseases cause 12 million deaths each year, making them a leading cause of death in the world. Despite the technological advances in medicine, the ability to predict CVD early and accurately remains a significant challenge. Heart disease encompasses a variety of cardiovascular disorders, including coronary artery disease, arrhythmias, and congenital heart defects. Given its pervasive impact on global mortality, early and accurate prediction mechanisms are essential. Machine learning (ML) has emerged as a transformative approach in healthcare, particularly in identifying complex relationships within large datasets. This study evaluates the performance of ML models in predicting heart disease, providing a comparative analysis to determine the most effective approach.')

  st.markdown('\n')
  
  st.subheader('THE PROBLEM STATEMENT:')

  st.markdown('CVD often presents itself silently, which is referred to as "silent killers." The existing diagnostic systems are either inaccessible or incapable of predicting early onset. Despite advancements in medical diagnostics, the accurate and timely prediction of heart disease remains a challenge. Conventional techniques often rely on subjective assessments, which may lead to delays in treatment or misdiagnosis. Therefore, there is a pressing need for automated, data-driven methods to enhance predictive accuracy and reliability in heart disease detection. ML in healthcare can bridge this gap by analyzing large datasets and discovering hidden patterns that point towards heart disease.')

  st.markdown('\n')
  
  st.subheader('THE PROJECT GOALS:')

  st.markdown('To preprocess and analyze the Heart Disease dataset - Indicators of Heart Disease.')
   st.markdown('To implement and evaluate five machine learning algorithms.')
  st.markdown('To identify the most effective algorithm for heart disease prediction based on performance metrics.')
elif selected == "EDA":
  st.markdown("""<h style = " "> Exploratory Data Analysis </h>""", unsafe_allow_html = True)
 
  st.sidebar.subheader("Visualisation Settings")


  chart_select = st.sidebar.selectbox(
    label = "Select the Data",
    options = ['Heart Disease dataset']
  )
  if chart_select == 'Heart Disease dataset':
      df = pd.read_csv('HeartDiseasedataset.csv')
      st.subheader('HeartDiseasedataset')   
  show_data = st.sidebar.checkbox("Show dataset")

  if show_data:
    st.write(df)

  global numeric_columns
  try:
    numeric_columns  = list(df.select_dtypes(['float','int' ]).columns)
  except Exception as e:
    print(e)
    


  chart_select = st.sidebar.selectbox(
    label = "Select the Chart Type",
    options = ['Scatterplots', 'Lineplots', 'Histogram', 'Boxplot']
  )

  if chart_select == 'Scatterplots':
    st.sidebar.subheader('Scatterplot Settings')
    try:
        x_values = st.sidebar.selectbox('X axis', options = numeric_columns)
        y_values = st.sidebar.selectbox('Y axis', options = numeric_columns)
        plot = px.scatter(data_frame = df, x = x_values, y = y_values)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

  if chart_select == 'Lineplots':
    st.sidebar.subheader('Lineplots Settings')
    try:
        x_values = st.sidebar.selectbox('X axis', options = numeric_columns)
        y_values = st.sidebar.selectbox('Y axis', options = numeric_columns)
        plot = px.area(data_frame = df, x = x_values, y = y_values)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

  if chart_select == 'Boxplot':
    st.sidebar.subheader('Boxplot Settings')
    try:
        x_values = st.sidebar.selectbox('X axis', options = numeric_columns)
        y_values = st.sidebar.selectbox('Y axis', options = numeric_columns)
        plot = px.box(data_frame = df, x = x_values, y = y_values)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

  if chart_select == 'Histogram':
    st.sidebar.subheader('Histogram Settings')
    try:
        x_values = st.sidebar.selectbox('Select the variable to plot histogram', options = numeric_columns)
        bins = st.sidebar.slider("Select the number of bins", min_value=5, max_value=50, value=20, step=1)
        plot = px.histogram(data_frame = df, x = x_values, nbins=bins)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)
elif selected == "EDA 2":
  st.markdown("""<h style = " "> Exploratory Data Analysis </h>""", unsafe_allow_html = True)
 
  st.sidebar.subheader("Visualisation Settings")


  chart_select = st.sidebar.selectbox(
    label = "Select the Data",
    options = ['Heart Disease dataset']
  )
  if chart_select == 'Heart Disease dataset':
      df = pd.read_csv('HeartDiseasedataset.csv')
      st.subheader('HeartDiseasedataset')
  if show_data:
    st.write(df)

  
  try:
    numeric_columns  = list(df.select_dtypes(['float','int' ]).columns)
  except Exception as e:
    print(e)
  chart_select = st.sidebar.selectbox(
    label = "Select the Chart Type",
    options = ['Scatterplots', 'Lineplots', 'Histogram', 'Boxplot']
  )
  if chart_select == 'Scatterplots':
    st.sidebar.subheader('Scatterplot Settings')
    try:
        print("hi")
    except Exception as e:
        print(e)
  

