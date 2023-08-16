import subprocess
import os
import sys

def main(outclas, filename, clearqc, exe_yolu=os.path.join(os.path.join(os.path.dirname(__file__), "utils"), "mdldec.exe")):
    if filename == "":
        outclas.wo("Please select a file.")
        return
    edir = exe_yolu.encode(sys.getfilesystemencoding())

    def filedir(dosya_yolu):
        dosya_klasoru = os.path.dirname(dosya_yolu)
        return dosya_klasoru

    def gfn(dosya_yolu):
        dosya_adi = os.path.basename(dosya_yolu)
        return dosya_adi

    cmd_process = subprocess.Popen([edir, filename], cwd=filedir(filename), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    while True:
        output = cmd_process.stdout.readline()
        if output == b'' and cmd_process.poll() is not None:
            break
        if output:
            outclas.wo(output.strip().decode())

    origqc = []

    with open(filename.lower().replace(".mdl", ".qc"), "r", encoding="utf-8") as f:
        origqc = f.readlines()

    for l in origqc:
        lindex = origqc.index(l)
        if "//" in l:
            origqc.pop(lindex)
        if "$modelname" in l:
            origqc = origqc[lindex:]
        if clearqc == True:
            if "$bbox" in l:
                origqc.pop(lindex)
            if "$cbox" in l:
                origqc.pop(lindex)
            if "$hbox" in l:
                origqc.pop(lindex)
            if "$eyeposition" in l:
                origqc.pop(lindex)

    with open(filename.lower().replace(".mdl", ".qc"), "w", encoding="utf-8") as f:
        f.writelines(origqc)
        outclas.wo("QC Script edited.")


    #return_code = cmd_process.returncode
    #outclas.wo("Return code:", return_code)
