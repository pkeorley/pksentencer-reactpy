# PkSentencer on ReactPy (`pksentencer-reactpy`)
A website that will help you to re-examine your sentence for a Python code, when you execute it, you will get the same sentence you entered

## Launch the site
1) Run
```bash
python main.py
```
2) http://127.0.0.1:8080/

## Personal use
```python
from pksentencer_reactpy.modules.parser import LetterParser

parser = LetterParser()
value = parser.parse_sentence(sentence="Hello, world!")

print(value)

# value
# (str(hex)[-~-~-~(-~int() << int('100', 2))]).__add__((str(bool())[~int()])).__add__((str(float)[-~-~int()])).__add__(
# (str(float)[-~-~int()])).__add__((str(ord)[-~int() << int('100', 2)])).__add__((str(bytes)[-~-~(-~int() << 2)])).__add__(
# (str(pow)[-~-~-~-~-~(-~int() << int('100', int('10', 2)))])).__add__((str(ord)[-~int() << int('100', 2)])).__add__(
# (str(round)[-~-~-~(-~int() << 4)])).__add__((str(float)[-~-~int()])).__add__((str(dict)[~-~-~-~-~-~int()]))
```
