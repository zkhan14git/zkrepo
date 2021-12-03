# Python OOP -- inheritance
import datetime


class Employee(object):
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # Employee.__init__(first, last, pay)
        self.prog_lang = prog_lang


class Mananger(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emps(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emps(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        i = 1
        for emp in self.employees:
            print(f"{i}.  {emp.fullname()} ({emp.email})")
            i += 1


if __name__ == '__main__':
    emp_1 = Developer('Tahir', 'Khan', 5000, 'Python')
    emp_2 = Developer('Amir', 'Khan', 6000, 'Java')
    emp_3 = Developer('Sabir', 'Khan', 7000, 'Django')
    emp_4 = Developer('Waqar', 'Malik', 8000, 'MySQL')


    mgr_1 = Mananger('Sameen', 'Khan', 9000, [emp_1])
    mgr_1.add_emps(emp_2)
    mgr_1.add_emps(emp_3)
    mgr_1.add_emps(emp_4)


    print(f"Manager: {mgr_1.fullname()} ({mgr_1.email})")
    print("Employees:")
    mgr_1.print_emps()
