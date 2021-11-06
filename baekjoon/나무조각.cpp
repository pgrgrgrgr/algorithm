#include <iostream> 
using namespace std; 

int main(void) { 
	int pieces[5]; 

	for (int i = 0; i < 5; i++) 
		cin >> pieces[i]; 

	for (int i = 0; i < 4; i++) { 
		for (int j = 0; j < 4 - i; j++) { 
			if (pieces[j] > pieces[j + 1]) { 
				int tmp; 
				tmp = pieces[j]; 
				pieces[j] = pieces[j + 1]; 
				pieces[j + 1] = tmp; 
				for (int k = 0; k < 5; k++) 
					cout << pieces[k] << ' '; 
				cout << endl;
			} 
		} 
	} 
}
