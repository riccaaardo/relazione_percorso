# Project Steps

- Installed Llama tools and created a Python script to interact with the model (see `AiManager.py`);
- Created a Python script to generate a graph and its related colors (see `graphGeneratorTest.py`);
- Wrote a draft template prompt (see `template.txt`);
- Developed an ASP solver for the graph colorability problem (see `colourability.lp`);
- Created an injector script to replace the placeholders in the template with the generated graph and colors;
- all the scripts contains now callable methods;
- see `test.py` to try to generate a graph and check the answer of the model

## TODO:
- `injector.py` could be better (how?);
- Implement a way to feed the facts to the asp program and get the result.
