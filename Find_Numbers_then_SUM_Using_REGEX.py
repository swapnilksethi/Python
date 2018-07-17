import re
text = open('regex_sum_264486.txt')
result = 0
for line in text.readlines():
    for value in re.findall('[0-9]+', line):
        result += int(value)
text.close()
print('Sum is: %d' %result)