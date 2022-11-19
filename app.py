import streamlit as st
import pickle
import numpy as np
from numpy import array

model=pickle.load(open('Firemodel.pkl','rb'))


def predict_forest(FFMC,DMC,DC,ISI,temp,RH,Wind,rain):
    input=np.array([[FFMC, DMC, DC, ISI, temp, RH, Wind, rain]]).astype(np.float64)
    prediction=model.predict_proba(input)
    pred='{0:.{1}f}'.format(prediction[0][0], 2)
    return float(pred)

def main():
    st.title("AI BASED WILDFIRE PREDICTION")
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">ENTER DATA TO PREDICT </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    FFMC=st.text_input("FFMC","Fine Fuel Moisture Code: 28.6 to 92.5")
    DMC=st.text_input("DMC","Duff Moisture Code: 1.1 to 65.9 ")
    DC = st.text_input("DC", "Drought Code: 7 to 220.4")
    ISI = st.text_input("ISI", "Initial Spread Index: 0 to 18.5")
    temp = st.text_input("TEMPRATURE", "Temperature in Celsius degrees: 22 to 42")
    RH = st.text_input("RH","Relative Humidity in %: 21 to 90")
    Wind = st.text_input("WIND","Wind speed in km/h: 6 to 29")
    rain = st.text_input("RAIN","Total day in mm: 0 to 16.8")


    safe_html="""  
      <div style="background-color:#07654A;padding:10px >
       <h2 style="color:white;text-align:center;"> Your forest is in safe</h2>
       </div>
    """
    danger_html="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;"> Your forest is in danger</h2>
       </div>
    """

    if st.button("Predict"):
        output=predict_forest(FFMC,DMC,DC,ISI,temp,RH,Wind,rain)
        st.success('The probability of fire taking place is {}'.format(output))

        if output > 0.5:
            st.markdown(danger_html,unsafe_allow_html=True)
        else:
            st.markdown(safe_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()