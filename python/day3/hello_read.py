with open('python/day3/hello.txt','r') as file:
    content = file.read()
print(content)

#r -- read
#w -- write
#a -- append

with open('python/day3/hello.txt','r') as file:

    line_by_line = file.readlines()

print(line_by_line)    