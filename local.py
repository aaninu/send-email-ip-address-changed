
def get_saved_ip():
    try:
        path = 'old_ip.txt'
        fileOpen = open(path,'r')
        ipAddress = fileOpen.read()
        fileOpen.close()
    except:
        ipAddress = ""
    return ipAddress

def save_ip(address):
    path = 'old_ip.txt'
    fileOpen = open(path,'w')
    fileOpen.write(address)
    fileOpen.close()
