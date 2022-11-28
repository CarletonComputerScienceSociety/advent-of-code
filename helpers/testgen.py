
with open("testfile.txt", 'w') as f:
    for i in range(0,256):
        f.write(f"{i}\n")
