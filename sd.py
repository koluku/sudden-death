import click
import pyperclip

def generator(msg):
    length = len(msg)
    generating = '＿人'
    for i in range(length):
        generating += '人'
    generating += '人＿\n＞　' + msg + '　＜\n￣Y'
    for i in range(length):
        generating += '^'
        if(i != length - 1):
            generating += 'Y'
    generating += 'Y￣'
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
