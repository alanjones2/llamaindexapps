import ollama

def query(q: str)-> str:
    response = ollama.chat(model='gemma2:2b', messages=[
    {
        'role': 'user',
        'content': q,
    },
    ])
    return (response['message']['content'])

print(query("Why did the chicken cross the road"))