#include <iostream>

int main() {
	int t;
	std::cin >> t;

	int* harr, * warr, * narr;
	int roomfloor;
	int numcnt = 1;

	harr = (int*)malloc(sizeof(int) * t);
	warr = (int*)malloc(sizeof(int) * t);
	narr = (int*)malloc(sizeof(int) * t);

	for (int i = 0; i < t; i++) {
		std::cin >> harr[i] >> warr[i] >> narr[i];
	}
	
	for (int i = 0; i < t; i++) {
		while (narr[i] > harr[i]) {
			narr[i] -= harr[i];
			numcnt++;
		}
		roomfloor = narr[i];
		if (numcnt >= 10) {
			std::cout << roomfloor <<  numcnt << std::endl;
		}
		else {
			std::cout << roomfloor << 0 << numcnt << std::endl;
		}
		numcnt = 1;
	}

}
