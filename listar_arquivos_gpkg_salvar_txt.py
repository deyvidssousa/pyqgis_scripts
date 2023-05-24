from qgis.core import QgsVectorLayer, QgsProject

#colocar aqui o caminho do gpkg
caminho_gpkg = r"C:\bc250_2021_11_18\bc250_2021_11_18.gpkg"

layer = QgsVectorLayer(caminho_gpkg,"arquivos","ogr")
layerProvider =layer.dataProvider().subLayers()
lista_nome_arq = []

#colocar aqui o caminho onde deseja salvar o txt
caminho_txt = r"D:\gpkg_"

for subLayer in layerProvider:
    nome = subLayer.split('!!::!!')[1]
    uri = "%s|layername=%s" % (caminho_gpkg, nome,)
    lista_nome_arq.append(nome)

print(lista_nome_arq)

with open(caminho_txt + '\\' + 'lista_arquivos.txt', 'w') as arquivo:
    arquivo.write("\n".join(lista_nome_arq))