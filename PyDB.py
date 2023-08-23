class pydb:
    def __init__(self, f):
        self.file=f
    def getData(self, key:str):
        with open(self.file, 'r', encoding="utf-8") as f:
            l = f.readlines()
            for i in l:
                if i.find(":")==-1:
                    l.pop(l.index(i))
            il=[]
            for i in l:
                il.append(i.split(':')[0])
            if not key in il:
                return None
            else:
                for i in l:
                    a=i.split(':')
                    if a[0]==str(key):
                        if len(a) == 2:
                            if a[1]=="{True}\n":
                                return True
                            elif a[1]=="{False}\n":
                                return False
                            elif a[1]=="{None}\n":
                                return None
                            else:
                                return a[1].replace("\n", "")
                        elif len(a)>2:
                            return ":".join(a[1:]).replace("\n", "")
    def setData(self, key, newValue):
        with open(self.file, 'r+', encoding="utf-8") as f:
            lines = f.readlines()
            for i in lines:
                if i.split(':')[0]==str(key):
                    lines[lines.index(i)]=str(key).replace("\n", "").replace(":", "")+':'+str(newValue).replace("\n", "")+'\n'
                    f.seek(0)
                    with open(self.file, 'w') as fi:
                        fi.writelines(lines)