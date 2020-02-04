"""
Script to convert html table to csv
Explained here https://www.thepythoncode.com/article/convert-html-tables-into-csv-files-in-python
"""
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
LANGUAGE = "en-US,en;q=0.5"

def get_soup(url):
    """Constructs and returns a soup using the HTML content of `url` passed"""
    #Deschide sesiunea
    sesiune = requests.Session()
    #Seteaza User-Agent ca un browser normal
    sesiune.headers['User-Agent'] = USER_AGENT
    #Request pentru varianta in engleza
    sesiune.headers['Accept-Language'] = LANGUAGE
    sesiune.headers['Content-Language'] = LANGUAGE
    #Creaza requestul
    html = sesiune.get(url)
    #Returneaza soup
    return bs(html.content, "html.parser")

def obtine_toate_tabelele(soup):
    """Extrage si returneaza toate tabelele in obiect soup"""
    return soup.find_all("table")

def obtine_headerele_tabele(table):
    """Pentru o tabela soup, returneaza headerele"""
    headere = []
    for th in table.find("tr").find_all("th"):
        headere.append(th.text.strip())
    return headere

def obtine_liniile_tabele(table):
    """Pentru o tabela, returneaza toate liniile"""
    linii = []
    for tr in table.find_all("tr")[1:]:
        celule = []
        #retine toate tagurile td in linia procesata
        tds = tr.find_all("td")
        if len(tds) == 0:
            #daca nu este tag td, cauta th
            ths = tr.find_all("th")
            for th in ths:
                celule.append(th.text.strip())
            else:
                #foloseste tag-urile normal td
                for td in tds:
                    celule.append(td.text.strip())
            linii.append(celule)
    return linii

def salveaza_ca_csv(nume_tabela, headere, linii):
    pd.DataFrame(linii, columns=headere).to_csv(f"{nume_tabela}.csv")

def main(url):
    #ia soup
    soup = get_soup(url)
    tabele = obtine_toate_tabelele(soup)
    print(f"[+]Am gasit un total de {len(tabele)} tabele.")
    for i, tabela in enumerate(tabele, start=1):
        headere = obtine_headerele_tabele(tabela)
        linii = obtine_liniile_tabele(tabela)
        nume_tabela = f"tabela-{i}"
        print(f"[+] Saving {nume_tabela}")
        salveaza_ca_csv(nume_tabela, headere, linii)

if __name__ == "__main__":
    import sys
    try:
        url = sys.argv[1]
    except IndexError:
        print("Please specify a URL.\nUsage: python html_table_extractor.py [URL]")
        exit(1)
    main(url)