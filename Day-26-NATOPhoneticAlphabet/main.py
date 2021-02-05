import pandas as pd

nato_df = pd.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter:row.code for (index,row) in nato_df.iterrows()}

while True:
    word = input('Enter word here:\n').upper()
    try:
        list = [nato_dict[letter] for letter in word if letter!=' ' ]
    except KeyError:
        print('Sorry, only letter in the alphabet please')
    else:
        print(list)
        break