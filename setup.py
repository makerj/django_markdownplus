""" Setup Django-Markdownplus """
import os

from setuptools import setup, find_packages


def reads(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


setup(
    name='django_markdownplus',
    version='0.1.2',
    description='tiny django app for supporting markdown template tag',
    long_description=reads('README.rst'),
    license=reads('LICENSE'),

    author="makerj",
    author_email="ohenwkgdj@gmail.com",
    url="https://github.com/makerj/django_markdownplus",

    keywords='html markdown django media',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Programming Language :: Python',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Text Processing :: Markup',
    ],

    packages=find_packages(),
    install_requires=['django', 'markdown', 'bleach'],
)
