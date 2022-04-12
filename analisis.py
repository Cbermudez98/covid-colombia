import csv

casos = []

#function para crear el objeto caso
def createObject(row):
    return {
        'fecha reporte web': row[0],
        'ID de caso': row[1],
        'Fecha de notificación': row[2],
        'Código DIVIPOLA departamento': row[3],
        'Nombre departamento': row[4],
        'Código DIVIPOLA municipio': row[5],
        'Nombre municipio': row[6],
        'Edad': row[7],
        'Unidad de medida de edad': row[8],
        'Sexo': row[9],
        'Tipo de contagio': row[10],
        'Ubicación del caso': row[11],
        'Estado': row[12],
        'Código ISO del país': row[13],
        'Nombre del país': row[14],
        'Recuperado': row[15],
        'Fecha de inicio de síntomas': row[16],
        'Fecha de muerte': row[17],
        'Fecha de diagnóstico': row[18],
        'Fecha de recuperación': row[19],
        'Tipo de recuperación': row[20],
        'Pertenencia étnica': row[21],
        'Nombre del grupo étnico': row[22]
    }


def readCsv():
    with open('dataset.csv', newline='') as File:
        reader = csv.reader(File)
        try:
            #recorro el archivo y guardo los datos en una lista
            for row in reader:
                casos.append(createObject(row))
                #print("Recuperado => "+row[15])
        except Exception as e:
            print("Finished reading file")
        finally:
            File.close()
            return casos