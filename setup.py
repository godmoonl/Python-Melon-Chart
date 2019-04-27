from setuptools import setup, find_packages


setup(
    name             = 'Python Melon Chart',
    version          = '1.0',
    description      = 'Python Melon Music Chart',
    long_description = open('README.md').read(),
    author           = 'GODMOONL',
    author_email     = 'himoon345@gmail.com',
    url              = 'https://...',
    download_url     = 'https://...',
    install_requires = ['requests'],
    packages         = find_packages(exclude = ['docs', 'example']),
    keywords         = ['music chart', 'melon', 'melon music chart'],
    python_requires  = '>=3',
    zip_safe=False,
    classifiers      = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)