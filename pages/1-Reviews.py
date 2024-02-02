import pandas as pd
import sqlite3
import streamlit as st
import plotly.express as px

# Setup data
df = pd.read_csv("clean_dataset.csv")

# Make page
st.set_page_config(page_title="Olist Dataset")
st.header("Olist Dataset")
st.markdown("Etude du review score")
# st.sidebar.header("Review score")

show_df = df.filter(items=["review_score"])

plot = px.histogram(
    show_df,
    x='review_score',
    title=f"Répartitions des notes clients",
    color="review_score"
)

st.plotly_chart(plot)

# On répartit les notes : en 2 groupes : de 0 à 4 et 5
df['score'] = df['review_score'].apply(lambda x : 1 if x==5 else 0)


st.markdown("On répartit les notes : en 2 groupes : de 0 à 4 et 5."
            "On regarde la répartition.")

# On définit l'histogramme
fig = px.histogram(df, x='score', color_discrete_sequence=['#636EFA'], labels={'score': 'Note obtenue'}, title='Distribution des notes attribuées aux commandes')

# On affiche les pourcentages
total = len(df['score'])

for i in range(2):
    count = len(df[df['score'] == i])
    percentage = f'{100 * count / total:.1f}%'
    fig.add_annotation(
        x=i,
        y=count + 1000,
        text=percentage,
        showarrow=True,
        font=dict(color='black')
    )

# Ajustez la mise en page
fig.update_layout(
    xaxis_title='Note obtenue',
    yaxis_title='Fréquence',
    xaxis=dict(tickmode='linear'),
    height=600,
    width=400
)

# Affichez le graphique
st.plotly_chart(fig)