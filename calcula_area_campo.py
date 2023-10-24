layer = iface.activeLayer()
exp = '$area/10000'

def calcula_Area (nomeCampo, tipoCampo, comprimento, precisao):

	provedor = layer.dataProvider()
	provedor.addAttributes([QgsField(nomeCampo, tipoCampo, len=comprimento, prec=precisao)])
	layer.updateFields()

	expressao = QgsExpression(exp)
	contexto = QgsExpressionContext()
	contexto.appendScopes(QgsExpressionContextUtils.globalProjectLayerScopes(layer))


	with edit (layer):
		for atributo in layer.getFeatures():
			contexto.setFeature(atributo)
			atributo[nomeCampo] = expressao.evaluate(contexto)
			layer.updateFeature(atributo)


calcula_Area('Area_ha', QVariant.Double, 6, 2)

print('Área Calculada em Hectares')