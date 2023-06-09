import numpy as np

class Memory:
    def __init__(self):
        self.memory = []

    def to_binary(self, number):
        bin_ = [int(x) for x in bin(number)[2:]]
        while len(bin_) != 16:
            bin_.insert(0, 0)
        return bin_

    def insert(self, number):
        self.memory.append(self.to_binary(number))

    def sort_11(self):
        for i in range(len(self.memory)):
            for j in range(len(self.memory)):
                if self.memory[j] > self.memory[j + 1]:
                    temp_word = self.memory[j]
                    self.memory[j] = self.memory[j+1]
                    self.memory[j+1] = temp_word

    def sort_1(self):
        self.memory.sort()

    def sort_22(self):
        for i in range(len(self.memory)):
            for j in range(len(self.memory)):
                if memory[j] > memory[j + 1]:
                    temp_word = memory[j]
                    memory[j] = memory[j + 1]
                    memory[j + 1] = temp_word

    def sort_2(self):
        self.memory.sort(reverse=True)

    def get_elements_in_interval(self, lower_limit, upper_limit):
        target_words = []
        lower_limit_word = self.to_binary(lower_limit)
        upper_limit_word = self.to_binary(upper_limit)
        for word in self.memory:
            if lower_limit_word < word < upper_limit_word:
                target_words.append(word)
        return target_words

    def get_matrix(self):
        return np.array(self.memory)

    def __str__(self):
        return str(self.get_matrix())

if __name__ == '__main__':
    memory = Memory()
    numbers = [255, 6212, 2341, 23421, 7593, 20, 1234, 8139, 50000, 1]
    for number in numbers:
        memory.insert(number)
    lower_limit = 500
    upper_limit = 50000
    print(f'Память:\n{memory}\n')
    print(f'Слова между {memory.to_binary(lower_limit)} и {memory.to_binary(upper_limit)}:')
    print(memory.get_elements_in_interval(lower_limit, upper_limit))
    memory.sort_1()
    print('Отсортированный результат (возрастание):\n', memory, '\n')
    memory.sort_2()
    print('Отсортированный результат (убывание):\n', memory)