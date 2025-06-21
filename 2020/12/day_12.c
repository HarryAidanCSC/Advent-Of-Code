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

int* waypointRecalibration(int num, int eWay, int nWay, char rorl, int output[2]){
    num = (num / 90) % 4;
    if (rorl == 'L') num = (4 - num) % 4;

    int tempEWay = eWay;
    int tempNWay = nWay;

    if (num == 1){
        nWay = -tempEWay;
        eWay = tempNWay;
    } else if (num == 2){
        nWay = -tempNWay;
        eWay = -tempEWay;
    } else if (num == 3){
        nWay = tempEWay;
        eWay = -tempNWay;
    }
    
    output[0] = eWay;
    output[1] = nWay;
    return output;
    
}

int main(){
    FILE *file = fopen("input.txt", "r");
    char line[5];
    int east = 0;
    int north = 0;
    int dirs[2] = {1, 0};
    
    // Part two values
    int northWaypoint = 1;
    int eastWayPoint = 10;
    int northP2 = 0;
    int eastP2 = 0;

    // Temporary vars for direction detection
    char tempDir;
    char tempNum[5];

    // Read in data
    while(fgets(line, sizeof(line), file)){
        line[strcspn(line, "\n")] = '\0';
        // Get the D
        tempDir = line[0];
        // Get a numeric 
        memcpy(tempNum, line + 1, strlen(line));
        int num = atoi(tempNum);
        

        // Move in direction of east/west/north/south
        if(tempDir == 'N'){
            north += num; 
            northWaypoint += num;
        }
        else if(tempDir == 'S'){
            north -= num;
            northWaypoint -= num; 
        }
        else if(tempDir == 'E'){
            east += num; 
            eastWayPoint += num; 
        }
        else if(tempDir == 'W'){
            east -= num; 
            eastWayPoint -= num; 
        } else if (tempDir ==  'F') {
            // p1
            north += (dirs[1] * num);
            east += (dirs[0] * num);

            // p2
            northP2 += (num * northWaypoint);
            eastP2 += (num * eastWayPoint);
        } else if ((tempDir == 'L') || (tempDir == 'R')){
            int newDirs[2];
            newDirection(num, dirs, tempDir, newDirs);
            
            // Reassign to direction vector p1
            dirs[0] = newDirs[0];
            dirs[1] = newDirs[1];

            // Part two waypoint rotation
            int newWaypointVector[2];
            waypointRecalibration(num, eastWayPoint, northWaypoint, tempDir, newWaypointVector);
            eastWayPoint = newWaypointVector[0];
            northWaypoint = newWaypointVector[1];
        }
    }
    

    fclose(file);
    int partOne = abs(east) + abs(north) ;
    int partTwo = abs(eastP2) + abs(northP2);
    printf("Part One: %d\n", partOne);
    printf("Part Two: %d\n", partTwo);
    return 0;


}