def num_of_words(string):
    wordList = string.split()
    num_words = len(wordList)
    return num_words

def character_count(string):
    string = string.lower()
    characterList = {}
    for character in string:
        if character in characterList:
            characterList[character] += 1
        else:
            characterList[character] = 1
    return characterList

def sort_on(items):
    return items["num"]

def sort_dictionary(dictionary):
    listDictionary = []
    for character in dictionary:
        listDictionary.append({"char": character, "num": dictionary[character]})
    listDictionary.sort(reverse=True, key=sort_on)
    return listDictionary

def prepare_report(wordCount, characterData):
    # Build header
    report = "============ BOOKBOT ============\n"
    report += "Analyzing book found at books/frankenstein.txt...\n"
    
    # Add word count section
    report += "----------- Word Count ----------\n"
    report += f"Found {wordCount} total words\n"
    
    # Add character count section
    report += "--------- Character Count -------\n"
    for char_dict in characterData:
        if char_dict["char"].isalpha():
            report += f"{char_dict['char']}: {char_dict['num']}\n"
    
    # Add footer
    report += "============= END ==============="
    
    return report