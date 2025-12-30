import streamlit as st 
import random 
st.markdown("""
            <style>
            .stApp{
                  background:linear-gradient(135deg,#ff4d4d,#ff99cc);
                  
            }
            h1,h2,h3,h4,h5,h6,label{
                  color:white !important;
                  
            }
            input,textarea{
                  color:black!important;
            }
            div.stButton>button,
            div.stButton>button span{
                  color:black !important;
            }
            </style>
            """,
            unsafe_allow_html=True)
st.title("Love Percentage Calculator")
name1=st.text_input("Enter first name")
name2=st.text_input("Enter second name")
if(st.button("Calculate")):
      if name1 and name2:
            random.seed(name1.lower()+name2.lower())
            lover_percentage=random.randint(50,100)
            st.success(f"{name1} & {name2} compatibilty: {lover_percentage}%")
            st.caption("Python decided this, not me!")
      else:
            st.warning("Please enter both names !")
