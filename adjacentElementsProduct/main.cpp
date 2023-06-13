int solution(vector<int> inputArray)
{
    int majorProduct;

    for (int i = 0; i < inputArray.size() - 1; i++)
    {
        const int actualProduct = inputArray[i] * inputArray[i + 1];

        if (i == 0 || actualProduct > majorProduct)
        {
            majorProduct = actualProduct;
        }
    }

    return majorProduct;
}
