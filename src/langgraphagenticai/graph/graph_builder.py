from src.langgraphagenticai.state.state import State
from langgraph.graph import StateGraph,START,END
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphagenticai.tools.search_tool import get_tools,create_tool_node
from src.langgraphagenticai.nodes.chatbot_with_tools_node import ChatbotwithtoolsNode
from langgraph.prebuilt import tools_condition

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

    def chatbot_with_tools_build_graph(self):
        """
        Builds an advanced chatbot graph with tool integration.
        This method creates a chatbot graph that includes both a chatbot node 
        and a tool node. It defines tools, initializes the chatbot with tool 
        capabilities, and sets up conditional and direct edges between nodes. 
        The chatbot node is set as the entry point.
        """
        ## Define the tool and tool node
        tools=get_tools()
        tool_node=create_tool_node(tools=tools)

        # Define LLM
        llm=self.llm


        # Define chatbot node
        obj=ChatbotwithtoolsNode(model=llm)
        chatbot_node=obj.create_chatbot(tools=tools)

        # Define nodes
        self.graph_builder.add_node('chatbot',chatbot_node)
        self.graph_builder.add_node('tools',tool_node)

        # Define conditional and direct edges
        self.graph_builder.add_edge(START,'chatbot')
        self.graph_builder.add_conditional_edges('chatbot',tools_condition)
        self.graph_builder.add_edge('tools','chatbot')


    def setup_graph(self,usecase:str):
        """
        Sets up the graph for the selected use case.
        """
        if usecase=='Basic Chatbot':
            self.basic_chatbot_build_graph()

        elif usecase=='Chatbot with Tool':
            self.chatbot_with_tools_build_graph()
        return self.graph_builder.compile()
