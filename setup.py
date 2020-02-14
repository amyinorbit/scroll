from setuptools import setup

setup(name='scroll',
    version='0.1',
    description='Tailored, useless to anyone else BibTex/ADS bib manager',
    url='http://github.com/amyinorbit/scroll',
    author='Amy Parent',
    author_email='amy@amyparent.com',
    license='MIT',
    packages=['scroll'],
    entry_points = {
        'console_scripts': [
            'scroll = scroll.cli:main'
        ],
    },
    install_requires=[
        'biblib-simple',
        'colorama',
        'docopt'
    ],
    zip_safe=False)
