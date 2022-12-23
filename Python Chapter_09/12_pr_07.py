content = True
i = 1

with open("log.txt","r") as f:
    while content :
        content = f.readline()

        if "python" in content.lower():
           print(content)
           print(f"Yes, python is present in the content.in line no {i}")
        i+=1