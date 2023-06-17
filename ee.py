#Пример No 1
'''class Counter:
    def __init__(self):
        self.value = 0

    def inc(self):
        self.value += 1

    def dec(self):
        self.value -= 1

class NonDecreasingCounter(Counter):
    def dec(self):
        pass'''
#Пример No 2
'''class A:
    x = 'A'
class B(A):
    x = 'B'
    def super_x(self):
        return super().x

B().x  # 'B'
B().super_x() '''

#Пример No 3
'''class Employee:  
    emp_count = 0  
  
    def __init__(self, name, salary):  
        self.name = name  
        self.salary = salary  
        Employee.emp_count += 1  
  
    def display_count(self):  
        print('Всего сотрудников: %d' % Employee.emp_count)
        
    def display_employee(self):  
        print('Имя: {}. Зарплата: {}'.format(self.name, self.salary))  
  
emp1 = Employee("Андрей", 2000)  
emp2 = Employee("Мария", 5000)  
emp1.display_employee()  
emp2.display_employee()  
print("Всего сотрудников: %d" % Employee.emp_count)'''

#Пример No 4
'''lass Albom:
    def __init__(self):
        self.pages = []
    def add_page(self, page):
        self.pages.append(page)
    def print_pages(self):
        print [tt.number for tt in self.pages]
    def print_image_from_page(self, page):
        for p in self.pages:
            if p.number == page:
                print [pp.name for pp in p.images]
    def draw_horns(self, page, image_name):
        for p in self.pages:
            if p.number == page:
                for n in p.images:
                    if n.name == image_name:
                        n.name = n.name + "_with_horns"'''

#Пример No 5
'''a = Albom()
data = {1: ["cat", "dog"], 2: ["sky"], 3: ["sea", "island"]}
for h in data:
    b = Page(h)
    for d in data[h]:
        c = Image(d)
        b.add_image(c)
    a.add_page(b)

a.print_pages()
a.print_image_from_page(1)
a.draw_horns(1, "dog")
a.print_image_from_page(1)'''

