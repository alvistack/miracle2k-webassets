# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='webassets',
    version='3.0.0',
    description='Media asset management for Python, with glue code for various web frameworks',
    author_email='Michael Elsdoerfer <michael@elsdoerfer.com>',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
    ],
    install_requires=[
        'pyyaml>=6.0.2',
        'zope-dottedname>=6.0',
    ],
    extras_require={
        'closure': [
            'closure>=20191111',
        ],
        'cssutils': [
            'cssutils>=2.11.1',
        ],
        'jinja2': [
            'jinja2>=3.1.4',
        ],
        'ply': [
            'ply>=3.11',
        ],
        'rcssmin': [
            'rcssmin>=1.1.2',
        ],
        'sass': [
            'libsass>=0.23.0',
        ],
        'slimit': [
            'slimit>=0.8.1',
        ],
    },
    entry_points={
        'console_scripts': [
            'webassets = webassets.script:run',
        ],
    },
    packages=find_packages('src'),
    package_dir={'': 'src'},
)
