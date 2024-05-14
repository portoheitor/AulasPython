import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
from collections import Counter

# Função para obter os resultados de todos os sorteios
def obter_resultados():
    resultados = []
    url = "https://loterias.caixa.gov.br/wps/portal/loterias/landing/lotofacil/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", {"class": "simple-table lotofacil"})
    linhas = table.find_all("tr")
    for linha in linhas[1:]:  # Ignorando o cabeçalho da tabela
        colunas = linha.find_all("td")
        resultado = [coluna.text.strip() for coluna in colunas]
        resultados.append(resultado)
    return resultados

# Função para salvar os resultados em um arquivo CSV
def salvar_resultados(resultados):
    df = pd.DataFrame(resultados, columns=["Concurso", "Data", "Resultado"])
    df.to_csv("resultados_lotofacil.csv", index=False)

# Função para analisar os resultados e dar sugestões para os próximos sorteios
def analisar_resultados(resultados):
    numeros_sorteados = [int(num) for resultado in resultados for num in resultado[2].split(" ")]
    
    # Calculando a frequência de cada número
    frequencia_numeros = Counter(numeros_sorteados)
    
    # Ordenando os números pela frequência (do mais frequente para o menos frequente)
    numeros_ordenados_por_frequencia = sorted(frequencia_numeros.items(), key=lambda x: x[1], reverse=True)
    
    # Escolhendo os próximos números com base na frequência dos números sorteados
    proximos_numeros = [num for num, _ in numeros_ordenados_por_frequencia[:15]]  # Selecionando os 15 números mais frequentes
    
    return proximos_numeros

# Função principal
def main():
    resultados = obter_resultados()
    salvar_resultados(resultados)
    sugestao_proximos_numeros = analisar_resultados(resultados)
    print("Sugestão para os próximos números:", sugestao_proximos_numeros)

if __name__ == "__main__":
    main()
