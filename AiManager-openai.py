from openai import OpenAI
from pydantic import BaseModel

# to force the model to use a specific output format
class Edge(BaseModel):
    source_node: str
    target_node: str

class Output(BaseModel):
    edges: list[Edge]
    colors: list[str]

client = OpenAI(
    # required but ignored
    api_key="sk-BpoVo3TVOeR4dr3958kLpfqP_-00fjs6uKNtzjVQ6YT3BlbkFJIY4KmQb3HX6NiRH1SDe1WK0unGBQHxIk2QqzZ6iP8A"
)

#SYSTEM_PROMPT = """You are a helpful assistant designed to solve graph colourabilites problems."""

SYSTEM_PROMPT = """You are a helpful assistant designed to parse natural language description of graphs into a structured JSON-like format."""

def askOllama(question):
    # help(client.chat.completions.create) uncomment to see all the parameters
    chat_completion = client.beta.chat.completions.parse(
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
        model='gpt-4o-mini',
        response_format = Output
    )
    # return validate_json(chat_completion)
    return chat_completion


def validate_json(chat_completion):
    output = Output.model_validate_json(chat_completion.choices[0].message.content)
    print("STAMPO L'OUTPUT FORZATO CON LO SCHERMA JSON:\n ", output)
    return output



# print(chat_completion.choices[0].message.content)

# print(chat_completion.choices[0].message)
