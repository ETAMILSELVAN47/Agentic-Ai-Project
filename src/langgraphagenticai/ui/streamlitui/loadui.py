import streamlit as st
import os
from src.langgraphagenticai.ui.uiconfigfile import Config


class LoadStreamlitUI:

    def __init__(self):
        self.config=Config()
        self.user_controls=dict()

    def initialize_session(self):
        return {
        "current_step": "requirements",
        "requirements": "",
        "user_stories": "",
        "po_feedback": "",
        "generated_code": "",
        "review_feedback": "",
        "decision": None
    }

    def load_streamlit_ui(self):
        st.set_page_config(page_title="🤖 "+self.config.get_page_title(),layout="wide")
        st.header("🤖 "+ self.config.get_page_title())
        st.session_state.timeframe=""
        st.session_state.isFetchButtonClicked=False
        st.session_state.isSDLC=False

        with st.sidebar:
            # Get options from config
            llm_options=self.config.get_llm_options()
            usecase_options=self.config.get_usecase_options()

            # LLM Selection
            self.user_controls["selected_llm"]=st.selectbox(label="Select LLM",options=llm_options)

            if self.user_controls["selected_llm"]=='Groq':
                # Model selection
                model_options=self.config.get_groq_model_options()
                self.user_controls["selected_model"]=st.selectbox(label="Select Model",options=model_options)

                # API Key input
                self.user_controls['GROQ_API_KEY']=st.session_state['GROQ_API_KEY']=st.text_input(label="API Key",type='password')

                if not self.user_controls['GROQ_API_KEY']:
                    st.warning("⚠️ Please enter your GROQ API key to proceed. Don't have? refer : https://console.groq.com/keys ")

                
                # usecase selection
                self.user_controls['selected_usecase']=st.selectbox(label="Select Usecase",options=usecase_options)

                if self.user_controls['selected_usecase']=='Chatbot with Tool':
                    # API key input
                    os.environ['TAVILY_API_KEY']=self.user_controls['TAVILY_API_KEY']=st.session_state['TAVILY_API_KEY']=st.text_input(label='Tavily API Key',type='password')
                    
                    # Validate API key
                    if not self.user_controls['TAVILY_API_KEY']:
                        st.warning("⚠️ Please enter your TAVILY_API_KEY key to proceed. Don't have? refer : https://app.tavily.com/home")


                if 'state' not in st.session_state:
                    st.session_state.state=self.initialize_session()
                
                return self.user_controls
                

