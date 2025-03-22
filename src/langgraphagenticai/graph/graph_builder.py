from src.langgraphagenticai.state.state import State
from langgraph.graph import StateGraph,START,END
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode

class GraphBuilder:

    def __init__(self,model):
        self.llm=model
        self.graph_builder=StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using LangGraph.
        This method initializes a chatbot node using the `BasicChatbotNode` class 
        and integrates it into the graph. The chatbot node is set as both the 
        entry and exit point of the graph.
        """
        basic_chatbot_node=BasicChatbotNode(model=self.llm)
        self.graph_builder.add_node('Chatbot',basic_chatbot_node.process)
        self.graph_builder.add_edge(START,'Chatbot')
        self.graph_builder.add_edge('Chatbot',END)

    
    def setup_graph(self,usecase:str):
        """
        Sets up the graph for the selected use case.
        """
        if usecase=='Basic Chatbot':
            self.basic_chatbot_build_graph()
        return self.graph_builder.compile()
