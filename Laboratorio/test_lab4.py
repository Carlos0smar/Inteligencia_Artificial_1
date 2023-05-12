

# EMPTY = None

# lista= [[EMPTY, "\\", EMPTY, EMPTY],
#         ["\\", "/","\\", EMPTY],
#         ["/", "\\", "/", EMPTY ],
#         [EMPTY, "/", EMPTY, EMPTY]]


# final = [[EMPTY, EMPTY, EMPTY, EMPTY],
#         [EMPTY, "/","\\", EMPTY],
#         ["/", "\\", "/", "\\"],
#         [EMPTY, "/", "\\", EMPTY]]


# # for row in lista:
# #     for element in row:
# #             # element = " "
# #         print(element, end=" ")
# #     print()        

# # for f in range(len(lista)):
# #     for c in range(len(lista[f])):
# #             if lista[f][c] is not None:
# #                 print(lista[f][c], end=" " )


# # for f in range(len(lista)):
# #     for c in range(len(lista[f])):
# #         if (lista[f][c] ) != (final[f][c] ):
# #             if lista[f][c] is None:
# #                 print(lista[f][c], end=" " )
# #                 print(f, c, end=" " )


# # for f in range(len(lista)):
# #     for c in range(len(lista[f])):
# #         if (lista[f][c] ) != (final[f][c] ):
# #             if lista[f][c] == "/" or lista[f][c] == "\\":
# #                 print(lista[f][c], end=" " )
# #                 print(f, c, end=" " )






# # Las acciones

# def find_location(lista, final):
#     '''Encuentra la ubicacion de una pieza en el rompecabezas.
#        Devuelve una tupla: fila, columna'''
#     for f in range(len(lista)):
#       for c in range(len(lista[f])):
#           if (lista[f][c] ) != (final[f][c] ):
#               if(lista[f][c] == "/" or lista[f][c] == "\\"):
#                 print(f,c)
#                 return f , c
# estadoo =[[None, None, '\\', None], 
#           [None, '/', '\\', None], 
#           ['/', '\\', '/', '\\'], 
#           [None, '/', None, None]]
# # estadoo = [[None, None, None, None], 
# #  [None, '/', '\\', '\\'], 
# #  ['/', '\\', '/', '\\'], 
# #  [None, '/', None, None]]

# # estado_ = estadoo
# # acciones = []
# # row, column = find_location(estadoo, final)
# # if row > 0:
# #     if estado_[row - 1][column] is None:
# #         acciones.append([row - 1, column])
# #     elif estado_[row - 2][column] == None:
# #         acciones.append([row - 2, column])

# # if row < 3:
# #     if estado_[row + 1][column] is None:
# #         acciones.append([row + 1, column])
# #     elif estado_[row + 2][column] == None:
# #         acciones.append([row + 2, column])
# # if column > 0:
# #     if estado_[row][column - 1] is None:
# #         acciones.append([row, column - 1])
# #     elif estado_[row][column - 2] == None:
# #         acciones.append([row, column - 2])
# # if column < 3:
# #     if estado_[row][column + 1] is None:
# #         acciones.append([row, column + 1])
# #     elif estado_[row][column + 2] == None:
# #         acciones.append([row, column + 2])

# # print(acciones)
# # for accion in acciones:
# #     fila_n, columna_n = accion
# #     print(fila_n, columna_n)


# posiciones_objetivo = []
# for f in range(len(lista)):
#        for c in range(len(lista[f])):
#               if (lista[f][c] ) != (final[f][c] ):
#                      if(lista[f][c] == None): 
#                             posiciones_objetivo.append([f,c])

# for i in range(len(posiciones_objetivo)):
#     fila_n_objetivo, col_n_objetivo = posiciones_objetivo[i]
#     print(fila_n_objetivo, col_n_objetivo)


# row, column = find_location(estadoo, final)

# fila_n1_objetivo, col_n1_objetivo = posiciones_objetivo[0]
# fila_n_objetivo, col_n_objetivo = posiciones_objetivo[1]

# distancia1 = abs(row - fila_n1_objetivo) + abs(column - col_n1_objetivo)
# distancia = abs(row - fila_n_objetivo) + abs(column - col_n_objetivo)
# if distancia1 <= distancia:
#        print(distancia1)
# else:
#        print(distancia)
# # posiciones_objetivo = []
# # for f in range(len(lista)):
# #     for c in range(len(lista[f])):
# #         if (lista[f][c] ) != (final[f][c] ):
# #             if(lista[f][c] == None): 
# #                 posiciones_objetivo.append([f,c])

# # if posiciones_objetivo[0] < posiciones_objetivo[1]: 
# #     fila_n_objetivo, col_n_objetivo = posiciones_objetivo[0]
# #     print(fila_n_objetivo, col_n_objetivo)
# # else:
# #     fila_n_objetivo, col_n_objetivo = posiciones_objetivo[1]
# #     print(fila_n_objetivo, col_n_objetivo)




# # if posiciones_objetivo[0] < posiciones_objetivo[1]: 
# #     fila_n_objetivo, col_n_objetivo = posiciones_objetivo[0]
# # print(fila_n_objetivo, col_n_objetivo)	


# # Node <[[None, None, None, '\\'], 
# #        [None, '/', '\\', None],
# #        ['/', '\\', '/', '\\'], 
# #        [None, '/', None, None]]>


# # Node <[[None, None, '\\', None], 
# #        [None, '/', '\\', None], 
# #        ['/', '\\', '/', '\\'], 
# #        [None, '/', None, None]]>


# # [Node <[[None, None, None, '\\'], 
# #         [None, '/', '\\', None], 
# #         ['/', '\\', '/', '\\'], 
# #         [None, '/', None, None]]>, 

# #  Node <[[None, None, None, '\\'], 
# #         [None, '/', '\\', None], 
# #         ['/', '\\', '/', '\\'], 
# #         [None, '/', None, None]]>]


# # [[None, None, None, '\\'], 
# #  [None, '/', '\\', None], 
# #  ['/', '\\', '/', '\\'], 
# #  [None, '/', None, None]]



# # [[None, '\\', None, None], 
# #  [None, '/', '\\', None], 
# #  ['/', '\\', '/', '\\'], 
# #  [None, '/', None, None]]

# # [[None, None, None, '\\'], 
# #  [None, '/', '\\', None], 
# #  ['/', '\\', '/', '\\'], 
# #  [None, '/', None, None]]

# # [[None, None, None, None], 
# #  [None, '/', '\\', '\\'], 
# #  ['/', '\\', '/', '\\'], 
# #  [None, '/', None, None]]

# # [[None, None, '\\', None], 
# #  [None, '/', '\\', None], 
# #  ['/', '\\', '/', '\\'], 
# #  [None, '/', None, None]]

# # [[None, '\\', None, None], 
# #  [None, '/', '\\', None], 
# #  ['/', '\\', '/', '\\'],
# #    [None, '/', None, None]]

# # [[None, None, None, '\\'], 
# #  [None, '/', '\\', None], 
# #  ['/', '\\', '/', '\\'], 
# #  [None, '/', None, None]]


# # [[None, '\\', None, None], 
# #  ['\\', '/', '\\', None], 
# #  ['/', '\\', '/', None], 
# #  [None, '/', None, None]]
# # [[None, None, None, None], 
# #  [None, '/', '\\', None], 
# #  ['/', '\\', '/', '\\'], 
# #  [None, '/', '\\', None]]

# # [[None, None, None, None], [None, '/', '\\', '\\'], ['/', '\\', '/', '\\'], [None, '/', None, None]]
# # [[None, None, '\\', None], [None, '/', '\\', None], ['/', '\\', '/', '\\'], [None, '/', None, None]]
# # [[None, '\\', None, None], [None, '/', '\\', None], ['/', '\\', '/', '\\'], [None, '/', None, None]]
# # [[None, None, None, '\\'], [None, '/', '\\', None], ['/', '\\', '/', '\\'], [None, '/', None, None]]
# # [[None, None, None, None], [None, '/', '\\', '\\'], ['/', '\\', '/', '\\'], [None, '/', None, None]]
# # [[None, None, '\\', None], [None, '/', '\\', None], ['/', '\\', '/', '\\'], [None, '/', None, None]]
# # [[None, '\\', None, None], [None, '/', '\\', None], ['/', '\\', '/', '\\'], [None, '/', None, None]]
# # [[None, None, None, '\\'], [None, '/', '\\', None], ['/', '\\', '/', '\\'], [None, '/', None, None]]
# # [[None, None, None, None], [None, '/', '\\', '\\'], ['/', '\\', '/', '\\'], [None, '/', None, None]]
# # [[None, None, '\\', None], [None, '/', '\\', None], ['/', '\\', '/', '\\'], [None, '/', None, None]]
# # [[None, '\\', None, None], [None, '/', '\\', None], ['/', '\\', '/', '\\'], [None, '/', None, None]]
# # [[None, None, None, '\\'], [None, '/', '\\', None], ['/', '\\', '/', '\\'], [None, '/', None, None]]
# # [[None, None, None, None], [None, '/', '\\', '\\'], ['/', '\\', '/', '\\'], [None, '/', None, None]]
# # [[None, None, '\\', None], [None, '/', '\\', None], ['/', '\\', '/', '\\'], [None, '/', None, None]]
# # [[None, '\\', None, None], [None, '/', '\\', None], ['/', '\\', '/', '\\'], [None, '/', None, None]]
# # [[None, None, None, '\\'], [None, '/', '\\', None], ['/', '\\', '/', '\\'], [None, '/', None, None]]
# # [[None, None, None, None], [None, '/', '\\', '\\'], ['/', '\\', '/', '\\'], [None, '/', None, None]]
# # [[None, None, '\\', None], [None, '/', '\\', None], ['/', '\\', '/', '\\'], [None, '/', None, None]]
# # [[None, '\\', None, None], [None, '/', '\\', None], ['/', '\\', '/', '\\'], [None, '/', None, None]]
# # [[None, None, None, '\\'], [None, '/', '\\', None], ['/', '\\', '/', '\\'], [None, '/', None, None]]
# # [[None, None, None, None], [None, '/', '\\', '\\'], ['/', '\\', '/', '\\'], [None, '/', None, None]]
# # [[None, None, '\\', None], [None, '/', '\\', None], ['/', '\\', '/', '\\'], [None, '/', None, None]]
# # [[None, '\\', None, None], [None, '/', '\\', None], ['/', '\\', '/', '\\'], [None, '/', None, None]]
# # [[None, None, None, '\\'], [None, '/', '\\', None], ['/', '\\', '/', '\\'], [None, '/', None, None]]
# # [[None, None, None, None], [None, '/', '\\', '\\'], ['/', '\\', '/', '\\'], [None, '/', None, None]]
# # [[None, None, '\\', None],
# #  [None, '/', '\\', None], 
# #  ['/', '\\', '/', '\\'], 
# #  [None, '/', None, None]]

# # [[None, '\\', None, None], [None, '/', '\\', None], ['/', '\\', '/', '\\'], [None, '/', None, None]]
# # [[None, None, None, '\\'], [None, '/', '\\', None], ['/', '\\', '/', '\\'], [None, '/', None, None]]
# # [[None, None, None, None], [None, '/', '\\', '\\'], ['/', '\\', '/', '\\'], [None, '/', None, None]]



# # ode <[[None, None, None, '\\'], 
# #       ['\\', '/', '\\', None], 
# #       ['/', '\\', '/', None], 
# #       [None, '/', None, None]]>
# # 15235
# # Node <[[None, None, '\\', None], 
# #        ['\\', '/', '\\', None], 
# #        ['/', '\\', '/', None], 
# #        [None, '/', None, None]]>


# # Node <[[None, None, '\\', None], 
# #        [None, '/', '\\', '\\'], 
# #        ['/', '\\', '/', None], 
# #        [None, '/', None, None]]>
# # 10708
# # Node <[[None, None, None, '\\'],
# #         [None, '/', '\\', '\\'], 
# #         ['/', '\\', '/', None], 
# #         [None, '/', None, None]]>


# # Node <[[None, None, '\\', None], 
# #        [None, '/', '\\', None], 
# #        ['/', '\\', '/', '\\'], 
# #        [None, '/', None, None]]>
# # 16318
# # Node <[[None, None, None, '\\'], 
# #        [None, '/', '\\', None], 
# #        ['/', '\\', '/', '\\'], 
# #        [None, '/', None, None]]>


# #IMPORTANTEEEEE HATA EL 8 DE DERECHA A ARRIBA

# Node <[[None, '\\', None, None], 
#        ['\\', '/', '\\', None], 
#        ['/', '\\', '/', None], 
#        [None, '/', None, None]]>
# 1
# Node <[[None, None, '\\', None], 
#        ['\\', '/', '\\', None], 
#        ['/', '\\', '/', None], 
#        [None, '/', None, None]]>
# 2
# Node <[[None, None, None, '\\'], 
#        ['\\', '/', '\\', None], 
#        ['/', '\\', '/', None], 
#        [None, '/', None, None]]>
# 3
# Node <[[None, None, '\\', None], 
#        [None, '/', '\\', '\\'], 
#        ['/', '\\', '/', None], 
#        [None, '/', None, None]]>
# 4
# Node <[[None, None, None, '\\'], 
#        [None, '/', '\\', '\\'], 
#        ['/', '\\', '/', None], 
#        [None, '/', None, None]]>
# 5
# Node <[[None, None, '\\', None], 
#        [None, '/', '\\', None], 
#        ['/', '\\', '/', '\\'], 
#        [None, '/', None, None]]>
# 6

# Node <[[None, None, None, '\\'], 
#        [None, '/', '\\', None], 
#        ['/', '\\', '/', '\\'], 
#        [None, '/', None, None]]>
# 7
# Node <[[None, None, '\\', None], 
#        [None, '/', '\\', None], 
#        ['/', '\\', '/', '\\'], 
#        [None, '/', None, None]]>
# 8



# #IMPORTANTE AL REVEEES DE ARRIBA A DERECHA
# Node <[[None, None, None, None], 
#        [None, '/', '\\', None],
#        ['/', '\\', '/', '\\'], 
#        [None, '/', '\\', None]]>
# 1
# Node <[[None, None, None, None], 
#        [None, '/', '\\', None], 
#        ['/', '\\', '/', None], 
#        [None, '/', '\\', '\\']]>
# 2
# Node <[[None, None, None, None], 
#        [None, '/', '\\', None], 
#        ['/', '\\', '/', None], 
#        ['\\', '/', None, '\\']]>
# 3
# Node <[[None, None, None, None], 
#        ['\\', '/', '\\', None], 
#        ['/', '\\', '/', None], 
#        [None, '/', '\\', None]]>
# 4
# Node <[[None, None, None, None], 
#        ['\\', '/', '\\', None], 
#        ['/', '\\', '/', None], 
#        [None, '/', None, '\\']]>
# 5
# Node <[[None, None, None, None], 
#        ['\\', '/', '\\', None], 
#        ['/', '\\', '/', None], 
#        [None, '/', '\\', None]]>
# 6
# Node <[[None, None, None, None], 
#        ['\\', '/', '\\', None], 
#        ['/', '\\', '/', None], 
#        [None, '/', None, '\\']]>
# 7

# #DE IZQUIERDA A ARRIBA
# Node <[[None, None, '/', None], 
#        [None, '/', '\\', '/'], 
#        [None, '\\', '/', '\\'], 
#        [None, None, '\\', None]]>
# 1
# Node <[[None, None, None, '/'], 
#        [None, '/', '\\', '/'], 
#        [None, '\\', '/', '\\'], 
#        [None, None, '\\', None]]>
# 2
# Node <[[None, None, '/', None], 
#        [None, '/', '\\', '/'], 
#        [None, '\\', '/', '\\'], 
#        [None, None, '\\', None]]>
# 3
# Node <[[None, None, None, '/'], 
#        [None, '/', '\\', '/'], 
#        [None, '\\', '/', '\\'], 
#        [None, None, '\\', None]]>
# 4
# Node <[[None, None, '/', None], 
#        [None, '/', '\\', '/'], 
#        [None, '\\', '/', '\\'], 
#        [None, None, '\\', None]]>
# 5
# Node <[[None, None, None, '/'], 
#        [None, '/', '\\', '/'], 
#        [None, '\\', '/', '\\'], 
#        [None, None, '\\', None]]>
# 6

# #DE ARRIBA A IZQUIERDA
# Node <[[None, None, None, None], 
#        [None, '/', '\\', None], 
#        ['/', '\\', '/', '\\'], 
#        [None, '/', '\\', None]]>
# 1
# Node <[[None, None, None, None], 
#        [None, '/', '\\', None],
#        [None, '\\', '/', '\\'], 
#        ['/', '/', '\\', None]]>
# 2
# Node <[[None, None, None, None], 
#        [None, '/', '\\', None], 
#        ['/', '\\', '/', '\\'], 
#        [None, '/', '\\', None]]>
# 3
# Node <[[None, None, None, None], 
#        [None, '/', '\\', None], 
#        [None, '\\', '/', '\\'], 
#        ['/', '/', '\\', None]]>
# 4
# Node <[[None, None, None, None], 
#        [None, '/', '\\', None], 
#        ['/', '\\', '/', '\\'], 
#        [None, '/', '\\', None]]>
# 5
# Node <[[None, None, None, None], 
#        [None, '/', '\\', None], 
#        [None, '\\', '/', '\\'], 
#        ['/', '/', '\\', None]]>
# 6
# Node <[[None, None, None, None], 
#        [None, '/', '\\', None], 
#        ['/', '\\', '/', '\\'], 
#        [None, '/', '\\', None]]>


# #DE ABAJO A IZQUIERDA
# Node <[[None, '\\', '/', None], 
#        ['\\', '/', '\\', '/'], 
#        [None, '\\', '/', None], 
#        [None, None, None, None]]>
# 1
# Node <[[None, None, '/', '\\'], 
#        ['\\', '/', '\\', '/'], 
#        [None, '\\', '/', None], 
#        [None, None, None, None]]>
# 2
# Node <[[None, '\\', '/', None], 
#        [None, '/', '\\', '/'], 
#        [None, '\\', '/', '\\'], 
#        [None, None, None, None]]>
# 3
# Node <[[None, None, '/', '\\'], 
#        [None, '/', '\\', '/'], 
#        [None, '\\', '/', '\\'], 
#        [None, None, None, None]]>
# 4
# Node <[[None, '\\', '/', None], 
#        [None, '/', '\\', '/'], 
#        [None, '\\', '/', '\\'], 
#        [None, None, None, None]]>
# 5
# Node <[[None, None, '/', '\\'], 
#        [None, '/', '\\', '/'], 
#        [None, '\\', '/', '\\'], 
#        [None, None, None, None]]>
# 6
# Node <[[None, '\\', '/', None], 
#        [None, '/', '\\', '/'], 
#        [None, '\\', '/', '\\'], 
#        [None, None, None, None]]>
# 7
# Node <[[None, None, '/', '\\'], 
#        [None, '/', '\\', '/'], 
#        [None, '\\', '/', '\\'], 
#        [None, None, None, None]]>
# 8


# #DE ABOJO A ARRIBA
# Node <[[None, '\\', '/', None], 
#        ['\\', '/', '\\', '/'], 
#        [None, '\\', '/', None], 
#        [None, None, None, None]]>
# 1
# Node <[[None, None, '/', '\\'], 
#        ['\\', '/', '\\', '/'], 
#        [None, '\\', '/', None], 
#        [None, None, None, None]]>
# 2
# Node <[[None, '/', None, '\\'], 
#        ['\\', '/', '\\', '/'], 
#        [None, '\\', '/', None], 
#        [None, None, None, None]]>
# 3
# Node <[[None, None, '/', '\\'], 
#        ['\\', '/', '\\', '/'], 
#        [None, '\\', '/', None], 
#        [None, None, None, None]]>
# 4
# Node <[[None, '/', None, '\\'], 
#        ['\\', '/', '\\', '/'], 
#        [None, '\\', '/', None], 
#        [None, None, None, None]]>
# 5
# Node <[[None, None, '/', '\\'], 
#        ['\\', '/', '\\', '/'], 
#        [None, '\\', '/', None], 
#        [None, None, None, None]]>
# 6
# Node <[[None, '/', None, '\\'], 
#        ['\\', '/', '\\', '/'], 
#        [None, '\\', '/', None], 
#        [None, None, None, None]]>
# 7
# Node <[[None, None, '/', '\\'], 
#        ['\\', '/', '\\', '/'], 
#        [None, '\\', '/', None], 
#        [None, None, None, None]]>
# 8