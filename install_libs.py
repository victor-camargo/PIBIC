import subprocess
import os,sys
import importlib




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

libs = {"numpy":"numpy",
        "matplotlib":"matplotlib",
        "skimage":"scikit-image",
        "sklearn":"scikit-learn",
        "cv2":"opencv-python",
        "mnist":"python-mnist",
        "scipy":"scipy"}

install(libs)
print("\nEnd of installing!")
