from phi.assistant import Assistant
from phi.llm.ollama import Ollama


def use_system_prompt():
    assistant = Assistant(
        llm=Ollama(model="llama3"),
        system_prompt="Share a 2 sentence story about",
        debug_mode=True,
    )
    assistant.print_response("Tell about Indian Culture")


def use_description_instructions():
    assistant = Assistant(
        llm=Ollama(model="llama3"),
        description="You are a famous short story writer asked to write for a magazine",
        instructions=["You are a pilot on a plane flying from USA to India."],
        markdown=True,
        debug_mode=True,
    )
    assistant.print_response("Tell me a 2 sentence indian story.")


if __name__ == "__main__":
    # use_system_prompt()
    use_description_instructions()
