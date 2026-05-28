from src.imports import *
from main import main

#Python Typing Text Effect - www.101computing.net/python-typing-text-effect/
def typingPrint(text):
   for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.05)


def check_platform():
    if platform.system() == "Windows" or platform.system() == "win32" or platform.system() == "windows":
        hostname = os.getenv("COMPUTERNAME")
        return hostname
    elif platform.system() == "Linux" or platform.system() == "linux" or platform.system() == "linux2":
        hostname = socket.gethostname()
        return hostname
    
