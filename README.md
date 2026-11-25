# Grammar Corrector

Correct English grammar in informal or spoken text using a fine-tuned transformer model.

## Features

- Wraps the `vennify/t5-base-grammar-correction` sequence-to-sequence model
- Accepts a plain string and returns the corrected string
- Deterministic output (greedy decoding, no sampling)
- Simple, class-based API (`GrammarCorrector`)

## Requirements

- Python 3.8 or newer
- `transformers`
- PyTorch (`torch`) as the backend
- An internet connection on the first run, to download the model weights

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from language_assistant_app import GrammarCorrector

corrector = GrammarCorrector()
print(corrector.correct("He go to store yesterday"))
```

The input is prefixed with `grammar:` internally, and the model returns the corrected sentence. The first call downloads the model, so it may take a moment.

## Project Structure

```text
language_assistant_app/
├── language_assistant_app.py   # GrammarCorrector implementation
├── requirements.txt
└── README.md
```

## License

This project is released under the **MIT License**.

## Author

**Roxana Khaleghi**
