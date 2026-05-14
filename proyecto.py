nombre_proyecto = '' #Loacalup
descripcion = '' # donde parcharse en la ciudad
tecnologias = ['HTML', 'Python', 'MySQL'] # 
integrantes = ['Sofia Rodas', 'Estefania Restrepo', 'Miguel castro'] 
funcionalidades = [] # ['Login', 'Registro', 'Reportes']

def mostrar_info(): 
    print(f'Proyecto: {nombre_proyecto}')
    print(f'Descripción: {descripcion}')
    print(f'Equipo: {", ".join(integrantes)}')
    print(f'Tecnologías: {", ".join(tecnologias)}')
    print('Funcionalidades:')
    for f in funcionalidades:
        print(f' - {f}')
mostrar_info()