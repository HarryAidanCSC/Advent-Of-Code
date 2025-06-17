#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int sortDesc(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int main(){
    FILE *file = fopen("input.txt", "r");
    int partOne = 0;
    int partTwo;
    char line[12];
    char row[8];
    char col[4];
    int arr[945];
    int j = 0;

    while(fgets(line, sizeof(line), file)){
        line[strcspn(line, "\n")] = '\0';
        strncpy(row, line, 7);
        row[7] = '\0';
        strcpy(col, line + 7);
        
        // Row logic 
        int bottom = 0, top = 127;
        float mid;

        for(int i = 0; i < 7; i++){
            char upDown = row[i];
            mid = (bottom + top) / 2;
            if (upDown == 'B'){
                bottom = mid+1;
            } else {
                top = mid; 
            }
        }

        // Col logic
        int left = 0, right = 7;

        for (int i = 0; i < 4; i++){
            char leftRight = col[i];
            mid = (left + right) / 2;
            if (leftRight == 'R'){
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        int id = (bottom * 8) + left;
        partOne = fmax(partOne, id);
        arr[j++] = id;
    }

    // Part Two logic
    qsort(arr, sizeof(arr) / sizeof(arr[0]), sizeof(int), sortDesc);
    int prev = 7, cur;
    for (int i = 1; i < 945; i++){
        int cur = arr[i];
        if (cur > prev + 1) {
            partTwo = prev + 1;
            break;
        }
        prev = cur;
    }


    printf("\nPart One: %d", partOne);
    printf("\nPart Two: %d", partTwo);

    return 0;
}