from setuptools import setup

setup(
    name='mreg',
    version='0.1',
    py_modules=['mreg'],
    install_requires=[
        'Click',
        'requests',
        'flask',
        'bs4',
        'configparser',
        'pathlib',
    ],
    entry_points='''
        [console_scripts]
        mreg=mreg:mreg
    ''',
)