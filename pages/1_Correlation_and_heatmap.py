import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.title('Heatmap and Pairplot')


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

# st.write(df_cars.unique())


# Afficher le describe
# df_cars.describe(include="all")

# Heatmap
df_filtered["continent_id"] = pd.factorize(df_filtered["continent"])[0]
df_cars_to_corr = df_filtered[["mpg", "cylinders", "cubicinches", "hp", "weightlbs", "time-to-60", "year"]]
viz_correlation = sns.heatmap(df_cars_to_corr.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True),
                                annot=True
								)
plt.xticks(rotation=45)

st.pyplot(viz_correlation.figure)

df_cars_to_pair = df_filtered[["mpg", "cylinders", "cubicinches", "hp", "weightlbs","continent"]]
# Pairplot
viz_pairplot = sns.pairplot(df_cars_to_pair, hue="continent")

st.pyplot(viz_pairplot.figure)