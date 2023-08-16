"""# PyDB
# A Simple Database Module"""
__version__ = 1.4
__name__ = "pydb"

class pydb:
    """
    ## Example:
    ```py
    import PyDB
    db=PyDB.pydb("File.x")
    ```
    """
    def __init__(self, f):
        self.file=f
    def getData(self, key:str):
        """
        ## Example:
        ### file.db file:
        ```
        key1:hello
        key2:hallo
        ```
        ### Python File:
        ```py
        import PyDB
        db=PyDB.pylist("file.db")
        print(db.getData("key1"))
        ```
        ### Output:
        ```
        hello
        ```
        """
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
    def keys(self):
        """
        ## Example:
        ### file.db file:
        ```
        key1:hello
        key2:hallo
        ```
        ### Python File:
        ```py
        import PyDB
        db=PyDB.pylist("file.db")
        print(db.keys())
        ```
        ### Output:
        ```
        ('key1','key2')
        ```
        """
        with open(self.file, 'r', encoding="utf-8") as f:
            keys=[]
            lines = f.readlines()
            for i in lines:
                keys.append(i.split(':')[0].replace("\n", ""))
            return tuple(keys)
    def values(self):
        """
        ## Example:
        ### file.db file:
        ```
        key1:hello
        key2:hallo
        ```
        ### Python File:
        ```py
        import PyDB
        db=PyDB.pylist("file.db")
        print(db.values())
        ```
        ### Output:
        ```
        ('hello','hallo')
        ```
        """
        with open(self.file, 'r', encoding="utf-8") as f:
            keys=[]
            lines = f.readlines()
            for i in lines:
                if len(i.split(':')) < 3:
                    keys.append(i.split(':')[1].replace("\n", ""))
                else:
                    keys.append(":".join(i.split(':')[1:].replace("\n", "")))
            return tuple(keys)
    def items(self):
        """
        ## Example:
        ### file.db file:
        ```
        key1:hello
        key2:hallo
        ```
        ### Python File:
        ```py
        import PyDB
        db=PyDB.pylist("file.db")
        print(db.items())
        ```
        ### Output:
        ```
        (('key','hello'),('key2','hallo'))
        ```
        """
        with open(self.file, 'r', encoding="utf-8") as f:
            items=[]
            lines = f.readlines()
            for i in lines:
                if len(i.split(':')) < 3:
                    items.append([i.split(':')[0], i.split(':')[1].replace("\n", "")])
                else:
                    items.append([i.split(':')[0], ":".join(i.split(':')[1:]).replace("\n", "")])
            return tuple(items)
    def addData(self, key, value):
        """
        ## Example:
        ### file.db file:
        ```
        key1:hello
        key2:hallo
        ```
        ### Python File:
        ```py
        import PyDB
        db=PyDB.pylist("file.db")
        db.addData("key3", "holla")
        ```
        ### New file.db file:
        ```
        key1:hello
        key2:hallo
        key3:holla
        ```
        """
        with open(self.file, 'r+', encoding="utf-8") as f:
            valu=value.replace("\n","")
            keys=[]
            lines = f.readlines()
            for i in lines:
                keys.append(i.split(':')[0])
            if not key in keys:
                if lines!=[]:
                    if lines[len(lines)-1].find('\n') == -1:
                        lines[len(lines)-1]=lines[len(lines)-1]+'\n'
                lines.append(str(key).replace("\n", "").replace(":", "")+':'+str(valu).replace("\n", "")+'\n')
            f.seek(0)
            f.writelines(lines)
            f.truncate()
    def removeData(self, key):
        """
        ## Example:
        ### file.db file:
        ```
        key1:hello
        key2:hallo
        key3:holla
        ```
        ### Python File:
        ```py
        import PyDB
        db=PyDB.pylist("file.db")
        db.removeData("key3")
        ```
        ### New file.db file:
        ```
        key1:hello
        key2:hallo
        ```
        """
        with open(self.file, 'r+', encoding="utf-8") as f:
            lines = f.readlines()
            for i in lines:
                if i.split(':')[0]==str(key):
                    lines.remove(i)
            f.seek(0)
            f.writelines(lines)
            f.truncate()
    def clear(self):
        """
        ## Example:
        ### file.db file:
        ```
        key1:hello
        key2:hallo
        ```
        ### Python File:
        ```py
        import PyDB
        db=PyDB.pylist("file.db")
        db.clear()
        ```
        ### New file.db file:
        ```
        (Empty)
        ```
        """
        with open(self.file, 'w') as f:
            f.write('')
    def backUp(self, newfile:str):
        """
        ## Example:
        ### file.db file:
        ```
        key1:hello
        key2:hallo
        ```
        ### Python File:
        ```py
        import PyDB
        db=PyDB.pylist("file.db")
        db.backUp("newFile.db")
        ```
        ### newFile.db file:
        ```
        key1:hello
        key2:hallo
        ```
        """
        with open(self.file, 'r', encoding="utf-8") as f:
            lines = f.readlines()
            with open(newfile, 'w') as f:
                f.writelines(lines)
    def setData(self, key, newValue):
        """
        ## Example:
        ### file.db file:
        ```
        key1:hello
        key2:hallo
        ```
        ### Python File:
        ```py
        import PyDB
        db=PyDB.pylist("file.db")
        db.setData("key2", "holla")
        ```
        ### newFile.db file:
        ```
        key1:hello
        key2:holla
        ```
        """
        with open(self.file, 'r+', encoding="utf-8") as f:
            lines = f.readlines()
            for i in lines:
                if i.split(':')[0]==str(key):
                    lines[lines.index(i)]=str(key).replace("\n", "").replace(":", "")+':'+str(newValue).replace("\n", "")+'\n'
                    f.seek(0)
                    with open(self.file, 'w') as fi:
                        fi.writelines(lines)
    def fileToDICT(self):
        """
        ## Example:
        ### file.db file:
        ```
        key1:hello
        key2:hallo
        ```
        ### Python File:
        ```py
        import PyDB
        db=PyDB.pylist("file.db")
        db.fileToDICT()
        ```
        ### Output:
        ```
        {'key1':'hello','key2','hallo'}
        ```
        """
        with open(self.file, 'r', encoding="utf-8") as f:
            dictionary={}
            lines= f.readlines()
            for i in lines:
                if i.find(":")!=-1:
                    a=i.split(':')
                    if len(a)==2:
                        dictionary[a[0]]=a[1].replace("\n", "")
                    if len(a)>2:
                        dictionary[a[0]]=":".join(a[1:]).replace("\n", "")
            return dictionary
    def dictToFILE(self, dictionary:dict):
        """
        ## Example:
        ### Python File:
        ```py
        import PyDB
        db=PyDB.pylist("file.db")
        db.dictToFILE({'key1':'hello','key2','hallo'})
        ```
        ### file.db file:
        ```
        key1:hello
        key2:hallo
        ```
        """
        with open(self.file, 'w', encoding="utf-8") as f:
            lines=[]
            for k,v in dictionary.items():
                lines.append("{}:{}\n".format(str(k).replace("\n", "").replace(":", ""),str(v).replace("\n","")))
            f.writelines(lines)
    def control(self, key):
        """
        ### This Command Checks Whether There Is a Counterpart to the Key
        """
        with open(self.file, 'r', encoding="utf-8") as f:
            l= f.readlines()
            for i in l:
                if i.find(":")== -1:
                    l.pop(l.index(i))
            for i in l:
                if i.split(':')[0]==str(key):
                    return True
            return False

class pylist:
    """
    ## Example:
    ```py
    import PyDB
    db=PyDB.pylist("File.x")
    ```
    """
    def __init__(self, file:str):
        self.f=file
    def getData(self, index:int):
        """
        ## Example:
        ### db.list file:
        ```
        hello
        hallo
        ```
        ### Python File:
        ```py
        import PyDB
        db=PyDB.pylist("db.list")
        print(db.getData(0))
        ```
        ### Output:
        ```
        hello
        ```
        """
        with open(self.f, 'r', encoding="utf-8") as f:
            l=f.readlines()
            if len(l)-1 < index:
                return None
            else:
                return l[int(index)].replace("\n", "")
    def listFile(self):
        """
        ## Example:
        ### db.list file:
        ```
        hello
        hallo
        ```
        ### Python File:
        ```py
        import PyDB
        db=PyDB.pylist("db.list")
        print(db.listFile())
        ```
        ### Output:
        ```
        ['hello','hallo']
        ```
        """
        with open(self.f, 'r', encoding="utf-8") as f:
            liste=f.readlines()
            op = []
            for i in liste:
                a=i.replace("\n","")
                op.append(a)
            return op
    def listToFILE(self, lst:list):
        """
        ## Example:
        ### Python File:
        ```py
        import PyDB
        db=PyDB.pylist("db.list")
        db.listToFILE(['hello','hallo'])
        ```
        ### New db.list file:
        ```
        hello
        hallo
        ```
        """
        with open(self.f, 'w', encoding="utf-8") as f:
            liste= []
            for i in lst:
                liste.append(str(i).replace("\n","")+"\n")
            f.writelines(liste)
    def addData(self, value):
        """
        ## Example:
        ### db.list file:
        ```
        hello
        hallo
        ```
        ### Python File:
        ```py
        import PyDB
        db=PyDB.pylist("db.list")
        db.addData("holla")
        ```
        ### New db.list file:
        ```
        hello
        hallo
        holla
        ```
        """
        with open(self.f, 'r+', encoding="utf-8") as f:
            lines = f.readlines()
            lines.append(str(value).replace("\n","")+"\n")
            f.seek(0)
            f.writelines(lines)
            f.truncate()
    def setData(self, index:int, value):
        """
        ## Example:
        ### db.list file:
        ```
        hello
        hallo
        ```
        ### Python File:
        ```py
        import PyDB
        db=PyDB.pylist("db.list")
        db.setData(1, "holla")
        ```
        ### New db.list file:
        ```
        hello
        holla
        ```
        """
        with open(self.f, 'r+', encoding="utf-8") as f:
            lines = f.readlines()
            lines[int(index)]=str(value).replace("\n","")+"\n"
            f.seek(0)
            f.writelines(lines)
            f.truncate()
    def removeData(self, index:int):
        """
        ## Example:
        ### db.list file:
        ```
        hello
        hallo
        holla
        ```
        ### Python File:
        ```py
        import PyDB
        db=PyDB.pylist("db.list")
        db.removeData(2)
        ```
        ### New db.list file:
        ```
        hello
        hallo
        ```
        """
        with open(self.f, 'r+', encoding="utf-8") as f:
            lines=f.readlines()
            lines.pop(int(index))
            f.seek(0)
            f.writelines(lines)
            f.truncate()
    def clear(self):
        
        """
        ## Example:
        ### db.list file:
        ```
        hello
        hallo
        holla
        ```
        ### Python File:
        ```py
        import PyDB
        db=PyDB.pylist("db.list")
        db.clear()
        ```
        ### New db.list file:
        ```
        (Empty)
        ```
        """
        f= open(self.f, 'w', encoding="utf-8")
        f.write("")
        f.close()
    def lenFile(self):
        
        """
        ## Example:
        ### db.list file:
        ```
        hello
        hallo
        holla
        ```
        ### Python File:
        ```py
        import PyDB
        db=PyDB.pylist("db.list")
        print(db.lenFile())
        ```
        ### Output:
        ```
        3
        ```
        """
        with open(self.f, 'r', encoding="utf-8") as f:
            liste=f.readlines()
            op = []
            for i in liste:
                a=i.replace("\n","")
                op.append(a)
            return len(op)


def dictToTABLE(dictionary):
    """
    ## Example:
    ```py
    import PyDB
    print(PyDB.dictToTABLE({"Key":"Value","Apple":"Orange"}))
    ```
    ## Output:
    ```
    +---------+---------------+
    |   Key   |     Value     |
    +---------+---------------+
    |Key      |Value          |
    +---------+---------------+
    |Apple    |Orange         |
    +---------+---------------+
    ```
    """
    ll="+"+"-"*9+"+"+"-"*15+"+\n"
    table=ll+"|   Key   |     Value     |\n"+ll
    for k,v in dictionary.items():
        table+="|{:<9}|{:<15}|\n".format(k, v)
        table+=ll
    return table
def listToTABLE(list):
    """
    ## Example:
    ```py
    import PyDB
    print(PyDB.listToTABLE(["Value","Apple"]))
    ```
    ## Output:
    ```
    +-----+---------------+
    |Index|     Value     |
    +-----+---------------+
    |0    |Value          |
    +-----+---------------+
    |1    |Apple          |
    +-----+---------------+
    ```
    """
    ll="+"+"-"*5+"+"+"-"*15+"+\n"
    table=ll+"|Index|     Value     |\n"+ll
    for v in list:
        table+="|{:<5}|{:<15}|\n".format(list.index(v), v)
        table+=ll
    return table
