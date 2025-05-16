# language_assistant_app/corrector.py
from transformers import pipeline

class GrammarCorrector:
    def __init__(self):
        self.corrector = pipeline("text2text-generation", model="vennify/t5-base-grammar-correction")

    def correct(self, text):
        result = self.corrector("grammar: " + text, max_length=128, do_sample=False)
        return result[0]['generated_text']

# language_assistant_app/README.md
"""
# Grammar Corrector

Uses a fine-tuned transformer to correct English grammar in informal or spoken text.

## Example:
```python
g = GrammarCorrector()
print(g.correct("He go to store yesterday"))
```
"""
