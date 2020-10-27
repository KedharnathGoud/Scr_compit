# $language = "python"
# $interface = "1.0"

from datetime import datetime
from datetime import timedelta
import webbrowser
import os
import subprocess
import difflib
import re

class compit():

    def __init__(self):
        tab = crt.GetScriptTab()
        self.date = datetime.today().strftime('%m-%d-%Y')
        self.date = str(self.date)
        self.screenrow = crt.Screen.CurrentRow
        self.hostnamein = crt.Screen.Get(self.screenrow, 1, self.screenrow, 80)
        self.hostnamein = str(self.hostnamein).strip()
        self.hostname = self.hostnamein[:-1]
        self.prelogpath = "H:\\CompareTool\\Prechange"
        self.postlogpath = "H:\\CompareTool\\Postchange"
        self.outputlogpath = "H:\\CompareTool\\Differance_with_complete_config"
        self.hostnameofdevice = self.hostname
        self.hostnameofdevice = str(self.hostname)
        self.prepath = self.prelogpath + "/" + self.hostnameofdevice + "-" + self.date + ".txt"
        self.postpath = self.postlogpath + "/" + self.hostnameofdevice + "-" + self.date + ".txt"
        self.outputpath = self.outputlogpath + "/" + self.hostnameofdevice + "-" + self.date + ".txt"
        tab.Session.Log(False)


    def compare(self,router="1"):
        hostn = crt.Screen.Get(crt.Screen.CurrentRow, 1, crt.Screen.CurrentRow, 20)
        hostn = hostn.strip()
        tab = crt.GetScriptTab()
        xx = ""
        # rr=crt.Dialog.Prompt('Please Select the type of router name'   'Enter Your Option', nn)
        show = ""

        ked = "!"
        y = ""

        tab.Session.LogFileName = self.outputpath
        tab.Session.Log(True)
        tab.Session.Log(False)
        crt.Session.SetStatusText(
            "Analyzing the logs please be patience the log files are larger than expected and make sure this session doesn't expire ")
        try:
            text1 = open(self.prepath, "r")


        except IOError:
            w = datetime.today() - timedelta(days=1)
            w = w.strftime('%m-%d-%Y')
            self.prepath = self.prelogpath + "/" + self.hostnameofdevice + "-" + w + ".txt"
        try:
            text1 = open(self.prepath, "r")


        except IOError:
            p = datetime.today() + timedelta(days=1)
            p = p.strftime('%m-%d-%Y')
            self.prepath = self.prelogpath + "/" + self.hostnameofdevice + "-" + p + ".txt"
        try:
            text1 = open(self.prepath, "r")

        except IOError:
            crt.Dialog.MessageBox(
                "Error Seem like You didn't take the Pre checks log if you took the logs 1 day before then just change date on the log file")
            return
        try:
            text2 = open(self.postpath, "r")
        except IOError:
            w = datetime.today() - timedelta(days=1)
            w = w.strftime('%m-%d-%Y')
            self.postpath = self.postlogpath + "/" + self.hostnameofdevice + "-" + w + ".txt"
        try:
            text2 = open(self.postpath, "r")

        except IOError:
            p = datetime.today() + timedelta(days=1)
            p = p.strftime('%m-%d-%Y')
            self.postpath = self.postlogpath + "/" + self.hostnameofdevice + "-" + p + ".txt"
        try:
            text2 = open(self.postpath, "r")
        except:
            crt.Dialog.MessageBox(
                "Sorry Seem like You didn't take the Post checks log if you took the logs 1 day before then just change date on the log file")
            return
        d = difflib.Differ()
        diff = list(d.compare(text1.readlines(), text2.readlines()))
        crt.Session.SetStatusText("Working on the comparison.")
        with open(self.outputpath, 'w+') as diff_file:
            _diff = ''.join(diff)
            diff_file.write(_diff)
            ff = open(self.outputpath, 'r')
            _line = ''
            f = open("H:\\CompareTool\\Differance_in_Config_" + self.hostnameofdevice + ".txt", "w+")
            f.write(
                "## Note:'+' Represents the line you have added,\n '-' Represents the line you have removed if you don�t see any line expect this \n Then you haven't made any changes# If a '-' is follwed '+' then you have replaced the line with - by + ##\n\n")
            for line in ff:
                crt.Session.SetStatusText("Working on the comparison..")
                hostn = str(self.hostnamein)
                # if router=='2':
                # count=0
                # if line.startswith('      '):
                # if not line.startswith('       '):
                # y=line

                if line.startswith('  '):
                    if not line.startswith('   '):
                        x = line
                if line.startswith('  ' + hostn + 'sh'):
                    show = line
                # f.write(x)
                if line.startswith('-'):
                    _d = '-'
                    _line = line
                    if router == "1":
                        shows = ""
                        if show != shows:
                            f.write("\n In " + show + "\n")
                            show = shows

                        if x != xx:
                            f.writelines("\n***ON or After this line = " + x + "\n")
                            x = xx
                        f.write(_line)

                    else:
                        f.write(y)
                        f.write(_line)
                elif line.startswith('+'):

                    _d = '+'
                    _line = line

                    if x != xx:
                        f.writelines("\n***ON or After this line = " + x + "\n")
                        x = xx
                    f.write(_line)

            # if line.startswith('?'):
            # dp = line.find(_d)
            # dp=_line
            # f.write(_line)
            # if dp == -1:
            # _d = '+'
            # dp = line.find('^')
            # dpl = _line.rfind(',', 0, dp)
            # if dpl == -1:
            # dpl = 2
            # else:
            #   dpl += 1
            #  dpr = _line.find(',', dp)
            #   if dpr == dp:
            #   _d = ' '
            #  dpl = dp
            #  dpr = dp+1

            # dpw = dpr - dpl
            # line = line[:dpl] + _d*dpw + line[dpr:]
            # _line = line
            # f.write(_line)
            crt.Session.SetStatusText("Working on the comparison....")
        self.LaunchViewer("H:\\CompareTool\\Differance_in_Config_" + self.hostnameofdevice + ".txt")
        crt.Session.SetStatusText("comparison completed Look for the output file")
        return

        # crt.Dialog.MessageBox("!! Wrong input Please select any of the options from 1 or 2 or 3 !!\n" + chr(13))
        # return
        # LaunchViewer("H:\Differance in Config with complete config.txt")

   # tab.Session.Log(True)
    def prechecks(self,Result):
        objTab = crt.GetScriptTab()
        objTab.Screen.Synchronous = True
        tab = crt.GetScriptTab()
        dir = "C:\\Comp\\Temp\\Show_commands.txt"
        tab.Session.LogFileName =self.prepath
        tab.Session.Log(True)
        crt.Screen.Synchronous = True
        crt.Session.SetStatusText("Taking Backups of Cisco Devices")
        crt.Screen.Send("term len 0" + chr(13))
        for line in open(dir):
            #crt.Dialog.MessageBox(line)
            line = str(line)
            line = line.strip()
            crt.Screen.Send(line+chr(13))

        if Result == "y":
            szCommand = "pwd"
            objTab.Screen.Send(szCommand + "\r\n")
            objTab.Screen.WaitForString(szCommand + "\r\n")
            Dir = objTab.Screen.ReadString(self.hostnamein)
            # tab.Session.Log(False)
            Dir=Dir.strip()
            #crt.Dialog.MessageBox(Dir)

            crt.Screen.Send("copy running-config "+Dir+"config_"+ self.date  + ".old")
        crt.Screen.Synchronous = False
    def postchecks(self):
        tab = crt.GetScriptTab()
        dir = "C:\\Comp\\Temp\\Show_commands.txt"
        tab.Session.LogFileName =self.postpath
        tab.Session.Log(True)
        crt.Screen.Synchronous = True
        crt.Session.SetStatusText("Taking Backups of Cisco Devices")
        crt.Screen.Send("term len 0" + chr(13))
        for line in open(dir):
            #crt.Dialog.MessageBox(line)
            line = str(line)
            line = line.strip()
            crt.Screen.Send(line+chr(13))
        crt.Screen.Synchronous = False


    def LaunchViewer(self,filename):
        try:
            os.startfile(filename)
        except AttributeError:
            subprocess.call(['open', filename])






def main():
    LOG_DIRECTORY = os.path.join(os.path.expanduser('~'), 'C:\\Comp\\Temp')
    LOG_FILE_TEMPLATE = os.path.join(LOG_DIRECTORY, "HOST + .txt")
    if not os.path.exists(LOG_DIRECTORY):
        os.makedirs(LOG_DIRECTORY)

    if not os.path.isdir(LOG_DIRECTORY):
        print("Log output directory %r is not a directory" % LOG_DIRECTORY)

    LOG_DIRECTORY = os.path.join(os.path.expanduser('~'), 'C:\\Comp\\')
    # LOG_FILE_TEMPLATE = os.path.join(LOG_DIRECTORY, "HOST + .txt")
    if not os.path.exists(LOG_DIRECTORY):
        os.makedirs(LOG_DIRECTORY)

    if not os.path.isdir(LOG_DIRECTORY):
        print("Log output directory %r is not a directory" % LOG_DIRECTORY)

    objTab = crt.GetScriptTab()
    objTab.Screen.Synchronous = True
    opt = ""
    ip = []
    opthostname = ""
    router = ""
    Dir = ""
    hostname = ""
    crt.Screen.Synchronous = False
    crt.Screen.Send('\n')

    tab = crt.GetScriptTab()
    Result = "n"
    opt = crt.Dialog.Prompt(
        'Please select your option \n\n 1= Before Change-PRE CHECKS  \n \n 2=After Change POST CHECKS  \n \n 3= Compare the PRE & POST Checks \n',
        'Enter Your option', opt)
    objofcompit=compit()
    if opt == "1":
        dir = "C:\\Comp\\Temp\\Show_commands.txt"

        with open(dir, "w+") as dd:
            # dd2=subprocess.Popen("H:\Desktop\HOST.txt",shell=True)

            crt.Dialog.MessageBox(
                "!! Add the SHOW commands in the C:\Comp\Temp\Show_commands.txt file in Sequence\n Example \n Show int des \n sh ip int br\n and save the text file   !!\n" + chr(
                    13))

        objofcompit.LaunchViewer(dir)
        Result = crt.Dialog.Prompt('Do you want to save the backup to the flash \n\n y=Yes \n\n n=No \n\n',
                                   'Enter Your Option', Result)

        #crt.Dialog.MessageBox("Started Processing")

        objofcompit.prechecks(Result)


        crt.Screen.Synchronous = False
    elif opt == "2":
        dir = "C:\\Comp\\Temp\\Show_commands.txt"
        #crt.Dialog.MessageBox("Starting Process")
        objofcompit.postchecks()
    elif opt == "3":
        objofcompit.compare()
main()