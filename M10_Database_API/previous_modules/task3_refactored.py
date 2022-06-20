import os
import re

initial_string = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87. """


def remove_empty_lines(text):
    return os.linesep.join([i for i in text.splitlines() if i])


def count_whitespaces(text):
    cnt = 0
    for symbol in text:
        if symbol.isspace() or symbol == '\n' or symbol == '\t':
            cnt += 1
    print(f'Text provided contains {cnt} whitespaces')


def replace_iz_with_is(text):
    input_str = text.replace("“", " “", 1)
    return input_str.replace(' iz ', ' is ')


def create_sentence_from_last_words(text):
    sentence = ''
    matches = re.findall(r" [a-zA-Z0-9]*\.", text)
    for word in matches:
        sentence = sentence + word[:-1]
    return sentence[1:] + '.'


def append_sentence_as_last_paragraph(text, sentence):
    text_split = text.splitlines()
    paragraph_number = len(text_split) - 1
    text_split[paragraph_number] += '\n\t' + sentence
    return '\n'.join(text_split)


def normalize_string_case(text):
    text = text.lower()
    # 1 - capitalize first letter in sentence (separated by '.')
    # 2 - capitalize first letter in word in new paragraph
    normalized_text = re.sub(r"((^[a-z])|\. ([a-z])|\t([a-z]))"
                             , lambda reg_match: reg_match.group(1).upper(), text)
    return normalized_text


def main():
    count_whitespaces(initial_string)
    text_without_empty_lines = remove_empty_lines(initial_string)
    sentence_to_add = create_sentence_from_last_words(text_without_empty_lines)
    text_extended = append_sentence_as_last_paragraph(text_without_empty_lines, sentence_to_add)
    text_to_normalize = normalize_string_case(text_extended)
    final_text = replace_iz_with_is(text_to_normalize)
    print(final_text)


# main()
