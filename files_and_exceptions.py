def read_file_to_dict(entrada):
    dic_final={}
    try:
        with open(entrada,"r") as archivo:
            contenido=archivo.read()
            sin_punto_coma=contenido.split(";")
            for formato in sin_punto_coma:
                for producto,valor in formato:
                    if producto not in dic_final:
                        dic_final[producto]=[]
                    dic_final[producto].append(valor)
        return dic_final

    except FileNotFoundError:
        print("No existe el archivo",entrada)
    except Exception as e:
        print("Ocurrio un error inesperado",e)


def process_dict(data):
    """Para cada producto, imprime el total de ventas y el promedio, en el orden natural del diccionario.

    :param data: dict - diccionario a procesar.
    :return: None
    """
    pass
