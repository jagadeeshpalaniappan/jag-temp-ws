from ask_ai import ask_ai
from ask_ai_with_knowledge import ask_ai_with_knowledge
from load_knowledge import load_knowledge

query = "Who is Alice?"
existing_pdf_file_name = "pdf/alice.pdf"

if __name__ == "__main__":
    # print(ask_ai(query))
    # print(load_knowledge(existing_pdf_file_name))
    print(ask_ai_with_knowledge(query))
