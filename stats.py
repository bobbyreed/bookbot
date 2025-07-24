num_words = 0
def num_of_words(string):
    wordList = string.split()
    num_words = len(wordList)
    return print(f"{num_words} words found in the document")

def character_count(string):
    characterList = {}
    for character in string:
        if character in characterList:
            characterList[character] += 1
        else:
            characterList[character] = 1
    return sort_dictionary(characterList)

def sort_on(items):
    return items["num"]

def sort_dictionary(dictionary):
    listDictionary = []
    for character in dictionary:
        listDictionary.append({"char": character, "num": dictionary[character]})
    listDictionary.sort(reverse=True, key=sort_on)
    return prepare_report(listDictionary)

def prepare_report(data):
    return f"============ BOOKBOT ============ \n Analyzing book found at books/frankenstein.txt...\n ----------- Word Count ---------- \n Found {num_words} total words \n --------- Character Count ------- \n {data} \n ============= END ==============="