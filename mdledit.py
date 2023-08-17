import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from mdleditgui import *
import subprocess
import os
import shutil

#-----------DataBase------------#
if not os.path.exists("config.txt"):
    with open('config.txt', 'w') as f:
        f.write("last_selected_file:{None}\nlast_tab:decomp\nmoddir:C:/Program Files (x86)/Steam/steamapps/common/Half-Life/valve\nshortcut_dir:{None}\nstart_by_selecting_a_file:{False}\ncustom_studiomdl:{None}\n")
import modules.PyDB
db=modules.PyDB.pydb("config.txt")
#-----------DataBase------------#

#-----------tools------------#
def filedir(dosya_yolu):
    dosya_klasoru = os.path.dirname(dosya_yolu)
    return dosya_klasoru
def gfn(dosya_yolu):
    dosya_adi = os.path.basename(dosya_yolu)
    return dosya_adi
#-----------tools------------#


#---------------codes--------------#
class CutomUi_MainWindow(Ui_MainWindow):
    #-----------modules------------#
    def test(self, filename, moddir, shortcut):
        oldname = moddir+"/models/"+gfn(filename)
        newname = moddir+"/models/"+gfn(filename).replace(".", "_oldmodel.")
        if os.path.exists(newname):
            shutil.copy2(filename, moddir+"/models/")
        else:
            os.rename(oldname, newname)
            shutil.copy(filename, moddir+"/models/")
        if db.getData("shortcut_dir") != None:
            self.wo("Info: Starting Game...")
            os.startfile(db.getData("shortcut_dir"))
        else:
            self.wo("Error: Please enter a shortcut direction in config menu.")
    def wo(self, message):
        current_text = self.kosol.toPlainText()
        new_text = f"{current_text}{str(message)}\n"
        self.kosol.setPlainText(new_text)
    def compress(self, filename, bol):
        if filename == "":
            self.wo("Please select a file.")
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
        self.wo(f"Info: your animation frame count is {str(fc)}.")
        self.wo("Info: GoldSrc supports a maximum of 512 frames per sequence.")
        #bol = int(input("How should the SMD file be divided? Please enter a value of 2 or more.  "))
        if bol < 2:
            self.wo("Please enter a value of 2 or more.")
            return
        parsed_frames = parsed_frames[::bol]
        outf = []
        for fr in parsed_frames:
            fp = f"time {str(parsed_frames.index(fr))}\n"
            frb = fr.insert(0, fp)
            outf = outf+fr
        with open(filename, "w") as f:
            f.writelines(pref+outf+suff)
        self.wo("The compression process was completed successfully.")
    def compiler(self, filename):
        exe_yolu=os.path.join(os.path.join(os.path.dirname(__file__), "utils"), "studiomdl.exe")
        if db.getData("custom_studiomdl") != None:
            exe_yolu=db.getData("custom_studiomdl")
        self.kosol.setPlainText("")
        if filename == "":
            self.wo("Please select a file.")
            return
        edir = exe_yolu.encode(sys.getfilesystemencoding())
        cmd_process = subprocess.Popen([edir, filename], cwd=filedir(filename), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        while True:
            output = cmd_process.stdout.readline()
            if output == b'' and cmd_process.poll() is not None:
                break
            if output:
                self.wo(output.strip().decode())
    def decompiler(self, filename, clearqc, exe_yolu=os.path.join(os.path.join(os.path.dirname(__file__), "utils"), "mdldec.exe")):
        self.kosol.setPlainText("")
        if filename == "":
            self.wo("Please select a file.")
            return
        edir = exe_yolu.encode(sys.getfilesystemencoding())
        cmd_process = subprocess.Popen([edir, filename], cwd=filedir(filename), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        while True:
            output = cmd_process.stdout.readline()
            if output == b'' and cmd_process.poll() is not None:
                break
            if output:
                self.wo(output.strip().decode())
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
            if "\n" == l:
                if origqc[origqc.index(l)+1] == "\n":
                    origqc.pop(lindex)
        with open(filename.lower().replace(".mdl", ".qc"), "w", encoding="utf-8") as f:
            f.writelines(origqc)
            self.wo("QC Script edited.")
    def cutter(self,filename, max_triangles):
        if filename == "":
            self.wo("Please select a file.")
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
        self.wo("Warning: GoldSrc supports a maximum of 4080 triangles!")
        self.wo("Info: The selected file consists of "+str(num_triangles)+" triangles.")
        #max_triangles = int(input("How many triangles should a file have at most?  "))
        num_files = (num_triangles + max_triangles - 1) // max_triangles
        i = 0
        while i < num_files:
            with open(filename.replace(".SMD", "").replace(".smd", "") + str(i + 1) + ".smd", "w") as f:
                start = i * max_triangles * 4
                end = min(start + (max_triangles * 4), len(refcon))
                f.writelines(pref + refcon[start:end] + [suffix])
            i += 1
        self.wo(f"{num_files} files created successfully.")
    def cls(self):
        self.kosol.setPlainText("")
    def rev(self, filename):
        if filename == "":
            self.wo("Please select a file.")
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
        self.wo(f"Info: Reversing {str(fc)} frames.")
        parsed_frames = parsed_frames[::-1]
        outf = []
        for fr in parsed_frames:
            fp = f"time {str(parsed_frames.index(fr))}\n"
            frb = fr.insert(0, fp)
            outf = outf+fr
        with open(filename, "w") as f:
            f.writelines(pref+outf+suff)
        self.wo("Done!")
    #-----------modules------------#
    #-----------init------------#
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        #-----------onstart------------#
        if db.getData("start_by_selecting_a_file") == True:
            self.open_file_dialog()
            sbs_checkbox = self.cfgmenu.findChild(QtWidgets.QCheckBox, "sbs")
            if sbs_checkbox:
                sbs_checkbox.setChecked(True)
        if db.getData("custom_studiomdl") != None:
            self.stpath.setText(db.getData("custom_studiomdl"))
        if db.getData("shortcut_dir") != None:
            self.shpath.setText(db.getData("shortcut_dir"))
        if db.getData("last_selected_file") != None:
            self.filepath.setText(db.getData("last_selected_file"))
        self.moddir.setText(db.getData("moddir"))
        if db.getData("last_tab") == "cfg":
            self.sekmeler.setCurrentWidget(self.cfgmenu)
            self.filepath.hide()
            self.kosol.hide()
            self.sfile.hide()
        if db.getData("last_tab") == "tst":
            self.sekmeler.setCurrentWidget(self.testmenu)
        if db.getData("last_tab") == "comp":
            self.sekmeler.setCurrentWidget(self.compmenu)
        if db.getData("last_tab") == "decomp":
            self.sekmeler.setCurrentWidget(self.decompmenu)
        if db.getData("last_tab") == "cut":
            self.sekmeler.setCurrentWidget(self.cutmenu)
        if db.getData("last_tab") == "zip":
            self.sekmeler.setCurrentWidget(self.compressmenu)
        if db.getData("last_tab") == "rev":
            self.sekmeler.setCurrentWidget(self.revmenu)
        #-----------onstart------------#
        self.sfile.clicked.connect(self.open_file_dialog)
        self.compbutton.clicked.connect(self.compile_button_clicked)
        self.decompbutton.clicked.connect(self.decompile_button_clicked)
        self.stfsel.clicked.connect(self.studiomdlselect_button_clicked)
        self.shsel.clicked.connect(self.lnksel_button_clicked)
        self.savebtn.clicked.connect(self.save_button_clicked)
        self.compressbutton.clicked.connect(self.compr_button_clicked)
        self.cutbutton.clicked.connect(self.cut_button_clicked)
        self.revbutton.clicked.connect(self.rev_button_clicked)
        self.testbtn.clicked.connect(self.test_button_clicked)
        self.smoddir.clicked.connect(self.modbtn_button_clicked)
        self.sbs.stateChanged.connect(self.save_button_clicked)
        self.sekmeler.currentChanged.connect(self.tab_changed)
    #-----------init------------#
    #-----------functions------------#
    def open_file_dialog(self):
        file_dialog = QFileDialog()
        user_home_dir = os.path.expanduser("~")
        desktop_dir = os.path.join(user_home_dir, "Desktop")
        file_dialog.setDirectory(desktop_dir)
        if db.getData("last_selected_file") != None:
            file_dialog.setDirectory(filedir(db.getData("last_selected_file")))
        file_dialog.setNameFilter("Model Files (*.qc *.mdl *.smd)")
        file_dialog.setViewMode(QFileDialog.List)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                selected_file = selected_files[0]
                """if selected_file.lower().endswith('.mdl'):
                    self.sekmeler.setCurrentWidget(self.decompmenu)
                    self.filepath.setText(selected_file)"""
                if selected_file.lower().endswith('.qc'):
                    self.sekmeler.setCurrentWidget(self.compmenu)
                    self.filepath.setText(selected_file)
                else:
                    self.filepath.setText(selected_file)
            db.setData("last_selected_file", selected_file)
    def compr_button_clicked(self):
        self.cls()
        file_path = self.filepath.text()
        bol=self.bolengirdi.text()
        self.compress(file_path, int(bol))
    def test_button_clicked(self):
        file_path= self.filepath.text()
        self.test(file_path, db.getData("moddir"), db.getData("shortcut_dir"))
    def cut_button_clicked(self):
        self.cls()
        file_path= self.filepath.text()
        max_triangles=self.ucgengirdi.text()
        self.cutter(file_path, int(max_triangles))
    def rev_button_clicked(self):
        self.cls()
        filepath=self.filepath.text()
        self.rev(filepath)
    def compile_button_clicked(self):
        self.cls()
        file_path = self.filepath.text()
        self.wo(f"Compiling: {file_path}")
        self.compiler(file_path)
    def decompile_button_clicked(self):
        self.cls()
        file_path = self.filepath.text()
        self.wo("Decompiling: {}".format(file_path))
        clqc_checked = self.clqc.isChecked()
        if clqc_checked:
            self.decompiler(file_path, True)
        else:
            self.decompiler(file_path, False)
    def lnksel_button_clicked(self):
        file_dialog = QFileDialog()
        user_home_dir = os.path.expanduser("~")
        desktop_dir = os.path.join(user_home_dir, "Desktop")
        file_dialog.setDirectory(desktop_dir)
        file_dialog.setNameFilter("Model Files (*.lnk)")
        file_dialog.setViewMode(QFileDialog.List)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                self.shpath.setText(selected_files[0])
                self.save_button_clicked()
    def modbtn_button_clicked(self):
        file_dialog = QFileDialog()
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly
        user_home_dir = os.path.expanduser("~")
        desktop_dir = os.path.join(user_home_dir, "Desktop")
        file_dialog.setDirectory(desktop_dir)
        directory = file_dialog.getExistingDirectory(None, "Klasör Seç", "", options=options)
        if directory:
            self.moddir.setText(directory)
            self.save_button_clicked()
    def studiomdlselect_button_clicked(self):
        file_dialog = QFileDialog()
        user_home_dir = os.path.expanduser("~")
        desktop_dir = os.path.join(user_home_dir, "Desktop")
        file_dialog.setDirectory(desktop_dir)
        file_dialog.setNameFilter("Model Files (*.exe)")
        file_dialog.setViewMode(QFileDialog.List)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                self.stpath.setText(selected_files[0])
                self.save_button_clicked()
    def save_button_clicked(self):
        sbs_checked = self.sbs.isChecked()#db.getData("moddir")
        if sbs_checked:
            db.setData("start_by_selecting_a_file", "{True}")
        else:
            db.setData("start_by_selecting_a_file", "{False}")
        if self.stpath.text()=="":
            db.setData("custom_studiomdl", "{None}")
        else:
            db.setData("custom_studiomdl", self.stpath.text())
        if self.moddir.text()!="":
            db.setData("moddir", self.moddir.text())
        if self.shpath.text()!="":
            db.setData("shortcut_dir", self.shpath.text())
    def tab_changed(self, index):
        if index == self.sekmeler.indexOf(self.testmenu):
            db.setData("last_tab", "tst")
        if index == self.sekmeler.indexOf(self.cfgmenu):
            db.setData("last_tab", "cfg")
        if index == self.sekmeler.indexOf(self.compmenu):
            db.setData("last_tab", "comp")
        if index == self.sekmeler.indexOf(self.decompmenu):
            db.setData("last_tab", "decomp")
        if index == self.sekmeler.indexOf(self.cutmenu):
            db.setData("last_tab", "cut")
        if index == self.sekmeler.indexOf(self.compressmenu):
            db.setData("last_tab", "zip")
        if index == self.sekmeler.indexOf(self.revmenu):
            db.setData("last_tab", "rev")
        if index == self.sekmeler.indexOf(self.cfgmenu):
            self.filepath.hide()
            self.kosol.hide()
            self.sfile.hide()
        else:
            self.filepath.show()
            self.kosol.show()
            self.sfile.show()
    #-----------functions------------#
#----------------codes---------------#
app = QApplication(sys.argv)
window = QMainWindow()
ui = CutomUi_MainWindow()
ui.setupUi(window)
window.setFixedSize(569, 385)
window.show()
sys.exit(app.exec_())
