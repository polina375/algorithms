import sys
input=sys.stdin.readline

class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        self.height=1

def height(v):
    return v.height if v else 0

def update(v):
    v.height=1+max(height(v.left),height(v.right))

def balance(v):
    return height(v.right)-height(v.left)

def left(v):
    u=v.right
    v.right=u.left
    u.left=v
    update(v)
    update(u)
    return u


def right(v):
    u=v.left
    v.left=u.right
    u.right=v
    update(v)
    update(u)
    return u


def fix(v):
    update(v)
    if balance(v)==2:
        if balance(v.right)<0:
            v.right=right(v.right)
        return left(v)
    if balance(v)==-2:
        if balance(v.left)>0:
            v.left=left(v.left)
        return right(v)
    return v

def add(v,x):
    if v is None:
        return Node(x)
    if x<v.key:
        v.left=add(v.left, x)
    elif x>v.key:
        v.right=add(v.right, x)
    else:
        return v
    return fix(v)

def find_min(v):
    while v.left is not None:
        v=v.left
    return v

def delete(v,x):
    if v is None:
        return None
    if x<v.key:
        v.left=delete(v.left, x)
    elif x>v.key:
        v.right=delete(v.right, x)
    else:
        if v.left is None:
            return v.right
        if v.right is None:
            return v.left
        m=find_min(v.right)
        v.key=m.key
        v.right=delete(v.right, m.key)
    return fix(v)

def exists(v, x):
    while v:
        if x==v.key:
            return True
        v=v.left if x<v.key else v.right
    return False

def next_key(v,x):
    ans=None
    while v:
        if v.key>=x:
            ans=v.key
            v=v.left
        else:
            v=v.right
    return ans

def prev_key(v,x):
    ans=None
    while v:
        if v.key<=x:
            ans=v.key
            v=v.right
        else:
            v=v.left
    return ans

def preorder(v,result):
    if v is None:
        return
    result.append(str(v.key))
    preorder(v.left,result)
    preorder(v.right,result)

root=None
q=int(input())
for t in range(q):
    cmd=input().split()
    if cmd[0]=="add":
        root=add(root, int(cmd[1]))
    elif cmd[0]=="del":
        root=delete(root, int(cmd[1]))
    elif cmd[0]=="exists":
        print("YES" if exists(root,int(cmd[1]))else "NO")
    elif cmd[0]=="next":
        print(next_key(root, int(cmd[1])))
    elif cmd[0]=="prev":
        print(prev_key(root, int(cmd[1])))
    elif cmd[0]=="root":
        print(root.key if root else "Empty")
    elif cmd[0]=="height":
        print(height(root))
    elif cmd[0]=="print":
        result=[]
        preorder(root,result)
        print(" ".join(result) if result else "Empty")
