#include <iostream>
#include <string>
using namespace std;

int main() {
	string lines[5] = { "", };
	for (int i = 0; i < 5; i++) {
		getline(cin, lines[i]);
	}

	for (int i = 0; i < 15; i++) {
		for (int j = 0; j < 5; j++) {
			if (i < lines[j].length())
				cout << lines[j][i];
		}
	}

	return 0;
}
