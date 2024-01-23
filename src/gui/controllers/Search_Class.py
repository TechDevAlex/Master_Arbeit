class search:

    def __init__(self, searchtype, indicator):
        self.searchtype = searchtype
        self.indicator = indicator

    def search_config(self):
        print('Search is ', self.searchtype, 'indicator is', self.indicator)


    def update(self):
        self.indicator = 4

    def compare(self,other):
        if self.indicator == other.indicator:
            return True
        else:
            return False

search1 = search('range', 1)
search2 = search('fixed', 2)


search1.search_config()
search2.search_config()

search1.compare(search2)


class Car:

    wheels = 4

    def __init__(self):
        self.mil = 10
        self.com = 'BMW'


c1 = Car()
c2 = Car()

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)


#class range search
#class simple search
#class complex search


class Student:

    school = 'Gymnasium'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return(self.m1+self.m2+self.m3)/3

    def get_m1(self):
        return self.m1

    def set_m1(self,value):
        self.m1 = value

    @classmethod
    def getSchool(cls):
        return cls.school
    @staticmethod
    def info():
        print('This is student class... in abc module')

s1 = Student(23, 45, 78)
s2 = Student(10, 30, 20)

print(s1.avg())


Student.info()


class Student1:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno= rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = Student1('Niko', 2)

s1.show()


class A:

    def __init__(self):
        print('in A init')

    def feature1(self):
        print('feature1-A working')

    def feature2(self):
        print('feature2 working')


class B:

    def __init__(self):
        super().__init__()
        print('in B init')

    def feature1(self):
        print('feature1_B working')

    def feature4(self):
        print('feature4 working')

class C(A,B):

    def __init_(self):
        super().__init__()
        print('in C init')

    def feat(self):
        super().feature2()



a1 = C()
a1.feature1()
a1.feat()


class PyCharm:

    def execute(self):
        print('Compiling')
        print('Running')

class MyEditor:

    def execute(self):
        print('Spell Check')
        print('Convention Check')
        print('Compiling')
        print('Running')

class Laptop1():

    def code(self, ide):
        ide.execute()

ide = MyEditor()


lap1 = Laptop1()
lap1.code(ide)

a = 5
b = 6

print(int.__add__(a,b))


class Student2():

    def __init__(self, m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2

        s3 = Student2(m1, m2)
        return s3

    def __gt__(self, other):
        r1 =self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False


s1 = Student2(38,29)
s2 = Student2(59,40)

s3 = s1 + s2

print(s3.m1)

if s1 > s2:
    print('s1 wins')
else:
    print('s2 wins')


class Student3:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None,b=None,c=None):
        s = 0

        if a!=None and b!=None and c!=None:
            s = a+b+c

        elif a!=None and B!=None:
            s = a+b

        else:
            s = a


        return s

s5 = Student3(58,29)
print(s5.sum(5,9,6))


class Z:

    def show(self):
        print('in Z show')


#class X(Z):

    #def show(self):


#z1 = X()
#z1.show()


class Laptop2:
    def __init__(self, brand, cpu):
        self.brand = brand
        self.memory = self.Memory()
        self.cpu = cpu

    def print_details(self):
        print(self.brand, self.memory.size, self.cpu)

    class Memory:
        def __init__(self):
            self.size = '8gb'



hp_laptop = Laptop2('HP', 'i7')

hp_laptop.print_details()

class Employee:

    num_of_emp = 0
    raise_amount = 1.04

    def __init__(self, first_name, last_name, pay=None):
        self.first = first_name
        self.last = last_name
        self.pay = pay
        #self.email = first_name + '.' + last_name + '@company.com'

        Employee.num_of_emp += 1

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    def apply_raise(self):
        self.pay = int(self.pay *self.raise_amount)


    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or  day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay )

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

class Developer (Employee):
    raise_amount = 1.1

    def __init__(self, first_name, last_name, pay, prog_lang):
        super().__init__(first_name, last_name, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first_name, last_name, pay, employees = None):
        super().__init__(first_name, last_name, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp  in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())






dev_1 = Developer('alex', 'stahl', 10000, 'python')
dev_2 = Developer('matthias', 'fehlner', 20000, 'python')

mgr_1 = Manager('Niko', 'Nagengast', 90000, [dev_1])


mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

print(issubclass(Developer,Employee))

emp_1 = Employee('michi', 'frisch')
print(emp_1)

emp_1.first = 'Niko'

print(emp_1.email)

'''
print(dev_1.email)
print(dev_1.prog_lang)
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

import datetime
my_date = datetime.date(2024, 1, 17)

print(Employee.is_workday(my_date))


emp_1 = Employee('Niko', 'Nagengast', 50000)
emp_2 = Employee('Test', 'User', 60000)

Employee.set_raise_amt(1.05)
emp_str_1 = 'Toni-Kopf-70000'

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)


print(Employee.raise_amount)


'''

