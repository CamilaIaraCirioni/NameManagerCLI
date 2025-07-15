# Program

class Alumnos:
    """
    Manages a collection of student names and provides a simple CLI menu,
    """

    def __init__(self) -> None:
        """
        Initialize the Alumnos class with
        an empy set of student names and an option list
        """
        self.nombres = set()
        self.opcion = None
        self.salir = False

    def pedir_opcion(self):
        """Prompt the user to enter a number option between 1 and 5.

        Keeps asking until a valid integer is entered to prevent input errors.

        Returns:
            int: The user-selected option as an integer.
        """
        while True:
            try:
                opcion = int(input("\nIngrese una opcion del 1 al 5: "))
                return opcion
            except ValueError:
                print("Porfavor, ingrese un numero")

    def validar_opcion(self):
        """
        Continuosly prompt the user until a valid option
        between 1 and 5 is entered
        """
        while True:
            self.opcion = self.pedir_opcion()
            if 0 < self.opcion <= 5:
                return self.opcion
            print("Solo opciones de 1 - 5")

    def presentar_menu(self):
        """
        Display the main menu to the user
        """
        print("__________________________________________________")
        print("WELCOME TO THE MENU. CHOOSE AN OPTION")
        print("1 - Cargar Alumnos")
        print("2 - Listar Alumnos")
        print("3 - Buscar Alumnos")
        print("4 - Modificar Alumno")
        print("5 - Finalizar programa")
        print("__________________________________________________")

    def elegir_menu(self):
        """
        Execute the corresponding menu funtion
        based on the user's selected option
        """
        if self.opcion == 1:
            self.agregar_nombre()
        elif self.opcion == 2:
            self.listar_alumnos()
        elif self.opcion == 3:
            self.buscar_alumnos()
        elif self.opcion == 4:
            self. modificar_nombres()
        elif self.opcion == 5:
            self.finalizar_programa()

    def agregar_nombre(self):
        nombre=self.solicitar_nombre_valido("Ingrese nombre: ")
        if nombre in self.nombres:
            print("\nNombre ya existe")    
        else:
            self.nombres.add(nombre)
            print("\nNombre agregado correctamente")
               

    def validar_nombre(self, nombre):
        return nombre.replace(" ", "").isalpha()

    def pedir_nombre(self, mensaje="Ingrese nombre: "):
        nombre=input(mensaje).strip()
        return nombre
    
    def solicitar_nombre_valido(self,mensaje):
        while True:
            nombre = self.pedir_nombre(mensaje)

            if self.validar_nombre(nombre):
                return nombre   
            else: 
                print("\nIncorrecto. Solo letras.")  
    
    def obtener_lista(self):
        """ 
        returns:
            List: A sorted list of student names sored in the 'nombre' set.
        """
        return sorted(self.nombres)
    
    def listar_alumnos(self):
        """
            Prints the list of student names in alfabetical order.
            If not student are registered. It prints a message indicating that the list is empty.
        """
        alumnos=self.obtener_lista()
        if alumnos:
            for alumno in alumnos:
                print(f"- {alumno}")   
        else:
            print("Lista vacia.")  

    def buscar_alumnos(self):
        nombre = self.solicitar_nombre_valido("Ingrese nombre a buscar: ")
        if nombre in self.nombres:
            print(f"\n{nombre} fue encontrado.") 
        else:
            print(f"\n{nombre} no fue encontrado")


    def pedir_nombre_antiguo(self):
        nombre_antiguo = self.solicitar_nombre_valido("Ingrese nombre a buscar:")
        return nombre_antiguo

    def pedir_nombre_nuevo(self):
        nombre_nuevo = self.solicitar_nombre_valido("Ingrese nombre nuevo")
        return nombre_nuevo

    def validar_nombres_antiguo_nuevo(self):
        nombre_antiguo = self.pedir_nombre_antiguo()
        
        if nombre_antiguo in self.nombres:
            print(f"\n{nombre_antiguo} fue encontrado.")
            nombre_nuevo = self.pedir_nombre_nuevo()
            if nombre_nuevo == nombre_antiguo:
                print("\nEl nombre nuevo es igual al nombre actual. No se realizará modificación.")
                return None, None
            if nombre_nuevo in self.nombres:
                print(f"\n{nombre_nuevo} esta usado. No se puede modificar.")
                return None, None
            else:
                print("Nombre valido. Listo para agregar")
                return nombre_antiguo, nombre_nuevo

        else:
            print(f"\n{nombre_antiguo} no fue encontrado")
            return None, None


    def modificar_nombres(self):
        nombre_antiguo, nombre_nuevo = self.validar_nombres_antiguo_nuevo()
        if nombre_antiguo and nombre_nuevo:
            self.nombres.remove(nombre_antiguo)
            self.nombres.add(nombre_nuevo)
            print("\n Modificado correctamente")
        else:
            print("\n No se realizo ninguna modificacion")


 

    def finalizar_programa(self):
        print("Finalizar programa")
        self.salir = True


def iniciar_menu():
    alumno = Alumnos()
    while not alumno.salir:
        alumno.presentar_menu()
        alumno.validar_opcion()
        alumno.elegir_menu()


try:
    if __name__ == "__main__":
        iniciar_menu()
except KeyboardInterrupt:
    print("\nProgram exited by user with Ctrl+C")
