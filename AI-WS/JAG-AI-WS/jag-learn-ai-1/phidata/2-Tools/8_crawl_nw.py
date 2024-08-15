from phi.assistant import Assistant
from phi.llm.ollama import Ollama
from phi.tools.apify import ApifyTools

assistant = Assistant(
    llm=Ollama(model="llama3"), tools=[ApifyTools()], show_tool_calls=True
)
assistant.print_response(
    "Tell me about https://docs.phidata.com/introduction", markdown=True
)
