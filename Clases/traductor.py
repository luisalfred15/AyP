pairs = input('Please write words in Spanish with their translation. The word and the translation must be separated with : and each pair with , \n ->')
dictionary = {}

list = pairs.split(',')

for i in range(len(list)):
    translation = list[i].lower()
    words = translation.split(';')
    dictionary[words[0].lower()] = words[1].lower()

phrase = input('Please enter a phrase in Spanish to translate it using the words you wrote before \n ->')
phrase_words = phrase.split(' ')

# for j in range(len(phrase_words)):
#     if j == 0:
#         translated_word = dictionary.get(phrase_words[j].lower())
#         print(translated_word.capitalize(), end = ' ')
#     else:
#         translated_word = dictionary.get(phrase_words[j].lower())
#         print(translated_word, end = ' ')

for phrase_word in phrase_words:
    print(dictionary.get(phrase_word.lower(),phrase_word.lower()), end = ' ')

# Escribe;Write,Un;A,Programa;Program , Escribe un programa