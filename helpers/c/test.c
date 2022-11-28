#include "helper.h"

#include <stdio.h>
#include <stdlib.h>

int main() {
    char** data = NULL;
    int size = 0;
    int retcode = 0;

    printf("Running test\n");
    size = read_input("../testfile.txt", &data);

    printf("Validating output\n");
    for (int i=0; i < size; i++) {
        printf("i: %d; file: %s", i, data[i]);
        if (i != atoi(data[i])) {
            retcode = 1;
        }
    }

    cleanup(data, size);
    return retcode;
}
