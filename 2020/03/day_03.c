#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    FILE *file = fopen("input.txt", "r");
    char str[100];
    int x = 0, y = 0;
    int partOne = 0;
    char value;

    //  Get file length
    fgets(str, sizeof(str), file);
    int n = strlen(str);
    if (str[n-1] == '\n'){
        n--;
    }
    rewind(file);


    // Loop through file
    while(fgets(str, 100, file)){
        printf("%s", str);
        value = str[x];
        if (value == '#'){
            partOne++;
        }
        x = (x + 3) % n;
        y++;
    }
    fclose(file);
    printf("\n\nPart One: %d", partOne);
    return 0;
}