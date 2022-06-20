import re

input_str = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87. """

input_str = input_str.lower().replace("“", " “", 1)  # to add space between word and “
input_str = input_str.replace(' iz ', ' is ')  # replacing "iz" with correct "is"

# Capitalize first letter in a paragraph and join back to string
paragraphs = input_str.split('\t')
paragraphs = [line.strip().capitalize() for line in paragraphs]
str_to_normalize = '\n'.join(paragraphs)  # Can be added not only wrapping symbol, but tab to make it more eye pleasant

# String from previous step divide on sentences inside paragraph and capitalize only first letter in a word
sentences = str_to_normalize.split('. ')
words = [word[0].capitalize() for word in sentences]
sentences = [letter+word[1:] for letter, word in zip(words, sentences)]
str_to_normalize = '. '.join(sentences)

# Cut off last word from the normalizes string
str_output = str_to_normalize.split('.')
str_output = [i.rsplit(' ', 1)[-1] for i in str_output]

# Concatenate last words into normalized string (from new paragraph)
final_string = str_to_normalize + '\n' + ' '.join(str_output).capitalize().rstrip() + '.'

print(final_string) 

# Calculate space and whitespace count in initial string
cnt = 0
for i in str_to_normalize:
    if i == ' ' or i == '\n' or i == '\t':
        cnt += 1
print("Count whitespaces, spaces and tabs in string:", cnt)
