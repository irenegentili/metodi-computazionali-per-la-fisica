#include <stdio.h>
#include <math.h>

double fib(int n) {
    int prec1=1;
    int prec2=1;
    int succ;
    if (n>2){
    for (int i = 3; i <=n; i++) {
        succ=prec1+prec2;
        prec1=prec2;
        prec2=succ;
    }
    } else {
        return 1;
    }
    double r=(double)succ/prec1;
    return r;
}