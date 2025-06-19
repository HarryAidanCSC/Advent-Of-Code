#include <stdlib.h>
#include <stdio.h>
#include <string.h>

// Sorting function
int compareInts(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

// Main execution
int main(){
    FILE *file = fopen("input.txt", "r");
    int lines[128];
    char line[10];
    
    int addOne = 0;
    int addThree = 1;

    // Part One
    int i = 0;
    int maxValue = -1;

    while(fgets(line, sizeof(line), file)){
        int value;
        line[strcspn(line, "\n")] = '\0';
        value = atoi(line);
        lines[i++] = value;
        if (value > maxValue) maxValue = value;
    }

    // Sort array
    lines[i++] = 0;
    lines[i++] = maxValue + 3;
    qsort(lines, i, sizeof(int), compareInts);

    // Part One
    int prev = 0;
    for (int x = 0; x < i; x++){
        int cur = lines[x];
        int diff = cur - prev;
        if (diff == 1) addOne++;
        else if (diff == 3) addThree++;
        prev = cur;
    }

    // Part Two: DP array to count ways to reach each adapter
    long long int ways[i]; 
    for (int k = 0; k < i; k++) ways[k] = 0;
    ways[0] = 1; 

    for (int x = 1; x < i; x++) {
        for (int y = x - 1; y >= 0 && lines[x] - lines[y] <= 3; y--) {
            ways[x] += ways[y];
        }
    }

    printf("\nPart One: %d", addOne * addThree);
    printf("\nPart Two: %lld\n", ways[i-1]);
    fclose(file);
    return 0;
}