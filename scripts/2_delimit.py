import sys
import re


def is_whitespace(text):
    pattern = re.compile(r' ')
    return pattern.match(text)


def is_an_integer(text):
    pattern = re.compile(r'[0-9]')
    return pattern.match(text)


def has_many_definitions(text):
    pattern = re.compile(r'[2-5bcde]\)')
    return pattern.match(text)


def has_comma_or_close_parentheses(text):
    return re.compile(r'[,)]').match(text)


def is_common_gender(text):
    return re.compile(r'de\([mf]\)').match(text)


def is_written_incorrectly_feminine(text):
    return re.compile(r'de\(f').match(text)


def precedes_definition(text):
    return re.compile(r'(prep|pron|art|conj|verb|adv|adj|de|het|num|\([fm]\))\|').search(text)


def place_delimiter(text_line, i):
    return text_line[:i] + "|" + text_line[i + 1:]


def delete_char(text_line, i):
    return text_line[:i] + text_line[i + 1:]


filename = '../files/2_cleaned/% s.txt' % sys.argv[1]
delimitedFilename = '../files/3_delimited/% s.txt' % sys.argv[1]
delimitedFile = open(delimitedFilename, "w")

index = 0
with open(filename) as file:
    # For each line in the document
    for line in file:
        # Go through each character
        for char in line:
            if is_whitespace(char):
                prev_char = line[index - 1]
                prevFiveChars = line[index - 5:index]
                nextTwoChars = line[index + 1:index + 3]
                # If the character is whitespace and prev characters are not , or )
                # and the next two characters are not bcde) or 2345)...
                if not (has_comma_or_close_parentheses(prev_char)) and not (has_many_definitions(nextTwoChars)):
                    #  ...delete whitespace if transcribed incorrectly...
                    if is_written_incorrectly_feminine(line[index - 4:index]):
                        line = delete_char(line, index)
                        index -= 1
                    else:
                        # ... else replace whitespace with bar
                        line = place_delimiter(line, index)
                # If the whitespace precedes a noun w/ a gender, place a delimiter
                if is_common_gender(prevFiveChars):
                    line = place_delimiter(line, index)
            # Increase index by 1 for next char
            index += 1
            # If the next section is a word definition, stops replacing whitespace
            partialLine = line[0:index]
            if precedes_definition(partialLine): break
        # Reset index to 0 for next line
        index = 0
        delimitedFile.write(line)
delimitedFile.close()

print("Finished creating the delimited file for % s.txt" % sys.argv[1])

