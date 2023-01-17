from datetime import datetime
from dateutil.relativedelta import relativedelta

valor_t = 1_000_000
data_emprestimo = datetime(2020, 12, 20)
delta_anos = relativedelta(years=5)
data_fim = data_emprestimo + delta_anos

datas_pars = []
data_parcela = data_emprestimo
while data_parcela < data_fim:
    datas_pars.append(data_parcela)
    data_parcela += relativedelta(months=+1)

for data in datas_pars:
    print(data)