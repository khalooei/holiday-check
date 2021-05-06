from setuptools import setup

DESCRIPTION = open('README.md').read()

setup(
    name='holiday-check',
    version='0.1',
    url='https://github.com/khalooei/holiday-check',
    license='MIT',
    description='A python library for checking and detecting the holiday status of the Gregorian date in solar Hijri and lunar Hijri calendar ',
    long_description=DESCRIPTION,
    author='Mohammad Khalooei',
    packages=['SalavatiHolidayCheck'],
    install_requires=[
          'jdatetime',
          'hijri_converter',
      ],
    project_urls={
        'Changelog': ('https://github.com/khalooei/holiday-check/README.md'),
        'Docs': 'https://github.com/khalooei/holiday-check/README.md',
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    
)