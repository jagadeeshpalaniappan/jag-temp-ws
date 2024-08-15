from phi.assistant import Assistant
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.newspaper4k import Newspaper4k

assistant = Assistant(
    llm=Ollama(model="llama3"),
    tools=[DuckDuckGo(), Newspaper4k()],
    show_tool_calls=True,
    description="You are a senior NYT researcher writing an article on a topic.",
    instructions=[
        "For the provided topic, search for the top 3 links.",
        "Then read each URL and extract the article text, if a URL isn't available, ignore and let it be.",
        "Analyse and prepare an NYT worthy article based on the information.",
    ],
    add_datetime_to_instructions=True,
)
assistant.print_response("Latest developments in AI", markdown=True)

from phi.assistant import Assistant
from phi.llm.ollama import Ollama
from phi.llm.openai import OpenAIChat

assistant = Assistant(
    llm=Ollama(model="llama3"),
    description="You help people with their health and fitness goals.",
    instructions=["Recipes should be under 5 ingredients"],
    debug_mode=True,
)

# -*- Print the response in markdown format
assistant.print_response("Share a breakfast recipe.", markdown=True)
