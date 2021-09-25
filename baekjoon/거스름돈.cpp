  #include <iostream>
using namespace std;

int main() {
	int price;
	cin >> price;

	int cnt = 1;
	int result = 0;

	while (!(price < 10)) {
		price -= 5;
		result++;
	}
	if (price % 2 == 0) {
		result += price / 2;
	}
	else {
		if (price == 1 || price == 3) {
			cout << -1;
			return 0;
		}
		if (price == 5)result += 1;
		if (price == 7)result += 2;
		if (price == 9)result += 3;
	}


	cout << result << endl;
	return 0;
}
