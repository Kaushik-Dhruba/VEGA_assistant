# 🤖 Meet VEGA: A Voice-Activated AI Assistant

VEGA is a voice-enabled AI assistant that listens, understands, and responds—powered by a fine-tuned [LLaMA 3.2](https://huggingface.co/unsloth/llama-3.2-3b-bnb-4bit) model with LoRA adapters. It uses speech recognition, contextual memory, and text-to-speech to enable natural spoken conversations. 

> Current version of code is not connected to the Huggingface trained model. It uses local llama 3.2 model instead.

---

## 🔧 Features

- Voice-Controlled: Speak and listen to your assistant using a microphone and speaker
- Conversational Memory: Tracks previous interactions for coherent replies
- Offline-Ready: Runs locally using Ollama—no cloud APIs or external calls
- Custom Personality: Configure the personality of "VEGA"


---

## 🗂️ Project Structure

VEGA_assistant/

├── main.py                            # Main program loop – runs voice recognition + chatbot

├── dialogue_test.py                   # Interfaces with the local Ollama model

├── speechrecog_test.py                # Handles voice input (speech-to-text) and output (text-to-speech)

└── environmental_variables.py         # Stores global variables


---

## 🚀 How It Works

1. Start the program (`main.py`)
2. Speak into your microphone
3. The assistant will be activated upon hearing the keyword `"VEGA"`
4. Ask questions to the assistant
5. The assistant transcribes your speech into text
6. Sends your prompt + history to a locally running LLaMA 3.2 model via Ollama
7. Receives the model’s response and speaks it aloud
8. Repeats until you say `"exit"`, `"quit"`, or `"bye"`

---

## 🧠 Model Used

The assistant uses a local [LLaMA 3.2](https://ollama.com/library/llama3) model through [Ollama](https://ollama.com/), a local model runner for large language models.

> You must have Ollama installed and the model pulled before running this project.

---

## 📦 Requirements

Install the following packages with pip:

```bash
pip install pyttsx3 SpeechRecognition
