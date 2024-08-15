import streamlit as st
from threading import Thread

# Define the chat state (this will be shared across all users)
chat_state = {"messages": [], "users": []}

class ChatServer:
    def __init__(self):
        self.clients = []

    def broadcast(self, message):
        for client in self.clients:
            client.send(message)

    def handle_client_connection(self, client):
        while True:
            message = client.recv().decode("utf-8")
            if message.startswith("/join"):
                user_name = message.split(":")[1]
                chat_state["users"].append(user_name)
                broadcast_message = f"User {user_name} joined the chat."
                self.broadcast(broadcast_message.encode("utf-8"))
            elif message.startswith("/leave"):
                user_name = message.split(":")[1]
                if user_name in chat_state["users"]:
                    chat_state["users"].remove(user_name)
                    broadcast_message = f"User {user_name} left the chat."
                    self.broadcast(broadcast_message.encode("utf-8"))
            else:
                self.broadcast(message.encode("utf-8"))

    def run(self):
        st.title("Jag Chat App")

        # Create a text input for users to send messages
        message_input = st.text_input("Message:", value="")

        # Create a button to send the message
        if st.button("Send"):
            user_name = "User"  # you would get this from user authentication
            chat_state["messages"].append(f"{user_name}: {message_input}")
            st.write("You entered: ", f"{user_name}: {message_input}")
            message_input = ""

        # Display the chat log
        chat_log = st.text_area("Chat Log:", value="\n".join(chat_state["messages"]))
        st.write(chat_log)

if __name__ == "__main__":
    server = ChatServer()
    server.run()