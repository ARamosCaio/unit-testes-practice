import string

def verify_pangram(sentence):
    for i in string.ascii_lowercase:
        if i not in sentence.lower():
            return False
    return True