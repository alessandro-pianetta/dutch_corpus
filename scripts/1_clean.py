import sys
import re


def use_regex(text):
    pattern = re.compile(r'(\d{1,4} [\w,() ]+)|(\d[)] [\w]+ \d[)])')
    return pattern.match(text)


# filename = '../TXT/Sectioned/Cleaned - A frequency dictionary of Dutch - % s.txt' % sys.argv[1]
from_file = "../files/1_sectioned/% s.txt" % sys.argv[1]
new_file = open('../files/2_cleaned/% s.txt' % sys.argv[1], 'a')
count = 0

with open(from_file) as file:
    for line in file:
        if use_regex(line):
            count += 1
            new_file.write(line)
new_file.close()

print("Operation finished, created ~% s words" % count)
