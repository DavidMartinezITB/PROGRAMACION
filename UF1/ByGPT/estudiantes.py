import signal, sys

estudiantes = {}

menu = f"""{'-' * 50}
GESTION DE ESTUDIANTES
{'-' * 50}
  [1] - Agregar alumno
  [2] - Eliminar alumno
  [3] - Ver alumnos
  [4] - Ver alumno
  [5] - Agregar materia a alumno
  [6] - Eliminar materia a alumno
{'-' * 50}"""

def restart(msg):
    input(f'{msg}\n  Pulsa enter para continuar...')
    main()

def agregar(dni, nombre, curso):
    if dni not in estudiantes:
        estudiantes[dni]= {
            'nombre'    : nombre,
            'curso'     : curso,
            'materias'  : []
        }
    else:
        restart('El alumno ya ha sido registrado!')

def eliminar(dni):
    if dni in estudiantes:
        del estudiantes[dni]
    else:
        restart('El alumno no existe!')

def printAlumno(dni):
    nombre = estudiantes[dni]['nombre']
    curso = estudiantes[dni]['curso']
    materias = estudiantes[dni]['materias']
    
    print(f'  - DNI\t\t{dni}')
    print(f'  - NOMBRE\t{nombre}')
    print(f'  - CURSO\t{curso}')
    if len(materias) != 0:
        print(f'  - MATERIAS')
        for materia in materias:
            print(f'    - {materia}')

def printAlumnos():
    if len(estudiantes) == 0:
        print('  No hay alumnos registrados!')
        return
    
    for i in estudiantes:
        print('-' * 50)
        dni = i
        printAlumno(dni)
    print('-' * 50)

def agregarMateria(dni, materia):
    estudiantes[dni]['materias'].append(materia)

def eliminarMateria(dni, materia):
    estudiantes[dni]['materias'].pop(materia)

def interrupt(signum, frame):
    print('\nSaliendo...')
    print(estudiantes)
    sys.exit(0)

def main():
    print(menu)
    input('    -> ')

if __name__ == '__main__':
    main()