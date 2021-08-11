#include <iostream>

int main() {
	int a, b, c;
	int num_sell = 0;

	std::cin >> a >> b >> c;

	if (b >= c) {
		std::cout << -1;
	}
	else {
		while (num_sell < a / (c - b)) {
			num_sell += 1;
		}
		std::cout << num_sell + 1;
	}
}
