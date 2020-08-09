"""
パッケージインストール用スクリプト
"""

from setuptools import setup


def _requires_from_file(filename):
    is_in_packages = False
    requires = []

    with open(filename) as _f:
        for _r in _f:
            _r = _r.strip()
            if _r == '[packages]':
                is_in_packages = True
            elif _r.startswith('['):
                is_in_packages = False
            elif _r and is_in_packages:
                requires.append(_r.replace('"', '')
                                .replace(' ', '')
                                .replace('=', '', 1))

    return requires


setup(
    name="sudden_death",
    version="0.0.1",
    license="MIT",
    description="突然の死(ハリフキダシ)を生成するツール",
    author="koluku",
    url="https://github.com/koluku/sudden-death",
    install_requires=_requires_from_file('Pipfile'),
    packages=['sudden_death'],
    package_data={
        "sudden_death": ["py.typed"],
    }
)
