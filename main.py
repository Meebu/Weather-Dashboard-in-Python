import streamlit as st
import plotly.express as px
from backend import get_data
st.title("Weather Forecast For The Next Days")
st.write(" ")

place=st.text_input(label="Place",placeholder="Enter place...")
st.divider()

days = st.select_slider(
    'Select a range of days',options=[0,1,2,3,4,5])
type=st.selectbox(label="Select Data to View:",options=("Temperature","Sky"))

st.subheader(f"{type} for Next {days} days in {place}")
st.divider()


if type=="Temperature":
    try:
        temperature, date = get_data(place, days, type)
        figure=px.line(x=date,y=temperature,labels={"x":"Date","y":"Temperature (C)"})
        st.plotly_chart(figure)
    except KeyError:
        st.subheader("Place Dont Exist")

if type=="Sky":

    try:
        sky,date=get_data(place,days,type)
        try:
            paths = []
        except NameError:
            st.write("Paths not Defined")
        for item in sky:
            if item=='Clear':
                paths.append("images/clear.png")
            if item=='Rain':
                paths.append("images/rain.png")
            if item=='Clouds':
                paths.append("images/cloud.png")
            if item =='Snow':
                paths.append("images/snow.png")
        print("Paths are: ")
        print(paths)
        st.image(paths, width=115)# if i wll use loops it will print image in new line so put all the paths into list
    except KeyError:
        st.subheader("Place Dont Exist")




