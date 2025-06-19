#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main() {
    FILE *file = fopen("input.txt", "r");
    int partOne = 0;
    char line[20];
    int lineNumeric[25];
    long long int cur;
    int stacklen = 0;
    int preamble = 25;

    int i = 0;
    while(fgets(line, sizeof(line), file)){
        line[strcspn(line, "\n")] = '\0';
        if (strcmp(line, "\n") == 0) break;
        cur = atoll(line);

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
                break;
            }
        }


        // Maintain stack length
        lineNumeric[i++] = cur;
        stacklen = fmax(stacklen, i);
        if (i == preamble) {
            i = 0;
        }
    }

    printf("\nPart One: %lld", cur);
    return 0;
}
