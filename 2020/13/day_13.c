#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <limits.h>

int main(){
    FILE *file = fopen("input.txt", "r");
    char line[150];
    int minDiff = INT_MAX;
    int minID;

    // Get the departure earliest time 
    fgets(line, sizeof(line), file);
    line[strcspn(line, "\n")] = '\0';
    int T0 = atoi(line);
    // Get the timetable
    fgets(line, sizeof(line), file);
    line[strcspn(line, "\n")] = '\0';

    // Split string by comma delim
    char *token = strtok(line, ",");
    while (token != NULL) {
        if (token[0] != 'x') {
            int divisor = atoi(token);
            if (T0 % divisor == 0) {
                minDiff = 0;
                minID = divisor;
                break;
            } else {
                int factor = 1 + (T0 / divisor);
                int justBigEnough = divisor * factor;
                int diff = justBigEnough - T0;
                // printf("\nToken: %d\nFactor %d\nJBE: %d\nDiff: %d\n", divisor, factor, justBigEnough, diff);
                if (diff < minDiff){
                    minDiff = diff;
                    minID = divisor;
                }
            }
        }
        token = strtok(NULL, ",");
    }

    printf("Part One: %d", minID * minDiff);
    fclose(file);
    return 0;
}