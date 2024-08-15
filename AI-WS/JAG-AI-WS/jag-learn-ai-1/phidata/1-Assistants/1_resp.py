from phi.assistant import Assistant
from phi.llm.ollama import Ollama
from rich.pretty import pprint

assistant = Assistant(
    llm=Ollama(model="llama3"),
    description="You help people with their health and fitness goals.",
    instructions=["Recipes should be under 5 ingredients"],
    debug_mode=True,
)


# -*- Print the response in markdown format
def print_response():
    assistant.print_response("Share a breakfast recipe.", markdown=True)


#  Return response as a variable (with Stream)
def get_resp_with_stream():
    response = ""
    for delta in assistant.run("Share a breakfast recipe."):
        response += delta
    pprint("########################## response ################################")
    pprint(response)


#  Return response as a variable (without Stream)
def get_resp_without_stream():
    response = assistant.run("Share a breakfast recipe.", stream=False)
    pprint("########################## response ################################")
    pprint(response)


if __name__ == "__main__":
    # print_response()
    # get_resp_with_stream()
    get_resp_without_stream()
