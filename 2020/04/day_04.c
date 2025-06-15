#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

// This function is logically correct, no changes needed here.
int successCondition(int checklist[]){
    int tempAns = 0;
    for (int i = 0; i < 7; i++) tempAns += checklist[i];
    if (tempAns == 7) return 1;
    else return 0;
}


int main(){
    // It's good practice to check if the file opened successfully.
    FILE *file = fopen("input.txt", "r");
    if (file == NULL) {
        perror("Error opening input.txt");
        return 1;
    }
    
    char str[400];
    const char delim[] = " \n";
    char *token;
    char prefix[4];
    char suffix[100];
    int partOne = 0;
    int partTwo = 0;
    int checklistPartOne[7] = {0,0,0,0,0,0,0};
    int checklistPartTwo[7] = {0,0,0,0,0,0,0};
    const char *colors[] = {"amb" ,"blu" ,"brn" ,"gry" ,"grn" ,"hzl" ,"oth", NULL};
    
    int val;
    char suffixCopy[100];
    int n;
    char lastChars[3];

    while(fgets(str, sizeof(str), file)){
        str[strcspn(str, "\n")] = 0;

        if (str[0] == '\0'){
            partOne += successCondition(checklistPartOne);
            partTwo += successCondition(checklistPartTwo);
            for (int i = 0; i < 7; i++) {
                checklistPartOne[i] = 0; 
                checklistPartTwo[i] = 0; 
            }
        } else {
            token = strtok(str, " ");
            while (token != NULL) {
                if (strlen(token) < 4) {
                    token = strtok(NULL, " ");
                    continue;
                }
                
                strncpy(prefix, token, 3);
                prefix[3] = '\0';

                strcpy(suffix, token + 4);

                // Check 0: Birth Year
                if (strcmp(prefix, "byr") == 0) {
                    checklistPartOne[0] = 1;
                    val = atoi(suffix);
                    if((val >= 1920) && (val <= 2002)) checklistPartTwo[0]=1;
                }
                // Check 1: Issue Year
                else if (strcmp(prefix, "iyr") == 0){
                    checklistPartOne[1] = 1;
                    val = atoi(suffix);
                    if ((val >= 2010) && (val <= 2020)) checklistPartTwo[1]=1;
                }
                // Check 2: Expiration Date
                else if (strcmp(prefix, "eyr") == 0){
                    checklistPartOne[2] = 1;
                    val = atoi(suffix);
                    if((val >= 2020) && (val <= 2030)) checklistPartTwo[2]=1;
                }
                // Check 3: Height
                else if (strcmp(prefix, "hgt") == 0){
                    checklistPartOne[3] = 1;

                    n = strlen(suffix);
                    if (n > 2) {
                        strncpy(lastChars, suffix + n - 2, 2);
                        lastChars[2] = '\0';

                        if (strcmp(lastChars, "in") == 0){
                            strncpy(suffixCopy, suffix, n - 2);
                            suffixCopy[n - 2] = '\0';
                            val = atoi(suffixCopy);
                            if ((val >= 59) && (val <= 76)) checklistPartTwo[3]=1;
                        } else if (strcmp(lastChars, "cm") == 0){
                            strncpy(suffixCopy, suffix, n - 2);
                            suffixCopy[n - 2] = '\0';
                            val = atoi(suffixCopy);
                            if ((val >= 150) && (val <= 193)) checklistPartTwo[3]=1;
                        }
                    }
                }
                // Check 4: Hair color
                else if (strcmp(prefix, "hcl") == 0) {
                    checklistPartOne[4] = 1;
                    if (suffix[0] == '#' && strlen(suffix) == 7){
                        int valid = 1;
                        for (int z = 1; z < 7; z++){
                            char c = suffix[z];
                            if (!isxdigit((unsigned char)c)) {
                                valid = 0;
                                break;
                            }
                        }
                        if (valid) checklistPartTwo[4] = 1;
                    }
                }
                // Check 5: Eye color
                else if (strcmp(prefix, "ecl") == 0) {
                    checklistPartOne[5] = 1;
                    int len = 0;
                    while (colors[len] != NULL) {
                        if (strcmp(suffix, colors[len]) == 0){
                            checklistPartTwo[5]=1;
                            break;
                        }
                        len++;
                    }
                }
                // Check 6: Passport ID
                else if (strcmp(prefix, "pid") == 0){
                    checklistPartOne[6] = 1;
                    if (strlen(suffix) == 9) {
                        int valid = 1;
                        for (int b = 0; b < 9; b++){
                            if (!isdigit((unsigned char)suffix[b])) {
                                valid = 0;
                                break;
                            }
                        }
                        if (valid) {
                            checklistPartTwo[6] = 1;
                        }
                    }
                }
                token = strtok(NULL, " ");
            }
        }
    }

    partOne += successCondition(checklistPartOne);
    partTwo += successCondition(checklistPartTwo);

    fclose(file);
    printf("\nPart One: %d\nPart Two: %d\n\n", partOne, partTwo);
    return 0;
}
