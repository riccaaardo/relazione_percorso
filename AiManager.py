from openai import OpenAI
from pydantic import BaseModel

# to force the model to use a specific output format
class Output(BaseModel):
    node: list[str]
    edge: list[str]
    color: list[str]

client = OpenAI(
    base_url='http://localhost:11434/v1/',

    # required but ignored
    api_key='ollama',
)

#SYSTEM_PROMPT = """You are a helpful assistant designed to solve graph colourabilites problems."""

SYSTEM_PROMPT = """You are a helpful assistant designed to parse natural language description of graphs into a JSON format.
The form your output, use the following output example:
{
    "node": ["1", "2", ...],
    "edge": ["(1, 2)", "(2, 3)", ...],
    "color": ["red", "blue", ..."]
}
You are absolutely not allowed to reply with something that is not in pure json format.
"""

def askOllama(question):
    # help(client.chat.completions.create) uncomment to see all the parameters
    chat_completion = client.beta.chat.completions.parse(
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": question,
            }
        ],
        model='llama3.2:1b',
        response_format=Output.model_json_schema(),
    )
    return validate_json(chat_completion)
    #return chat_completion


def validate_json(chat_completion):
    output = Output.model_validate_json(chat_completion.choices[0].message.content)
    # print("OUTPUT IN JSON FORMAT:\n ", chat_completion.choices[0].message.content)
    return extract_content(output)

def extract_content(json_data):
    result = []

    # Estrai i nodi
    for node in json_data.node:  # Usa la notazione a punti
        result.append(f'node("{node}").')

    # Estrai gli archi
    for edge in json_data.edge:  # Usa la notazione a punti
        # Rimuovi parentesi e spazi, quindi separa i nodi
        u, v = edge.strip("()").split(", ")
        result.append(f"edge(\"{u}\",\"{v}\").")

    # Estrai i colori
    for color in json_data.color:  # Usa la notazione a punti
        result.append(f"color(\"{color}\").")

    # Unisci il risultato in una stringa con nuove righe
    return "\n".join(result)


# print(chat_completion.choices[0].message.content)

# print(chat_completion.choices[0].message)