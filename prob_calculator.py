import random
import copy

class Hat():

#take arguments as list (self.contents)
    def __init__ (self, **all_balls):
        self.contents = []
        for key, value in all_balls.items():
            for i in range(value):
                self.contents.append(key)
        #print(self.contents)

    def draw(self, drawn_num):
        self.drawn_num = drawn_num
        self.drawn_balls = []
        self.remain_balls = copy.copy(self.contents)

        if self.drawn_num <= len(self.contents):
            for i in range(self.drawn_num):
                ranball = self.remain_balls[random.randint(0,len(self.remain_balls)-1)]
                self.remain_balls.remove(ranball)
                self.drawn_balls.append(ranball)

            return self.drawn_balls
        else:
            self.drawn_balls = self.contents
            return self.drawn_balls



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    m=0

    for i in range(num_experiments):
        hat.draw(num_balls_drawn)

# Count each ball and save at dict 'items'
        items=dict()
        for key in hat.contents:
            items[key] = items.get(key,0)

        for key in hat.drawn_balls:
            items[key] = items.get(key,0)+1
        #print(items)

#Compare to remain balls and expected balls
#If remain ball has more than all expected ball return aa as True and m++
        aa=True
        for k in expected_balls:
            if expected_balls[k] > items[k]:
                aa = False

        if aa == True:
            m = m + 1

#print probability
    #print(m)
    print('probability: %f'%(m/num_experiments))




hat1 = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat1, expected_balls={"red":2,"green":1}, num_balls_drawn=5,num_experiments=20000)
