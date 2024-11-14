import google.generativeai as ai
import socket

def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False


def chatBot():
    if not is_connected():
        print("No wifi availble !")
        return
    KEY = "YOUR_API_KEY"

    ai.configure(api_key=KEY)
    model  = ai.GenerativeModel("gemini-pro")
    chat = model.start_chat()
 

    try:
        while True:
            message = input("You : ")
            if message.lower() == "bye":
                print("\nChatbot: Goodbye\n")
                break
            response = chat.send_message(message)
            print(f"\nChatbot: {response.text}\n")
    except Exception as e:
        print(f"Error : {e}")

if __name__ == "__main__":
    chatBot()
else:
    print("Run the code in the original file !")
