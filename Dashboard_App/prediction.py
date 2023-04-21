import streamlit as st
import pandas as pd
import requests
import json

# @st.experimental_memo
def binary_model(payload):
    
    headers={"Content-type":"application/json"}
    url = 'http://svc-3ed43365-272d-48cf-856a-deb1af27ee27:5001/predictivemaintenancebinaryclassification/ec2b1439-42f2-4c69-94e7-e52dd57c3e6c/score'
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
    url = 'http://svc-23cff8be-6a11-492a-a1d4-61c71e7b0bdc:5001/predictivemaintenancemulticlassification/f6da9f28-e4ea-4226-80fd-8a5e5685b733/score'
#     url = 

    data={"payload":str(payload)}
    response_json = requests.post(url, json=data, headers=headers)
    #st.text_input("API Response: ",response_json.content)
    response = response_json.json()
    try:
        return response['upload_logging_data']['response_data']
    except ValueError:
        return response.status_code