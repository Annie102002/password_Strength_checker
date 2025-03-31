import streamlit as st
import re

st.set_page_config(page_title="password Strength checker",page_icon=":guardsman:",layout="wide")
st.title("Password Strength checker")
st.markdown(""
"###welcome to the utlimate passwword Strength checker and get suggestions on how to make it stronger.""")

password = st.text_input("enter your password",type="password")
feedback =[]
score =0
if password:
     if len(password)>=8:
        score+=1
     else:
         feedback.append("password should be at least 8 characters long")

     if re.search(r'[A-Z]', password) and re.search(r'[a-z]',password):
            score+=1
     else:
             feedback.append("password should contain both upper and lower case letters")
     if re.search(r'[0-9]',password):
          score+=1
        
     else:
            feedback.append("password should contain at least one digit")              
     if re.search(r'[@$!%*?&]',password):
           score+=1
     else:
              feedback.append("password should contain at least one special character")     

     if score ==4:
            feedback.append("passsword is strong")
     elif  score==3: 
            feedback.append("password is medium")
     else:
           feedback.append("password is weak")
          
     if feedback:
            st.markdown("## improvement suggestions")    
            for tip in feedback:
                   st.write(tip)
else:  
   st.info("please enter a password to check its strength")                  
