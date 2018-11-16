from setuptools import setup

# https://packaging.python.org/distributing/#packaging-your-project

def readme():
    with open('README.rst') as f:
        return f.read()
setup(
    name = 'linuxdroid-create-package',
    version = '0.7',
    license = 'MIT',
    description = 'Lightweight tool for creating deb packages',
    long_description = readme(),
    author = 'Fredrik Fornwall',
    author_email = 'fredrik@fornwall.net',
    url = 'https://github.com/linuxdroid/linuxdroid-create-package',
    scripts = ['linuxdroid-create-package'],
    classifiers = (
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3'
    )
)
