from SalavatiHolidayCheckup import HolidayCheck
from hijri_converter import convert
import jdatetime

hc = HolidayCheck()

specific_datatime = jdatetime.date(1400, 1, 1, locale='fa_IR').togregorian()
print(hc.get_holiday_status_of_datetime(specific_datatime))

specific_datatime = convert.Hijri(1442, 8, 15).to_gregorian()
print(hc.get_holiday_status_of_datetime(specific_datatime))