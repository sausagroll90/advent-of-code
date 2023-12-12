public class Solution
{

    public static void Main(string[] args)
    {
        string[] input = File.ReadAllLines("input.txt");

        // part 1
        Console.WriteLine($"Calibration value total: {GetTotalValue(input)}");

        // part 2
        Console.WriteLine($"Calibration value total including spelt numbers: {GetTotalValueWithReplacements(input)}");
    }

    public static Dictionary<string, string> numConversions = new Dictionary<string, string>
    {
        { "one", "1" },
        { "two", "2" },
        { "three", "3" },
        { "four", "4" },
        { "five", "5" },
        { "six", "6" },
        { "seven", "7" },
        { "eight", "8" },
        { "nine", "9" }
    };


    public static int GetLineValue(string line)
    {
        bool first = true;
        char firstDigit = new char();
        char lastDigit = new char();
        foreach (char c in line)
        {
            if (char.IsDigit(c))
            {
                lastDigit = c;
                if (first)
                {
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

    public static int GetTotalValue(string[] input)
    {
        int totalValue = 0;
        foreach (string line in input)
        {
            totalValue += GetLineValue(line);
        }
        return totalValue;
    }

    public static string ReplaceSpellingsWithDigits(string line)
    {
        string replaced = line;

        foreach (KeyValuePair<string, string> conversion in numConversions)
        {
            replaced = replaced.Replace(conversion.Key, conversion.Value);
        }

        return replaced;
    }

    public static int GetTotalValueWithReplacements(string[] input)
    {
        int totalValue = 0;
        foreach (string line in input)
        {
            totalValue += GetLineValue(ReplaceSpellingsWithDigits(line));
        }
        return totalValue;
    }
}