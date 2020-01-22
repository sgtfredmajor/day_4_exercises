string = input('Enter your text: ')

for char in string:
    if char == 'A':
      string = string.replace('A', '4')
    elif char == 'E':
      string = string.replace('E', '4')
    elif char == 'G':
      string = string.replace('G', '6')
    elif char == 'I':
      string = string.replace('I', '1')
    elif char == 'O':
      string = string.replace('O', '0')
    elif char == 'S':
      string = string.replace('S', '5')
    elif char == 'T':
      string = string.replace('T', '7')
    else:
        pass
print(string)