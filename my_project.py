def read_from_file(file_name):
    read_file = []
    open(file_name)
    for line in file_name.readlines():
        read_file.append(line.strip())
    return read_file


def save_to_file(file_name, insert):
    open(file_name, 'w+')
    for line in insert:
        file_name.writelines(line + '\n')


Morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
              'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
              '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-',
              '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'}


def morse_cipher(msg):
    cp = ''
    for line in msg:
        for l in line:
            if l != ' ':
                cp += Morse_code[l.upper] + ' '
            else:
                cp += '    '
        cp += '\n'
    return cp


def morse_decipher(msg):
    deciphered = ''
    sign = ''
    for line in msg:
        for l in line:
            if l != ' ':
                i = 0
                sign += l
            else:
                i += 1
                if i == 5:
                    deciphered += ' '
                else:
                    deciphered += list(Morse_code.keys())[list(Morse_code.values()).index(sign)]
                    sign = ''
        deciphered += '\n'
    return deciphered


def cesar_cipher(msg, shift):
    result = ''
    for line in msg:
        for i in range(len(line)):
            x = line[i]
            if x == ' ':
                result += ' '
            elif x.isupper():
                result += chr((ord(x) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(x) + shift - 97) % 26 + 97)
        result += '\n'
    return result


def cesar_decipher(msg, shift):
    result = ''
    for line in msg:
        for i in range(len(line)):
            x = msg[i]
            if x == ' ':
                result += ' '
            elif x.isupper():
                result += chr((ord(x) - shift - 65) % 26 + 65)
            else:
                result += chr((ord(x) - shift - 97) % 26 + 97)
        result += '\n'
    return result


def exeuc(a, b):
    x, y, z, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - z * q, y - v * q
        b, a, x, y, z, v = a, r, z, v, m, n
    gcd = b
    return gcd, x, y


def encr(a):
    gcd, x, y = exeuc(a, 26)
    if gcd != 1:
        return None
    else:
        return x % 26


def affine_cipher(text, a, b):
    result = ''
    for line in text:
        for t in line.upper():
            if t == ' ':
                result += ' '
            else:
                result += chr(((a * (ord(t) - ord('A')) + b) % 26) + ord('A'))
        result += '\n'
    return result


def affine_decipher(ciphered, a, b):
    result = ''
    for line in ciphered:
        for c in line:
            if c == ' ':
                result += ' '
            else:
                result += chr(((encr(a) * (ord(c) - ord('A') - b)) % 26) + ord('A'))
        result += '\n'
    return result


def main():
    print('Hello \n What do you want to do?')
    print('1. Code to Morse \n 2. Code from Morse \n 3. Code to Caesar cipher \n 4. Code form Caesar cipher \n'
          '5. Code to affine cipher \n 6. Code from affine cipher')
    choice = input()
    print('Do you want to code from file?')
    print('1. Yes, I want to code from file. \n 2. No, I wish to enter the message myself')
    choice2 = input()
    print('Do you wish to save to file?')
    print('1. Yes \n 2. No')
    choice3 = input()
    if choice == '1':
        if choice2 == '1':
            print('Enter file name:')
            file_name = input()
            msg = read_from_file(file_name)
        else:
            print('Enter the message:')
            msg = input()
        d = morse_cipher(msg)
        print('Do you wish to save to file?')
        print('1. Yes \n 2. No')
        choice3 = input()
        if choice3 == '1':
            print('Enter file name:')
            name_file = input()
            save_to_file(name_file, d)
        else:
            print(d)
    elif choice == '2':
        if choice2 == '1':
            print('Enter file name:')
            file_name = input()
            msg = read_from_file(file_name)
        else:
            print('Enter the message:')
            msg = input()
        m = morse_decipher(msg)

        if choice3 == '1':
            print('Enter file name:')
            name_file = input()
            save_to_file(name_file, m)
        else:
            print(m)
    elif choice == '3':
        if choice2 == '1':
            print('Enter file name:')
            file_name = input()
            msg = read_from_file(file_name)
        else:
            print('Enter the message:')
            msg = input()
        print('Enter shift:')
        shift = int(input())
        x = cesar_cipher(msg, shift)
        if choice3 == '1':
            print('Enter file name:')
            name_file = input()
            save_to_file(name_file, x)
        else:
            print(x)
    elif choice == '4':
        if choice2 == '1':
            print('Enter file name:')
            file_name = input()
            msg = read_from_file(file_name)
        else:
            print('Enter the message:')
            msg = input()
        print('Enter shift:')
        shift = int(input())
        y = cesar_decipher(msg, shift)
        if choice3 == '1':
            print('Enter file name:')
            name_file = input()
            save_to_file(name_file, y)
        else:
            print(y)
    elif choice == '5':
        if choice2 == '1':
            print('Enter file name:')
            file_name = input()
            msg = read_from_file(file_name)
        else:
            print('Enter the message:')
            msg = input()
        print('Enter a:')
        a = int(input())
        print('Enter b:')
        b = int(input())
        z = affine_cipher(msg, a, b)
        if choice3 == '1':
            print('Enter file name:')
            name_file = input()
            save_to_file(name_file, z)
        else:
            print(z)
    elif choice == '6':
        if choice2 == '1':
            print('Enter file name:')
            file_name = input()
            msg = read_from_file(file_name)
        else:
            print('Enter the message:')
            msg = input()
        print('Enter a:')
        a = int(input())
        print('Enter b:')
        b = int(input())
        c = affine_decipher(msg, a, b)
        if choice3 == '1':
            print('Enter file name:')
            name_file = input()
            save_to_file(name_file, c)
        else:
            print(c)


if __name__ == "__main__":
        main()