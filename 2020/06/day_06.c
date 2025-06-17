#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(){
    FILE *file = fopen("input.txt", "r");
    int partOne = 0;
    char line[28];
    int scores[26] = {0};

    while(fgets(line, sizeof(line), file)){
        line[strcspn(line, "\n")] = '\0';
        if (strlen(line) == 0){
            int groupScore = 0;
            for (int j = 0; j < 26; j++)  {
                groupScore += scores[j];
                scores[j] = 0;
            }
            partOne += groupScore;
            continue;
        } 

        for (int j = 0; j < strlen(line); j++){
            int idx = (int)line[j] - 97;
            scores[idx] = 1;
        }
        
    }
    // Last group 
    int groupScore = 0;
    for (int j = 0; j < 26; j++)  groupScore += scores[j];
    partOne += groupScore;

    printf("\nPart One: %d", partOne);
    return 0;
}