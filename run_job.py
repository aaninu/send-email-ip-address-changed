from local import *
from get_ip import *
from send_email import *

# Global State
sendEmailAddress = False

# Get old and new ip 
oldIpAddress = get_saved_ip()
newIpAddressList = get_ip()

# Compare 
for i in range(0, len(newIpAddressList)):
    if oldIpAddress != newIpAddressList[i][0]:
        sendEmailAddress = True

# Send email
if sendEmailAddress == True:
    print("The ip address was changed.")
    text = """\
    Hi,
    How are you?

    Your IP Address was changed.
    Old ip address: """ + str(oldIpAddress) + """
    The new IP address is: 
    """ + str(newIpAddressList) + """
    
    Have a nice day! :)"""
    htmlTableIPList = "<table>"
    htmlTableIPList += "<tr><td>IP Address</td><td>Returned By</td></tr>"
    for i in range(0, len(newIpAddressList)):
        save_ip(newIpAddressList[i][0])
        htmlTableIPList += "<tr><td>" +newIpAddressList[i][0]+ "</td><td>" +newIpAddressList[i][1]+ "</td></tr>"
    htmlTableIPList += "</table>"
    html = """\
    <html>
    <head>
    <style>
    table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
    }
    </style>
    </head>
    <body>
        <p>Hi,<br>
        How are you?<br>
        <br>
        Your IP Address was changed.<br>
        Old ip address: """ + str(oldIpAddress) + """ <br>
        The new IP address is: <br>
        """ + str(htmlTableIPList) + """
        <br>
        Have a nice day! :)
        </p>
    </body>
    </html>
    """
    send_email(text, html)
else:
    print("The ip address is the same.")
