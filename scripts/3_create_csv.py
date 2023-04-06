import sys
import csv

delimitedFilename = '../files/3_delimited/% s.txt' % sys.argv[1]
delimitedFile = open(delimitedFilename, "r")
newCSV = '../files/4_csv/% s.csv' % sys.argv[1]

with delimitedFile as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split("|") for line in stripped if line)
    with open(newCSV, 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('Rate', 'Dutch', 'PoS', 'English'))
        writer.writerows(lines)
