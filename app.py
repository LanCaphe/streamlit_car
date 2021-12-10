import streamlit as st
import pymongo
#title
st.title('Find your dream car')

# Initialize connection.
client = pymongo.MongoClient(**st.secrets["mongo"])