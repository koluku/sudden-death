import click
import pyperclip
import unicodedata

def text_len(text):
    count = 0
    for c in text:
        count += 2 if unicodedata.east_asian_width(c) in 'FWA' else 1
    return count

def generator(msg):
    length = text_len(msg)
    generating = '＿人'
    for i in range(length//2):
        generating += '人'
    generating += '人＿\n＞  ' + msg + '  ＜\n￣^Y'
    for i in range(length//2):
        generating += '^Y'
    generating += '^Y￣'
    return generating

@click.command()
@click.argument('msg')
def cmd(msg):
    sd = generator(msg)
    pyperclip.copy(sd)
    click.echo(sd)

def main():
    cmd()

if __name__ == '__main__':
    main()
