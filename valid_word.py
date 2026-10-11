def check_word(guess, data)-> bool:
    if guess in data:
        return True
    else:
        return False