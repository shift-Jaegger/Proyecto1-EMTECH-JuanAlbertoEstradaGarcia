from lifestore_file import*

#Interfaz de acceso
print('¡Bienvenido al sitio de análisis de ventas de Lifestore! \n \nIngrese su usuario y contraseña a continuación para acceder a los reportes disponibles')
usuarios_admin = [['',''],['Admin','Admin'], ['Daniela','2323']]
usuarios_cliente = [['User','User'],['Lorenzo','578']]

user = input('Teclee su usuario: ')
contra = input('Teclee su contraseña: ')

usr_exist = 0
log = 0
acceso_admin = 0
while acceso_admin == 0:
  for admin in usuarios_admin:
    if admin[0] == user:
      usr_exist = 1
    if admin[0] == user and admin[1] == contra:
      print(f'Validación exitosa \nNivel de acceso: Administrador \nBienvenido {admin[0]} al sitio.')
      log = 1
      acceso_admin = 1

  for cliente in usuarios_cliente:
    if cliente[0] == user:
      usr_exist = 1
    if cliente[0] == user and cliente[1] == contra:
      print(f'Validación exitosa \nNivel de acceso: Cliente \n{cliente[0]}, no tiene acceso al sitio.\nIntente con una cuenta válida')
      log = 1
      acceso_admin = 0
      user = input('Teclee su usuario: ')
      contra = input('Teclee su contraseña: ')

  if log == 0 and usr_exist == 1:
    print('Usuario existe, contraseña no coincide. \nIntente de nuevo')
    user = input('Teclee su usuario: ')
    contra = input('Teclee su contraseña: ')
    
  elif log == 0 and usr_exist == 0:
    print('Credenciales no coinciden, ingrese credenciales correctas')
    user = input('Teclee su usuario: ')
    contra = input('Teclee su contraseña: ')





opcion_valida = 0

while opcion_valida != 1:
  print('Haga una selección de la clase de reporte disponible al que desee acceder: \n1.- Productos más vendidos y productos rezagdos. \n2.- Productos por reseña en el servicio. \n3.- Ingresos  ventas \n4.- Finalizar sesión.\n')

  opcion_seleccionada = input('Teclee su selección: ')

  #Mas vendidos y rezagados
  if opcion_seleccionada == '1':
    print('Seleccionó los informes de productos más vendidos y productos rezgados. \nHaga una selección del reporte que desea consultar: \n1.- 50 productos con mayores ventas.\n2.- 50 productos con mayores búsquedas.\n3.- 10 productos con menores ventas por categoria. \n4.- 10 productos con menores búsquedas por categoría. \n5.- Regresar al menú anterior')
    opcion_valida = 1

    subopcion1_seleccionada = input('Teclee su selección: ')
    subopcion1_valida = 0

    while subopcion1_valida != 1:
      #lista 50 productos con mayores ventas
      if subopcion1_seleccionada == '1':
        
        ventas_totales = 0
        lista_ventas_ind = [] # [[id,ventas]]
        for producto in lifestore_products:
          ventas_individual = 0
          for venta in lifestore_sales:
            if producto[0] == venta[1]:
              ventas_individual += 1
              ventas_totales += 1 
          registro_individual = [producto[0],producto[1],ventas_individual]
          lista_ventas_ind.append(registro_individual)
        
        lista_ventas_max = list(lista_ventas_ind)
        ventas_ordenadas_max = []

        while lista_ventas_max:
          maximo = lista_ventas_max[0][2]
          registro_actual = lista_ventas_max [0]
          for registro in lista_ventas_max:
            if registro[2] > maximo:
              maximo = registro[2]
              registro_actual = registro
          ventas_ordenadas_max.append(registro_actual)
          lista_ventas_max.remove(registro_actual)

        for i in range(50) :
          print(f'El producto número {i+1} en ventas: ', ventas_ordenadas_max[i][1],'se ha vendido en total ',ventas_ordenadas_max[i][2], 'veces')
        opcion_valida = 0
        break
        subopcion1_valida = 1

      #lista 100 productos con mayores búsquedas  
      elif subopcion1_seleccionada == '2':
        
        busquedas_totales = 0
        lista_busquedas_ind = [] # [[id,ventas]]
        for producto in lifestore_products:
          busquedas_individual = 0
          for busca in lifestore_searches :
            if producto[0] == busca[1]:
              busquedas_individual += 1
              busquedas_totales += 1 
          registro_busq_individual = [producto[0],producto[1],busquedas_individual]
          lista_busquedas_ind.append(registro_busq_individual)
        
        lista_busquedas_max = list(lista_busquedas_ind)
        busquedas_ordenadas_max = []

        while lista_busquedas_max:
          maximo_busq = lista_busquedas_max[0][2]
          registro_actual = lista_busquedas_max [0]
          for registro in lista_busquedas_max:
            if registro[2] > maximo_busq:
              maximo_busq = registro[2]
              registro_actual = registro
          busquedas_ordenadas_max.append(registro_actual)
          lista_busquedas_max.remove(registro_actual)

        for i in range(50) :
          print(f'El producto número {i+1} en búsquedas: ', busquedas_ordenadas_max[i][1],'se ha buscado en total ',busquedas_ordenadas_max[i][2], 'veces')
        opcion_valida = 0
        break
        subopcion1_valida = 1
      #lista 50 productos con menores ventas por cat 
      elif subopcion1_seleccionada == '3':
        lista_categorias = [lifestore_products[0][3]]
        for producto in lifestore_products:
          categoria = producto[3]
          cat_registrada = 0
          for categorias in lista_categorias:
            if categoria == categorias:
              cat_registrada = 1
          if cat_registrada == 0:
            lista_categorias.append(categoria)

        ventas_totales = 0
        lista_ventas_ind_cat = [] # [[id,ventas]]
        for producto in lifestore_products:
          ventas_individual = 0
          for venta in lifestore_sales:
            if producto[0] == venta[1]:
              ventas_individual += 1
              ventas_totales += 1 
          registro_individual = [producto[0],producto[1],producto[3],ventas_individual]
          lista_ventas_ind_cat.append(registro_individual)


        for categoria in lista_categorias:
          lista_cat_venta_min = list(lista_ventas_ind_cat)
          lista_categoria_ind = []
          for producto in lista_ventas_ind_cat:
            if producto[2] == categoria:
              lista_categoria_ind.append(producto)

          lista_ventas_cat_min = list(lista_categoria_ind)
          ventas_ordenadas_cat_min = []

          while lista_ventas_cat_min:
            minimo = lista_ventas_cat_min[0][3]
            registro_actual = lista_ventas_cat_min[0]
            for registro in lista_ventas_cat_min:
              if registro[3] < minimo:
                minimo = registro[3]
                registro_actual = registro
            ventas_ordenadas_cat_min.append(registro_actual)
            lista_ventas_cat_min.remove(registro_actual)
          if len(ventas_ordenadas_cat_min) > 10:
            top=10
          else:   
            top = len(ventas_ordenadas_cat_min)

          for i in range(top) :
            print(f'De la categoria de {categoria}, el producto número {i+1} con menores ventas: ', ventas_ordenadas_cat_min[i][1],'se ha vendido en total ',ventas_ordenadas_cat_min[i][3], 'veces')
          print('\n')
        opcion_valida = 0
        break
        subopcion1_valida = 1
      #lista 100 productos con menores búsquedas por cat 
      elif subopcion1_seleccionada == '4':
        lista_categorias = [lifestore_products[0][3]]
        for producto in lifestore_products:
          categoria = producto[3]
          cat_registrada = 0
          for categorias in lista_categorias:
            if categoria == categorias:
              cat_registrada = 1
          if cat_registrada == 0:
            lista_categorias.append(categoria)

        lista_busquedas_ind_cat = [] # [[id,ventas]]
        for producto in lifestore_products:
          busquedas_individual = 0
          for busquedas in lifestore_searches:
            if producto[0] == busquedas[1]:
              busquedas_individual += 1
          registro_individual = [producto[0],producto[1],producto[3],busquedas_individual]
          lista_busquedas_ind_cat.append(registro_individual)


        for categoria in lista_categorias:
          lista_cat_busquedas_min = list(lista_busquedas_ind_cat)
          lista_categoria_busq_ind = []
          for producto in lista_cat_busquedas_min:
            if producto[2] == categoria:
              lista_categoria_busq_ind.append(producto)

          lista_busquedas_cat_min = list(lista_categoria_busq_ind)
          busquedas_ordenadas_cat_min = []

          while lista_busquedas_cat_min:
            minimo = lista_busquedas_cat_min[0][3]
            registro_actual = lista_busquedas_cat_min[0]
            for registro in lista_busquedas_cat_min:
              if registro[3] < minimo:
                minimo = registro[3]
                registro_actual = registro
            busquedas_ordenadas_cat_min.append(registro_actual)
            lista_busquedas_cat_min.remove(registro_actual)
          if len(busquedas_ordenadas_cat_min) > 10:
            top=10
          else:   
            top = len(busquedas_ordenadas_cat_min)

          for i in range(top) :
            print(f'De la categoria de {categoria}, el producto número {i+1} con menores búsquedas: ', busquedas_ordenadas_cat_min[i][1],'se ha buscado en total ',busquedas_ordenadas_cat_min[i][3], 'veces')
          print('\n')
        opcion_valida = 0
        break
        subopcion1_valida = 1
      elif subopcion1_seleccionada == '5':
        opcion_valida = 0
        break
      else:
        print('Su selección no es parte de las opciones. \nIntente una selección válida')
        subopcion1_seleccionada = input('Teclee su selección: ')

  elif opcion_seleccionada == '2':
    print('Seleccionó los informes de productos por reseña en el servicio. \nHaga una selección del reporte que desea consultar: \n1.- 20 productos con mejores reseñas.\n2.- 20 productos con peores reseñas.\n3.- Regresar al menú anterior.\n')
    opcion_valida = 1
    subopcion2_seleccionada = input('Teclee su selección: ')
    subopcion2_valida = 0
    while subopcion2_valida != 1:
      #lista 20 productos con mejores reseñas 
      if subopcion2_seleccionada == '1':
        lista_reviews_ind = [] # [[id,ventas]]
        for producto in lifestore_products:
          reviews_suma = 0
          reviews_conteo = 0
          for venta in lifestore_sales:
            if producto[0] == venta[1]:
              reviews_suma += venta[2]
              reviews_conteo += 1 
          if reviews_conteo == 0:
            division = 0
          else:
            division = reviews_suma/reviews_conteo
          registro_individual = [producto[0],producto[1],division]
          lista_reviews_ind.append(registro_individual)

        lista_reviews_max = list(lista_reviews_ind)
        reviews_ordenadas_max = []

        while lista_reviews_max:
          maximo = lista_reviews_max[0][2]
          registro_actual = lista_reviews_max[0]
          for registro in lista_reviews_max:
            if registro[2] > maximo:
              maximo = registro[2]
              registro_actual = registro
          reviews_ordenadas_max.append(registro_actual)
          lista_reviews_max.remove(registro_actual)

        for i in range(20) :
          print(f'El producto número {i+1} con mejores reseñas: ', reviews_ordenadas_max[i][1],'tiene una reseña promedio de ',reviews_ordenadas_max[i][2])
        print('\n')
        opcion_valida = 0
        break
        subopcion2_valida = 1
     
      #lista 20 productos con peores reseñas
      elif subopcion2_seleccionada == '2':
        lista_reviews_ind = [] # [[id,ventas]]
        for producto in lifestore_products:
          reviews_suma = 0
          reviews_conteo = 0
          devolucion_conteo = 0
          score = 0
          division = 0
          for venta in lifestore_sales:
            if producto[0] == venta[1]:
              reviews_suma += venta[2]
              reviews_conteo += 1 
              if venta[4] == 1:
                devolucion_conteo += 1
              if reviews_conteo == 0:
                division = 0
              else:
                division = reviews_suma/reviews_conteo
              score = division - devolucion_conteo
          registro_individual = [producto[0],producto[1],division,devolucion_conteo,score]
          lista_reviews_ind.append(registro_individual)

          lista_reviews_min = list(lista_reviews_ind)
          reviews_ordenadas_min = []

          while lista_reviews_min:
            minimo = lista_reviews_min[0][4]
            registro_actual = lista_reviews_min[0]
            for registro in lista_reviews_min:
              if registro[4] < minimo and registro[2] != 0:
                minimo = registro[4]
                registro_actual = registro
            reviews_ordenadas_min.append(registro_actual)
            lista_reviews_min.remove(registro_actual)

        for i in range(20) :
          print(f'El producto número {i+1} con peores reseñas: ', reviews_ordenadas_min[i][1],'tiene una reseña promedio de ',reviews_ordenadas_min[i][2],' y un total de ',reviews_ordenadas_min[i][3],' devoluciones.')
        print('\n')
        opcion_valida = 0
        break


        subopcion2_valida = 1
      elif subopcion2_seleccionada == '3':
        opcion_valida = 0
        break
      else:
        print('Su selección no es parte de las opciones. \nIntente una selección válida')
        subopcion2_seleccionada = input('Teclee su selección: ')
  elif opcion_seleccionada == '3':
    print('Seleccionó los informes de productos más vendidos y productos rezgados. \nHaga una selección del reporte que desea consultar: \n1.- Total de ingresos mensuales.\n2.- Ventas promedio mensuales.\n3.- Total de ventas anuales. \n4.- Meses con más ventas al año.\n5.- Regresar al menú anterior.')
    opcion_valida = 1
    subopcion3_seleccionada = input('Teclee su selección: ')
    subopcion3_valida = 0
    while subopcion3_valida != 1:
      #lista Total ingresos mensuales
      if subopcion3_seleccionada == '1':
        for mes in range(1,13):
          venta_meses = []
          ingreso_mensual = 0
          for producto in lifestore_products:
            ventas = 0
            for venta in lifestore_sales:
              if venta[1] == producto[0] and int(venta[3].split('/')[1]) == mes:
                ventas += 1
            if ventas == 0:
              continue
            else:
              venta_total = ventas*producto[2]
              registro = [producto,venta_total,mes]
              venta_meses.append(registro)
              ingreso_mensual += venta_total
          print(f'La venta del mes {mes} fue de $ {ingreso_mensual}' )  
          for venta in venta_meses:
            print(f'En el mes {venta[2]}, se vendieron $ {venta[1]} en productos del tipo {venta[0][1]}')
          print('\n')
        opcion_valida = 0
        break
        subopcion3_valida = 1
      #lista Ventas promedio mensuales
      elif subopcion3_seleccionada == '2':
        ventas_totales = 0
        ingresos_totales = 0
        for mes in range(1,13):
          venta_meses = []
          ingreso_mensual = 0
          for producto in lifestore_products:
            ventas = 0
            for venta in lifestore_sales:
              if venta[1] == producto[0] and int(venta[3].split('/')[1]) == mes:
                ventas += 1
            if ventas == 0:
              continue
            else:
              venta_total = ventas*producto[2]
              registro = [producto,venta_total,mes]
              venta_meses.append(registro)
              ingreso_mensual += venta_total
              ingresos_totales += ingreso_mensual
              ventas_totales += ventas
        print(f'\nLa venta total en fue de {ventas_totales} unidades, resultando en un promedio mensual de {ventas_totales/12} unidades')
        opcion_valida = 0
        break
        subopcion3_valida = 1
      #lista Total ventas anuales
      elif subopcion3_seleccionada == '3':
        ventas_totales = 0
        ingresos_totales = 0
        for mes in range(1,13):
          venta_meses = []
          ingreso_mensual = 0
          for producto in lifestore_products:
            ventas = 0
            for venta in lifestore_sales:
              if venta[1] == producto[0] and int(venta[3].split('/')[1]) == mes and venta[4] == 0:
                ventas += 1
            if ventas == 0:
              continue
            else:
              venta_total = ventas*producto[2]
              registro = [producto,venta_total,mes]
              venta_meses.append(registro)
              ingreso_mensual += venta_total
              ingresos_totales += ingreso_mensual
              ventas_totales += ventas
        print(f'\nEl ingreso total anual neto de devoluciones fue de ${ingresos_totales} , resultando en un ingreso promedio mensual de ${ingresos_totales/12}')
        opcion_valida = 0
        break
        subopcion3_valida = 1
      #lista Meses con más ventas al años
      elif subopcion3_seleccionada == '4':
        ventas_totales = 0
        ingresos_totales = 0
        venta_meses = []
        for mes in range(1,13):
          ingreso_mensual = 0
          for producto in lifestore_products:
            ventas = 0
            for venta in lifestore_sales:
              if venta[1] == producto[0] and int(venta[3].split('/')[1]) == mes and venta[4] == 0:
                ventas += 1
            if ventas == 0:
              continue
            else:
              venta_total = ventas*producto[2]
              ingreso_mensual += venta_total
              ingresos_totales += ingreso_mensual
              ventas_totales += ventas
          registro = [mes,ingreso_mensual]
          venta_meses.append(registro)

        venta_meses_max = list(venta_meses)
        venta_meses_ordenadas_max = []

        while venta_meses_max:
          maximo = venta_meses_max[0][1]
          registro_actual = venta_meses_max [0]
          for registro in venta_meses_max:
            if registro[1] > maximo:
              maximo = registro[1]
              registro_actual = registro
          venta_meses_ordenadas_max.append(registro_actual)
          venta_meses_max.remove(registro_actual)

        for i in range(12):
          print(f'El mes número {i+1} en ventas: es el mes {venta_meses_ordenadas_max[i][0]} con ventas totales de $ {venta_meses_ordenadas_max[i][1]}')
        subopcion3_valida = 1
        opcion_valida = 0
        break
      elif subopcion3_seleccionada == '5':
        opcion_valida = 0
        break
      else:
        print('Su selección no es parte de las opciones. \nIntente una selección válida')
        subopcion_seleccionada = input('Teclee su selección: ')
  elif opcion_seleccionada == '4':
    print('Ha cerrado sesión exitosamente. \n¡Hasta luego!')
    opcion_valida = 0
    break
  else:
    print('Su selección no es parte de las opciones. \nIntente una selección válida')
    opcion_valida = 0
    opcion_seleccionada = input('Teclee su selección: ')
#While o se cumpla el input correcto, que siga preguntando
#hacer variable bander e iterar mientras no se cumpla
#Depende de tu opción es el mensaje que te muestro de cofirmación de seleción
#Sino, mostrar la opción incorrecta y volver a pedirla

