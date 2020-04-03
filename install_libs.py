import subprocess
import os,sys
import importlib
import json



def install(packages):
    for libname in packages:
        try:
            importlib.import_module(libname)
            print(packages[libname] + " already installed")
        except ImportError:
            print("Installing "+packages[libname])
            proc = subprocess.Popen([sys.executable, "-m", "pip", "install", packages[libname]],stdout=subprocess.PIPE)
            while True:
                line = proc.stdout.readline()
                if not line:
                    break
                #the real code does filtering here
                print (line.rstrip().decode('utf-8'))

with open("libraries.json") as json_file:
    libs = json.load(json_file)
    install(libs)
    print("\nEnd of installing!")

