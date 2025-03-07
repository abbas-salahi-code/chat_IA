import g4f

def process_chat(message: str):
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=[{"role": "user", "content": message}]
    )
    return {"response": response}

