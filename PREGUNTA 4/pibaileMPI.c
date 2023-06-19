#include <stdio.h>
#include <math.h>

double calculatePiBBP()
{
    double pi = 0.0;
    double k;
    double currentTerm;
    
    for (k = 0; k < 100000; k++) {
        currentTerm = (1.0 / pow(16, k)) * (
            (4.0 / (8*k+1)) - (2.0 / (8*k+4)) - (1.0 / (8*k+5)) - (1.0 / (8*k+6))
        );
        
        pi += currentTerm;
    }
    
    return pi;
}

int main()
{
    double pi = calculatePiBBP();
    printf("El valor aproximado de Pi es: %.15f\n", pi);
    
    return 0;
}

