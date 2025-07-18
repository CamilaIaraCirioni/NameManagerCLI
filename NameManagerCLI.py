# Program

class NameManagement:
    """
    Manages a collection of student names and provides a simple CLI menu,
    """

    def __init__(self) -> None:
        """
        Initialize the Alumnos class with
        an empy set of student names and an option list
        """
        self.names = set()
        self.option = None
        self.exit = False

    def get_option(self):
        """Prompt the user to enter a number option between 1 and 5.

        Keeps asking until a valid integer is entered to prevent input errors.

        Returns:
            int: The user-selected option as an integer.
        """
        while True:
            try:
                option = int(input("\nChoose an option between 1 and 5: "))
                return option
            except ValueError:
                print("Only numbers allowed. Please try again.")

    def validate_option(self):
        """
        Continuosly prompt the user until a valid option
        between 1 and 5 is entered
        """
        while True:
            self.option = self.get_option()
            if 0 < self.option <= 5:
                return self.option
            print("Only 1 - 5 options")

    def display_menu(self):
        """
        Display the main menu to the user
        """
        print("__________________________________________________")
        print("WELCOME TO THE MENU. CHOOSE AN OPTION")
        print("1 - Add Names")
        print("2 - List Names")
        print("3 - Search Names")
        print("4 - Modify Name")
        print("5 - Exit Program")
        print("__________________________________________________")

    def handle_menu_action(self):
        """
        Execute the corresponding menu funtion
        based on the user's selected option
        """
        if self.option == 1:
            self.add_name()
        elif self.option == 2:
            self.list_students()
        elif self.option == 3:
            self.search_students()
        elif self.option == 4:
            self. update_names()
        elif self.option == 5:
            self.exit_program()

    def add_name(self):
        name=self.get_valid_name("Enter name: ")
        if name in self.names:
            print("\nName already exists")    
        else:
            self.names.add(name)
            print("\nName added successfully")
               

    def validate_name(self, name):
        return name.replace(" ", "").isalpha()

    def get_name(self, msg="Enter name: "):
        name=input(msg).strip()
        return name
    
    def get_valid_name(self,msg):
        while True:
            name = self.get_name(msg)

            if self.validate_name(name):
                return name   
            else: 
                print("\nInvalid input. Only letters allowed.")  
    
    def get_list(self):
        """ 
        returns:
            List: A sorted list of student names sored in the 'nombre' set.
        """
        return sorted(self.names)
    
    def list_students(self):
        """
            Prints the list of student names in alfabetical order.
            If not student are registered. It prints a message indicating that the list is empty.
        """
        students=self.get_list()
        if students:
            for student in students:
                print(f"- {student}")   
        else:
            print("The list is empty.")  

    def search_students(self):
        name = self.get_valid_name("Enter name to search: ")
        if name in self.names:
            print(f"\n{name} was found.") 
        else:
            print(f"\n{name} not found.")


    def get_old_name(self):
        old_name = self.get_valid_name("Enter name to search: ")
        return old_name

    def get_new_name(self):
        new_name = self.get_valid_name("Enter new name: ")
        return new_name

    def validate_old_and_new_names(self):
        old_name = self.get_old_name()
        
        if old_name in self.names:
            print(f"\n{old_name} was found.")
            new_name = self.get_new_name()
            if new_name == old_name:
                print("\nThe new name is the same as the current name. No changes were made.")
                return None, None
            if new_name in self.names:
                print(f"\n{new_name} already taken. Cannot be modified.")
                return None, None
            else:
                print("Valid name. Ready to be added.")
                return old_name, new_name

        else:
            print(f"\n{old_name} not found")
            return None, None


    def update_names(self):
        old_name, new_name = self.validate_old_and_new_names()
        if old_name and new_name:
            self.names.remove(old_name)
            self.names.add(new_name)
            print("\n Successfully modified")
        else:
            print("\n No changes were made")


 

    def exit_program(self):
        print("Exiting program")
        self.exit = True


def start_menu():
    name = NameManagement()
    while not name.exit:
        name.display_menu()
        name.validate_option()
        name.handle_menu_action()


try:
    if __name__ == "__main__":
        start_menu()
except KeyboardInterrupt:
    print("\nProgram exited by user with Ctrl+C")
