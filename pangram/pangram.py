def is_pangram(sentence):
    alphabets='abcdefghijklmnopqrstuvwxyz'
    check = sentence.lower()
    for x in alphabets:
        if x not in check:
            return False

    return True