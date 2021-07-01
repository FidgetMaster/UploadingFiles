import os
import dropbox
from dropbox.files import WriteMode


class UploadData:
    def __init__(self,accesstoken):
        self.accesstoken = accesstoken
    def uploadFiles(self, source, destination):
        dbx = dropbox.Dropbox(self.accesstoken)
        for root, dirs, files in os.walk(source):
            for i in files:
                localPath = os.path.join(root,i)
                relativePath = os.path.relpath(localPath,source)
                dropboxPath = os.path.join(destination,relativePath)

                f = open(localPath, 'rb')
                dbx.files_upload(f.read(),dropboxPath, mode = WriteMode("overwrite"))

def JustUpload():
    accesstoken = 'qQTegINbUwAAAAAAAAAAAX0huOjrx9dMkW1ZseNNbioZKu7JfLZ3haX43sE7jZNS'
    TransferData = UploadData(accesstoken)
    source = str(input("Enter File Path To Transfer: "))
    destination = input("Enter Full Path To Upload To Dropbox: ")
    TransferData.uploadFiles(source,destination)
    print("File Has Been Moved")
JustUpload()