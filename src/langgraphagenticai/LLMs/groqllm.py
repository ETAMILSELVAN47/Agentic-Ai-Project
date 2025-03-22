from langchain_groq import ChatGroq
import os
import streamlit as st


class GroqLLM:

    def __init__(self,user_controls_input):
        self.user_controls_input=user_controls_input


    def get_llm_model(self):
        try:
           groq_api_key=self.user_controls_input['GROQ_API_KEY']
           selected_model=self.user_controls_input['selected_model']
           
           if groq_api_key=="" and os.environ['GROQ_API_KEY'] =="":
               st.error("Please Enter the Groq API KEY")


           llm= ChatGroq(api_key=groq_api_key,model=selected_model)

        except Exception as e:
            raise ValueError(f"(GroqLLM) Error occured with exception: {str(e)}")
        
        return llm