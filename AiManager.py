from llamaapi import LlamaAPI
import solver
import json

#SYSTEM_PROMPT = """You are a helpful assistant designed to solve graph colourabilites problems."""

SYSTEM_PROMPT = """You are a helpful assistant designed to parse natural language description of graphs and solve graph colourability problems.
However, you are not allowed to answer with code or programming language, instead you have to call the function solve(facts) method.
You have to pass to the method a string that respects the following format:
1. Each node is represented as a string in the format: node("node_name").
2. Each edge is represented as a string in the format: edge("node1","node2").
3. Each color is represented as a string in the format: color("color_name").
Do not Add any other information, just the facts.
The function solve(facts) will call the clingo solver and return the result.
"""

def askOllama(question):
    # help(client.chat.completions.create) uncomment to see all the parameters
    llama = LlamaAPI("ollama")

    api_request_json = {
        "model": 'llama3.2:1b',
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": question,
            }
        ],

        "functions": [
            {
                "name": "solve",
                "description": "receives the logical facts of the graph solve the graph colourability problem",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "facts": {
                            "type": "string",
                            "description": "logical facts of the graph",
                        },
                    },
                },
                "required": ["facts"],
            }
        ],
        "stream": False,
        "function_call": "solve",
    }

    response = llama.run(api_request_json)
    print(json.dumps(response.json(), indent=4))

def solve(facts):
    return solver.call_clingo(facts)

