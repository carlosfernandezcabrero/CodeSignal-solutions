#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> a)
{
    vector<int> clean_vector;

    for (int i = 0; i < a.size(); i++)
    {
        if (a[i] == -1)
            continue;
        clean_vector.push_back(a[i]);
    }

    sort(clean_vector.begin(), clean_vector.end());

    for (int i = 0; i < a.size(); i++)
    {
        if (a[i] == -1)
            continue;
        a[i] = clean_vector[0];
        clean_vector.erase(clean_vector.begin());
    }

    return a;
}
