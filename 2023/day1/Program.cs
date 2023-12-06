using System;

string[] input = File.ReadAllLines("input.txt");

int valueTotal = 0;

foreach (string line in input)
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
    string valueLineString = new string(chars);
    int valueLine = Int32.Parse(valueLineString);
    valueTotal += valueLine;
}

Console.WriteLine(valueTotal);