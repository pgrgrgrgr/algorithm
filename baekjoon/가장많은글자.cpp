#include <iostream>
#include <string>
using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int alphabets[26] = { 0, }; 
	int max_alpha = -1; 
	string s;

	while (!cin.eof()) { 
		getline(cin, s); 

		for (int i = 0; i < s.size(); i++) { 
			if ('a' <= s[i] && s[i] <= 'z') { 
				alphabets[s[i] - 'a']++; 
			}
		}
	}

	for (int i = 0; i < 26; i++) {
		if (max_alpha < alphabets[i]) { 
			max_alpha = alphabets[i]; 
		}
	}

	for (int i = 0; i < 26; i++) {
		if (max_alpha == alphabets[i]) { 
			cout << char('a' + i);
		}
	}
}
