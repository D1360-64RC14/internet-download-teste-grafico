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


---
#### Crontab
Utilizei o [Crontab](https://pt.wikipedia.org/wiki/Crontab "Crontab") para executar automaticamente o script **main.py** a cada 10 minutos

```bash
*/10 * * * * cd /diretorio/ate/a/pasta/graficoInternetSpeed/; python main.py
```

---