with open('BebederosUnam.txt', 'r') as archivo_bebederos:
    with open('data.json', 'a') as archivo_json:
        
        archivo_json.write('[\n')
        contador = 1

        for linea in archivo_bebederos:
            bebedero_linea = linea
            bebedero_linea = bebedero_linea.replace('\n', '')

            if contador <= 84:
                if contador >= 79 and contador <= 84:
                    bebedero_linea = bebedero_linea.replace(',', '', 1)

                bebedero = bebedero_linea.split(', ', 1)
                nombre = bebedero[0]
                institucion = nombre[9:]
                ubicacion = bebedero[1] if len(bebedero) > 1 else institucion

            elif contador >= 85 and contador <= 100:
                bebedero = bebedero_linea.split(', ', 1)
                nombre = bebedero[0]
                institucion = bebedero[0][12:] if contador >= 87 and contador <= 97 else bebedero[0]
                ubicacion = bebedero[1] if contador >= 87 and contador <= 97 and not contador == 90 else bebedero[0]

            else:
                bebedero = bebedero_linea.split('. ')
                nombre = bebedero[0] + ', ' + bebedero[1]
                institucion = bebedero[1][12:]
                ubicacion = bebedero[2]

            palabras_clave = ', '.join(bebedero_linea.replace(',', '').split(' '))
                
            archivo_json.write('{\n')
            archivo_json.write('"pk": ' + str(contador) + ',\n')
            archivo_json.write('"model": "pumaguaAPP.bebederos",\n')
            archivo_json.write('"fields": {\n')
            archivo_json.write('"nombre": "' + nombre + '",\n')
            archivo_json.write('"ubicacion": "' + ubicacion + '",\n')
            archivo_json.write('"institucion": "' + institucion + '",\n')
            archivo_json.write('"palabras_clave": "' + palabras_clave + '"\n')
            archivo_json.write('}\n},\n')

            contador += 1

        archivo_json.write(']')
