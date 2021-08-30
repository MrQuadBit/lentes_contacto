import csv
#-------------------------------------------------
FILE = "Catálogo-Lentes de contacto - Hoja 1.csv"
IMG = "SRC/"
TITLE = "Catálogo Lentes de Contacto"
STYLE = '''
			<style type="text/css">
      			body{background-color: #D0E9EC;}

      			h1,h2{text-align: center;}

      			p{color: #F3F3F3;}
      
      			.container{
			    	display: flex;
			    	flex: nowrap;
			    	justify-content: center;
			    	align-items: center;
			    }
      			.info{
         			height: 160px;
         			background-color: #00A5BE;
         			padding: 20px;
         			border-radius: 0 10% 10% 0;
      			}
      			img{border-radius: 10% 0 0 10%;}
   			</style>
		'''
START = '<!DOCTYPE html><html><head><meta charset="utf-8"/><title>'+TITLE+'</title></head>'+STYLE+'<body><h1>Martínez Zárate Alexandra Marlene</h1>'
END = "</body></html>"
#-------------------------------------------------
def main():
	#De un archivo CSV crea una lista de listas por cada fila en el CSV
	lentes = leeArchivo(FILE)

	#Obtiene las N marcas (lentes[1]) que existan sin repetir
	marcas = obtenerMarcas(lentes)[1:]

	#Formatea las cadenas de texto en elementos HTML
	html = crearHTML(lentes, marcas)

	#Sobre escribe el catalogo con el nombre de index.html o lo crea si no existe
	catalogo = open("index.html", 'w', encoding='utf-8')
	catalogo.write(html)
	catalogo.close()
#-------------------------------------------------
def crearHTML(lentes, marcas):
	html = START + ""

	for marca in marcas:
		div = "<div>"
		div += "<h2>"+marca+"</h2>"
		
		for lente in lentes:
			if lente[1] == marca:
				div += '<div class="container">'
				div += '<img src='+IMG+lente[0]+' alt="imagen de producto" width="200" height="200">'
				new_element = '<div class="info">'
				new_element += "<p>" + lente[2] + "</p>"
				new_element += "<p><strong>Material:</strong> " + lente[3] + "</p>"
				new_element += "<p><strong>Contenido Hídrico:</strong> " + lente[4] + "</p>"
				new_element += "<p><strong>Permeabilidad:</strong> " + lente[5] + "</p>"
				new_element += "</div>"

				div += new_element
				div += "</div>"
				div += "<br>"
		
		div += "</div>"
		html += div

	return html + END

def obtenerMarcas(rows):
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
#-------------------------------------------------
if __name__ == "__main__":
	main()