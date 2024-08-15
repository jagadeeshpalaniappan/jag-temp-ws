import json

import httpx
from phi.assistant import Assistant
from phi.llm.ollama import Ollama

order_ids = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114]


def fetch_top_orders(num_orders):
    orders = []
    for order_id in order_ids[:num_orders]:
        order = {
            "orderId": order_id,
            "items": [
                {"name": f"Apple iPhone 10{order_id}", "price": "$1001"},
                {"name": f"Apple iPhone 11{order_id}", "price": "$1102"},
                {"name": f"Apple iPhone 12{order_id}", "price": "$1205"},
                {"name": f"Apple iPhone 13{order_id}", "price": "$1306"},
                {"name": f"Apple iPhone 14{order_id}", "price": "$1407"},
                {"name": f"Apple iPhone 15{order_id}", "price": "$1508"},
                {"name": f"Apple iPhone 16{order_id}", "price": "$1609"},
                {"name": f"Apple iPhone 17{order_id}", "price": "$1700"},
                {"name": f"Apple iPhone 18{order_id}", "price": "$1807"},
                {"name": f"Apple iPhone 19{order_id}", "price": "$1905"},
            ],
        }
        orders.append(order)
    # print(orders)
    return orders


def get_top_jag_ecommerce_orders(num_orders: int = 10) -> str:
    """Use this function to get top order from jag-ecommerce.
     If you do not find proper information, say order details not found

    Args:
        num_orders (int): Number of orders to return. Defaults to 15.

    Returns:
        str: JSON string of top orders.
    """

    # Fetch top order IDs
    orders = fetch_top_orders(num_orders)

    return json.dumps(orders)


assistant = Assistant(
    llm=Ollama(model="llama3"),
    tools=[get_top_jag_ecommerce_orders],
    show_tool_calls=True,
    debug_mode=True,
)
assistant.print_response("Get the jag-ecommerce top 3 orders include item details?")
