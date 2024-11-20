import pandas



{"A": "Alfa", "B": "Bravo"}
data_nato = pandas.read_csv("nato_phonetic_alphabet.csv")
dict_format = {row.letter: row.code for (index, row) in data_nato.iterrows()}



def generate_phonetic():
    user_input = input("Choose a word? ").upper()
    try:
        list_user_input = [dict_format[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters please")
        generate_phonetic()
    else:
        print(list_user_input)

generate_phonetic()