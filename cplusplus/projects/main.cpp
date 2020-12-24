#include <iostream>

using namespace std;

void LearnMultipleTable(int MultipleNum) {

        int result = 0;

        for (int c = 1;c < 10;c++) {
                cout << MultipleNum << " X " << c << " = ";
                cin >> result;

                if (result == MultipleNum * c) {
                        cout << "Parabens vc acertou" << endl;
                }
                else {
                        cout << "Você errou o resultado era " << MultipleNum << " X " << c << " = " << MultipleNum * c << endl;
                }
        }
}
void PracticeMultipleTable(int MultipleNum) {

        int result, Num;

        for (int c = 1;c < 10;c++) {
                Num = rand() % 9 + 1;

                cout << MultipleNum << " x " << Num << " = ";
                cin >> result;

                if (result == MultipleNum * Num) {
                        cout << "Parabens vc acertou" << endl;
                }
                else {
                        cout << "Voce errou" << endl;
                }
        }
}
void ShowLines(int SizeLines) {

        for (int c = 0;c < SizeLines;c++) {

                cout << "=";
                if (c == SizeLines - 1) {
                        cout << endl;
                }
        }
}

int main() {

        int LinesNum = 50; // Variable with the size of the Lines, of the whole program.

        while (true) {
                ShowLines(LinesNum);

                cout << "0 - Exit Program" << endl;
                cout << "1 - Learn Multiple Table" << endl;
                cout << "2 - Practice Multiple Table" << endl;

                ShowLines(LinesNum);

                int User;

                cout << "Enter a option: ";
                cin >> User;

                if (User == 0) {

                        ShowLines(LinesNum);
                        cout << "Thank you for using this program ..." << endl;

                        return 0;
                }
                else if (User == 1) {

                        ShowLines(LinesNum);
                        int NumFunction;        // The Number used in the function of the option
                        cout << "Enter the number that you want: ";
                        cin >> NumFunction;

                        LearnMultipleTable(NumFunction);
                }
                else if (User == 2) {

                        ShowLines(LinesNum);
                        int NumFunction;

                        cout << "Enter the number that you want to train: ";
                        cin >> NumFunction;

                        PracticeMultipleTable(NumFunction);
                }
                else {
                        system("cls");
                        cout << "Option None" << endl;
                        cout << "Please Enter a real option" << endl;

                }
        }

    return 0;
}
