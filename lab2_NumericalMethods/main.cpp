#include <iostream>
#include <math.h>
using namespace std;
double chordsMethod(double a, double b, const double eps);
double f(double x);
int main()
{
    double x = chordsMethod(1, 3, 1);
    std::cout << x << "\n";

    cout << f(x) << endl;
    system("pause");
    return 0;
}


double f(double x) {
    return pow(x,2) - cos(x);
}


double chordsMethod(double a, double b, const double eps)
{
    double x = a;
    double x_old = 0;
    do {
        x_old = x;
        x = a - f(a)*((b - a) / (f(b) - f(a)));
        f(x)*f(a) > 0 ? a = x:b = x;
    } while (fabs((x - x_old)/x)*100 > eps);
    return x;
}