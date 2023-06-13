int solution(int year)
{
    const short int twoDigitsYear = year / 100;
    const short int lowerLimit = twoDigitsYear * 100;

    if (year > lowerLimit)
    {
        return twoDigitsYear + 1;
    }

    return twoDigitsYear;
}
