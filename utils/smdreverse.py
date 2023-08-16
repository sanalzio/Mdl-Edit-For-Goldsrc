def main(filename, outclas):
    if filename == "":
        outclas.wo("Please select a file.")
        return

    con = []
    pref = []
    suff = ["end\n"]

    with open(filename, "r") as f:
        con = f.readlines()

    for l in con:
        if "skeleton" in l:
            pi = con.index(l)
            pref = con[:pi] + ["skeleton\n"]
            con = con[pi + 1 :]
            con.pop()
            break

    fc = 0
    for l in con:
        if "time" in l:
            fc += 1

    def parse_frame(con):
        frame = []
        for line in con:
            frame.append(line + "\n")
        return frame

    frames = []
    current_frame = []

    for line in con:
        if line.startswith("time"):
            if current_frame:
                frames.append(current_frame)
                current_frame = []
        else:
            current_frame.append(line.strip())

    if current_frame:
        frames.append(current_frame)

    parsed_frames = [parse_frame(frame) for frame in frames]

    outclas.wo(f"Info: Reversing {str(fc)} frames.")

    parsed_frames = parsed_frames[::-1]
    outf = []

    for fr in parsed_frames:
        fp = f"time {str(parsed_frames.index(fr))}\n"
        frb = fr.insert(0, fp)
        outf = outf+fr

    with open(filename, "w") as f:
        f.writelines(pref+outf+suff)

    outclas.wo("Done!")
