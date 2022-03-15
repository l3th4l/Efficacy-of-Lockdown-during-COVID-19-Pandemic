from datetime import datetime, date, timedelta
import os 
from urllib import request

path = "./Datasets/India_Daily/"

start_date = date(2020, 1, 30)
end_date = datetime.now().date()-timedelta(2)

days = (end_date - start_date).days

url = "https://www.mohfw.gov.in/pdf/CummulativeCovidVaccinationReport%i%s%i.pdf"

for date in [end_date - timedelta(n) for n in range(days)]:
    print(date)
    year = date.year
    month = date.strftime('%B')#.lower()
    day = date.day

    print(url%(day, month, year))

    try:
        request.urlretrieve(url%(day, month, year), "ind_vac_%i%s%i.pdf"%(year, month, day))
    except:
        print('NF')