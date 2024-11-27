import datetime

class Logger:
    def __init__(self, filePath):
        try: 
            print(filePath)
            self.fd = open(filePath, "a")
        except FileNotFoundError:
            print("FileNotFoundError, creating file")
            self.fd = open(filePath, "x")

    def WriteToFile(self,message):
        self.fd.write(f"{message}\n")

    def __del__(self):
        self.fd.close()        
        print("Fd Closed")
