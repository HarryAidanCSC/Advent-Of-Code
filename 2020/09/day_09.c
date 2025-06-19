#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <limits.h>

int main() {
    FILE *file = fopen("input.txt", "r");
    long long int lines[2000];
    int linesSize = 0;
    char line[20];
    int lineNumeric[25];
    long long int cur;
    long long int partOne;
    int stacklen = 0;
    int preamble = 25;

    // Part One
    int i = 0;
    while(fgets(line, sizeof(line), file)){
        line[strcspn(line, "\n")] = '\0';
        if (strcmp(line, "\n") == 0) break;
        cur = atoll(line);

        // Chuck into lines for later
        lines[linesSize++] = cur;

        // Checking logic
        // Break out the 0(N^2)
        if (stacklen == preamble){
            int breakflagMajor = 0;
            for (int x = 0; x < stacklen; x++){
                int breakflagMinor = 0; 
                int diff = cur - lineNumeric[x];
                for (int y = 0; y < stacklen; y++){
                    if (x == y) continue;
                    if (lineNumeric[y] == diff){
                        breakflagMinor = 1;
                        break;
                    }
                }  
                if (breakflagMinor == 1){
                    breakflagMajor = 1;
                    break;
                }
            }
            if (breakflagMajor == 0) {
                partOne = cur;
            }
        }


        // Maintain stack length
        lineNumeric[i++] = cur;
        stacklen = fmax(stacklen, i);
        if (i == preamble) {
            i = 0;
        }
    }

    // Part Two
    // Variable length sliding window
    int left = 0;
    long long int sumOfTerms = 0;
    long long int partTwo;
    for (int right = 0; right < linesSize; right++) {
        cur = lines[right];
        sumOfTerms += cur;

        // Checking logic
        while ((sumOfTerms > partOne) && (left < right - 1)){
            sumOfTerms -= lines[left++];
        }
        if (sumOfTerms == partOne){
            long long int minVal = LLONG_MAX;
            long long int maxVal = -1;
            for (int x = left; x <= right; x++){
                if (lines[x] < minVal) minVal = lines[x];
                if (lines[x] > maxVal) maxVal = lines[x];
                partTwo = maxVal + minVal;
            }
        } 
        
    }

    printf("\nPart One: %lld", partOne);
    printf("\nPart Two: %lld", partTwo);
    return 0;
}
