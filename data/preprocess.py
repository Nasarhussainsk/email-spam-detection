
import re
import spacy

nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])


def clean_text(text):

    text = str(text).lower()

    text = re.sub(r"http\S+|www\S+", "", text)

    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    doc = nlp(text)

    words = []

    for token in doc:

        if not token.is_stop and not token.is_punct and not token.is_space:
            words.append(token.lemma_)

    return " ".join(words)


def clean_batch(texts):

    cleaned = []

    docs = nlp.pipe(
        texts,
        batch_size=200
    )

    for doc in docs:

        words = [
            token.lemma_
            for token in doc
            if not token.is_stop
            and not token.is_punct
            and not token.is_space
        ]

        cleaned.append(" ".join(words))

    return cleaned
