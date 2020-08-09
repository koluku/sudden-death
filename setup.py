"""
パッケージインストール用スクリプト
"""

from setuptools import setup


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name="sudden_death",
    version="0.0.1",
    license="MIT",
    description="突然の死(ハリフキダシ)を生成するツール",
    author="koluku",
    url="https://github.com/koluku/sudden-death",
    install_requires=_requires_from_file('requirements.txt'),
    packages=['sudden_death'],
    package_data={
        ".": ["py.typed"],
    }
)
