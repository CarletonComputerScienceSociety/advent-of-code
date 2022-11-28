package main

import (
    "fmt"
    "log"
    "os"
    "strings"
    "strconv"
)


func ReadLines(file_path string) []string {
    dat, err := os.ReadFile(file_path)
    if err != nil {
        log.Fatal(err)
    }

    lines := strings.Split(string(dat), "\n")
    if lines[0] == "" {
        lines = lines[1:len(lines)-1]
    }
    if lines[len(lines)-1] == "" {
        lines = lines[0:len(lines)-2]
    }

    return lines
}

func main() {
    data := ReadLines("../testfile.txt")

    fmt.Println("Printing data")
    ret_code := 0
    for i:=0; i < len(data); i++ {
        fmt.Printf("i: %d; file: %s\n", i, data[i])
        val, _ := strconv.Atoi(data[i])
        if i != val {
            fmt.Println("Warning: Values do not match")
            ret_code = 1
        }
    }
    os.Exit(ret_code)
}

