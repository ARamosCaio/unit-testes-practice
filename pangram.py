import string

def verify_pangram(sentence):
    sentence = input('Insira a frase: ')
    for i in string.ascii_lowercase:
        if i not in sentence.lower():
            return False
    return True