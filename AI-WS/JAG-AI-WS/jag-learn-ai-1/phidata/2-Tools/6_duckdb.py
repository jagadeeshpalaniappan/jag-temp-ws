from phi.assistant import Assistant
from phi.llm.ollama import Ollama
from phi.tools.duckdb import DuckDbTools

assistant = Assistant(
    llm=Ollama(model="llama3"),
    tools=[DuckDbTools()],
    show_tool_calls=True,
    system_prompt="Use this file for Movies data: https://phidata-public.s3.amazonaws.com/demo_data/IMDB-Movie-Data.csv",
)

# assistant.print_response(
#     "What is the average rating of movies?", markdown=True, stream=False
# )

assistant.print_response(
    "List top 3 movies based on the rating", markdown=True, stream=False
)
