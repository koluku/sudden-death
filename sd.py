import sys
import pyperclip

def generator(reactant):
    length = len(reactant)
    generating = '＿人'
    for i in range(length):
        generating += '人'
    generating += '人＿\n＞　' + reactant + '　＜\n￣Y'
    for i in range(length):
        generating += '^'
        if(i != length - 1):
            generating += 'Y'
    generating += 'Y￣'
    return generating

def main():
    args = sys.argv
    number = len(args)
    count = 0
    for i in range(number):
        if args[i] in ['paste', '-p']:
            text = generator(pyperclip.paste())
        elif i < number-1 and args[i] in ['write', '-w']:
            text = generator(args[i+1])
        else:
            count += 1
    if count == number:
        text = generator(input())
    pyperclip.copy(text)
    print(text)

if __name__ == '__main__':
    main()
