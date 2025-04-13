import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')
df['manufacturer'] = df['model'].apply(lambda x:x.split()[0])

# Convert all numeric columns to PyArrow-friendly types
def fix_arrow_types(df):
    for col in df.select_dtypes(include=['int64']).columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').astype('Int64')  # Capital I - nullable integer
    return df

#df = fix_arrow_types(df.copy())
df['price'] = df['price'].astype(float)  # Add this before plotting
df['model_year'] = df['model_year'].astype(float)  # Also convert model_year to be safe

# create a text header above the dataframe
st.header('Data viewer') 
# display the dataframe with streamlit
st.dataframe(df)

st.header('Vehicle types by manufacturer')
# create a plotly histogram figure
fig = px.histogram(df, x='manufacturer', color='type')
# display the figure with streamlit
st.write(fig)

st.header('Histogram of `condition` vs `model_year`')
fig = px.histogram(df, x='model_year', color='condition')
st.write(fig)
