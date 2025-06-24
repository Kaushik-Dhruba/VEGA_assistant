import ollama
import speechrecog_test as st
from environment_variables import conversation_history
import environment_variables


def chat_with_llama3(prompt):
    try:
        conversation_history.append({"role": "user", "content": prompt})
        formatted_prompt = "\n".join(f"{msg['role'].capitalize()}: {msg['content']}" for msg in conversation_history)
        response = ollama.chat(model="llama3.2", messages=conversation_history)
        conversation_history.append({"role": "assistant", "content": response['message']['content']})
        return response['message']['content']
    
    except Exception as e:
        return str(e)

def chat_assistant(prompt):
    while True:
        user_input = prompt
        if user_input.lower() == "exit":
            print("Vega: Goodbye!")
            st.text_to_speech("Goodbye")
            environment_variables.variable = False
            return
        response = chat_with_llama3(user_input)
        print("Vega: ", response)
        st.text_to_speech(response)
        return



