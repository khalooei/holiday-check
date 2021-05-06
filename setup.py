from setuptools import setup
setup(
    name='holiday-check',
    version='0.1',
    description='A python library for checking and detecting the holiday status of the Gregorian date in solar Hijri and lunar Hijri calendar ',
    author='Mohammad Khalooei',
    packages=['SalavatiHolidayCheck'],
    install_requires=[
          'jdatetime',
          'hijri_converter',
      ],
)