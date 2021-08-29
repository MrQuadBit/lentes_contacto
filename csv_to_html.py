import csv

FILE = "catalogo.csv"
TITLE = "Catálogo Lentes de Contacto"
START = "<!DOCTYPE html><html><head><title>"+TITLE+"</title></head><body>"
END = "</body></html>"

def main():
	
	lentes = leeArchivo(FILE)
	marcas = getBrands(lentes)

	#print(lentes)
	#print(marcas)

	marcas = marcas[1:]

	html = START + ""

	for marca in marcas:
		div = "<div>"
		div += "<h1>"+marca+"</h1>"
		for lente in lentes:
			if lente[1] == marca:
				new_element = "<div>"
				new_element += "<p>" + lente[2] + "</p>"
				new_element += "<p>" + lente[3] + "</p>"
				new_element += "<p>" + lente[4] + "</p>"
				new_element += "<p>" + lente[5] + "</p>"
				new_element += "</div>"

				div += new_element
		div += "</div>"
		html += div

	html += END 

	print(html)


def getBrands(rows):
	brands = []

	for r in rows:
		if r[1] not in brands:
			brands.append(r[1])

	return brands[:]

def leeArchivo(file):
	rows = []

	with open(file, encoding='utf-8') as f:
		reader = csv.reader(f, delimiter=',')

		for r in reader:
			rows.append(r)

	return rows[:]

if __name__ == "__main__":
	main()