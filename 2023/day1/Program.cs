using System;

string[] input = File.ReadAllLines("input.txt");

int GetLineValue(string line)
{
    bool first = true;
    char firstDigit = new char();
    char lastDigit = new char();
    foreach (char c in line) {
        if (char.IsDigit(c)) {
            lastDigit = c;
            if (first) {
                firstDigit = c;
                first = false;
            }
        }
    }
    char[] chars = { firstDigit, lastDigit };
    string lineValueString = new string(chars);
    int lineValue = Int32.Parse(lineValueString);
    return lineValue;
}

int GetTotalValue(string[] input)
{
    int totalValue = 0;
    foreach (string line in input) {
        totalValue += GetLineValue(line);
    }
    return totalValue;
}

Console.WriteLine(GetTotalValue(input));