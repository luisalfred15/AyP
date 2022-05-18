input_word = input('Please enter a word: ')
word = input_word.lower()

number_a = word.count('a')
number_e = word.count('e')
number_i = word.count('i')
number_o = word.count('o')
number_u = word.count('u')

print(input_word,'has',number_a,'as,',number_e,'es,',number_i,'is,',number_o,'os and',number_u,'us')