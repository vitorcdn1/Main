#include <iostream>

using namespace std;

void sayHello(string name);
void sayHi(string name);

double cube(double num) {
	double result = num * num * num;
	return result;
}

int main() {

	sayHi("vitor");
	sayHello("vitor nascimento");
	
	double answer = cube(5.0);
	cout << answer << endl;

	return 0;
}

void sayHello(string name) {

	cout << "hello welcome " << name << endl;
}
void sayHi(string name) {
	cout << "Hello " << name << endl;
}
