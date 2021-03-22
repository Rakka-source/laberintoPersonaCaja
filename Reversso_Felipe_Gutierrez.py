import time
import sys
from collections import deque




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
    cont=0
    for x,y in reversed (second):
        resultado_x = x-previo_second_x
        resultado_y = y-previo_second_y
        traduccion  =   google_traductor_xd(resultado_x,resultado_y,"c")
        ruta_corta.append(traduccion)
        cont+=1

        if sw==1:
            resultado_px = previo_second_x-ultimo_first_x
            resultado_py = previo_second_y-ultimo_first_y
            traduccion  =   google_traductor_xd(resultado_px,resultado_py,"p")
            ruta_corta.append(traduccion)
            sw=0
            cont+=1

        else:
            traduccion  =   google_traductor_xd(memoria_x,memoria_y,"p")
            ruta_corta.append(traduccion)
            cont+=1
        memoria_x   = resultado_x
        memoria_y   =resultado_y
        previo_second_x = x
        previo_second_y = y
    ruta_corta.pop(len(ruta_corta)-1) #Se elimina que P llegue a D ya que la caja es lo importante
    return(ruta_corta)

def setupVariables(): #Reinicia el Setup de listas
    # setup lists
    camino = []
    visited = set()
    frontier = deque()
    solucion = {} 
    return camino,visited,frontier,solucion 

def crearLaberinto(grid,camino,visited,frontier,solucion,inicio="P",final="C"): 

    for y in range(len(grid)):                 
        for x in range(len(grid[y])):
            character = grid[y][x] 
            screen_x = (x)  
            screen_y = (y) 

            if character == "." or character == final or character=="D":
                camino.append((screen_x, screen_y)) 

            if character == final:
                end_x, end_y = screen_x,screen_y


            if character == inicio:
                start_x, start_y = screen_x, screen_y
    return(start_x,start_y,end_x,end_y,camino,visited,frontier,solucion)



def search(camino,visited,frontier,solucion,x=0,y=0,code=0,posicion_x=-1,posicion_y=-1):
    
    frontier.append((x, y))
    solucion[x,y] = x,y
    count=0

    while len(frontier) > 0:    # Termina con frontier en 0
        x, y = frontier.popleft()     
        if count==1 and code!=0:  # code(codigo de jugada) siginifica que ya se hizo el primer movimiento de la segunda jugada( movimiento de C). Agrega a camino posible la ex posicion de P previo a C
            camino.append((posicion_x, posicion_y))  

        if(x - 1, y) in camino and (x - 1, y) not in visited:  #Oeste
            casilla = (x - 1, y)
            solucion[casilla] = x, y  #diccionario que almacena de manera inversa los movimientos, Util para reconocer camino más corto
            frontier.append(casilla) #agrega al frontier para luego recorrer las opciones de manera ordenada
            visited.add((x-1, y))  #se agregan las casillas ya visitadas(si fue visitada no puede volver a hacerlo), ordena la funcion del diccionario

        if (x, y - 1) in camino and (x, y - 1) not in visited:  #Sur
            casilla = (x, y - 1)
            solucion[casilla] = x, y
            frontier.append(casilla)
            visited.add((x, y - 1))
            

        if(x + 1, y) in camino and (x + 1, y) not in visited: #Derecho
            casilla = (x + 1, y)
            solucion[casilla] = x, y
            frontier.append(casilla)
            visited.add((x +1, y))

        if(x, y + 1) in camino and (x, y + 1) not in visited: #izquieredo
            casilla = (x, y + 1)
            solucion[casilla] = x, y
            frontier.append(casilla)
            visited.add((x, y + 1))
        count=count+1



##### SEARCH RUTA C #######

def search_c(camino,visited,frontier,solucion,x=0,y=0,posicion_x=-1,posicion_y=-1):
    z = "Restriccion" #N=restringe Norte; S=restringe sur; E= restringe este, O= restringe oeste
    dicX={"o":-1,"e":1,"n":0,"s":0}
    dicY={"s":-1,"n":1,"e":0,"o":0}
    frontier.append((x, y, z))
    solucion[x,y] = x,y
    camino_circular= (0,0)
    camino_regreso=(0,0)
    sw=1
    while len(frontier) > 0 and sw==1:    # Termina con frontier en 0
        x, y, z = frontier.popleft()     
        print(x,y,z)
        if(x - 1, y) in camino and z!= "o":  #Oeste
            if (x - 1, y) not in visited:
                casilla = (x - 1, y)
                argumento = (x - 1, y,"e") 
                solucion[casilla] = x, y  #diccionario que almacena de manera inversa los movimientos, Util para reconocer camino más corto
                frontier.append(argumento) #agrega al frontier para luego recorrer las opciones de manera ordenada
                visited.add((x-1, y))  #se agregan las casillas ya visitadas(si fue visitada no puede volver a hacerlo), ordena la funcion del diccionario
            else:
                sw=0
                num_x=dicX[z]
                num_y=dicY[z]
                camino_circular = (x+num_x,y+num_y)
                camino_regreso  = (x, y)


        if (x, y - 1) in camino and z!="s" :  #Sur
            if (x, y - 1) not in visited:
                casilla = (x, y - 1)
                argumento=(x, y - 1,"n")
                solucion[casilla] = x, y
                frontier.append(argumento)
                visited.add((x, y - 1))
            else:
                sw=0
                num_x=dicX[z]
                num_y=dicY[z]
                camino_circular = (x+num_x,y+num_y)
                camino_regreso  = (x, y)

        if(x + 1, y) in camino and z!="e": #Norte
            if (x + 1, y) not in visited:
                casilla = (x + 1, y)
                argumento= (x + 1, y, "o")
                solucion[casilla] = (x, y)
                frontier.append(argumento)
                visited.add((x +1, y))
            else:
                sw=0
                num_x=dicX[z]
                num_y=dicY[z]
                camino_circular = (x+num_x,y+num_y)
                camino_regreso  = (x, y)


        if(x, y + 1) in camino and z!="n" : #Este
            if (x, y + 1) not in visited:
                casilla = (x, y + 1)
                argumento= (x, y + 1,"s")
                solucion[casilla] = x, y
                frontier.append(argumento)
                visited.add((x, y + 1))
            else:
                sw=0
                num_x=dicX[z]
                num_y=dicY[z]
                camino_circular = (x+num_x,y+num_y)
                camino_regreso  = (x, y)
    return camino_circular, camino_regreso ,solucion



##### FIN SEARCH RUTA C ####


def backRoute(end_x, end_y,start_x,start_y,solucion): #Analisa la ruta de manera inversa obteniendo la ruta atraves del punto final hacia inicial atraves del diccionario
    ruta=[]
    count=0
    print(start_x, start_y)
    while (end_x, end_y) != (start_x, start_y) and count<7:  
        ruta.append( (end_x,end_y))
        end_x, end_y = solucion[end_x, end_y]    
        print(ruta)
        count+=1
    ruta.append( (end_x,end_y)) 
    return (ruta) #regresa lista del recorrido hecho


                        
#### Main program  ####
def search_path(grid):
    camino,visited,frontier,solucion = setupVariables() #reinicia el setup de listas

    sw_valido = 1                                       #Si es uno el laberinto se considera valido
    sw_valido_aux=1
    opcion = 1                                          # opcion de ruta más corta


    ## Recorrido inicial P (ideal sin restriccion)
    base_p, base_py, end_p_x, end_p_y,camino,visited,frontier,solucion=crearLaberinto(grid,camino,visited,frontier,solucion) #Creacion Laberinto
    search(camino,visited,frontier,solucion,x=base_p,y=base_py)

    try:
        ruta_teo_p=(backRoute(end_p_x, end_p_y,base_p,base_py,solucion))
    except:
        sw_valido = 0                                   # Laberinto es invalido, ya que es imposible para P llegar a C

    mod_grid_x, mod_grid_y = solucion[end_p_x, end_p_y] # Se obtiene del diccionario la penultima posición de "P"  antes de llegar a "C" obteniendo eje x e y.
    auxgrid=grid                    # Modificamos el laberinto aux agregando en el punto previo a tomar la caja para que sea pared y no sea considerado ese bloque como ruta más corta
    auxgrid[base_py][base_p]="."    # Se limpia la posicion inicial de D como posible camino (permite dar la vuelta larga)



    ## Recorrido inicial C (ideal sin restriccion)
    camino,visited,frontier,solucion = setupVariables()
    start_p_x, start_p_y, end_p_x, end_p_y,camino,visited,frontier,solucion      =   crearLaberinto(auxgrid,camino,visited,frontier,solucion,inicio="C",final="D")
    search(camino,visited,frontier,solucion,x=start_p_x,y=start_p_y,posicion_x=mod_grid_x,posicion_y=mod_grid_y)
    try:
        ruta_teo_c                              =  (backRoute(end_p_x, end_p_y,start_p_x,start_p_y,solucion))
    except:
        sw_valido = 0



    ## Recorrido C con restriccion de Penultima posicion
    auxgrid[mod_grid_y][mod_grid_x]="P" # Modifica penultima posicion antes de la tomar la caja a P
    camino,visited,frontier,solucion = setupVariables()
    start_p_x, start_p_y, end_p_x, end_p_y ,camino,visited,frontier,solucion,     =   crearLaberinto(auxgrid,camino,visited,frontier,solucion,inicio="C",final="D")
    search(camino,visited,frontier,solucion,x=start_p_x,y=start_p_y,posicion_x=mod_grid_x,posicion_y=mod_grid_y,code=1)
    try:
        ruta_real_c =(backRoute(end_p_x, end_p_y,start_p_x,start_p_y,solucion))
        ruta_a = len(ruta_teo_p+ruta_real_c) #Sumatoria de ruta sin restriccion P y ruta C con restriccion
    except:
        sw_valido = 0
        ruta_teo_c=[]
        ruta_real_c=[]


    

    ## Comparación y comprovación de ruta más corta de C (restriccion vs no restriccion)
    if len(ruta_teo_c)<len(ruta_real_c) and sw_valido==1:
        ruta_b=0
        varx,vary=ruta_teo_c[len(ruta_teo_c)-2]
        auxgrid[vary][varx]="#"  #Se modifica a pared con motivo de buscar otra ruta factible entre P y C. Y comparar que sumatoria de rutas es mejor
        auxgrid[base_py][base_p]="P"
        
        ## Recorrido P con restriccion de Penultima posicion a C
        camino,visited,frontier,solucion = setupVariables()
        start_p_x, start_p_y, end_p_x, end_p_y,camino,visited,frontier,solucion=crearLaberinto(auxgrid,camino,visited,frontier,solucion)
        search(camino,visited,frontier,solucion,x=start_p_x,y=start_p_y)
        try:
            ruta_aux_p=(backRoute(end_p_x, end_p_y,start_p_x,start_p_y,solucion))
            ruta_b = len(ruta_teo_c+ruta_aux_p) #sumatoria de ruta ideal C más P restringida
        except:
            sw_valido_aux=0

        

        if ruta_b < ruta_a and sw_valido_aux==1:
            opcion  = 2 ## Ruta auxiliar de P con ruta teorica C resultan ser más corta


    if sw_valido == 1:       
        if opcion == 1: 
            mapa=traduccion(ruta_teo_p,ruta_real_c) #ruta A

        else:
            mapa = traduccion(ruta_aux_p,ruta_teo_c) # ruta B

    else: #Tapa de botella, Posible ruta C
        auxgrid[mod_grid_y][mod_grid_x]="#" #Sella con tapa el laberinto bajo, Idea de esto es que sea capaz de siempre ir adelante hasta reencontrar su ruta
        auxgrid[base_py][base_p]="P"
        camino,visited,frontier,solucion = setupVariables()
        start_c_x, start_c_y, end_p_x, end_p_y ,camino,visited,frontier,solucion,     =   crearLaberinto(auxgrid,camino,visited,frontier,solucion,inicio="C",final="D")
        circular,regreso,solucion=search_c(camino,visited,frontier,solucion,x=start_c_x,y=start_c_y)
        print(circular,regreso)
        regreso_x, regreso_y=regreso
        circular_x,circular_y=circular
        print(solucion)
        ruta_c=(backRoute(circular_x,circular_y,regreso_x, regreso_y,solucion))
        #ruta_aux_p=(backRoute(end_p_x, end_p_y,start_p_x,start_p_y,solucion))
        print(ruta_c)
        mapa=None
    return mapa



