
import dropbox
import os

class TransferData:
  def __init__(self,accessToken):
      self.accessToken = accessToken
      
  def upload_file(self,file_from,file_to):
    dbx = dropbox.Dropbox(self.accessToken)
    for root, dirs, files in os.walk(file_from, topdown=True):
      for name in files:
               file_name = os.path.join(root, name)
               print(file_name)
               relative_path = os.path.relpath(file_name,file_from)
               dropbox_path = os.path.join(file_to,relative_path)

               with open(file_name,'rb') as f:
                 dbx.files_upload(f.read(),dropbox_path)
                
               
def main():
   accessToken = "sl.BHVweOm0Dv9pTtgGuv7J1fbKPaCxEnYuF4xiDkkhrKN-hX7aiEGea1VJoTBsSD8SXxoRoH8cGZqXQlUjyAOgpXfcnIwW3l_txeLgyaA30AfA_QsLBneN7e-RTxXyFnCUy1iZyuF7Hm-K"
   hi = TransferData(accessToken)
   
   file_from = input("Enter the path of the folder to be uploaded ")
   file_to = input("The path of the file in the dropbox")
   hi.upload_file(file_from,file_to)
   
   print("The file has been moved!!!")
        
main()
           
