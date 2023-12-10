public class Solution
{
    public static void Main(string[] args)
    {
        string[] lines = File.ReadAllLines("input.txt");

        Console.WriteLine(GetPartNumberTotal(lines));
    }


    public static List<(string, int)> GetNumbersFromLine(string line)
    {
        List<(string, int)> lineNumbers = new List<(string, int)>();

        bool readingNumber = false;
        int startIndex = 0;
        string numStagingArea = "";

        for (int i = 0; i < line.Length; i++)
        {
            if (char.IsDigit(line[i]))
            {
                numStagingArea += line[i];
                if (!readingNumber)
                {
                    startIndex = i;
                    readingNumber = true;
                }
            }
            else if (readingNumber)
            {
                readingNumber = false;
                lineNumbers.Add((numStagingArea, startIndex));
                numStagingArea = "";
            }
        }

        if (!String.IsNullOrEmpty(numStagingArea))
        {
            lineNumbers.Add((numStagingArea, startIndex));
        }

        return lineNumbers;
    }


    public static List<List<(string, int)>> GetAllNumbers(string[] input)
    {
        List<List<(string, int)>> numberList = new List<List<(string, int)>>();

        foreach (string line in input)
        {
            numberList.Add(GetNumbersFromLine(line));
        }

        return numberList;
    }


    public static bool IsPartNumber((string numString, int startIndex) numData, int row, string[] input)
    {
        for (int rowIndex = row - 1; rowIndex <= row + 1; rowIndex++)
        {
            for (int i = numData.startIndex - 1; i <= numData.startIndex + numData.numString.Length; i++)
            {
                try
                {
                    if (!char.IsDigit(input[rowIndex][i]) && input[rowIndex][i].ToString() != ".")
                    {
                        return true;
                    }
                }
                catch (IndexOutOfRangeException) { }
            }
        }
        return false;
    }


    public static int GetPartNumberTotal(string[] input)
    {
        int partNumberTotal = 0;

        List<List<(string, int)>> allNumbers = GetAllNumbers(input);

        for (int row = 0; row < allNumbers.Count; row++)
        {
            foreach ((string numString, int startIndex) numData in allNumbers[row])
            {
                if (IsPartNumber(numData, row, input))
                {
                    partNumberTotal += int.Parse(numData.numString);
                }
            }
        }

        return partNumberTotal;
    }
}
