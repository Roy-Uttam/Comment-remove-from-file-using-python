import re
with open('comment.txt',"r") as f:
    data = f.read()

data = re.sub(r'//.*', "", data)
data = re.sub(r'/.*', "", data)

with open('comment-out.txt', "w") as f:
    f.write(data)