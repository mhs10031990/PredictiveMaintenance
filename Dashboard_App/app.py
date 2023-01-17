import streamlit as st
import streamlit.components.v1 as components
from prediction import binary_model, multi_model
import pandas as pd

st.set_page_config(page_title="Refract",layout="wide", page_icon="")
st.header("Predictive Maintenance Application")
st.write("Predictive maintenance predicts failure, and the actions could include corrective actions, the replacement of system, or even planned failure. This can lead to major cost savings, higher predictability,  and the increased availability of the systems.")
output1 = ""
output2 = ""
check_prediction  = 0

with st.sidebar:
    from PIL import Image
    image = Image.open('refract.png')

    st.image(image)
    st.sidebar.header("Adjust your inputs")

    air_temp = st.slider('Air temperature [°C]', 20, 40, 31)
    process_temp = st.slider('Process temperature [°C]', 25, 50, 38)
    rotation_rpm = st.slider('Rotational RPM', 1000, 3000, 1400)
    torque_nm = st.slider('Torque NM', 1, 90, 56)
    tool_wear_min = st.slider('Tool Wear Minimum',0,260,233)
    temp_diff =  process_temp - air_temp
    quality_type = st.radio('Quality Type',('Low','Medium','High'))

    if st.button('Predict'):
        payload = {"Air temperature [°C]":{"0":air_temp}, "Process temperature [°C]":{"0":process_temp}, "Rotational speed [rpm]":{"0":rotation_rpm}, "Torque [Nm]":{"0":torque_nm}, "Tool wear [min]":{"0":tool_wear_min} , "Temperature difference [°C]":{"0":temp_diff}}
          
        check_prediction = 1
        air_temp_k = air_temp + 273.15
        process_temp_k = process_temp + 273.15
        if quality_type == "Low":
            Type_L = 1.0
            Type_M = 0.0
        else:
            if quality_type == "Medium":
                Type_L = 0.0
                Type_M = 1.0
            else:
                Type_L = 0.0
                Type_M = 0.0
            
        payload_1 = {'Air temperature [K]':{'0':air_temp_k}, 'Process temperature [K]':{'0':process_temp_k}, 'Rotational speed [rpm]':{'0':rotation_rpm}, 'Torque [Nm]':{'0':torque_nm}, 'Tool wear [min]':{'0':tool_wear_min} , 'Type_L':{'0':Type_L}, 'Type_M':{'0':Type_M}}
        
    else :
        st.write('Please submit once you are ready!')

tab1, tab2, tab3 = st.tabs(["Data Profile", "Insights", "Prediction"])
with tab1:
    HtmlFile = open("data_profile.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height = 600, scrolling=True)

with tab2:
    image1 = Image.open('Airtemperature.JPG')
    image2 = Image.open('Processtemperature.JPG')
    image3 = Image.open('Target.JPG')
    image4 = Image.open('Torque_failuretype.JPG')
    image5 = Image.open('Torque_type.JPG')
    image6 = Image.open('Type.JPG')

    #col1 = st.columns(1)
    st.image(image1, caption='Air Temperature distribution')
    st.write("#")

    #col2 = st.columns(1)
    st.image(image2, caption='Process Temperature distribution')
    st.write("#")

    #col3= st.columns(1)
    st.image(image3, caption='Failure column distribution')
    st.write("#")

    #col4 = st.columns(1)
    st.image(image4, caption='Torque versus Failure')
    st.write("#")

    #col5= st.columns(1)
    st.image(image5, caption='Torque versus Product Quality')
    st.write("#")

    #col6= st.columns(1)
    st.image(image6, caption='Product Quality Distribution')

with tab3:
    if check_prediction > 0:
        st.text_input("Binary Model Input", payload)
        st.text_input("Binary Model Input Type", type(payload))
        data_1 = pd.DataFrame.from_dict(payload)
        st.table(data_1)
        output1 = binary_model(payload)
        st.text_input ('Binary Model Output',output1)
        st.write("#")
        st.write("#")
        if output1 == "Failure":
            
            st.text_input("Multi Model Input", payload_1)
            st.text_input("Multi Model Input Type", type(payload_1))
            data_1 = pd.DataFrame.from_dict(payload_1)
            st.table(data_1)
            output2 = multi_model(payload_1)
            st.text_input ('Multi Model Output',output2)
    else:
        st.write("Submit to check the model prediction")

