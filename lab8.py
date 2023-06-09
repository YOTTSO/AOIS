import random

SIZE = 16
DIVIDER = "-----------------------------------"


class Memory:
    def __init__(self):
        memory = [[False] * SIZE for _ in range(SIZE)]
        self.memory = memory

    def __str__(self):
        return format(self.memory)

    def getNormalMatrix(self):
        memory = []
        for i in range(SIZE):
            memory.append(self.ReadFunc(i))
        return memory

    def getDiagonalMatrix(self, matrix):
        for i in range(len(matrix)):
            self.Write(matrix[i], i)
        return self.memory

    def getMatrix(self):
        return self.memory

    def getElementsInInterval(self, lowerLimitWord, upperLimitWord):
        target_words = []
        for i in range(len(self.memory)):
            if lowerLimitWord < self.ReadFunc(i) and upperLimitWord > self.ReadFunc(i):
                target_words.append(self.ReadFunc(i))
        return target_words

    def getRandomWord(self):
        return [random.randint(0, 1) for _ in range(SIZE)]

    def Write(self, word, address):
        for i in range(address, SIZE):
            self.memory[i][address] = word[i - address]
        for j in range(address):
            self.memory[j][address] = word[SIZE - address + j]

    def ReadFunc(self, address):
        word = []
        for i in range(address, SIZE):
            word.append(self.memory[i][address])
        for i in range(address):
            word.append(self.memory[i][address])
        return word

    def ReadFunc_alter(self, address):
        word = []
        tmp_j = 0
        for i in range(address, SIZE):
            word.append(self.memory[i][tmp_j])
            tmp_j += 1
        if tmp_j < SIZE:
            for j in range(tmp_j, SIZE):
                word.append(self.memory[j - tmp_j][j])
        return word

    def sum(self, V):
        for i in range(SIZE):
            Vj = []
            word = self.ReadFunc(i)
            for j in range(3):
                Vj.append(word[j])
            if Vj == V:
                Aj = []
                Bj = []
                for k in range(3, 7):
                    Aj.append(word[k])
                for k in range(7, 11):
                    Bj.append(word[k])
                Sj = self.sumBinaries(Aj, Bj)
                for k in range(11, 16):
                    word[k] = Sj[k - 11]
                self.Write(word, i)

    def sumBinaries(self, A, B):
        S = []
        carry = False
        for i in range(3, -1, -1):
            a = A[i]
            b = B[i]
            c = carry
            if a + b + c == 3:
                S.insert(0, 1)
            elif a + b + c == 2:
                S.insert(0, 0)
                carry = True
            elif a + b + c == 1:
                carry = False
                S.insert(0, 1)
            else:
                S.insert(0, 0)
        S.insert(0, carry)
        return S

    def function_of_two(self, address_1, address_2, address_3):
        word_1 = self.ReadFunc(address_1)
        word_2 = self.ReadFunc(address_2)
        result_word = []
        for i in range(SIZE):
            result_word.append(word_1[i] * (not word_2[i]))
        self.Write(result_word, address_3)
        return result_word

    def function_of_seven(self, address_1, address_2, address_3):
        word_1 = self.ReadFunc(address_1)
        word_2 = self.ReadFunc(address_2)
        result_word = []
        for i in range(SIZE):
            result_word.append(word_1[i] + word_2[i])
        self.Write(result_word, address_3)
        return result_word

    def function_of_eight(self, address_1, address_2, address_3):
        word_1 = self.ReadFunc(address_1)
        word_2 = self.ReadFunc(address_2)
        result_word = []
        for i in range(SIZE):
            result_word.append(not (word_1[i] + word_2[i]))
        self.Write(result_word, address_3)
        int_list = [int(x) for x in result_word]
        return int_list

    def function_of_thirteen(self, address_1, address_2, address_3):
        word_1 = self.ReadFunc(address_1)
        word_2 = self.ReadFunc(address_2)
        result_word = []
        for i in range(SIZE):
            result_word.append(not word_1[i] + word_2[i])
        self.Write(result_word, address_3)
        int_list = [int(x) for x in result_word]
        return int_list

if __name__ == '__main__':
    memor = Memory()
    vec_1 = [0,1,1]
    vec_2 = [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1]
    vec_3 = [0,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1]
    for i in range(16):
        memor.Write(memor.getRandomWord(), i)
    print(f'Исходная память:{memor}')
    print(f'Нормальная матрица: {memor.getNormalMatrix()}')
    print(f'Адрес 0x04: {memor.ReadFunc(0x04)}')
    print(f'Адрес 0x04: {memor.ReadFunc_alter(0x04)}')
    print(f'Адрес 0x0C:{memor.ReadFunc_alter(0x0C)}')
    print(f'Адрес 0x00:{memor.ReadFunc_alter(0x00)}')
    print(f'Диагональная матрица из нормальной для исходной памяти: {memor.getDiagonalMatrix(memor.getNormalMatrix())}')
    memor.sum(vec_1)
    print(f'Память после суммы в диагональном виде: {vec_1}, {memor}')
    print(f'Память после суммы в нормальном виде: {memor.getNormalMatrix()}')
    print(f'Функция №2 {memor.function_of_two(0x00, 0x01, 0x02)}')
    print(f'Функция №7 {memor.function_of_seven(0x03, 0x04, 0x05)}')
    print(f'Функция №8 {memor.function_of_eight(0x06, 0x07, 0x08)}')
    print(f'Функция №13 {memor.function_of_thirteen(0x09, 0x0A, 0x0B)}')
    print(f'Память после функций: {memor.getNormalMatrix()}')
    print(f'Поиск в памяти: {memor.getElementsInInterval(vec_2,vec_3)}')