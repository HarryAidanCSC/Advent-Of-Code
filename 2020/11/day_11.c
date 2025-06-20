#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(){
    FILE *file = fopen("input.txt", "r");
    char line[120];
    char lines[120][120]; // Give a nice buffer
    char linesOG[120][120]; // Secondary OG set for part 2
    int n = 0;

    // Read in data
    while(fgets(line, sizeof(line), file)){
        line[strcspn(line, "\n")] = '\0';
        strcpy(lines[n], line);
        strcpy(linesOG[n++], line);
    }

    // Close the file
    fclose(file);

    // Get length 
    int nx = strlen(lines[0]);

    // Part one
    int changes = -1; // Init to any non-zero value
    while (changes != 0){
        changes = 0;
        char linesDupe[120][120]; // Init an empty copy
        for (int y = 0; y < n; y++){ // Hit them with that hawk squared
            for (int x = 0; x < nx; x++){
                // We are about to deoptimise the hell out of this thing
                char seat = lines[y][x];
                linesDupe[y][x] = seat;
                if (seat == '.') continue;
                // Check all 8 adjacent for empty seats
                int xi;
                int yj;
                int comparisonValue = 0;
                for (int j = -1; j <= 1; j++){
                    for (int i = -1; i <= 1; i++){
                        if ((i == 0) && (j == 0)) continue;
                        // X Y check
                        xi = x + i;
                        if ((xi < 0) || (xi >= nx)) continue;
                        yj = y + j;
                        if ((yj < 0) || (yj >= n)) continue;
                        // Check number of matches in the valid space
                        if (lines[yj][xi] == '#') comparisonValue++;
                    }
                }
                // Update dupe array (array)
                if (seat == '#'){
                    if (comparisonValue >= 4) {
                        linesDupe[y][x] = 'L';
                        changes++;
                        continue;
                    }
                        
                } else if (seat == 'L'){
                    if (comparisonValue == 0) {
                        linesDupe[y][x] = '#';
                        changes++;
                        continue;
                    }
                }
            }
        }
        for (int y = 0; y < n; y++) {
            strcpy(lines[y], linesDupe[y]);
        }
    }

    // Part one calc
    int partOne  = 0;
    for (int y0MrWhite = 0; y0MrWhite < n; y0MrWhite++){
        for (int x = 0; x < nx; x++){
            if (lines[y0MrWhite][x] == '#') partOne++;
        }
    }

    // Part Two
    // =====================================================
    changes = -1; // Init to any non-zero value
    while (changes != 0){
        changes = 0;
        char linesDupe[120][120]; // Init an empty copy
        for (int y = 0; y < n; y++){ // Hit them with that hawk squared
            for (int x = 0; x < nx; x++){
                char seat = linesOG[y][x];
                linesDupe[y][x] = seat;
                if (seat == '.') continue;

                // Check all 8 adjacent vectors for empty seats
                int comparisonValue = 0;

                for (int j = -1; j <= 1; j++){
                    for (int i = -1; i <= 1; i++){
                        if ((i == 0) && (j == 0)) continue;
                        int xi = x + i;
                        int yj = y + j; 
                        char comparisonChar;
                        while ((xi >= 0) && (xi < nx) && (yj >= 0) && (yj < n)){
                            comparisonChar = linesOG[yj][xi];
                            if (comparisonChar == '.'){
                                xi += i;
                                yj += j;
                            } else {
                                if (linesOG[yj][xi] == '#') comparisonValue++;
                                break;
                            }
                        }
                    }
                }
                // Update dupe array (array)
                if (seat == '#'){
                    if (comparisonValue >= 5) {
                        linesDupe[y][x] = 'L';
                        changes++;
                        continue;
                    }
                        
                } else if (seat == 'L'){
                    if (comparisonValue == 0) {
                        linesDupe[y][x] = '#';
                        changes++;
                        continue;
                    }
                }
            }
        }
        for (int y = 0; y < n; y++) {
            strcpy(linesOG[y], linesDupe[y]);
        }
    }

    int partTwo  = 0;
    for (int y0MrWhite = 0; y0MrWhite < n; y0MrWhite++){
        for (int x = 0; x < nx; x++){
            if (linesOG[y0MrWhite][x] == '#') partTwo++;
        }
    }


    printf("Part One: %d\n", partOne);
    printf("Part Two: %d\n", partTwo);
    return 0;
}