#include <stdio.h>
#include <string.h>
#include <ctype.h>

int successCondition(int checklist[]){
    int tempAns = 0;
    for (int i = 0; i < 7; i++){
        tempAns += checklist[i];
    }
    if (tempAns == 7) return 1;
    else return 0;
}


int main(){
    FILE *file = fopen("input.txt", "r");
    
    char str[400];
    const char delim[] = " ";
    char *token;
    char prefix[4];
    int isBlank;
    int partOne = 0;
    int checklist[7] = {0,0,0,0,0,0,0};

    while(fgets(str, sizeof(str), file)){
        // Check if is whitespace. If yes then we can reset to new passport entry
        // Also conduct correctness test
        isBlank = isspace((unsigned char)str[0]);
        if (isBlank != 0){
            partOne += successCondition(checklist);
            for (int i = 0; i < 7; i++) checklist[i] = 0; 
        } else {
            token = strtok(str, delim);
            while (token != NULL) {
                strncpy(prefix, token, 3);
                if (strcmp(prefix, "byr") == 0) checklist[0]=1;
                else if (strcmp(prefix, "iyr") == 0) checklist[1]=1;
                else if (strcmp(prefix, "eyr") == 0) checklist[2]=1;
                else if (strcmp(prefix, "hgt") == 0) checklist[3]=1;
                else if (strcmp(prefix, "hcl") == 0) checklist[4]=1;
                else if (strcmp(prefix, "ecl") == 0) checklist[5]=1;
                else if (strcmp(prefix, "pid") == 0) checklist[6]=1;
                token = strtok(NULL, delim);
        }
        }
        
    }
    partOne += successCondition(checklist);
    fclose(file);
    printf("\nPart One: %d", partOne);
    return 0;
}