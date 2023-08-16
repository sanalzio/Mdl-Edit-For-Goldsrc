import subprocess
import os
import sys

def main(filename, exe_yolu, outclas):
    if filename == "":
        outclas.wo("Please select a file.")
        return
    if exe_yolu == "":
        outclas.wo("Viewer exe file not found.")
        return

    outclas.wo("Starting model viewer.")
    def filedir(dosya_yolu):
        dosya_klasoru = os.path.dirname(dosya_yolu)
        return dosya_klasoru

    def gfn(dosya_yolu):
        dosya_adi = os.path.basename(dosya_yolu)
        return dosya_adi

    edir = exe_yolu.encode(sys.getfilesystemencoding())

    cmd_process = subprocess.Popen([edir, filename], cwd=filedir(filename), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    while True:
        output = cmd_process.stdout.readline()
        if output == b'' and cmd_process.poll() is not None:
            break
        if output:
            outclas.wo(output.strip().decode())
