


def check_correct(guess,selected_word) -> None:

    for i,char in enumerate(selected_word):
        if guess[i] == char:
            print(f'the {guess[i]} is correct')

    for i, guess_char in enumerate(guess):

        #Skip if the character is in the exact same position
        if guess_char == selected_word[i]:
            continue

        #Otherwise, check if the character exists elsewhere in the word
        if guess_char in selected_word:
            print(f"'{guess_char}' is in the word, but in the wrong spot")
        else:
            print(f"'{guess_char}' is not in the word at all.")