from phi.assistant import Assistant
from phi.llm.ollama import Ollama
from phi.tools.duckduckgo import DuckDuckGo

assistant = Assistant(
    llm=Ollama(model="llama3"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    read_chat_history=True,
)
assistant.cli_app(markdown=True)

# Whats happening in india?
