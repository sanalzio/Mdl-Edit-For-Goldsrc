filename=r"C:\Users\User\Desktop\mpt-76\source\p_\p_m4a1.mdl"
with open(filename.lower().replace(".mdl", ".qc"), "r", encoding="utf-8") as f:
    origqc = f.readlines()
for l in range(0, len(origqc)):
    try:
        line=origqc[l]
        if line.startswith("//"):
            origqc.pop(l)
        if "$modelname" in line:
            origqc = origqc[l:]
        if "$bbox" in line:
            origqc.pop(l)
        if "$cbox" in line:
            origqc.pop(l)
        if "$hbox" in line:
            origqc.pop(l)
        if "$eyeposition" in line:
            origqc.pop(l)
            if "\n" == line and origqc[l+1] == "\n":
                origqc.pop(l)
    except IndexError:
        pass