import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.title('Boxplots')


link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)

with st.sidebar:
    options = st.multiselect(
        'Choose a region',
        [' US.', ' Europe.', ' Japan.'],
        [])
    
# st.write(options)
if len(options) != 0:
    df_filtered = df_cars[df_cars['continent'].isin(options)]
else:
    df_filtered = df_cars

# Boxplots
for columns in df_filtered:
        # print(columns)
        fig, ax = plt.subplots(figsize = (8,2))
        viz_boxplot = sns.boxplot(data=df_filtered, x =columns)
        st.pyplot(viz_boxplot.figure)
        

fig, ax = plt.subplots(figsize = (8,2))
# Histoplot
viz_histplot = sns.histplot(
    df_filtered, x="cylinders"
)

st.pyplot(viz_histplot.figure)