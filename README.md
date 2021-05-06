# holiday-check
A python library for checking and detecting the holiday status of the Gregorian date in solar Hijri and lunar Hijri calendar

+ Python 3.x support




## Usage

```python
>>> from SalavatiHolidayCheck import HolidayCheck
>>> from hijri_converter import convert
>>> import jdatetime

>>> hc = HolidayCheck()


>>> specific_datatime = jdatetime.date(1400, 1, 1, locale='fa_IR').togregorian()
>>> print(hc.get_holiday_status_of_datetime(specific_datatime))
{'weekend_status': {'status': False, 'comment': 'it is Sun and is a normal day in iran'}, 'official_iran_holiday_status': {'status': True, 'comment': "it is norooz and is in the iran's official holiday list"}, 'official_islam_holiday_status': {'status': False, 'comment': "it is eid ghadir and is in the islam's official holiday list"}}


>>> specific_datatime = convert.Hijri(1403, 2, 20).to_gregorian()
>>> print(hc.get_holiday_status_of_datetime(specific_datatime))
{'weekend_status': {'status': False, 'comment': 'it is Sun and is a normal day in iran'}, 'official_iran_holiday_status': {'status': False, 'comment': "it is melli shodan naft and is in the iran's official holiday list"}, 'official_islam_holiday_status': {'status': True, 'comment': "it is birth of imam zaman  and is in the islam's official holiday list"}}
```



## Installation

The latest stable version of HolidayCheck can be installed through `pip`:

	pip install holiday-check

But for testing or using HoidayCheck with the latest updates you may use:

	pip install https://github.com/khalooei/holiday-check/archive/master.zip --upgrade



