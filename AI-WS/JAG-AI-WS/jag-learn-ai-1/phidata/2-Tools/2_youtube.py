from phi.assistant import Assistant
from phi.llm.ollama import Ollama
from phi.tools.youtube_tools import YouTubeTools

assistant = Assistant(
    llm=Ollama(model="llama3"),
    tools=[YouTubeTools()],
    show_tool_calls=True,
    description="You are a YouTube assistant. Obtain the captions of a YouTube video and answer questions.",
    debug_mode=True,
)
assistant.print_response(
    "Summarize this video https://www.youtube.com/watch?v=Iv9dewmcFbs&t", markdown=True
)
