import pandas as pd
import streamlit as st
st.set_page_config(page_icon = 'logo.png', layout='centered', initial_sidebar_state = 'collapsed', page_title='Census Data')
@st.cache()
def load_data():
	df = pd.read_csv('https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/adult.csv', header=None)
	df.head()
	column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 'relationship', 'race',
	'gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']
	for i in range(df.shape[1]):
	  df.rename(columns={i:column_name[i]},inplace=True)
	df.head()
	df['native-country'] = df['native-country'].replace(' ?',np.nan)
	df['workclass'] = df['workclass'].replace(' ?',np.nan)
	df['occupation'] = df['occupation'].replace(' ?',np.nan)
	df.dropna(inplace=True)
	df.drop(columns='fnlwgt',axis=1,inplace=True)
	return df
df = load_data()
st.header('Census Data')

if st.checkbox('Show data\'s first 5 rows'):
	st.table(df.head())
	st.write(f'Size of dataset: {df.shape[0]} rows and {df.shape[1]} columns')
if st.checkbox('Show data (It may take some time to load)'):
	st.table(df)
	st.write(f'Size of dataset: {df.shape[0]} rows and {df.shape[1]} columns')
