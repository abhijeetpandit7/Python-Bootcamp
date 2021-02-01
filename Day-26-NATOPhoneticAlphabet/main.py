import pandas as pd

nato_df = pd.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter:row.code for (index,row) in nato_df.iterrows()}

word = input('Enter word here:\n').upper()
list = [nato_dict[letter] for letter in word if letter!=' ' ]
print(list)