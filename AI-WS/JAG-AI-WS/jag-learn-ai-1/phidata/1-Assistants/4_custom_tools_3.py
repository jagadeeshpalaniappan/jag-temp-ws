import json
from typing import List

from phi.assistant import Assistant
from phi.llm.ollama import Ollama
from rich.pretty import pprint


def fetch_tags_by_ids(tags_ids):
    tags = []
    for tags_id in tags_ids:
        order = {
            "id": tags_id,
            "name": f"Tag {tags_id}",
            "description": "This is a temperature sensor",
        }
        tags.append(order)
    pprint(tags)
    return tags


def get_asset_tags_details(tags: List[str]) -> str:
    """Use this function to get asset tags details

    Args:
        tagIds (List[str]): List of Tag IDs

    Returns:
        str: JSON string of requested the tags.
    """

    # Fetch the Tag Details
    pprint("######################tags######################")
    pprint(tags)
    tags_response = fetch_tags_by_ids(tags)

    return json.dumps(tags_response)


assistant = Assistant(
    llm=Ollama(model="llama3"),
    tools=[get_asset_tags_details],
    show_tool_calls=True,
    debug_mode=True,
)
assistant.print_response("Please get the TAG-A,TAG-B,TAG-C asset tag details")
