
# How to use

First, install the needed dependencies running the following command:

    pip install -r requirements.txt

```
> **WARNING**: It is higly reccomended to use an env
```

Then, run the `test.py` script.

You can run it in two different ways:

1. `python3 test.py` - In this way it will use 5 nodes;
2. `python3 test.py 42` - Where 42 can be any integer: it represents the number of nodes.


```
> **Note**: the model llama3.2:1b is used, you can either install it or change the value "model" in the AiManager script.
```

  
  

# Scripts

## AiManager

Contains the system prompt, it's responsible for calling the model and returning its response.

  

## colourability

Logic ASP program that solves the graph coloring problem.

  

## graphGeneratorTest

Given a certain number of nodes, generates a graph. It also contains the method to generate a number of colors between 1 and nNodes.

  

## template

A prompt template for the model.

  

## Injector

Given the generated graph information, injects it into the template.

  

## Solver

Calls clingo to solve the graph coloring problem.

  

## test

Main program, run it to test the whole pipeline.
