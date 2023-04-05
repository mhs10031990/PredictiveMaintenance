import streamlit as st
import pandas as pd
import requests
import json

# @st.experimental_memo
def binary_model(payload):
    
    headers={"Content-type":"application/json"}
#     url = 'http://svc-1a0c7b69-afcc-4146-9444-9f19d15dee59-6fcd675fdc:5001/predictivemaintenancebinaryclassification/074e09f2-dec7-4179-829f-05bdfdbc798a/score'
    url = "https://refract.fosfor.com/predictivemaintenancebinaryclassification/074e09f2-dec7-4179-829f-05bdfdbc798a/score"
    data={"payload" : str(payload)}
    return payload
    response_json = requests.post(url, json=data, headers=headers)
    
    #st.text_input("API Response: ",response_json.content)
    response = response_json.json()
    try:
        return response['upload_logging_data']['response_data']
    except ValueError:
        return response.status_code 

def multi_model(payload):
    
    headers={"Content-type":"application/json"} 
    url = 'http://svc-33df36f1-5b37-4b8b-995f-93562b2df15f-5b5f8fb999:5001/predictivemaintenancemulticlassification/b6f10f20-e5b1-42f6-a9e2-de6a2a60b069/score'
#     url = 

    data={"payload":str(payload)}
    response_json = requests.post(url, json=data, headers=headers)
    #st.text_input("API Response: ",response_json.content)
    response = response_json.json()
    try:
        return response['upload_logging_data']['response_data']
    except ValueError:
        return response.status_code