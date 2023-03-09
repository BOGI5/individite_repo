#include "passwordGenerator.h"
#include <iostream>
#include <random>
using namespace std;

string* generatePassword(size_t size, bool difficulty)
// difficulty:
// -> true - generate password with special symbols, digits and letters
// -> false - generate password only with digits or letters
{
    string* password = new string;
    for(size_t i = 0; i < size; i++)
    {
        int symbolCode;
        bool pass = false;
        while(!pass){
            random_device rd; // obtain a random number from hardware
            mt19937 gen(rd()); // seed the generator
            uniform_int_distribution<> distr(33, 126);
            symbolCode = distr(gen);
            if(inRange(symbolCode, difficulty))pass = true;
        }
        password[i] = symbolCode;
    }
    return password;
}


bool inRange(int value, bool difficulty)
// difficulty:
// -> true - generate password with special symbols, digits and letters
// -> false - generate password only with digits or letters
{
    if(value >= 33 && value <= 126)
    {
        if(difficulty) return true;
        else {
            if(value >= '0' && value <= '9')return true;
            else if(value >= 'A' && value <= 'Z')return true;
            else if(value >= 'a' && value <= 'z')return true;
        }
    }
    return false;
}
