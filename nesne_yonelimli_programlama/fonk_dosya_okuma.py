# fonksiyon dosya okuma

def read(filename):
    with open(filename,"r") as f:
        return [line for line in f]
    
def count(lines):
    return len(lines)

example=read("deneme.txt")
ex_count=count(example)
ex_count
example    
        