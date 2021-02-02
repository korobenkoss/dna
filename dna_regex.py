import re
from sys import argv

if len(argv) != 3:
    print("Error")
    exit(1)

csv_file = open(argv[1], 'r') # open csv file as string

tandems = []
persons = {}

for ind, row in enumerate(csv_file):
    if ind == 0:
        tandems = [tandem for tandem in row.strip().split(',')][1:]
    else:
        curr_row = row.strip().split(',')
        persons[curr_row[0]] = [int(x) for x in curr_row[1:]]

# print(persons)
# print(tandems)

dna_strand = open(argv[2], 'r').read()
# print(dna_strand)

final_count = []

for tandem in tandems:
    pos = 0
    counts = []

    while pos < len(dna_strand):
        x = re.search((r"(" + tandem + ")+"), dna_strand[pos:])
        if x:
            print(x.span())
            print("position before: " + str(x.start()))
            print("position after: " + str(x.end()))
            pos += x.end()
            print("position: " + str(pos))
            count = int((x.end() - x.start()) / len(tandem))
            print("count: " + str(count))
            counts.append(count)
            print("list of counts: " + str(counts))
        else:
            break
    
    if counts:
        max_count = max(counts)
        final_count.append(max_count)
        print("final list of counts: " + str(final_count))
    #print(tandem + "repeats at most " + str(final_count) + " times.")



print(persons.items())
print(final_count)
for name, data in persons.items():
    if data == final_count:
        print(name)
        exit(0)

print('No match')