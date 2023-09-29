# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


class ABACStudent():
    def __init__(self, student_id: int, student_name: str, previous_institute: str, credits: int, gpa: float):
        self.__student_id = student_id
        self.__student_name = student_name
        self.__previous_institute = previous_institute
        self.__credits = credits
        self.__gpa = gpa

    def display(self):
        return str(self.__student_id) + self.__student_name

    def display_gpa(self):
        return print('GPA earned:' + f"{self.__student_name}" +': '+ f"{str(self.__gpa)}")

    def display_credits_earned(self):
        return print('Credits earned:' + f"{self.__student_name}" + ':' + f"{self.__credits}")


class MSMEStudent(ABACStudent):
    def __init__(self,student_id,student_name,major: str,specialization: str,certificate: str):
        super().__init__(student_id, student_name)
        self.__major = major
        self.__specialization = specialization
        self.__certificate = True

    def display_major(self):
        print('Major:' + f"{self.__student_name}" + ':' + f"{self.__major}")

    def display_certification(self):
        if self.__certificate:
            print(f"{self.__student_name}" + 'has earned a certificate.')
        else:
            print(f"{self.__student_name}" +  'has not earned a certificate.')

