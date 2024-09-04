class Topping:
    def __init__(self, topping_type, weight):
        self.__topping_type = topping_type
        self.__weight = weight


class Dough:
    def __init__(self, flour_type, baking_technique, weight):
        self.__flour_type = flour_type
        self.__baking_technique = baking_technique
        self.__weight = weight


class Pizza:
    def __init__(self, name, dough:Dough, toppings_capacity):
        self.__name = name
        self.__dough = dough
        self.__toppings = {}
        self.__toppings_capacity = toppings_capacity

    def add_topping(self, topping:Topping):
        if len(self.__toppings.values()) < self.__toppings_capacity:
            if topping.__topping_type in self.__toppings:
                self.__toppings[topping.__topping_type] += topping.__weight
            else:
                self.__toppings[topping.__topping_type] = topping.__weight
        else:
            return "ValueError: Not enough space for another topping"
        
    def calculate_total_weight(self):
        total_weight = self.__dough.__weight
        for weight in self.__toppings.values():
            total_weight += weight
        return total_weight