def read_time(text):
    textList = text.split(" ")
    return len(textList)/200


def check_grammar(text):
    if text[0].isupper() and not text[-1].isalpha():
        return "The grammar is correct"
    return "The grammar is incorrect"

