#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int partTwoFunction(int arr[], int size, const char *str, const char *lines[], int lineCount){    for (int i = 0; i < size; i++){
        int idx = arr[i];
        const char *linesCopy[1000]; 
        char lineToCopy[50];
        char modified[50];

        // Copy the orignal with single modification
        for (int j = 0; j < lineCount; j++){
            if (j == idx) {
                strcpy(modified, str);
                strcpy(modified + 3, lines[j] + 3);
                linesCopy[j] = strdup(modified);;
            } else{
                linesCopy[j] = strdup(lines[j]);
            }
        };

        // Loop through - can we get to the end?
        int visited[lineCount];
        memset(visited, 0, sizeof(visited));
        int score = 0;
        int p = 0;

        while (p < lineCount) {
            // Infinite loop check
            if (visited[p] == 1) break;
            visited[p] = 1;
            char *cur = strdup(linesCopy[p]);
            char *operator = strtok(cur, " ");
            char *token = strtok(NULL, " ");
            int xtoken = atoi(token);
            if (strcmp(operator, "nop") == 0) {
                p++;
            } else if (strcmp(operator, "acc") == 0){
                score += xtoken;
                p++;
            } else {
                p += xtoken;
            }
            free(cur);
        }
        if (p >= lineCount){
            // Free memory
            for (int j = 0; j < lineCount; j++) {
                free((void *)linesCopy[j]);
            }
            return score;
        }
    }
    return -1000000000;
}

int main(){
    FILE *file = fopen("input.txt", "r");
    int partOne = 0;
    int partTwo = 0;
    const char *lines[1000];
    char line[50];
    int count = 0;

    int jmpIDX[1000]; // max buffer
    int jIDX = 0;
    int nopIDX[1000]; // max buffer
    int nIDX = 0;

    while(fgets(line, sizeof(line), file)){
        line[strcspn(line, "\n")] = '\0';
        lines[count++] = strdup(line);

        char *operator = strtok(line, " ");
        if (strcmp(operator, "jmp") == 0){
            jmpIDX[jIDX++] = count - 1;
        } else if (strcmp(operator, "nop") == 0){
            nopIDX[nIDX++] = count - 1;
        }
    }

    int visited[count];
    memset(visited, 0, sizeof(visited));

    // Part one logic
    int i = 0;
    while (1) {
        // Infinite loop check
        if (visited[i] == 1) break;
        visited[i] = 1;

        char *cur = strdup(lines[i]);
        char *operator = strtok(cur, " ");
        char *token = strtok(NULL, " ");
        int xtoken = atoi(token);

        if (strcmp(operator, "nop") == 0) {
            i++;
        } else if (strcmp(operator, "acc") == 0){
            partOne += xtoken;
            i++;
        } else {
            i += xtoken;
        }
        free(cur);
    }


    partTwo = fmax(partTwoFunction(nopIDX, nIDX, "jmp", lines, count), partTwoFunction(jmpIDX, jIDX, "nop", lines, count));

    printf("\nPart One: %d", partOne);
    printf("\nPart Two: %d", partTwo);
    return 0;
}