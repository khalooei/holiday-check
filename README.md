# holiday checkup 
A python library for checking and detecting the holiday status of the Gregorian date in solar Hijri and lunar Hijri calendar

[![PyPi version](https://img.shields.io/pypi/v/holiday-checkup.svg)](https://pypi.python.org/pypi/holiday-checkup/)
[![](https://img.shields.io/badge/python-3.5+-blue.svg)](https://www.python.org/downloads/) 
![t](https://img.shields.io/badge/status-stable-green.svg) 
[![](https://img.shields.io/github/license/khalooei/holiday-checkup.svg)](https://github.com/khalooei/holiday-checkup/blob/master/LICENSE.md) 



## Installation
The latest stable version of HolidayCheck can be installed through `pip`:

	pip install holiday-checkup



## Usage

```python
>>> from SalavatiHolidayCheckup import HolidayCheck
>>> from hijri_converter import convert
>>> import jdatetime

>>> hc = HolidayCheck()


>>> specific_datatime = jdatetime.date(1400, 1, 1, locale='fa_IR').togregorian()
>>> print(hc.get_holiday_status_of_datetime(specific_datatime))
{
   'weekend_status': {'status': False, 'comment': 'it is Sunday and is a normal day in iran'}, 
   'official_iran_holiday_status': {'status': True, 'comment': "it is norooz and is in the iran's official holiday list"}, 
   'official_islam_holiday_status': {'status': False, 'comment': "it is eid ghadir and is in the islam's official holiday list"}
 }


>>> specific_datatime = convert.Hijri(1403, 2, 20).to_gregorian()
>>> print(hc.get_holiday_status_of_datetime(specific_datatime))
{
   'weekend_status': {'status': False, 'comment': 'it is Sun and is a normal day in iran'}, 
   'official_iran_holiday_status': {'status': False, 'comment': "it is melli shodan naft and is in the iran's official holiday list"}, 
   'official_islam_holiday_status': {'status': True, 'comment': "it is birth of imam zaman  and is in the islam's official holiday list"}
}
```


## build/test 
For testing or using HoidayCheck with the latest updates you may use:

	pip install https://github.com/khalooei/holiday-checkup/archive/master.zip --upgrade


