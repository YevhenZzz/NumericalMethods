#include <iostream>
#include <cmath>


using namespace std;
int main()
{
    double a11 = 24.21, a12 = 2.42, a13 = 3.85;
    double a21 = 2.31, a22 = 31.49, a23 = 1.52;
    double a31 = 3.49, a32 = 4.84, a33 = 28.72;

    double b1 = 30.24, b2 = 40.95, b3 = 42.81;

    double x1 = 0, x2 = 0, x3 = 0;
    double x1n, x2n, x3n, x4n;
    double eps = 0.00000000001;
    int count;

    count = 0;
    do
    {
        x1n = (b1 - (a12*x2 + a13*x3))/a11;
        x2n = (b2 - (a21*x1 + a23*x3))/a22;
        x3n = (b3 - (a31*x1 + a32*x2))/a33;
        count = count + 1;
        if(fabs(x1n-x1) < eps &&
           fabs(x2n-x2) < eps &&
           fabs(x3n-x3) < eps) break;
        x1 = x1n;
        x2 = x2n;
        x3 = x3n;

        cout << "²  ¹" << count << endl << "x1 = " << x1n << endl << "x2 = " << x2n << endl << "x3 = " << x3n << endl << endl;
    } while(1);
    x1 = x1n;
    x2 = x2n;
    x3 = x3n;
    cout << " resultfrom sycle = " << count-1 << endl << "x1 = " << x1 << endl
         << "x2 = " << x2 << endl << "x3 = " << x3 << endl;

    cout << " 1: " << 24.21*x1 + 2.42*x2 + 3.85*x3 << endl;
    cout << " 2: " << 2.31*x1 + 31.49*x2 + 1.52*x3 << endl;
    cout << "3 : " << 3.49*x1 + 4.84*x2 + 28.72*x3 << endl;
}