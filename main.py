"""Example usage for the grammar corrector.

Run:  python main.py "He go to store yesterday"
"""

import sys

from language_assistant_app.corrector import GrammarCorrector


def main() -> None:
    text = sys.argv[1] if len(sys.argv) > 1 else "He go to store yesterday"
    corrector = GrammarCorrector()
    print(corrector.correct(text))


if __name__ == "__main__":
    main()
