import openai
import pandas as pd

openai.api_key = "INSERISCI_LA_TUA_API_KEY"

def translate(text, memory={}):
    if not isinstance(text, str) or text.strip() == "":
        return ""
    
    if text in memory:
        return memory[text]
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Traduci questo testo in polacco. Usa uno stile coerente e terminologia medica corretta."},
            {"role": "user", "content": text}
        ],
        temperature=0
    )
    translation = response['choices'][0]['message']['content'].strip()
    memory[text] = translation
    return translation
