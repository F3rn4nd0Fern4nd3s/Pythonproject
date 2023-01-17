# datetime.timedelta e dateutil.relativetimedelta (Calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
#https://docs.python.org/3/library/datetime.html#timedelta-objects
from datetime import datetime, timedelta
fmt = '%d/%m/%Y %H:%M:%S'

data_in = datetime.strptime('22/06/2020 09:50:30', fmt)
data_fim = datetime.strptime('20/04/2022 09:50:30', fmt)
delta = timedelta(days=10, hours=2)
print(data_fim)
print(data_fim + delta) # some delta a data final
print(data_fim - data_in) # diferença das duas datas
print(data_fim > data_in) # True or False