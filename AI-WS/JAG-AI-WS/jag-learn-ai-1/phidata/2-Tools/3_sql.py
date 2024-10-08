from phi.assistant import Assistant
from phi.llm.ollama import Ollama
from phi.tools.sql import SQLTools

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

assistant = Assistant(
    llm=Ollama(model="llama3"),
    tools=[
        SQLTools(
            db_url=db_url,
        )
    ],
    show_tool_calls=True,
)

assistant.print_response(
    "List the tables in the database. Tell me about contents of one of the tables",
    markdown=True,
)
