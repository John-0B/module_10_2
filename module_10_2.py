from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        sleep(0.4)
        warriors = 100
        for i in range(warriors):
            warriors -= self.power
            if warriors < 0:
                warriors = 0
                i += 1
                print(f'{self.name} сражается {i} суток(сутки), осталось {warriors} воинов.')
            if warriors == 0:
                print(f'{self.name} одержал победу спустя {i} суток(сутки)!')
                break
            print(f'{self.name} сражается {i+1} суток(сутки), осталось {warriors} воинов.')
            sleep(1)


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
third_knight = Knight('Sir Luther', 70)
first_knight.start()
second_knight.start()
third_knight.start()
first_knight.join()
second_knight.join()
third_knight.join()
print('Все битвы закончились!')
