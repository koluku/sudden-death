import click
import pyperclip
import unicodedata

def text_len(text):
    count = 0
    for c in text:
        count += 2 if unicodedata.east_asian_width(c) in 'FWA' else 1
    return count

def generator(msg: str) -> str:
    messages = msg.split('\n')
    length = list(map(lambda message: text_len(message), messages))
    max_length = max(length)

    generating = '＿人'
    for i in range(max_length//2):
        generating += '人'

    generating += '人＿\n'

    for leng, msg in zip(length, messages):
        padding = ' ' * ((max_length - leng) // 2)
        generating += '＞  ' + padding + msg + padding + '  ＜\n'

    generating += '￣^Y'

    for i in range(max_length//2):
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
