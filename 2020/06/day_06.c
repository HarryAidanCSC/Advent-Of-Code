#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    FILE *file = fopen("input.txt", "r");
    int partOne = 0;
    int partTwo = 0;
    char line[28];
    int scores[26] = {0};
    int scoresInverse[26] = {0};

    while(fgets(line, sizeof(line), file)){
        line[strcspn(line, "\n")] = '\0';
        if (strlen(line) == 0){
            int groupScorePartOne = 0, groupScorePartTwo = 0;
            for (int j = 0; j < 26; j++)  {
                groupScorePartOne += scores[j];
                groupScorePartTwo += (1 - scoresInverse[j]);
                scores[j] = 0;
                scoresInverse[j] = 0;
            }
            partOne += groupScorePartOne;
            partTwo += groupScorePartTwo;
            continue;
        } 

        int temp[26] = {0};
        for (int j = 0; j < strlen(line); j++){
            int idx = (int)line[j] - 97;
            temp[idx] = 1;
        }
        for (int j = 0; j < 26; j++){
            if (temp[j] == 1){
                scores[j] = 1;
                continue;
            } else {
                scoresInverse[j] = 1;
            }
        }
        
    }

    // Last group 
    int groupScorePartOne = 0, groupScorePartTwo = 0;
    for (int j = 0; j < 26; j++)  {
        groupScorePartOne += scores[j];
        groupScorePartTwo += (1 - scoresInverse[j]);
    }
    partOne += groupScorePartOne;
    partTwo += groupScorePartTwo;

    printf("Part One: %d", partOne);
    printf("\nPart Two: %d", partTwo);
    return 0;
}