#include <iostream>

using namespace std;

int main() {

	string phrase = "vitor nascimento batista";


	cout << "Hello {phrase}" << endl;
	cout << phrase.length() << endl;
	cout << phrase.find("v", 0) << endl;
	cout << phrase.substr(phrase.find("n", 4), 10) << endl;

	return 0;
}
