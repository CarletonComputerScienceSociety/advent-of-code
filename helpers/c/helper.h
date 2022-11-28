#ifndef __HELPER_H__
#define __HELPER_H__

#define MAX_SIZE 2048

/*
 * read_input
 * Input:
 *   file_path (char*): The path to the file to load
 *   output (char***): Unitialized return variable for an arry of c strings
 * Output:
 *   int: The size of the array returned, -1 for failed
 */
int read_input(const char* file_path, char*** output);

void cleanup(char** arr, int size);

#endif /* __HELPER_H__*/
