f = open("top_canada_site.txt","r+")
lines = f.readlines()
f.seek(0)
count = 0
for line in lines:
    # print(line, count)
    if count <= 0:
        count = 12
        f.write(line)
        print(line)
    count -= 1
f.truncate()
f.close()