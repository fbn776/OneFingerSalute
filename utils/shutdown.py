import platform
import subprocess

def shutdown():
    system = platform.system()
    if system == "Windows":
        subprocess.run(["shutdown", "/s", "/t", "0"], shell=True)
    elif system == "Linux" or system == "Darwin":
        subprocess.run(["shutdown", "-h", "now"])
    else:
        print("Unsupported OS")

