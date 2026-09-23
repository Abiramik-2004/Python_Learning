try:
    fp=open("file.txt","r")
    data=fp.read()
    print(data)
    fp.close()
except Exception as e:
    print(e)
