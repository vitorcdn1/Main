#include <iostream>

using namespace std;

int main() {

	string phrase = "Giraffe Academy";

	cout << phrase.length() << endl;
	cout << phrase[0] << endl;
	cout << phrase.find("Academy", 0) << endl;
	cout << phrase.substr(8, 3) << endl;
	cout << endl;

	return 0;
}
