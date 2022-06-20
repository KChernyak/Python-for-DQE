input_string = """homEwork:
    tHis iz your homeWork, copy these Text to variable. 

    You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

    it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

    last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87. """


def normalize_string(inp=input_string):
    str = inp.lower().replace("“", " “", 1)
    str = str.replace(" iz ", " is ")
    return str


def capitalize_first_letter_in_paragraph(inp=normalize_string()):
    paragraphs = inp.splitlines()
    paragraphs = [line.strip().capitalize() for line in paragraphs]
    str_to_normalize = '\n'.join(filter(None, paragraphs))
    return str_to_normalize


def capitalize_first_letter_in_sentence(inp=capitalize_first_letter_in_paragraph()):
    sentences = inp.split('. ')
    words = [word[0].capitalize() for word in sentences]
    sentences = [letter + word[1:] for letter, word in zip(words, sentences)]
    str_to_normalize = '. '.join(sentences)
    return str_to_normalize


def last_words_in_sentences(inp=capitalize_first_letter_in_sentence()):
    str_output = inp.split('.')
    str_output = [i.rsplit(' ', 1)[-1] for i in str_output]
    return str_output


def string_with_added_last_sentence(norm_string=capitalize_first_letter_in_sentence(),
                                    last_sentence=last_words_in_sentences()):
    final_string = norm_string + '\n' + ' '.join(last_sentence).capitalize().rstrip() + '.'
    return final_string


# Calculate space and whitespace count in initial string
def all_space_count(inp=string_with_added_last_sentence()):
    c = 0
    for i in inp:
        if i == ' ' or i == '\n' or i == '\t':
            c += 1
    return print("Count whitespaces, spaces and tabs in string:", c)


# print(string_with_added_last_sentence())
# all_space_count()
