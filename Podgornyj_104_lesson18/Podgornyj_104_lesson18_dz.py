class Tomato:  # Создаем класс Tomato
    # Создаем статическое свойство словаря states, которое будет содержать все стадии созревания помидора
    states = {0: "семечко",
              1: "посадка",
              2: "уход (поливка и окучивание)",
              3: "созрел"}

    # Создаем метод __init__(), внутри которого будут определены два динамических protected свойства:
    def __init__(self, index):
        self._index = index  # передается параметром
        self._state = 0  # Принимает первое значение из словаря states

    def grow(self):  # Создаем метод для перевода томата на следующую стадию созревания
        if self._state < 3:  # Если self._state < 3 (не на последней стадии "созрел"), то
            self._state += 1  # Прибавляем 1 к self._state, чтобы перейти на следующую стадию
        # Выводим на экран номер объекта класса Tomato и стадию на которую он перешел
        print(f"Томат № {self._index} - {Tomato.states[self._state]}")

    def is_ripe(self):  # Создаем метод для проверки, что томат созрел (достиг последней стадии созревания)
        if self._state == 3:  # self._state == 3 (на последней стадии "созрел"), то возвращаем True, иначе False
            return True
        return False


class TomatoBush:  # Создаем класс TomatoBush

    # Определяем метод __init__(), который будет принимать в качестве параметра количество томатов и на его основе будет
    # создавать список объектов класса Tomato. Данный список будет храниться внутри динамического свойства tomatoes.
    def __init__(self, quantity):
        # На основании количества томатов создаем список объектов класса Tomato
        self.tomatoes = [Tomato(index) for index in range(1, quantity + 1)]

    def grow_all(self):  # Создаем метод, который будет переводить все объекты из списка томатов на следующий этап
        # Запускаем цикл (итераций будет столько, сколько будет введено при создании экземпляра класса TomatoBush)
        for tomato in self.tomatoes:
            tomato.grow()  # Метод grow() класса Tomato будет вызван для каждого элемента из списка объектов (Tomato)

    def all_are_ripe(self):  # Создаем метод, который будет возвращать True, если все томаты из списка стали спелыми
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):  # Создаем метод, который будет чистить список томатов после сбора урожая
        self.tomatoes = []


class Gardener:  # Создаём класс Gardener

    # Создайте метод __init__(), внутри которого будут определены два динамических свойства: 1) name - передается
    # параметром, является публичным и 2) _plant - принимает объект класса TomatoBush, является protected
    def __init__(self, name, obj):
        self.name = name
        self._plant = obj

    # Создаем метод, который заставляет садовника работать, что позволяет растению становиться более зрелым
    def work(self):
        print(f"Садовник {self.name} начал работать...")
        # При создании экземпляра класса TomatoBush (self._plant = экземпляр класса TomatoBush),
        # вызывается метод grow_all класса TomatoBush
        self._plant.grow_all()
        print(f"Садовник {self.name} поработал.")

    # Создаем метод, который проверяет, все ли плоды созрели. Если все - садовник собирает урожай.
    # Если нет - метод печатает предупреждение
    def harvest(self):
        if self._plant.all_are_ripe():  # Если все томаты находятся на последней стадии "созрел", то запускаем
            # метод give_away_all для очистки списка объектов класса Tomato
            self._plant.give_away_all()  #
            print(f"Садовник {self.name} собрал томаты.")
        else:
            print('Томат нельзя собирать!')

    @staticmethod  # Создаем статический метод, который выводит в консоль справку по садоводству.
    def knowledge_base():
        print("Инструкция! Если томат находится НЕ на этапе 'созрел', то собирать нельзя.")


Gardener.knowledge_base()  # Вызываем справку по садоводству
tomato_bush = TomatoBush(3)  # Создайте объект класса TomatoBush
gardener = Gardener('Густав', tomato_bush)  # Создайте объект класса Gardener
gardener.work()  # Запускаем метод work() класса Gardener (для ухаживания за томатами)
gardener.work()  # Запускаем опять метод work() класса Gardener (для ухаживания за томатами)
gardener.harvest()  # Запускаем метод harvest() класса Gardener (Проверяем можно ли собрать томаты)
gardener.work()  # Запускаем опять метод work() класса Gardener (для ухаживания за томатами т.к. томаты не созрели)
gardener.harvest()  # Запускаем метод harvest() класса Gardener (Проверяем можно ли собрать томаты)
