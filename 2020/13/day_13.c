#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <limits.h>

int mod_inverse(int a, int m) {
    int m0 = m, x0 = 0, x1 = 1;
    if (m == 1) return 0;
    
    while (a > 1) {
        int q = a / m;   
        int t = m;        
        m = a % m;        
        a = t;             
        t = x0;            
        x0 = x1 - q * x0;  
        x1 = t;           
    }
    if (x1 < 0) x1 += m0;
    return x1;
}

long long chinese_remainder(int a[], int m[], int n) {
    long long M = 1;
    for (int i = 0; i < n; i++) M *= m[i];

    long long result = 0;
    for (int i = 0; i < n; i++) {
        long long Mi = M / m[i];
        int yi = mod_inverse(Mi % m[i], m[i]);
        result = (result + (long long)a[i] * Mi % M * yi % M) % M;
    }
    return result;
}


int mod(int a, int b) {
    return ((a % b) + b) % b;
}

int main(){
    FILE *file = fopen("input.txt", "r");
    
    char line[150];
    int minDiff = INT_MAX;
    int minID;

    // Part two vars
    int n = -1;
    int IDn = 0;
    int ID[50];
    int TMinus[50];

    fgets(line, sizeof(line), file);
    line[strcspn(line, "\n")] = '\0';
    int T0 = atoi(line);
    fgets(line, sizeof(line), file);
    line[strcspn(line, "\n")] = '\0';
    fclose(file);

    // Split string by comma delim
    char *token = strtok(line, ",");
    while (token != NULL) {
        n++;
        if (token[0] != 'x') {
            int divisor = atoi(token);
            ID[IDn] = divisor;
            TMinus[IDn++] = n;
            if (T0 % divisor == 0) {
                minDiff = 0;
                minID = divisor;
            } else {
                int factor = 1 + (T0 / divisor);
                int justBigEnough = divisor * factor;
                int diff = justBigEnough - T0;
                if (diff < minDiff){
                    minDiff = diff;
                    minID = divisor;
                }
            }
        }
        token = strtok(NULL, ",");
    }

    int China[IDn];
    for (int x = 0; x < IDn; x++){
        China[x] = mod(-TMinus[x], ID[x]);
    }
    
    long long partTwo = chinese_remainder(China, ID, IDn);
    printf("\nPart One: %d", minID * minDiff);
    printf("\nPart Two: %lld\n", partTwo);

    return 0;
}