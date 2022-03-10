from setuptools import setup

setup(
    name='FoodMe',
    author='Group 14'
    version='0.1.0',
    packages=find_packages(include=['scripts', 'exampleproject.*']),
    python_requires=3.8,
    install_requires=[
        'matplotlib',
        'mltk',
        'numpy',
        'pandas',
        'plotly',
        'wordcloud',
        'sklearn'
    ]
)
