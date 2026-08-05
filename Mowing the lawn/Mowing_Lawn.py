open_file = open("file mowing.in", 'r')
print(open_file)
read_file = open_file.readlines()
for i in range(len(read_file)):
    read_file[i] = read_file[i].strip()
    read_file[i] = read_file[i].split()
print(read_file)
