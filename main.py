import speechrecog_test as st
from speechrecog_test import listen_for_voice
from dialogue_test import chat_with_llama3
import ollama


while 1: 
    st.start_recognizer()
    conversation_history = []
    limit = list(range(1, 100, 2))
    basic = "You are Vega, an AI assistant who is helpful and has a playful personality. You will help the user based on the previous converations which user will provide"
    conversation_history[0] = ollama.chat(model="llama3.2", messages=[{"role": "system", "content": basic}])
    for i in limit:
            chat = listen_for_voice.user_input
            
            if listen_for_voice.user_input.lower() in ['exit', 'quit', 'bye']:
                print("Vega: Goodbye!")
                st.text_to_speech("Goodbye")
                break
            
            conversation_history[i] = "User: {chat}"
            response = chat_with_llama3(conversation_history)
            print(f"\nVega: {response}")
            st.text_to_speech(response)
            conversation_history.append ("Vega: {response}")




        