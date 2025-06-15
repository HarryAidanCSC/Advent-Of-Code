#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    FILE *file = fopen("input.txt", "r");
    char str[100];
    int y = 0;
    char value;
    int slopeX[5] = {0,0,0,0,0};
    int right[5] ={1, 3, 5, 7, 1};
    int x;
    int treeArr[5] = {0,0,0,0,0};

    //  Get file length
    fgets(str, sizeof(str), file);
    int n = strlen(str);
    if (str[n-1] == '\n'){n--;}
    rewind(file);

    // Loop through file
    while(fgets(str, 100, file)){
        for (int i=0; i < 5; i++){
            if (i == 4 && y % 2 != 0){continue;} // Skip every odd row for the 0.5 slope
            x = slopeX[i];
            value = str[x];          ;
            if (value == '#'){
                treeArr[i]++;
            }
            slopeX[i] = (x + right[i]) % n;
        }
        y++;
    }
    fclose(file);
    int partOne = treeArr[1];
    long long partTwo = treeArr[0];

    for (int i = 1; i < 5; i ++){
        partTwo *= treeArr[i];
    }
    printf("\nPart One: %d\nPart Two: %lld\n\n", partOne, partTwo);
    return 0;
}