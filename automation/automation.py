import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'



with open('existing-contacts.txt', 'r') as file:
    lines = file.readlines()
    newlines = []
    for line in lines:
        newlines.append(line[:-1])
    

file2 = open('phone_numbers.txt', 'w')
file = open('emails.txt', 'w')    
for line in newlines:
    
    if(re.fullmatch(regex, line)):
        file.write(line +'\n')

    if re.match('^[+]', line) :
        line = line. replace('+', '')
        if len(line) < 9:
            file2.write('(206) ' + line +'\n')
            continue
        else:
            file2.write(line +'\n')


    if re.match('^[(]', line):
        line = line. replace('(', '')
        line = line. replace(')', '-')

        if len(line) < 9:
            file2.write('(206) ' + line +'\n')
            continue
        else:
            file2.write(line +'\n')


    if re.match('[0-9][^A-Z]*', line):
        if line[3] == '.':
            line = line. replace('.', '-')
        if len(line) < 9:
            file2.write('(206) ' + line +'\n')
            continue
        else:
            file2.write(line +'\n')
            

        



file.close()
file2.close()
            






if __name__ == "__main__":
    pass