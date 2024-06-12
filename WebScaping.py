from bs4 import BeautifulSoup
import requests
import time
import webbrowser

url = requests.get("https://articulo.mercadolibre.cl/MLC-950490184-south-park-coleccion-5-figuras-_JM#position=14&search_layout=stack&type=item&tracking_id=766aebb2-9d0e-4858-92af-8d26c3fb102e")

soup = BeautifulSoup(url.content, "html.parser") 
resultado = soup.find("span", {"class":"andes-money-amount__fraction"})

precioInicio_text = resultado.text
precioInicial = float(precioInicio_text)

precioDeseado = 10.000

if precioInicial < precioDeseado:
    print(f" ¡ATENCION! Hay oferta, bajo el precio! Esta en:  {'$'+str(precioInicial)} ")
else:
    print("El precio sigue demasiado alto")