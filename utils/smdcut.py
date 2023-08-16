def main(filename, max_triangles, outclas):
    if filename == "":
        outclas.wo("Please select a file.")
        return

    refcon = []
    pref = []
    suffix = "end\n"

    with open(filename, "r") as f:
        refcon = f.readlines()

    for l in refcon:
        if "triangles" in l:
            pi = refcon.index(l)
            pref = refcon[:pi] + ["triangles\n"]
            refcon = refcon[pi + 1 :]
            refcon.pop()
            break

    num_triangles = len(refcon) // 4

    outclas.wo("Warning: GoldSrc supports a maximum of 4080 triangles!")
    outclas.wo("Info: The selected file consists of "+str(num_triangles)+" triangles.")
    #max_triangles = int(input("How many triangles should a file have at most?  "))

    num_files = (num_triangles + max_triangles - 1) // max_triangles

    i = 0
    while i < num_files:
        with open(filename.replace(".SMD", "").replace(".smd", "") + str(i + 1) + ".smd", "w") as f:
            start = i * max_triangles * 4
            end = min(start + (max_triangles * 4), len(refcon))
            f.writelines(pref + refcon[start:end] + [suffix])
        i += 1

    outclas.wo(f"{num_files} files created successfully.")
    #print(Fore.GREEN + f"{num_files} files created successfully." + Fore.RESET)
