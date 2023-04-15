#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Paul Gierz",
    author_email='pgierz@mac.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Extracts 'docstring' style descriptions out of a script header (e.g. from bash) and generates a markdown file out of it.",
    entry_points={
        'console_scripts': [
            'script_header_markdown_extractor=script_header_markdown_extractor.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='script_header_markdown_extractor',
    name='script_header_markdown_extractor',
    packages=find_packages(include=['script_header_markdown_extractor', 'script_header_markdown_extractor.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/pgierz/script_header_markdown_extractor',
    version='0.1.0',
    zip_safe=False,
)
