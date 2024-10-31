import pandas



{"A": "Alfa", "B": "Bravo"}
data_nato = pandas.read_csv("nato_phonetic_alphabet.csv")
dict_format = {row.letter: row.code for (index, row) in data_nato.iterrows()}



user_input = input("Choose a word? ").upper()
list_user_input = [value for (letter, value) in dict_format.items()if letter in user_input]
print(list_user_input)
