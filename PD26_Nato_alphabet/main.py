# TODO 1. Create a dictionary in this format:
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

dict = {value.letter:value.code for (key,value) in data.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Enter a word:").upper()
nato_list = [dict[item] for item in list(name)]
print(nato_list)
