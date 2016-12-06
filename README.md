# Sudden Death

＿人人人人人人＿  
＞　突然の死　＜  
￣Y^Y^Y^Y^Y￣

↑を簡単に作るためのPythonスクリプトです。

## Requirements

- Python 3.5 over
- ```pip install -r requirements.txt```

## Usage

sd.pyを実行することで次に入力した文字が吹き出しになって出力されます。また、同時に出力された吹き出しはクリップボードにもコピーされます。

```
python sd.py
```

めんどくさがり屋の方のためにコマンドを打ちながら吹き出しにしたい文字を入力することが出来ます。入力する文字はシングルクォーテーションで囲う必要がありません。

```
python sd.py write 入力する文字
// または
python sd.py -w
```

さらにめんどくさがり屋のためにクリップボードの文字を吹き出しにすることが出来ます。

```
python sd.py paste
// または
python sd.py -p
```

## License

[MIT LICENSE](LICENSE)

## Author

- [koluku](https://github.com/koluku)