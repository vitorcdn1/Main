#include <iostream>

using namespace std;

int main() {

	string separator = "=======================================\n";
	bool isMale = true;
	bool isTall = true;
	
	if (isMale && isTall) {
		cout << "you are a tall male" << endl;
	} 
	else {
		cout << "you are not male" << endl;
	}

	cout << separator;

	if (isMale || isTall) {
		cout << "you are a tall male" << endl;
	}
	else {
		cout << "you are not male" << endl;
	}
	
	cout << separator;

	if (isMale && isTall){
		cout << "you are a tall male" << endl;
	}
	else if (isMale && !isTall) {
		cout << "You are a short male";
	}
	else if (!isMale && isTall) {
		cout << "You are tall but not male";
	}
	else {
		cout << "You are not male and not tall";
	}

	return 0;
}
