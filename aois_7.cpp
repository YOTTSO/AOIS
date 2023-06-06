#include <vector>
#include <iostream>
#define SIZE 16

class Memory
{
private:
    std::vector<std::vector<bool>> memory;
public:
    void insert(unsigned short&);
    void sort_1();
    void sort_2();//0 - less, 1 - greater
    std::vector<bool> toBinary(unsigned short);
    std::vector<std::vector<bool>> getElementsInInterval(unsigned short&, unsigned short&);
    std::vector<std::vector<bool>> getMatrix();
};
inline std::ostream& operator<<(std::ostream& os, const Memory& memory)
{
    Memory memoryss = memory;
    std::vector<std::vector<bool>> matrix = memoryss.getMatrix();
    for (int i = 0; i < matrix.size(); i++)
    {
        for (int j = 0; j < matrix[i].size() - 1; j++)
        {
            os << matrix[i][j] << ',';
        }
        os << matrix[i][matrix[i].size() - 1] << '\n';
    }
    return os;
}
inline std::ostream& operator<<(std::ostream& os, std::vector<std::vector<bool>> matrix)
{
    for (int i = 0; i < matrix.size(); i++)
    {
        for (int j = 0; j < matrix[i].size() - 1; j++)
        {
            os << matrix[i][j] << ',';
        }
        os << matrix[i][matrix[i].size() - 1] << '\n';
    }
    return os;
}
inline std::ostream& operator<<(std::ostream& os, std::vector<bool> word)
{
    for (int i = 0; i < word.size() - 1; i++)
    {
        os << word[i] << ',';
    }
    return os << word[word.size() - 1];
}
inline bool operator >(std::vector<bool>& word_1, std::vector<bool>& word_2)
{
    for (int i = 0; i < word_1.size(); i++)
    {
        if (word_1[i] == 1 && word_2[i] == 0)
        {
            return true;
        }
        else if (word_2[i] == 1 && word_1[i] == 0)
        {
            return false;
        }
    }
    return false;
}
inline bool operator <(std::vector<bool>& word_1, std::vector<bool>& word_2)
{
    for (int i = 0; i < word_1.size(); i++)
    {
        if (word_1[i] == 1 && word_2[i] == 0)
        {
            return false;
        }
        else if (word_2[i] == 1 && word_1[i] == 0)
        {
            return true;
        }
    }
    return false;
}
inline bool operator ==(std::vector<bool>& word_1, std::vector<bool>& word_2)
{
    for (int i = 0; i < word_1.size(); i++)
    {
        if (word_1[i] != word_2[i])
        {
            return false;
        }

    }
    return true;
}

std::vector<std::vector<bool>> Memory::getMatrix()
{
    return memory;
}
std::vector<bool> Memory::toBinary(unsigned short number)
{
    std::vector<bool> bin;
    while (number != 0)
    {
        bin.insert(bin.begin(), number % 2);
        number /= 2;
    }
    while (bin.size() != 16)
    {
        bin.insert(bin.begin(), 0);
    }
    return bin;
}
void Memory::insert(unsigned short& number)
{
    memory.push_back(toBinary(number));
}
void Memory::sort_1() //0 - less, 1 - greater
{
    for (int i = 0; i < memory.size(); i++) {
        for (int j = 0; j < memory.size() - i - 1; j++) {
            if (memory[j] > memory[j + 1]) {
                std::vector<bool> temp_word = memory[j];
                memory[j] = memory[j + 1];
                memory[j + 1] = temp_word;
            }
        }
    }
}
void Memory::sort_2() //0 - less, 1 - greater
{
    for (int i = 0; i < memory.size(); i++) {
        for (int j = 0; j < memory.size() - i - 1; j++) {
            if (memory[j] < memory[j + 1]) {
                std::vector<bool> temp_word = memory[j];
                memory[j] = memory[j + 1];
                memory[j + 1] = temp_word;
            }
        }
    }
}
std::vector<std::vector<bool>> Memory::getElementsInInterval(unsigned short& lowerLimit, unsigned short& upperLimit)
{
    std::vector<std::vector<bool>> target_words;
    std::vector<bool> lowerLimitWord = toBinary(lowerLimit);
    std::vector<bool> upperLimitWord = toBinary(upperLimit);
    for (int i = 0; i < memory.size(); i++)
    {
        if (lowerLimitWord < memory[i] && memory[i] < upperLimitWord)
        {
            target_words.push_back(memory[i]);
        }
    }
    return target_words;
}

int main()
{
    system("chcp 1251");
    Memory memoryss;
    std::vector<unsigned short> numbers = { 255,6212,2341,23421,7593,20,1234,8139,50000,1 };
    for (uint8_t i = 0; i < numbers.size(); i++)
    {
        memoryss.insert(numbers[i]);
    }
    unsigned short lowerLimit = 500;
    unsigned short upperLimit = 50000;
    std::cout << "Память:\n" << memoryss << '\n';
    std::cout << "Слова между " << memoryss.toBinary(lowerLimit) << " и " << memoryss.toBinary(upperLimit) << '\n';
    std::cout << memoryss.getElementsInInterval(lowerLimit, upperLimit) << '\n';
    memoryss.sort_1();
    std::cout << "Отсортированный результат(возрастание):\n" << memoryss << '\n';
    memoryss.sort_2();
    std::cout << "Отсортированный результат(убывание):\n" << memoryss;
    return 0;
}
