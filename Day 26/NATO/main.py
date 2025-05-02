import pandas

data=  pandas.read_csv('./Day 26/NATO/nato_phonetic_alphabet.csv')
phonetic_dict ={row.letter:row.code for(index, row) in data.iterrows()}
# print(phonetic_dict)

def genearte_phonetic():
    word = input("enter a word ").upper()
    try:
        output_list =[phonetic_dict[letter] for letter in word]
    except KeyError:
        print("only letters are allowed")
        genearte_phonetic()
    else:
        print(output_list)

genearte_phonetic()


