with open('Input/Names/invited_names.txt','r') as f:
    # Return all lines in the file, as a list where each line is an item in the list object: with '\n'
    # name_list = f.readlines()
    # But splitlines returns same list without '\n'
    name_list = f.read().splitlines()

with open('Input/Letters/starting_letter.txt','r') as f:
    letter = f.read()

for name in name_list:
    filename = f'Output/ReadyToSend/letter_for_{name}.txt'
    # The replace() method replaces a specified phrase with another specified phrase.
    custom_letter = letter.replace('[name]',name)
    with open(filename,'w') as f:
        f.write(f'{custom_letter}')

# strip() used to remove unwanted spaces