#include <iostream>
using namespace std;

void f(int x, int y ) {
    cout << "values: " << x << ", " << x << endl;
}

void f(int x, double y ) {
    cout << "values: " << x << ", " << x << endl;
}

void f(double x, int y ) {
    cout << "values: " << x << ", " << x << endl;
}

void f(double x, double y ) {
    cout << "values: " << x << ", " << x << endl;
}


int main()
{
    f(42, 43); 
    f(42, 43.7); 
    f(42.3,43);
    f(42.0, 43.9); 
}

