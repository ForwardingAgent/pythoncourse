import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwars):
        self.kwars = kwars
        self.cont()
        self.match = 0
        self.all_removed_balls = []

    def cont(self):
        self.contents = []
        for self.k, self.v in self.kwars.items():
            for _ in range(self.v):
                self.contents.append(self.k)
        return self.contents

    def draw(self, balls_amount):
        # draw принимает аргумент, указывающий количество шаров, 
        # которые нужно извлечь из шляпы. Этот метод должен случайным образом
        # удалять шары из содержимого и возвращать эти шары в виде списка строк.
        # Шары не должны возвращаться в шляпу во время розыгрыша.
        # Если количество шаров для розыгрыша превышает доступное количество, верните все шары.
        self.removed_balls = []
        self.balls_amount = balls_amount
        if self.balls_amount > len(self.contents):
            self.contents = self.contents + self.all_removed_balls
            return self.contents
        else:
            for i in range(self.balls_amount):
                self.ball = random.choice(self.contents)
                self.removed_balls.append(self.ball)
                self.contents.remove(self.ball)
        return self.removed_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    for _ in range(num_experiments):
        dic_removed_balls = {}  # словарь для сравнения с expected_balls
        the_hat = copy.deepcopy(hat)
        removed_balls = the_hat.draw(num_balls_drawn)  # вытаскиваем шары
        for m in removed_balls:
            dic_removed_balls[m] = removed_balls.count(m)
        count = 0
        for k, v in expected_balls.items():
            if k in dic_removed_balls:
                if dic_removed_balls[k] >= expected_balls[k]:
                    count = count + 1
                    if count == 2:
                        hat.match += 1
            else:
                break
    return print(hat.match / num_experiments)


hat = Hat(red=5, blue=2)
print(hat.draw(2))
hat = Hat(blue=3, red=2, green=6)
probability = experiment(
    hat=hat,
    expected_balls={"blue": 2, "green": 1},  # ожидаемые шары
    num_balls_drawn=4,  # количество вынимаемых шаров
    num_experiments=1000)  # количество экспериментов N
    # надо посчитать сколько раз М мы получим ожидаемые шары
    # M/N - вероятность
