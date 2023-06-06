#include <stdlib.h>
#include <vector>
#include <iostream>
#include <ctime>
#define SIZE 16
#define DIVIDER "--------------------------------------\n"

class Memory
{
private:
    std::vector<std::vector<bool>> memory;
public:
    Memory();
    void Write(std::vector<bool>, int);
    std::vector<std::vector<bool>> getNormalMatrix();
    std::vector<std::vector<bool>> getDiagonalMatrix(std::vector<std::vector<bool>>);
    std::vector<bool> Read(int);
    std::vector<bool> Read_2(int);
    std::vector<bool> getRandomWord();
    std::vector<std::vector<bool>> getElementsInInterval(std::vector<bool>&, std::vector<bool>&);
    std::vector<std::vector<bool>> getMatrix();
    std::vector<bool> function_2(int, int, int);
    std::vector<bool> function_7(int, int, int);
    std::vector<bool> function_8(int, int, int);
    std::vector<bool> function_13(int, int, int);
    void sum(std::vector<bool>);
    std::vector<bool> sumBinaries(std::vector<bool>, std::vector<bool>);
};
inline std::ostream& operator<<(std::ostream& os, const Memory& memory)
{
    Memory mem = memory;
    std::vector<std::vector<bool>> matrix = mem.getMatrix();
    for (int i = 0; i < matrix.size(); i++)
    {
        for (int j = 0; j < matrix[i].size() - 1; j++)
        {
            os << matrix[i][j] << '|';
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
            os << matrix[i][j] << '|';
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
    return os << word[word.size() - 1] << '\n';
}
inline bool operator <(std::vector<bool>& word_1, std::vector<bool>& word_2)
{
    bool g = false;
    bool l = false;
    for (int i = 0; i < word_1.size(); i++)
    {
        g = g | (!word_2[i] & word_1[i] & !l);
        l = l | (word_2[i] & !word_1[i] & !g);
    }
    if (g == 0 && l == 1)
    {
        return true;
    }
    return false;
}
inline bool operator >(std::vector<bool>& word_1, std::vector<bool>& word_2)
{
    bool g = false;
    bool l = false;
    for (int i = 0; i < word_1.size(); i++)
    {
        g = g | (!word_2[i] & word_1[i] & !l);
        l = l | (word_2[i] & !word_1[i] & !g);
    }
    if (g == 1 && l == 0)
    {
        return true;
    }
    return false;
}

Memory::Memory()
{
    std::vector<std::vector<bool>> memory(SIZE, std::vector<bool>(SIZE, 0));
    this->memory = memory;
}
std::vector<std::vector<bool>> Memory::getNormalMatrix()
{
    std::vector<std::vector<bool>> memory;
    for (int i = 0; i < SIZE; i++)
    {
        memory.push_back(this->Read(i));
    }
    return memory;
}
std::vector<std::vector<bool>> Memory::getDiagonalMatrix(std::vector<std::vector<bool>> matrix)
{
    for (int i = 0; i < matrix.size(); i++)
    {
        this->Write(matrix[i], i);
    }
    return this->memory;
}
std::vector<std::vector<bool>> Memory::getMatrix()
{
    return memory;
}
std::vector<std::vector<bool>> Memory::getElementsInInterval(std::vector<bool>& lowerLimitWord, std::vector<bool>& upperLimitWord)
{
    std::vector<std::vector<bool>> target_words;
    for (int i = 0; i < memory.size(); i++)
    {
        if (lowerLimitWord<this->Read(i) && upperLimitWord>this->Read(i))
        {
            target_words.push_back(this->Read(i));
        }
    }
    return target_words;
}
std::vector<bool> Memory::getRandomWord()
{
    std::vector<bool> word;
    for (int i = 0; i < SIZE; i++)
    {
        word.push_back(rand() % 2);
    }
    return word;
}
void Memory::Write(std::vector<bool> word, int address)
{
    for (int i = address; i < SIZE; i++)
    {
        memory[i][address] = word[i - address];
    }
    for (int j = 0; j < address; j++)
    {
        memory[j][address] = word[SIZE - address + j];
    }
}
std::vector<bool> Memory::Read(int address)
{
    std::vector<bool> word;
    for (int i = address; i < SIZE; i++)
    {
        word.push_back(memory[i][address]);
    }
    for (int i = 0; i < address; i++)
    {
        word.push_back(memory[i][address]);
    }
    return word;
}
std::vector<bool> Memory::Read_2(int address)
{
    std::vector<bool> word;
    int tmp_j = 0;
    for (int i = address, j = 0; i < SIZE; i++, j++)
    {
        word.push_back(memory[i][j]);
        tmp_j++;
    }
    if (tmp_j < SIZE)
    {
        for (int j = tmp_j, i = 0; i < SIZE - tmp_j; i++, j++)
        {
            word.push_back(memory[i][j]);
        }
    }
    return word;
}
void Memory::sum(std::vector<bool> V)
{
    for (int i = 0; i < SIZE; i++)
    {
        std::vector<bool> Vj;
        std::vector<bool> word = this->Read(i);
        for (int j = 0; j < 3; j++)
        {
            Vj.push_back(word[j]);
        }
        if (Vj == V)
        {
            std::cout << Vj << V << DIVIDER;
            std::cout << std::hex << i << '\n';
            std::vector<bool> Aj;
            std::vector<bool> Bj;
            for (int k = 3; k < 7; k++)
            {
                Aj.push_back(word[k]);
            }
            for (int k = 7; k < 11; k++)
            {
                Bj.push_back(word[k]);
            }
            std::vector<bool> Sj = this->sumBinaries(Aj, Bj);
            for (int k = 11; k < 16; k++)
            {
                word[k] = Sj[k - 11];
            }
            this->Write(word, i);
        }
    }
}
std::vector<bool> Memory::sumBinaries(std::vector<bool> A, std::vector<bool> B)
{
    std::vector<bool> S;
    bool carry = false;
    for (int i = 3; i >= 0; i--)
    {
        int a = A[i];
        int b = B[i];
        int c = carry;
        if (a + b + c == 3)
        {
            S.insert(S.begin(), 1);
        }
        else if (a + b + c == 2)
        {
            S.insert(S.begin(), 0);
            carry = 1;
        }
        else if (a + b + c == 1)
        {
            carry = 0;
            S.insert(S.begin(), 1);
        }
        else
        {
            S.insert(S.begin(), 0);
        }
    }
    S.insert(S.begin(), carry);
    return S;
}
std::vector<bool> Memory::function_2(int address_1, int address_2, int address_3)
{
    std::vector<bool> word_1 = this->Read(address_1);
    std::vector<bool> word_2 = this->Read(address_2);
    std::vector<bool> result_word;
    for (int i = 0; i < SIZE; i++)
    {
        result_word.push_back(word_1[i] * !word_2[i]);
    }
    this->Write(result_word, address_3);
    return result_word;
}
std::vector<bool> Memory::function_7(int address_1, int address_2, int address_3)
{
    std::vector<bool> word_1 = this->Read(address_1);
    std::vector<bool> word_2 = this->Read(address_2);
    std::vector<bool> result_word;
    for (int i = 0; i < SIZE; i++)
    {
        result_word.push_back(word_1[i] + word_2[i]);
    }
    this->Write(result_word, address_3);
    return result_word;
}
std::vector<bool> Memory::function_8(int address_1, int address_2, int address_3)
{
    std::vector<bool> word_1 = this->Read(address_1);
    std::vector<bool> word_2 = this->Read(address_2);
    std::vector<bool> result_word;
    for (int i = 0; i < SIZE; i++)
    {
        result_word.push_back(!(word_1[i] + word_2[i]));
    }
    this->Write(result_word, address_3);
    return result_word;
}
std::vector<bool> Memory::function_13(int address_1, int address_2, int address_3)
{
    std::vector<bool> word_1 = this->Read(address_1);
    std::vector<bool> word_2 = this->Read(address_2);
    std::vector<bool> result_word;
    for (int i = 0; i < SIZE; i++)
    {
        result_word.push_back(!word_1[i] + word_2[i]);
    }
    this->Write(result_word, address_3);
    return result_word;
}

int main()
{
    Memory memory;
    std::vector<bool> V = { 0,1,1 };
    std::vector<bool> V1 = { 0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1};
    std::vector<bool> V2 = { 0,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1 };
    std::srand(std::time(0));
    for (int i = 0; i < 16; i++)
    {
        memory.Write(memory.getRandomWord(), i);
    }
    std::cout << "Memory:\n" << memory << DIVIDER;
    std::cout << "Normal matrix of memory:\n" << memory.getNormalMatrix() << DIVIDER;
    std::cout << "Address 0x04 Word:  " << memory.Read(0x04) << DIVIDER;
    std::cout << "Address 0x04 Word:  " << memory.Read_2(0x04) << DIVIDER;
    std::cout << "Address 0x0C Word:  " << memory.Read_2(0x0C) << DIVIDER;
    std::cout << "Address 0x00 Word:  " << memory.Read_2(0x00) << DIVIDER;
    std::cout << "Diagonal matrix of memory from normal matrix:\n" << memory.getDiagonalMatrix(memory.getNormalMatrix()) << DIVIDER;
    memory.sum(V);
    std::cout << "Memory after sum(Diagonal view)" << "(For V=)" << V << memory << DIVIDER;
    std::cout << "Memory after sum in normal view:\n" << memory.getNormalMatrix() << DIVIDER;
    std::cout << "Function #2(Reading addresses: 0x00,0x01 Address for writing 0x02):\n" << memory.function_2(0x00, 0x01, 0x02) << DIVIDER;
    std::cout << "Function #7(Reading addresses: 0x03,0x04 Address for writing 0x05):\n" << memory.function_7(0x03, 0x04, 0x05) << DIVIDER;
    std::cout << "Function #8(Reading addresses: 0x06,0x07 Address for writing 0x08):\n" << memory.function_8(0x06, 0x07, 0x08) << DIVIDER;
    std::cout << "Function #13(Reading addresses: 0x09,0x0A Address for writing 0x0B):\n" << memory.function_13(0x09, 0x0A, 0x0B) << DIVIDER;
    std::cout << "Memory after functions:\n" << memory.getNormalMatrix() << DIVIDER;
    std::cout << "Memory after searching:\n" << memory.getElementsInInterval(V1, V2) << DIVIDER;
    return 0;
}   