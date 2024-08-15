import ai_utils


def ask_ai(query):
    response = ai_utils.llm.invoke(query)
    return response
