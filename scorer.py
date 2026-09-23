import re


def clean(text: str) -> str:
    """Basic cleanup."""
    return text.strip().lower()


def normalize_numbers(text: str) -> str:
    """Normalize simple number words to digits."""
    numbers = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "ten": "10",
        "twenty": "20",
    }

    for word, digit in numbers.items():
        text = re.sub(rf"\b{word}\b", digit, text)

    return text


def normalize_time(text: str) -> str:
    """Make formats such as 7:00 am and 7am comparable."""
    text = re.sub(r"\b(\d{1,2}):00\s*(am|pm)\b", r"\1 \2", text)
    text = re.sub(r"\b(\d{1,2})\s*(am|pm)\b", r"\1 \2", text)
    return text


def remove_punctuation(text: str) -> str:
    return re.sub(r"[^\w\s]", " ", text)


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def normalize(text: str) -> str:
    """Apply all normalization rules."""
    text = clean(text)
    text = normalize_numbers(text)
    text = normalize_time(text)
    text = remove_punctuation(text)
    text = normalize_whitespace(text)
    return text


def contains_expected(text: str, expects: str) -> bool:
    """Return True if the expected phrase occurs in the text."""
    return normalize(expects) in normalize(text)


def retrieved_contains_expected(results, expects: str) -> bool:
    """Check every retrieved chunk."""
    for result in results:
        if contains_expected(result.text, expects):
            return True

    return False


def judge(
    question: str,
    expects: str,
    answer: str,
    results,
) -> bool:
    """
    Judge whether retrieval found the expected answer.

    question and answer are accepted because run_eval.py requires
    this four-argument interface.
    """
    return retrieved_contains_expected(results, expects)