"""
＿人人人人人人人＿
＞  鳩は唐揚げ  ＜
￣^Y^Y^Y^Y^Y^Y^Y￣
を作る
"""

import unicodedata
import click
import pyperclip


def text_len(text: str) -> int:
    """
    一行の長さを出す
    """
    count = 0
    for character in text:
        count += 2 if unicodedata.east_asian_width(character) in 'FWA' else 1
    return count


def generator(msg: str) -> str:
    """
    ＿人人人人人人人＿
    ＞  鳩は唐揚げ  ＜
    ￣^Y^Y^Y^Y^Y^Y^Y￣
    を作る
    """
    messages = msg.split('\n')
    length = list(map(text_len, messages))
    max_length = max(length)

    generating = '＿人'
    for _ in range(max_length//2):
        generating += '人'

    generating += '人＿\n'

    for leng, message in zip(length, messages):
        padding = ' ' * ((max_length - leng) // 2)
        generating += '＞  ' + padding + message + padding + '  ＜\n'

    generating += '￣^Y'

    for _ in range(max_length//2):
        generating += '^Y'
    generating += '^Y￣'
    return generating


@click.command()
@click.argument('msg')
def cmd(msg: str = "") -> None:
    """
    コマンド
    """
    result = generator(msg)
    pyperclip.copy(result)
    click.echo(result)


def main() -> None:
    """
    メイン関数
    """
    cmd()


if __name__ == '__main__':
    main()
