#include <iostream>

using namespace std;

int main() {

	bool isMale = true;
	bool isTall = false;
	
	if (isMale && isTall) {
		cout << "your are a tall male" << endl;
	} 
	else {
		cout << "your are not male" << endl;
	}

	cout << "=========================" << endl;

	if (ismale || isTall) {
		cout << "your are a tall male" << endl;
	}
	else {
		cout << "your are not male" << endl;
	}
	

	return 0;
}
