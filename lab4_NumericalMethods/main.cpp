#include <iostream>
#include <cmath>
using namespace std;
typedef double(*pointFunc)(double);
double f(double x) {
    return x*pow(2, 2*x); //від 1 до 2
}

double rectangle_integral(pointFunc f, double a, double b, int n) {
    double x, h;
    double sum = 0.0;
    double fx;
    h = (b - a) / n;  //шаг

    for (int i = 0; i < n; i++) {
        x = a + i*h;
        fx = f(x);
        sum += fx;
    }
    return (sum * h);
}
int main(){
    double a, b, eps;
    double s1, s;
    int n = 1; // початкове число шагів

    cout << "Left border a: ";
    cin >> a;
    cout << "\nRight border b: ";
    cin >> b;
    cout << "\nAccuracy: ";
    cin >> eps;
    s1 = rectangle_integral(f, a, b, n); // перше приближення для інтерграла
    do {
        s = s1;     //друге приближення
        n = 2 * n;  //збільшення шагів в 2 рази
        s1 = rectangle_integral(f, a, b, n);
    }
    while (fabs(s1 - s) > eps);  //порівняння приближень із заданою точністю
    cout << "\nIntegral = " << s1 << endl;

    double x = ((b*pow(b, 2*x))/2*log(b)) - (pow(2, 2*b)/2*pow(log(2), 2));
    double y = ((b*pow(a, 2*x))/2*log(a)) - (pow(2, 2*a)/2*pow(log(2), 2));
    double c = x-y;
    cout << "\nCheck: " << c;
}