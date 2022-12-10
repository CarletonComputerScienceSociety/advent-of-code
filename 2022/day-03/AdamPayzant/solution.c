#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_SIZE 2048

int read_input(const char* file_path, char*** output);
void cleanup(char** arr, int size);
int part1(char** data, int size);
int part2(char** data, int size);


int read_input(const char* file_path, char*** output) {
    FILE* file = NULL;
    int arr_len = 0;
    char* line = NULL;
    size_t line_len = 0;
    ssize_t read = 0;

    // Open file
    file = fopen(file_path, "r");
    if (NULL == file) {
        printf("ERROR: FAILED TO READ FILE\n");
        return -1;
    }

    if (NULL == *output) {
        // Yes, allocating a large array is a bit of a waste, but I'm too lazy
        // to write a properly resizable array
        *output = malloc(MAX_SIZE * sizeof(char*));
        if (NULL == *output) {
            arr_len = -1;
            goto err;
        }
    }

    while ((read = getline(&line, &line_len, file)) != -1) {
        if (line_len > 0 && line[line_len-1] == '\n') {
            line[--line_len] = '\0';
        }
        if (line[0] == '\n' || line[0] == '\0') {
            continue;
        }

        (*output)[arr_len] = line; 
        arr_len++;

        line = NULL;
    }

err:
    fclose(file);
    return arr_len;
}

void cleanup(char** arr, int size) {
    for (int i = 0; i < size; i++) {
        if (NULL != arr[i]) {
            free(arr[i]);
        }
    }
    free(arr);
}

int part1(char** input, int size) {
    int res = 0;
    
    for (int i = 0; i < size; i++) {
        size_t len = strlen(input[i]);
        char common = 0;

        for (int a = 0; a < len/2; a++) {
            for (int b = len/2; b < len; b++) {
                if (input[i][a] == input[i][b]) {
                    common = input[i][a];
                    goto loopEnd;
                }
            }
        }
        loopEnd:
        if (common == 0) {
            printf("Something went wrong\n");
            continue;
        }
        if (common < 91) {
            // common - <ASCII conversion> + priority
            res += common - 65 + 27;
        } else {
            // common - <ASCII conversion> + priority
            res += common - 97 + 1;
        }
    }

    return res;
}

int part2(char** input, int size) {
    int res = 0;

    for (int i = 0; i < size; i += 3) {
        if (size - i < 3) {
            continue;
        }
        char common = 0;
        size_t a_len = 0, b_len = 0, c_len = 0;
        a_len = strlen(input[i]);
        b_len = strlen(input[i+1]);
        c_len = strlen(input[i+2]);

        for (int a = 0; a < a_len; a++) {
            for (int b = 0; b < b_len; b++) {
                for (int c = 0; c < c_len; c++) {
                    if (input[i][a] == input[i+1][b] && input[i][a] == input[i+2][c]) {
                        common = input[i][a];
                        goto loop2End;
                    }
                }
            }
        }
        loop2End:
        if (common == 0) {
            printf("Something went wrong");
            continue;
        }
        if (common < 91) {
            // common - <ASCII conversion> + priority
            res += common - 65 + 27;
        } else {
            // common - <ASCII conversion> + priority
            res += common - 97 + 1;
        }
    }

    return res;
}

int main(){
    char** data;
    int size = 0;
    int p1=0, p2=0;

    size = read_input("input", &data);

    p1 = part1(data, size);
    p2 = part2(data, size);

    printf("Part1 = %d\n", p1);
    printf("Part2 = %d\n", p2);

    cleanup(data, size);
}
