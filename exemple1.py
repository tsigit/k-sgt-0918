from datetime import datetime  
def write_DT_in_File(file_name):
    myFile = open(file_name, 'a')
    myFile.write('\nAccessed on ' + str(datetime.now()))
    myFile.close()
