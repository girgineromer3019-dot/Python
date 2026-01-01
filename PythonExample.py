""""""""""
class file():
    def __init__(self):
        with open("TvRemote.py", "r") as f:
            FileContent = f.read()
            words = FileContent.split()
            for i in words:
                print(i)

file = file()
"""""""""""

class file():
    def __init__(self):
        with open("TvRemote.py", "r") as f:
            FileContent = f.read()
            words = FileContent.split()
            for i in words:
                print(i)
file = file()