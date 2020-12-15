#include <iostream>

using namespace std;

int main() {

	int luckyNums[] = {4, 8, 15, 16,23, 42};
	int test[10];

	test[0] = 26;
	
	cout << test[0] << endl;
	cout << luckyNums[0] << endl;

	for (int c = 0;c < 6;c++) {
		cout << luckyNums[c] << " " << c << endl;
	}

	return 0;
}
