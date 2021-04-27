def is_pangram(sentence):
    alphabets='abcdefghijklmnopqrstuvwxyz'
    for x in alphabets:
        if x not in sentence.lower():
            return False

    return True
