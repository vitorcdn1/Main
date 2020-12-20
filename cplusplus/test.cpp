#include <iostream>


bool Login(int attempts= 5) {

        std::string login, passoword;
        std::string defaultlogin = "Vitor Nascimento";
        std::string defaultpassoword = "Hello World";

        int attemp = 0;

        while (true) {

                std::cout << "Login: ";
                getline(std::cin, login);

                std::cout << "Password: ";
                getline(std::cin, passoword);

                if (login != defaultlogin && passoword != defaultpassoword) {

                        attemp++;

                        std::cout << attemp << std::endl;

                        if (attemp == attempts) {
                                break;
                        }
                        else {
                                std::cout << "Error You have only " << attempts - attemp << " attempts" << std::endl;
                        }
                }
                else {
                        return true;
                }
        }
}

void Lines(char ch = '=', int Num = 10) {

    for (int c = 0;c < Num;c++) {

        std::cout << ch;

        if (c == (Num - 1)) {

            std::cout << std::endl;
        }
    }
}
int main() {

        bool result = Login();

        if (result == true) {

                int foo[5];

                for (int c = 0;c < 5;c++) {

                        std::cout << "Enter the number for " << c << ": ";
                        std::cin >> foo[c];
                }

                for (int c = 0;c < 5; c++) {
                        std::cout << foo[c];

                        if (c != 4){
                               std::cout << " | " ;
                        }
                        else {
                                std::cout << std::endl;
                        }
                }
        }
        else {
                std::cout << "Get Out of here you intruder" << std::endl;
                std::cout << "Hello World" << std::endl;
        }
}
