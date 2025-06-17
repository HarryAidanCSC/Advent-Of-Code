#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int main(){
    FILE *file = fopen("input.txt", "r");
    int partOne = 0;
    char line[12];
    char row[8];
    char col[4];

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
        partOne = fmax(partOne, (bottom * 8) + left);
    }
    
    printf("\nPart One: %d", partOne);

    return 0;
}