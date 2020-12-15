#include <iostream>

using namespace std;

void ShowMenu(string options[]) {
	cout << options.length();
}

int main() {

	string options[] = {"Exit program", "Show A Multiple Table", "Learn A Multiple Table", "Practice A Multiple Table"};

	while (true) {
		ShowMenu(options);
		break;
	}

	return 0;
}