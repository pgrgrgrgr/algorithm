#include <iostream>
#include <string>
using namespace std;

int main() {
	string word;
	getline(cin, word);

	for (int i = 0; i < word.length(); i++) {
		if (word[i] == 'C' || word[i] == 'A' || word[i] == 'M' || word[i] == 'B' || word[i] == 'R' || word[i] == 'I' || word[i] == 'D' || word[i] == 'G' || word[i] == 'E') {
			continue;
		}
		else {
			cout << word[i];
		}
	}

	return 0;
}
