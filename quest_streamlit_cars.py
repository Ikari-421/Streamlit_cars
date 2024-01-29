import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.title('Hello Wilders, welcome to my application!')

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)

# Afficher le describe
df_cars.describe(include="all")


# Heatmap
df_cars["continent_id"] = pd.factorize(df_cars["continent"])[0]
df_cars_to_corr = df_cars[["mpg", "cylinders", "cubicinches", "hp", "weightlbs", "time-to-60", "year"]]
viz_correlation = sns.heatmap(df_cars_to_corr.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)
plt.xticks(rotation=45)

st.pyplot(viz_correlation.figure)

# Pairplot
sns.pairplot(df_cars, hue="continent")
plt.show()


# Boxplots
for columns in df_cars:
        # print(columns)
        fig, ax = plt.subplots(figsize = (8,2))
        sns.boxplot(data=df_cars, x =columns)
        plt.show()

# Histoplot
sns.histplot(
    df_cars, x="cylinders"
)
plt.show()


