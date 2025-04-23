from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1/',

    # required but ignored
    api_key='ollama',
)

def askOllama(question):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': question,
            },
            {
                "role": "system",
                "content": "You are a helpful assistant designed to solve graph colourabilites problems. ",
            }
        ],
        model='llama3.2:1b',
    )
    return chat_completion



# print(chat_completion.choices[0].message.content)

# print(chat_completion.choices[0].message)

