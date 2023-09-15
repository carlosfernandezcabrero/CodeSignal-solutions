int solution(vector<int> statues)
{
    const vector<int>::iterator minValue = min_element(begin(statues), end(statues));
    const vector<int>::iterator maxValue = max_element(begin(statues), end(statues));
    const short correctSize = (*maxValue - *minValue) + 1;

    return correctSize - statues.size();
}
