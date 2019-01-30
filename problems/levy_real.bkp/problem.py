from collections import OrderedDict
class Problem():
    def __init__(self):
        space = OrderedDict()
        nparam = 10
        #problem specific parameters
        for i in range(nparam):
            space['p%d'%(i+1)] = (-10,10)
        self.space = space
        self.params = self.space.keys()
        self.starting_point = [-10] * nparam
        
if __name__ == '__main__':
    instance = Problem()
    print(instance.space)
    print(instance.params)

