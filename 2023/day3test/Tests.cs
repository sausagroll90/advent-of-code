using Xunit;

public class Tests
{
    [Fact]
    public void TestGetNumbersFromLine()
    {
        string testLine = File.ReadLines("../../../testinput.txt").First();

        List<(string, int)> expected = new List<(string, int)>([ ("467", 0), ("114", 5) ]);
        List<(string, int)> actual = Solution.GetNumbersFromLine(testLine);

        Assert.Equal(expected, actual);
    }

    [Fact]
    public void TestGetNumbersFromLine2()
    {
        string testLine = ".123";

        List<(string, int)> expected = new List<(string, int)>([("123", 1)]);
        List<(string, int)> actual = Solution.GetNumbersFromLine(testLine);

        Assert.Equal(expected, actual);
    }

    [Fact]
    public void TestGetAllNumbers()
    {
        string[] testInput = File.ReadAllLines("../../../testinput.txt");

        List<List<(string, int)>> expected = new List<List<(string, int)>>([[("467", 0), ("114", 5)], [], [("35", 2), ("633", 6)]]);
        List<List<(string, int)>> actual = Solution.GetAllNumbers([testInput[0], testInput[1], testInput[2]]);

        Assert.Equal(expected, actual);
    }

    [Fact]
    public void TestIsPartNumber1()
    {
        string[] testInput = [
            ".*.......$",
            "..23..498.",
            ".100...5..",
            "%.......@."
        ];

        Assert.True(Solution.IsPartNumber(("23", 2), 1, testInput));
    }

    [Fact]
    public void TestIsPartNumber2()
    {
        string[] testInput = [
            ".*.......$",
            "..23..498.",
            ".100...5..",
            "%.......@."
        ];

        Assert.True(Solution.IsPartNumber(("498", 6), 1, testInput));
    }

    [Fact]
    public void TestIsPartNumber3()
    {
        string[] testInput = [
            ".*.......$",
            "..23..498.",
            ".100...5..",
            "%.......@."
        ];

        Assert.True(Solution.IsPartNumber(("100", 1), 2, testInput));
    }

    [Fact]
    public void TestIsPartNumber4()
    {
        string[] testInput = [
            ".*.......$",
            "..23..498.",
            ".100...5..",
            "%.......@."
        ];

        Assert.True(Solution.IsPartNumber(("5", 7), 2, testInput));
    }

    [Fact]
    public void TestIsPartNumber5()
    {
        string[] testInput = ["%123"];

        Assert.True(Solution.IsPartNumber(("123", 1), 0, testInput));
    }

    [Fact]
    public void TestIsPartNumber6()
    {
        string[] testInput = ["123^"];

        Assert.True(Solution.IsPartNumber(("123", 0), 0, testInput));
    }

    [Fact]
    public void TestIsPartNumber7()
    {
        string[] testInput = [
            ".@.",
            "123"
        ];

        Assert.True(Solution.IsPartNumber(("123", 0), 1, testInput));
    }

    [Fact]
    public void TestIsPartNumber8()
    {
        string[] testInput = [
            "123",
            ".@."
        ];

        Assert.True(Solution.IsPartNumber(("123", 0), 0, testInput));
    }
}