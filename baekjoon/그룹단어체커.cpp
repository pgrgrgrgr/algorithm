#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
	int N;
	cin >> N;

	int isgroupnum = 0;
	int j = 0;

	for (int i = 0; i < N; i++) {
		string word;
		cin >> word;

		int arr[26] = { 0, };
		arr[word[0] - 97] = 1;

		for (j = 1; j < word.length(); j++) {
			if (word[j] != word[j - 1])
				if (arr[word[j] - 97] == 0)
					arr[word[j] - 97]++;
				else
					break;
		}
		if (j == word.length())
			isgroupnum++;
	}
	cout << isgroupnum;
	return 0;
}
