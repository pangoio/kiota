from distutils.core import setup
from setuptools import setup


setup(
    name='kiota',
    author='Pango.io Ltd',
    author_email='info@pango.io',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    version='0.3dev',
    py_modules=['template'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        kiota=template:main
    ''',
    project_urls={  
        'Bug Reports': 'https://github.com/pangoio/kiota/issues',
        'Source': 'https://github.com/pangoio/kiota/',
    },
)