import spacy

class ClauseSplitter:

    nlp = spacy.load("en_core_web_sm")

    CLAUSE_CONNECTORS = {
        "but",
        "however",
        "although",
        "though",
        "yet",
        "while",
        "whereas"
    }

    @classmethod
    def split(cls, text):

        doc = cls.nlp(text)

        clauses = []

        for sent in doc.sents:

            split_index = []

            tokens = list(sent)

            for i, token in enumerate(tokens):

                if token.text.lower() in cls.CLAUSE_CONNECTORS:
                    split_index.append(i)
                    continue

                if token.text.lower() == "and":

                    # Skip "doctor and nurses"
                    if token.head.pos_ == "NOUN":
                        continue

                    if cls.has_new_clause(tokens, i):
                        split_index.append(i)

                if token.text == ",":

                    if cls.has_new_clause_after_comma(tokens, i):
                        split_index.append(i)

                    continue

            if not split_index:

                clauses.append(sent.text.strip())

            else:

                start = 0

                for idx in split_index:

                    part = "".join(
                        t.text_with_ws
                        for t in tokens[start:idx]
                    ).strip()

                    if part:
                        clauses.append(part)

                    start = idx + 1

                # Last clause
                part = "".join(
                    t.text_with_ws
                    for t in tokens[start:]
                ).strip()

                if part:
                    clauses.append(part)

        return clauses
    
    @staticmethod
    def has_new_clause(tokens, and_index):

        has_subject = False
        has_verb = False

        for token in tokens[and_index + 1:]:

            # Stop when another conjunction is reached
            if token.text.lower() in ("and", "but", "however", "although"):
                break

            if token.dep_ in ("nsubj", "nsubjpass"):
                has_subject = True

            if token.pos_ in ("VERB", "AUX"):
                has_verb = True

        return has_subject and has_verb
    

    @staticmethod
    def has_new_clause_after_comma(tokens, comma_index):

        has_subject = False
        has_verb = False

        for token in tokens[comma_index + 1:]:

            if token.text == ",":
                break

            if token.dep_ in ("nsubj", "nsubjpass"):
                has_subject = True

            if token.pos_ in ("VERB", "AUX"):
                has_verb = True

            if has_subject and has_verb:
                return True

        return False