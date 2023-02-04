import streamlit as st
import pandas as pd
import requests
import json

# @st.experimental_memo
def binary_model(payload):
    
    headers={"Content-type":"application/json"}
    url = 'http://svc-37bdffd0-efb5-4474-becc-5dc3185116a1:5001/predictivemaintenancebinaryclassification/074e09f2-dec7-4179-829f-05bdfdbc798a/score'
    data={"payload" : str(payload)}
    response_json = requests.post(url, json=data, headers=headers)
    #st.text_input("API Response: ",response_json.content)
    response = response_json.json()
    try:
        return response['upload_logging_data']['response_data']
    except ValueError:
        return response.status_code 

def multi_model(payload):
    
    headers={"Content-type":"application/json"} 
    url = 'http://svc-33df36f1-5b37-4b8b-995f-93562b2df15f:5001/predictivemaintenancemulticlassification/b6f10f20-e5b1-42f6-a9e2-de6a2a60b069/score'
    data={"payload":str(payload)}
    response_json = requests.post(url, json=data, headers=headers)
    #st.text_input("API Response: ",response_json.content)
    response = response_json.json()
    try:
        return response['upload_logging_data']['response_data']
    except ValueError:
        return response.status_code