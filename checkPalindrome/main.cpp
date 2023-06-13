bool solution(string inputString)
{
    string reverseWord = inputString;
    reverse(reverseWord.begin(), reverseWord.end());

    return inputString == reverseWord;
}
