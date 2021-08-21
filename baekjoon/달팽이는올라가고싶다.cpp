#include <iostream>

int main() {
	int a, b, v;
	int days = 0;

	std::cin >> a >> b >> v;
	
	days = (v - b) % (a - b) == 0 ? (v - b) / (a - b) : (v - b) / (a - b) + 1;
	if (days < 1) {
		days = 1;
	}
	std::cout << days;
	return 0;
}
