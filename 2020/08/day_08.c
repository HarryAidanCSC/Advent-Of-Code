#include <stdlib.h>
#include <stdio.h>
#include<string.h>

int main(){
        FILE *file = fopen("input.txt", "r");
    int partOne = 0;
    int partTwo = 0;
    const char *lines[1000];
    char line[50];
    int count = 0;

    while(fgets(line, sizeof(line), file)){
        line[strcspn(line, "\n")] = '\0';
        lines[count++] = strdup(line);
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
    }

    printf("\nPart One: %d", partOne);
    return 0;
}