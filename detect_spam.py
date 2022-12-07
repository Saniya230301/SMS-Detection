import pickle
import streamlit as st
from win32com.client import Dispatch
from PIL import Image
import numpy as np

def speak(text):
	speak=Dispatch(("SAPI.SpVoice"))
	speak.Speak(text)

model=pickle.load(open("spam.pkl","rb"))
cv=pickle.load(open("vectorizer.pkl","rb"))
st.sidebar.write("Email/SMS spam, also referred to as junk email or simply spam, is unsolicited messages sent in bulk by emails/text messages.")
st.sidebar.write("The legal definition and status of spam varies from one jurisdiction to another, but nowhere have laws and lawsuits been particularly successful in stemming spam.")
st.sidebar.write("dangerous because they may contain links that lead to phishing web sites or sites that are hosting malware or include malware as file attachments.")

def main():

    st.title("Spam message Classifier")
    st.subheader(" ")
    msg=st.text_area("Enter the text message : ")
    if st.button("Detect"):
    	data=[msg]
    	vect=cv.transform(data).toarray()
    	prediction=model.predict(vect)
    	result=prediction[0]
    	if result==1:
    		st.error("Beware! This is a spam message")
    		st.subheader("Prediction accuracy = 97.75784753363229%")
    		st.sidebar.error("Caution!\n This is a spam message. ")
    		st.sidebar.error("Do not give any information or any passwords, it may lead to fraud or phishing.")
    		speak("Beware! This is a spam message")
    	else:
    		st.success("This is not a spam message")
    		st.subheader("Prediction accuracy = 97.75784753363229%")
    		st.sidebar.success("No need to worry its a safe and non-spam message.")





main()

st.image('img.jpg',use_column_width=True)
