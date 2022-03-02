from re import S


string = input()
count = 0
list(string)

i = 0
while i < len(string):
    if i == len(string) - 1:
        count += 1
        break


    if string[i] == 'c':
        if string[i+1] == '-':
            i += 1
        elif string[i+1] == '=':
            i += 1
        count += 1

    elif string[i] == 'd':
        if i+2 < len(string):
            if string[i+1] == 'z' and string[i+2] == '=':
                i += 2
            elif string[i+1] == '-':
                i += 1
        elif string[i+1] == '-':
            i += 1
        count += 1

    elif (string[i] == 'l' or string[i] == 'n') and string[i+1] == 'j':
        i += 1
        count += 1
    
    elif (string[i] == 's' or string[i] == 'z') and string[i+1] == '=':
        i += 1
        count += 1
    
    else:
        count += 1

    i += 1

print(count)