#Дерево. Несколько полных кодов разграничим #######################
class BinaryTree: #Класс узла
    def __init__(self, value): #Конструктор
        self.value = value # и значение что он хранит
        self.left_child = None #Инициализировали потомков
        self.right_child = None #Пока что значения пустые

    def insert_left(self, next_value): #Левый потомок
        if self.left_child is None: #Если в текущем узле нет потомка то-
            self.left_child = BinaryTree(next_value) #-новый узел вставляется на его место
        else: #Иначе он остается таким же левым потомком но уже нового узла
            new_child = BinaryTree(next_value)
            new_child.left_child = self.left_child
            self.left_child = new_child
        return self

    def insert_right(self, next_value): #Правый потомок
        if self.right_child is None: #Тут всё тоже самое что и с левым
            self.right_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.right_child = self.right_child
            self.right_child = new_child
        return self

#Виды обходов дерева(поиска) в глубину
    def pre_order(self): #Метод префиксного обхода в глубину
        print(self.value)  # процедура обработки

        if self.left_child is not None:  # если левый потомок существует
            self.left_child.pre_order()  # рекурсивно вызываем функцию

        if self.right_child is not None:  # если правый потомок существует
            self.right_child.pre_order()  # рекурсивно вызываем функцию


    def post_order(self):#Метод постфиксного обхода в глубину
        if self.left_child is not None:  # если левый потомок существует
            self.left_child.post_order()  # рекурсивно вызываем функцию

        if self.right_child is not None:  # если правый потомок существует
            self.right_child.post_order()  # рекурсивно вызываем функцию

        print(self.value)  # процедура обработки

def in_order(self): #Метод инфиксного обхода в глубину
    if self.left_child is not None: # если левый потомок существует
        self.left_child.in_order() # рекурсивно вызываем функцию

    print(self.value) # процедура обработки

    if self.right_child is not None: # если правый потомок существует
        self.right_child.in_order() # рекурсивно вызываем функцию


A_node = BinaryTree('A').insert_left('B').insert_right('C')
#Задание 22.5.5 СМОТРЕТЬ КАРТИНКУ ТАМ ОБЯЗАТЕЛЬНО
# создаём корень и его потомков /7|2|5\
node_root = BinaryTree(2).insert_left(7).insert_right(5)
# левое поддерево корня /2|7|6\
node_7 = node_root.left_child.insert_left(2).insert_right(6)
# правое поддерево предыдущего узла /5|6|11\
node_6 = node_7.right_child.insert_left(5).insert_right(11)
# правое поддерево корня /|5|9\
node_5 = node_root.right_child.insert_right(9)
# левое поддерево предыдущего узла корня /4|9|\
node_9 = node_5.right_child.insert_left(4)

node_root.post_order()
###################################################################################################
#Создаём собственную структуру данных
class Node:  # класс элемента
    def __init__(self, value=None, next_=None):  # инициализируем
        self.value = value  # значением
        self.next = next_  # и ссылкой на следующий элемент

    def __str__(self):
        return "Node value = " + str(self.value)


class LinkedList:  # класс списка
    def __init__(self):  # инициализируем пустым
        self.first = None
        self.last = None

    def clear(self):  # очищаем список
        self.__init__()

    def __str__(self):  # функция печати
        R = ''

        pointer = self.first  # берем первый указатель
        while pointer is not None:  # пока указатель не станет None
            R += str(pointer.value)  # добавляем значение в строку
            pointer = pointer.next  # идем дальше по указателю
            if pointer is not None:  # если он существует добавляем пробел
                R += ' '
        return R

    def pushleft(self, value): #вставляет новый элемент в начало списка то есть влево
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value, self.first)
            self.first = new_node

    def pushright(self, value): #Вставляет элемент в конец списка то есть в правую часть
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value)
            self.last.next = new_node
            self.last = new_node


    #Удалить элемент из начала списка легко
    def popleft(self):
        if self.first is None:  # если список пустой, возвращаем None
            return None
        elif self.first == self.last:  # если список содержит только один элемент
            node = self.first  # сохраняем его
            self.__init__()  # очищаем
            return node  # и возвращаем сохраненный элемент
        else:
            node = self.first  # сохраняем первый элемент
            self.first = self.first.next  # меняем указатель на первый элемент
            return node  # возвращаем сохраненный

    #А вот из конца удалить чуть сложнее
    def popright(self):
        if self.first is None:  # если список пустой, возвращаем None
            return None
        elif self.first == self.last:  # если список содержит только один элемент
            node = self.first  # сохраняем его
            self.__init__()  # очищаем
            return node  # и возвращаем сохраненный элемент
        else:
            node = self.last  # сохраняем последний
            pointer = self.first  # создаем указатель
            while pointer.next is not node:  # пока не найдем предпоследний
                pointer = pointer.next
            pointer.next = None  # обнуляем указатели, чтобы
            self.last = pointer  # предпоследний стал последним
            return node  # возвращаем сохраненный

############################################################################################
#Задание 22.6.3
class Node:  # класс элемента
    def __init__(self, value=None, next=None):  # инициализируем
        self.value = value  # значением
        self.next = next  # и ссылкой на следующий элемент


    def __str__(self):
        return "Node value = " + str(self.value)


class LinkedList:  # класс списка
    def __init__(self):  # инициализируем пустым
        self.first = None
        self.last = None


    def clear(self):  # очищаем список
        self.__init__()


    def __str__(self):  # функция печати
        R = ''


        pointer = self.first  # берем первый указатель
        while pointer is not None:  # пока указатель не станет None
            R += str(pointer.value)  # добавляем значение в строку
            pointer = pointer.next  # идем дальше по указателю
            if pointer is not None:  # если он существует добавляем пробел
                R += ' '
        return R


    def pushleft(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value, self.first)
            self.first = new_node


    def pushright(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value)
            self.last.next = new_node
            self.last = new_node


    def popleft(self):
        if self.first is None: # если список пустой, возвращаем None
            return None
        elif self.first == self.last: # если список содержит только один элемент
            node = self.first # сохраняем его
            self.__init__() # очищаем
            return node # и возвращаем сохраненный элемент
        else:
            node = self.first # сохраняем первый элемент
            self.first = self.first.next # меняем указатель на первый элемент
            return node # возвращаем сохраненный


    def popright(self):
        if self.first is None:  # если список пустой, возвращаем None
            return None
        elif self.first == self.last:  # если список содержит только один элемент
            node = self.first  # сохраняем его
            self.__init__()  # очищаем
            return node  # и возвращаем сохраненный элемент
        else:
            node = self.last  # сохраняем последний
            pointer = self.first  # создаем указатель
            while pointer.next is not node:  # пока не найдем предпоследний
                pointer = pointer.next
            pointer.next = None  # обнуляем указатели, чтобы
            self.last = pointer  # предпоследний стал последним
            return node  # возвращаем сохраненный


LL = LinkedList()

LL.pushright(1)
LL.pushleft(2)
LL.pushright(3)
LL.popright()
LL.pushleft(4)
LL.pushright(5)
LL.popleft()

print(LL)

############################################################################################################
#Превратим класс в итератор
def __iter__(self): # объявляем класс как итератор
    self.current = self.first # в текущий элемент помещаем первый
    return self # возвращаем итератор

def __next__(self): # метод перехода
    if self.current is None: # если текущий стал последним
        raise StopIteration # вызываем исключение
    else:
        node = self.current # сохраняем текущий элемент
        self.current = self.current.next # совершаем переход
        return node # и возвращаем сохраненный

def __len__(self):
    count = 0
    pointer = self.first
    while pointer is not None:
        count += 1
        pointer = pointer.next
    return count
