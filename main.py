from rich.console import Console
from os import system, name


def clear_cls():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


console = Console()
shapes = [
    'прямокутник',
    'параллелограмм',
    'рівнобедрений трикутник',
    'прямокутний трикутник',
    'квадрат',
    'ромб'
]


class Program:
    def __init__(self):
        self.start()

    def restart(self):
        question = console.input('Перезапустити программу? (y/n): ')
        if question == 'y':
            self.__init__()
        else:
            console.print('Программа завершена.')

    def start(self):
        clear_cls()
        formatted_shapes = '\n'.join([f'{i + 1}. {shape}' for i, shape in enumerate(shapes)])
        console.print(f'Раді вас бачити, ви можете вибрати одну з таких фігур:\n{formatted_shapes}\n')
        index = int(console.input('Виберіть номер фігури: '))
        self.work(index)

    def work(self, index):
        clear_cls()
        match index:
            case 1:
                a = int(console.input('Введіть довжину (a): '))
                b = int(console.input('Введіть ширину (b): '))
                console.print(f'Площа прямокутника: {a * b} см²')
                self.restart()
            case 2:
                clear_cls()
                a = int(console.input('Введіть довжину (a): '))
                h = int(console.input('Введіть висоту (h): '))
                console.print(f'Площя параллелограмма: {a * h} см²')
                self.restart()
            case 3:
                clear_cls()
                a = int(console.input('Введіть довжину основи (a): '))
                h = int(console.input('Введіть висоту (h): '))
                console.print(f'Площа рівнобедреного трикутника: {(1/2) * a * h} см²')
                self.restart()
            case 4:
                clear_cls()
                a = int(console.input('Введіть перший катет (a): '))
                b = int(console.input('Введіть другий катет (b): '))
                console.print(f'Площа прямокутного трикутника: {(a + b)/2} см²')
                self.restart()
            case 5:
                a = int(console.input('Введіть довжину (a): '))
                b = int(console.input('Введіть ширину (b): '))
                console.print(f'Площа квадрата: {a * b} см²')
                self.restart()
            case 6:
                clear_cls()
                d1 = int(console.input('Введіть першу діагональ (d1): '))
                d2 = int(console.input('Введіть другу диагональ (d2): '))
                console.print(f'Площа ромба: {1/2 * d1 * d2} см²')
            case _:
                clear_cls()
                console.print('Неправильний номер фігури!', style='bold red')
                self.restart()


if __name__ == '__main__':
    Program()
  