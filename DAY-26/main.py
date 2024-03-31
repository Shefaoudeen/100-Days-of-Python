import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def user_call():
    user_input = input("Enter a word : ").upper()

    try:
        output = [data_dict[letter] for letter in user_input]
    except KeyError:
        print("Please enter Letters alone")
        user_call()
    else:
        print(output)

user_call()