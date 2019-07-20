# internet-download-teste-grafico

**Um simples script de terminal que eu criei enquanto estava aprendendo Python**

---
#### main.py
Quando executado, este script testa a velocidade de conexão com a internet (speedtest-cli) e armazena o resultado em um arquivo *database.json*. (apenas o download)
```json
[
    [
        "dd/mm HH:MM",
        "download speed in Mbps"
    ]
]
```

---
#### grafico.py
Este script lê o arquivo *database.json* e, com o [matplotlib](https://matplotlib.org/ "matplotlib"), monta um gráfico de linhas com as informações obtidas. Tendo a opção de filtrar por dia/mês ou hora.

[![Exemplo do terminal](https://raw.githubusercontent.com/D1360-64RC14/internet-download-teste-grafico/master/exemplos/terminalExemplo.png "Exemplo do terminal")](https://github.com/D1360-64RC14/internet-download-teste-grafico/blob/master/exemplos/terminalExemplo.png "Exemplo do terminal")
[![Exemplo do gráfico](https://raw.githubusercontent.com/D1360-64RC14/internet-download-teste-grafico/master/exemplos/graficoExemplo.png "Exemplo do gráfico")](https://github.com/D1360-64RC14/internet-download-teste-grafico/blob/master/exemplos/graficoExemplo.png "Exemplo do gráfico")
---
#### Crontab
Utilizei o [Crontab](https://pt.wikipedia.org/wiki/Crontab "Crontab") para executar automaticamente o script **main.py** a cada 10 minutos

```bash
*/10 * * * * cd /diretorio/ate/a/pasta/graficoInternetSpeed/; python main.py
```

---
