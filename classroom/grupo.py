from classroom.asignatura import Asignatura

class Grupo:

    grado = None

    def __init__(self, grupo="grupo predeterminado", asignaturas=[], estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **args):
        for x in args.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=[]):
        if lista is None:
            lista.append(alumno)
            self.listadoAlumnos = self.listadoAlumnos + lista
        else:
            self.listadoAlumnos = lista + [alumno]
    
    def salida(self):
        print("Grupo de estudiantes: ",self._grupo)

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
