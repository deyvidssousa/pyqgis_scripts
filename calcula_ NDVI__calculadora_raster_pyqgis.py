#calculadora raster para geração de NDVI

import processing

NIR = 'insira o caminho da banda NIR'
RED = 'insira o caminho da banda RED'

saida = 'insira o caminho e nome do arquivo que será criado o raster de NDVI (.tiff)'

processing.run("gdal:rastercalculator", 
{'INPUT_A': NIR,
 'BAND_A':1,
 'INPUT_B': RED, 
 'BAND_B':1,
 'FORMULA':'(A-B)/(A+B)',
 'OUTPUT':saida
 })
