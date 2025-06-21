#include <stdlib.h>
#include <stdio.h>
#include <string.h>
int* newDirection(int num, int d[2], char rorl, int output[2]) {
    num = (num / 90) % 4;
    if (rorl == 'R') num = (4 - num) % 4;

    // Iterate n times through the directions
    int intermed[2];
    memcpy(intermed, d, sizeof(int) * 2);
    for (int n = 0; n < num; n++){
        int tempo = intermed[0];
        int tampa = intermed[1];
        
        // Replace logic 
        intermed[0] = (tampa * -1);
        intermed[1] = tempo;
    }

    output[0] = intermed[0];
    output[1] = intermed[1];
    return output;
}


int main(){
    FILE *file = fopen("input.txt", "r");
    char line[7];
    int east = 0;
    int north = 0;
    int dirs[2] = {1, 0};

    // Temporary vars for direction detection
    char tempDir;
    char tempNum[5];

    // Read in data
    while(fgets(line, sizeof(line), file)){
        line[strcspn(line, "\n")] = '\0';
        // Get the D
        tempDir = line[0];
        printf("%c\n", tempDir);
        // Get a numeric 
        memcpy(tempNum, line + 1, strlen(line));
        int num = atoi(tempNum);
        

        // Move in direction of east/west/north/south
        if(tempDir == 'N'){
            north += num; 
        }
        else if(tempDir == 'S'){
            north -= num; 
        }
        else if(tempDir == 'E'){
            east += num; 
        }
        else if(tempDir == 'W'){
            east -= num; 
        } else if (tempDir ==  'F') {
            north += (dirs[1] * num);
            east += (dirs[0] * num);
        } else if ((tempDir == 'L') || (tempDir == 'R')){
            int newDirs[2];
            newDirection(num, dirs, tempDir, newDirs);
            
            // Reassign to direction vector
            dirs[0] = newDirs[0];
            dirs[1] = newDirs[1];
        }
    }
    

    fclose(file);
    int partOne = abs(east) + abs(north) ;
    printf("Part One: %d (%d + %d)\n", partOne, east, north);
    return 0;


}