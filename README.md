# English Grammar Corrector

Corrects English grammar in informal or spoken sentences using the fine-tuned
`vennify/t5-base-grammar-correction` sequence-to-sequence model.

## What it does

`language_assistant_app.py` defines `GrammarCorrector`, which wraps a `text2text-generation`
pipeline and returns a corrected version of the input text.

```python
from language_assistant_app import GrammarCorrector

corrector = GrammarCorrector()
print(corrector.correct("He go to store yesterday"))
# -> "He went to the store yesterday."
```

## Requirements

- Python 3.9+
- `transformers`, `torch` (see `requirements.txt`)

```bash
python -m pip install -r requirements.txt
```

The first run downloads the model weights (about 900 MB).

## Notes and limitations

- Trained on English data only; other languages are not supported.
- Input is prefixed with `grammar: ` and truncated at 128 tokens, so long paragraphs should
  be split into sentences first.
- Decoding is greedy (`do_sample=False`), which keeps output stable but less fluent on very
  noisy input.

## Status

Single-module prototype. Packaging as an importable package and a command-line entry point
is planned.

## License

No license file is present yet. Until one is added, the default copyright applies.
