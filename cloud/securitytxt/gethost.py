import os

def hostlists(id):
    ID = id

    file_list = os.listdir('C:/Users/user/Desktop/test')
    serverlist = []
    file_name =[]
    for file in file_list:
        if file.split("_")[0] == ID:
            name = file.split("_")[1]
            file_name.append(name)
    
    for name in file_name:
        server = str(name).split(".")[0]
        serverlist.append(server)

    return serverlist
