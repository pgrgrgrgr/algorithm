#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

int main()
{
    string A, B;
    cin >> A >> B;

    int res;
    for (int i = 0; i <= B.size() - A.size(); i++)
    {
        int cnt = 0;
        for (int j = 0; j < A.size(); j++)
            if (A[j] == B[i + j]) cnt++;
        res = max(res, cnt);
    }

    cout << A.size() - res << endl;
}
