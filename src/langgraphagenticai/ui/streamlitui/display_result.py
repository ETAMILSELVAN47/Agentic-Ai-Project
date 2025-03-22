import streamlit as st

class DisplayResultStreamlit:

    def __init__(self,usecase:str,graph,user_message):
        self.usecase=usecase
        self.graph=graph
        self.user_message=user_message

    def display_result_on_ui(self):
        usecase=self.usecase
        graph=self.graph
        user_message=self.user_message

        if usecase=='Basic Chatbot':
            for event in graph.stream({"messages":('user',user_message)}):
                for value in event.values():
                    with st.chat_message('user'):
                        st.write(user_message)
                    
                    with st.chat_message('assistant'):
                        st.write(value['messages'].content)