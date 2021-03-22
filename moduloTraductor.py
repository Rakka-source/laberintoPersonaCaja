def google_traductor_xd(resultado_x,resultado_y,objeto):
    # Traduccion movimientos
    diccionario = {"px1":"p-r",
            "px-1":"p-l",
            "py1":"p-d",
            "py-1":"p-u",
            "cx1":"c-r",
            "cx-1":"c-l",
            "cy1":"c-d",
            "cy-1":"c-u"     
            }
    if resultado_x != 0:
        significante = objeto+"x"+str(resultado_x)
        return diccionario[significante]
    if resultado_y != 0:
        significante = objeto+"y"+str(resultado_y)
        return diccionario[significante]




def traduccion(first,second):
    ruta_corta = []
    # Largo cadena
    largo_first=len(first)-1    # -2 porque se eliminara uno a continuación previo a la utilización
    largo_second=len(second)-1

    # Salvar posiciones
    ultimo_first_x,ultimo_first_y = first[1] 
    previo_first_x,previo_first_y = first[largo_first]
    previo_second_x,previo_second_y = second[largo_second]

    # Eliminar excedente
    first.pop(largo_first)
    first.pop(0)
    second.pop(largo_second)




    for x,y in reversed (first):
        resultado_x = x-previo_first_x
        resultado_y = y-previo_first_y
        previo_first_x = x
        previo_first_y = y
        traduccion  =   google_traductor_xd(resultado_x,resultado_y,"p")
        ruta_corta.append(traduccion)



    sw=1

    for x,y in reversed (second):
        resultado_x = x-previo_second_x
        resultado_y = y-previo_second_y
        traduccion  =   google_traductor_xd(resultado_x,resultado_y,"c")
        ruta_corta.append(traduccion)
        if sw==1:
            resultado_px = previo_second_x-ultimo_first_x
            resultado_py = previo_second_y-ultimo_first_y
            traduccion  =   google_traductor_xd(resultado_px,resultado_py,"p")
            ruta_corta.append(traduccion)
            sw=0
        else:
            print(memoria_x)
            traduccion  =   google_traductor_xd(memoria_x ,memoria_y,"p")
            ruta_corta.append(traduccion)
        memoria_x   = resultado_x
        memoria_y   =resultado_y
        previo_first_x = x
        previo_first_y = y
    ruta_corta.pop(len(ruta_corta)-1) #Se elimina que P llegue a D ya que la caja es lo importante
    return(ruta_corta)