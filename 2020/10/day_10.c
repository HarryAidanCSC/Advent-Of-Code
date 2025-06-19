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
    int maxValue = -1;
    int lines[128];
    char line[10];
    
    int addOne = 0;
    int addThree = 1;

    // Part One
    int i = 0;
    while(fgets(line, sizeof(line), file)){
        int value;
        line[strcspn(line, "\n")] = '\0';
        value = atoi(line);
        lines[i++] = value;
        if (value > maxValue) maxValue = value;
    }

    // Sort array
    qsort(lines, i, sizeof(int), compareInts);

    int prev = 0;
    for (int x = 0; x < i; x++){
        int cur = lines[x];
        int diff = cur - prev;
        printf("\n%d", diff);
        if (diff == 1) addOne++;
        else if (diff == 3) addThree++;
        prev = cur;
    }

    printf("\nPart One: %d", addOne * addThree);
    return 0;
}
