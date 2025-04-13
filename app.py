import streamlit as st
import pandas as pd
import plotly.express as px

# Load and prepare data
df = pd.read_csv('vehicles_us.csv')
df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])

# Convert numeric columns to compatible types
numeric_cols = ['price', 'days_listed', 'model_year']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')  # Convert to float, set invalid as NaN
df = df.dropna(subset=numeric_cols)  # Remove rows with missing numeric values

# Data Viewer
st.header('Data viewer')
st.dataframe(df)

# Vehicle Types by Manufacturer
st.header('Vehicle types by manufacturer')
fig = px.histogram(df, x='manufacturer', color='type')
st.write(fig)

# Condition vs Model Year
st.header('Histogram of `condition` vs `model_year`')
fig = px.histogram(df, x='model_year', color='condition')
st.write(fig)

# Price Comparison
st.header('Compare price distribution between manufacturers')
manufac_list = sorted(df['manufacturer'].unique())

manufacturer_1 = st.selectbox(
    'Select manufacturer 1',
    options=manufac_list,
    index=manufac_list.index('chevrolet')
)

manufacturer_2 = st.selectbox(
    'Select manufacturer 2',
    options=manufac_list, 
    index=manufac_list.index('hyundai')
)

# Filter and plot
df_filtered = df[df['manufacturer'].isin([manufacturer_1, manufacturer_2])
normalize = st.checkbox('Normalize histogram', value=True)

fig = px.histogram(
    df_filtered,
    x='price',
    nbins=30,
    color='manufacturer',
    histnorm='percent' if normalize else None,
    barmode='overlay'
)
st.write(fig)
