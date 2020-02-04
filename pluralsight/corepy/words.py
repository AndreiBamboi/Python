import sys
from urllib.request import urlopen
def extrage_cuvinte(url):
    """
    Args:
        url: The url of a UTF-8 text document
    Retuns:
        A list of string containing words from document
    """
    poveste = urlopen(url)
    poveste_cuvinte = []
    for linie in poveste:
        cuvinte_per_linie = linie.decode('utf8').split()
        for cuvant in cuvinte_per_linie:
            poveste_cuvinte.append(cuvant)
    poveste.close
    return poveste_cuvinte

def afiseaza_item(items):
    """
    Print items one per line
    Args:
        An iterable series of printable items.
    """
    for item in items:
        print(item)

def main(url):
    # url = sys.argv[1]
    cuvinte = extrage_cuvinte(url)
    afiseaza_item(cuvinte)

if __name__ == '__main__':
    main(sys.argv[1])

#http://sixty-north.com/c/t.txt