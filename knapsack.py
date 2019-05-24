class Item(object):
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def get_value(self):
        return self.value
    
    def get_weight(self):
        return self.weight

    def __repr__(self):
        return '({}, {})'.format(self.value, self.weight)


class GreedKnapsack(object):
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.items = []

    def add_items(self, new_items):
        self.items.extend(new_items)

    def get_tip(self, item):
        return item.get_value() / item.get_weight()

    def solve(self):
        result = []

        self.items = sorted(self.items, key=self.get_tip, reverse=True)
        
        #print para testes
        #print(self.items)

        capacity = 0
        for item in self.items:
            if(capacity + item.get_weight() <= self.max_capacity):
                result.append(item)
                capacity += item.get_weight()

        return result

if __name__ == '__main__':
    values = [ 1, 4, 5, 7 ]
    weights = [ 1, 3, 4, 5 ] 

    items = []

    for i in range(len(weights)):
        items.append(Item(values[i], weights[i]))

    greed = GreedKnapsack(7)
    greed.add_items(items)
    print(greed.solve())

    #ler o pdf de computação evolutiva: http://www.inf.ufpr.br/aurora/tutoriais/Ceapostila.pdf
    #considerar isso para o trabalho
    #ga = GAKnapsack(7)
    #ga.add_items(items)
    #print(ga.solve(20))
