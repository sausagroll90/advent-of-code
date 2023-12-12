using Xunit;

public class Tests
{
    static string[] testInput = File.ReadAllLines("../../../testinput.txt");

    [Fact]
    public void TestReplaceSpellingsWithDigits()
    {
        string testString = "onetwothreefourfivesixseveneightnine";

        string expected = "123456789";
        string actual = Solution.ReplaceSpellingsWithDigits(testString);

        Assert.Equal(expected, actual);
    }

    [Fact]
    public void TestReplaceSpellingsWithDigits2()
    {
        List<string> expected = [
            "219",
            "8wo3",
            "abc123xyz",
            "x2ne34",
            "49872",
            "z1ight234",
            "7pqrst6teen"
        ];

        List<string> actual = new List<string>();
        foreach (string line in testInput)
        {
            actual.Add(Solution.ReplaceSpellingsWithDigits(line));
        }

        Assert.Equal(expected, actual);
    }

    [Fact]
    public void TestGetTotalValueWithReplacements()
    {
        int expected = 281;
        int actual = Solution.GetTotalValueWithReplacements(testInput);

        Assert.Equal(expected, actual);
    }
}