string[] input = File.ReadAllLines("input.txt");

int GetGameNum(string line)
{
    return Int32.Parse(line.Substring(line.IndexOf(" ") + 1, line.IndexOf(":") - line.IndexOf(" ") - 1));
}

string[] GetSets(string line)
{
    return line.Substring(line.IndexOf(":") + 1).Split(';');
}

bool IsSetPossible(string set)
{
    bool isPossible = true;
    string[] totals = set.Split(",");

    foreach (string total in totals)
    {
        string colour = total.Substring(total.LastIndexOf(" ") + 1);
        switch (colour)
        {
            case "red":
                if (Int32.Parse(total.Substring(1, total.LastIndexOf(" "))) > 12)
                {
                    isPossible = false;
                }
                break;

            case "green":
                if (Int32.Parse(total.Substring(1, total.LastIndexOf(" "))) > 13)
                {
                    isPossible = false;
                }
                break;

            case "blue":
                if (Int32.Parse(total.Substring(1, total.LastIndexOf(" "))) > 14)
                {
                    isPossible = false;
                }
                break;

        }
    }
    return isPossible;
}

int GetGameValue(string line)
{
    int value = GetGameNum(line);
    string[] sets = GetSets(line);
    foreach (string set in sets)
    {
        if (!IsSetPossible(set)) {
            value = 0;
        }
    }

    return value;
}

int total = 0;

foreach (string line in input)
{
    total += GetGameValue(line);
}

Console.WriteLine(total);