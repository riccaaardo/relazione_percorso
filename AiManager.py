from openai import OpenAI
from pydantic import BaseModel

client = OpenAI(
    base_url='http://localhost:11434/v1/',

    # required but ignored
    api_key='ollama',
)

#SYSTEM_PROMPT = """You are a helpful assistant designed to solve graph colourabilites problems."""

SYSTEM_PROMPT = """You are a helpful assistant designed to parse natural language description of graphs into logical facts of the following form:
- node(x) to say that x is a node;
- nNodes(n) to say that n is the number of nodes;
- edge(x,y) to say that there exist a link between the node x and the node y;
- color(z) to say that z is a color.

In all the above example, the contents of "node", "nNodes", "edge" and "color" must be double-quoted strings.

You are absolutely not allowed to reply with something that is not of the above form (such as Python code, or explanations).

Here is an example:

INPUT:
Given a graph with 4 nodes, the following colors: red, blue
and the following edges that compose the graph: (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3),
extract every node, the number of nodes, edge, and the colors.

OUTPUT:
node("0").
node("1").
node("2").
node("3").
nNodes("4").
edge("0","1").
edge("0","2").
edge("0","3").
edge("1","2").
edge("1","3").
edge("2","3").
color("red").
color("blue").

It is mandatory that you respect the example output format.
"""

def askOllama(question):
    # help(client.chat.completions.create) uncomment to see all the parameters
    chat_completion = client.chat.completions.create(
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
    )
    return chat_completion



# print(chat_completion.choices[0].message.content)

# print(chat_completion.choices[0].message)