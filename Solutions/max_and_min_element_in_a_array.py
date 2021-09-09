class node:
    def __init__(self):
        self.min = 0
        self.max = 0

def get_min_max(list):
    elem = node()
    elem.min, elem.max = list[0], list[0]
    for i in range(1, len(list)):
        if list[i] < elem.min:
            elem.min = list[i]
        if list[i] > elem.max:
            elem.max = list[i]
    return elem

obj = get_min_max([2, 1, 3, 6])
print(obj.min)
print(obj.max)
