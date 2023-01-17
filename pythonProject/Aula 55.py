# 1 - Criando datas com módulo datetime
# 2 - datetime(ano, mês, dia)
# 3 - datetime(ano, mês, dia, horas, minutos, segundos)
# 4 - datetime.striptime('DATA', 'FORMATO')
# 5 - datetime.now()
# 6 - https://pt.wikipedia.org/wiki/Era_Unix
# 7 - datetime.fromtimestamp(Unix Timestamp)
# 8 - https://docs.python.org/3/library/datetime.html
# 9 - Para timezones
#10 - https://en.wikipedia.org/wiki/list_of_tz_database_time_zones
#11 - Instalando o pytz
#12 - pip install pytz types-pytz
from datetime import datetime, timedelta

data_str = '2022-04-22 07:49:23'
fmt = '%Y-%m-%d %H:%M:%S' # = dia-mês-Ano Hora:minutos:segundos
data = datetime.strptime(data_str, fmt)
print(data.strftime('%Y'), data.year) # Ano em str / ano em int
print(data.strftime('%m'), data.month) # mes em str / mes em int
print(data.strftime('%H'), data.hour) # # hora em str / hora em int






