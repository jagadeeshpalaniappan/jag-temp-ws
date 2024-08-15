from phi.assistant import Assistant
from phi.llm.ollama import Ollama
from phi.tools.hackernews import HackerNews

story_researcher = Assistant(
    llm=Ollama(model="llama3"),
    name="HackerNews Story Researcher",
    role="Researches hackernews stories and users.",
    tools=[HackerNews()],
)
user_researcher = Assistant(
    llm=Ollama(model="llama3"),
    name="HackerNews User Researcher",
    role="Reads articles from URLs.",
    tools=[HackerNews()],
)

hn_assistant = Assistant(
    llm=Ollama(model="llama3"),
    name="Hackernews Team",
    team=[story_researcher, user_researcher],
    # debug_mode=True,
)
hn_assistant.print_response(
    "Write a report about the users with the top 2 stories on hackernews", markdown=True
)
