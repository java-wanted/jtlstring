from setuptools import setup

setup(
    name='pytlstring',
    version='0.0.1',
    license='GPLv3+',
    author='Boleslav Stankevich <microsoft-wanted@yandex.ru>',
    packages=[
        'pytlstring',
        ],
    install_requires=[
        'wheel',
        'pytest_runner',
        ],
    tests_require=[
        'pytest',
        ]
    )
