def getting_chars(selected_word)-> None:
    c1 = selected_word[0]
    c2 = selected_word[1]
    c3 = selected_word[2]
    c4 = selected_word[3]
    c5 = selected_word[4]


def check_correct(guess) -> None:
    if guess[0] == c1:
        print(f'{guess[0]} is Correct')
    if guess[1] == c2:
        print(f'{guess[1]} is Correct')
    if guess[2] == c3:
        print(f'{guess[2]} is Correct')
    if guess[3] == c4:
        print(f'{guess[3]} is Correct')
    if guess[4] == c5:
        print(f'{guess[4]} is Correct')