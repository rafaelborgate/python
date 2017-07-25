'''
ANÁLISE DE DUAS BASES DE DADOS: CHICAGO E SÃO FRANCISCO
DADOS ANALISADOS: PAGAMENTOS EFETUADOS À FORNECEDORES
ANO DE REFERÊNCIA 2015
'''

import requests
import json

urlChicago = "https://data.cityofchicago.org/resource/rjgc-4h37.json?check_date=2015"
urlSaoFrancisco = "https://data.sfgov.org/resource/jhcf-n6nn.json?fiscal_year=2015"

respostaChicago = requests.get(urlChicago)
respostaSF = requests.get(urlSaoFrancisco)

if respostaChicago.status_code == 200:
    dataChicago = respostaChicago.json()          #json.loads(response.content)
if respostaSF.status_code == 200:
    dataSF = respostaSF.json()


#CALCULA VALOR GASTO EM CHICAGO E IDENTIFICA O MAIOR VALOR PAGO
totalChicago=0
indiceMaior=0
maiorValor=0
for item in range(0,len(dataChicago)):
        totalChicago = totalChicago + float(dataChicago[item]["amount"])
        if float(dataChicago[item]["amount"]) > maiorValor:
            maiorValor = float(dataChicago[item]["amount"])
            indiceMaior = item

#CALCULA VALOR GASTO EM SÃO FRANCISCO E IDENTIFICA O MAIOR VALOR PAGO
totalSF = 0
indiceMaiorSF=0
maiorValorSF=0
for item in range(0,len(dataSF)):
    totalSF = totalSF + float(dataSF[item]["vouchers_paid"])
    if float(dataSF[item]["vouchers_paid"]) > indiceMaiorSF:
        maiorValorSF = float(dataSF[item]["vouchers_paid"])
        indiceMaiorSF = item


#IMPRIME DADOS
print("***** DADOS CIDADE DE CHICAGO *****")
print("Pagamentos a fornecedores: $%.2f" %(totalChicago))
print("Maior valor pago:$%.2f \tContrato:%s \tDepartamento:%s \tFornecedor:%s" %(float(dataChicago[indiceMaior]["amount"]),
                                                                              dataChicago[indiceMaior]["contract_number"],
                                                                              dataChicago[indiceMaior]["department_name"],
                                                                              dataChicago[indiceMaior]["vendor_name"]))
print("\n\n***** DADOS CIDADE DE SÃO FRANCISCO *****")
print("Pagamentos a fornecedores: $%.2f" %(totalSF))
print("Maior valor pago:$%.2f \tContrato:%s \tDepartamento:%s \tFornecedor:%s" %(float(dataSF[indiceMaiorSF]["vouchers_paid"]),
                                                                                 dataSF[indiceMaiorSF]["purchase_order"],
                                                                                 dataSF[indiceMaiorSF]["department"],
                                                                                 dataSF[indiceMaiorSF]["vendor"]))