import zipfile

# crear un archivo comprimido
mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w')

# incorporar A
mi_zip.write('mi_texto_A.txt')
# incorporar B
mi_zip.write('mi_texto_B.txt')

mi_zip.close()
