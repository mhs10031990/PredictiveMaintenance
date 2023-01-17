import streamlit as st
import pandas as pd
import requests
import json

# @st.experimental_memo
def binary_model(payload):
    
    headers={"Content-type":"application/json"}
    url = 'http://svc-d11ca779-f674-41c6-bb52-9e5f12a99c91:5001/predictivemaintenancebinaryclassification/d95dd4be-44d5-4952-8e14-0a5dc251f403/score'
    data={"payload" : str(payload)}
    response_json = requests.post(url, json=data, headers=headers)
    st.text_input("API Response: ",response_json.content)
    response = response_json.json()
    try:
        return response['upload_logging_data']['response_data']
    except ValueError:
        return response.status_code 

def multi_model(payload):
    
    headers={"Content-type":"application/json"} 
    url = 'http://svc-837f7bd0-4e0d-4297-9eb8-601e62b35355:5001/predictivemaintenancemulticlassification/507ec252-be83-43ff-a235-152e09433d59/score'
    data={"payload":str(payload)}
    response_json = requests.post(url, json=data, headers=headers)
    st.text_input("API Response: ",response_json.content)
    response = response_json.json()
    try:
        return response['upload_logging_data']['response_data']
    except ValueError:
        return response.status_code