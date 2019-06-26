import os 
import time 
import getpass 
#import pexpect 
#from pexpect 
#import pxssh 
import sys 
import subprocess

data={ 
    "user": "prestador", 
    "host": "zimbra", 
    "password": "s3rvidor3s", 
    "commands": "cucea" 
    } 
    
#command = "sshpass -p {password} ssh {user}@{host}" 
#os.system(command.format(**data)) 

#time.sleep(2)
#subprocess.run(["ssh","prestador@zimbra"],input=)
#os.system("ssh prestador@zimbra")
#subprocess.run("ssh prestador@zimbra", shell=True)
#subprocess.Popen("ssh prestador@zimbra",1,None)
subprocess.run('cucea',shell=True)
#os.system('cucea')#run the script 
os.system('2')#select alumnos 
os.system('2')#select alta 
os.system('testNewScript')#login 
os.system('testName')#name 
os.system('testLastName')#last name 
os.system('1')#select carrera 
os.system('2019A')#ciclo de admision 
os.system('hola@gmail.com')#alternative mail 
os.system('qwer786512hjcmrt02')#curp 
os.system('2136789670')#codigo 
time.sleep(5)
