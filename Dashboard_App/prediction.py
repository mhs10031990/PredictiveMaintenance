import streamlit as st
import pandas as pd
import requests
import json

# @st.experimental_memo
def binary_model(payload):
    
    headers={"Content-type":"application/json"}
    url = 'http://svc-3beb86ee-32ca-4775-92bc-2a8a463e12d4:5001/predictivemaintenancebinaryclassification/ec2b1439-42f2-4c69-94e7-e52dd57c3e6c/score'
    data={"payload" : str(payload)}
    print("data with Payload", data)
    response_json = requests.post(url, json=data, headers=headers)
    
    #st.text_input("API Response: ",response_json.content)
    response = response_json.json()
    try:
        return response['upload_logging_data']['response_data']
    except ValueError:
        return response.status_code 

def multi_model(payload):
    
    headers={"Content-type":"application/json"} 
    url = 'http://svc-15f321b3-dfe3-4dbd-83eb-903aa51a847f:5001/predictivemaintenancemulticlassification/f6da9f28-e4ea-4226-80fd-8a5e5685b733/score'
#     url = 

    data={"payload":str(payload)}
    response_json = requests.post(url, json=data, headers=headers)
    #st.text_input("API Response: ",response_json.content)
    response = response_json.json()
    try:
        return response['upload_logging_data']['response_data']
    except ValueError:
        return response.status_code