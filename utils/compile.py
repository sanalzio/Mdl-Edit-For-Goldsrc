import subprocess
import os
import sys

def main(outclas, filename, exe_yolu=os.path.join(os.path.join(os.path.dirname(__file__), "utils"), "studiomdl.exe")):
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

    #return_code = cmd_process.returncode
    #outclas.wo("Return code:", return_code)
