#include "helper.h"

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

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

