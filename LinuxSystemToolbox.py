"""
*********************************************************************************
|                                                                               |
|                             Linux System Toolbox                              |
|                 -------------------------------------------                   |   
|                         Written by: Lothar TheQuiet                           |
|                          lotharthequiet@gmail.com                             |
|                   Graphing Logic Assitance: Tai Gong Quan                     |
|                      Hounding about caMELCase: Rilvyk                         |
|                                                                               |
*********************************************************************************

Logging Levels:
------------------------------------------------------------
DEBUG: Detailed info
INFO: Confirmation of things working correctly
WARNING: (Default level) Indication things are not so good
ERROR: More serious prob preventing app from running
CRITICAL: Serious error
"""

#load necessary modules
from ctypes import alignment
from tkinter import ttk
from tkinter import *
from matplotlib.pyplot import fill
from pyparsing import col

import sys
import tkinter as tk                    
import os
import subprocess
import logging
from rx import catch

from sympy import expand

"""Define System Variables"""
LSTVER = "0.1a"                                                                         #Sytem Version number
LSTNAME = "Linux System Toolbox"                                                        #Application Name
LSTAUTHOR = "Lothar TheQuiet"                                                           #Application Author
LSTCONTACT = "lotharthequiet@gmail.com"                                                 #Application Author Contact
LSTGITHUBREPO = "https://github.com/lotharthequiet/LinuxSystemToolbox"                  #GitHub Repository
LSTGITHUB = "https://github.com/lotharthequiet/LinuxSystemToolbox.git"                  #GitHub Direct Link
DEFPADX = 10                                                                            #Static X Padding Value
DEFPADY = 5                                                                             #Static Y Padding Value
NARROWPAD = 5                                                                           #Static Narrow Pad Value
BTNSIZE = 12                                                                            #Static button size value
STATICSTICKY = W                                                                        #Static sticky direction
STATICFULLFRMSTICKY = NSEW                                                              #Static full sticky for label frames
LSTLOGGER = logging.getLogger(__name__) 
LSTLOGGER.setLevel(logging.DEBUG)
LSTLOGGERFMT = logging.Formatter('%(created)f:%(levelname)s:%(message)s')
LSTLOGHANDLER = logging.FileHandler('LinuxSystemToolbox.log')
LSTLOGHANDLER.setFormatter(LSTLOGGERFMT)
LSTLOGGER.addHandler(LSTLOGHANDLER)
LSTLOGGERSTRM = logging.StreamHandler()
LSTLOGGERSTRM.setFormatter(LSTLOGGERFMT)
LSTLOGGER.addHandler(LSTLOGGERSTRM)

""" Define routines/gather info """
def toggleinterface():
    LSTLOGGER.debug("Toggle Interface")

def dhcprelease():
    LSTLOGGER.debug("DHCP Release")

def dhcprenew():
    LSTLOGGER.debug("DHCP Renew")

def opennettoolbox():
    LSTLOGGER.debug("Open Toolbox")

def switchuser():
    LSTLOGGER.debug("Switch User")

def logout():
    LSTLOGGER.debug("Logout")

def restart():
    LSTLOGGER.debug("Restart")

def shutdown():
    LSTLOGGER.debug("Shutdown")

def openhelp():
    LSTLOGGER.debug("Open Help.")

def openabout():
    LSTLOGGER.debug("Open About Tab.")
    aboutwindow = Toplevel(root)
    aboutwindow.title(LSTNAME)
    aboutwinttlfrm = tk.LabelFrame(aboutwindow, text = LSTNAME)
    aboutwinttlfrm.grid(column = 0, row = 0, padx = DEFPADX, pady = DEFPADY, sticky=STATICFULLFRMSTICKY, columnspan=3)
    aboutauthorlbl = ttk.Label(aboutwindow, text ="Written By:")
    aboutauthorlbl.grid(column = 0, row = 1, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
    aboutauthor = ttk.Label(aboutwindow, text = LSTAUTHOR)
    aboutauthor.grid(column = 1, row = 1, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
    aboutcontactlbl = ttk.Label(aboutwindow, text ="Contact:")
    aboutcontactlbl.grid(column = 0, row = 2, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
    aboutcontact = ttk.Label(aboutwindow, text = LSTCONTACT)
    aboutcontact.grid(column = 1, row = 2, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
    aboutgithubrepolbl = ttk.Label(aboutwindow, text ="GitHub Repository:")
    aboutgithubrepolbl.grid(column = 0, row = 3, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
    aboutgithubrepo = ttk.Label(aboutwindow, text = LSTGITHUBREPO)
    aboutgithubrepo.grid(column = 1, row = 3, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
    aboutgitlbl = ttk.Label(aboutwindow, text ="Git Link:")
    aboutgitlbl.grid(column = 0, row = 4, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
    aboutgithubgit = ttk.Label(aboutwindow, text = LSTGITHUB)
    aboutgithubgit.grid(column = 1, row = 4, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
    aboutverlbl = ttk.Label(aboutwindow, text = "Version:")
    aboutverlbl.grid(column = 0, row = 5, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
    aboutver = ttk.Label(aboutwindow, text = LSTVER)
    aboutver.grid(column = 1, row = 5, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)

def runreports():
    LSTLOGGER.debug("Run reports.")

def selectinterface():
    LSTLOGGER.debug("Select Interface Function.")
    LSTLOGGER.debug(intcombo.get())
    #Get selected interface name
    intname = intcombo.get()
    #Get interface status
    intstatus = subprocess.Popen("ifconfig " + intname + " | head -n 1 | awk {'print$2'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    LSTLOGGER.debug(intstatus)
    intstatusStr = "UP"
    connectedStatusStr = "RUNNING"
    if intstatusStr in intstatus:                       #iterate through raw int status and find UP L1 status
        if connectedStatusStr in intstatus:             #iterate through raw int status and find RUNNING L2 status
            intstatusResult = True
    else:
            intstatusResult = False
    #Set button label
    if intstatusResult:
        disableintbtn.config(text="Disable")      #Change the button text to disable if interface is enabled
    else:
        disableintbtn.config(text="Enable")       #Change the button text to enable if interface is disabled
    #Get add info
    intmacaddress = subprocess.Popen("ifconfig " + intname + " | grep ether | awk '{print$2}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    intmtu = subprocess.Popen("ifconfig " + intname + " | head -n +1 | awk '{print$4}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    intipaddress = subprocess.Popen("ifconfig " + intname + " | grep inet | head -n +1 | awk '{print$2}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    intsubnetmask = subprocess.Popen("ifconfig " + intname + " | grep inet | head -n +1 | awk '{print$4}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    intdefaultgw = subprocess.Popen("netstat -r | tail -n +3 | awk '{print$2}' | head -n +1", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    intbroadcastaddress = subprocess.Popen("ifconfig " + intname + " | grep inet | head -n +1 | awk '{print$6}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    dnsserveraddresses = subprocess.Popen("cat /etc/resolv.conf | tail -n +3 | awk '{print$2}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    dnsserveraddresses = dnsserveraddresses.split()
    inthostname = subprocess.Popen("hostname", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    intdnsdomainname = subprocess.Popen("cat /etc/resolv.conf | tail -n +2 | awk '{print$2}' | head -n +1", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    #Get int stats
    rxpacketcount = subprocess.Popen("ifconfig " + intname + " | grep 'RX packets' | awk {'print$3'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    rxpacketbytecount = subprocess.Popen("ifconfig " + intname + " | grep 'RX packets' | awk {'print$5'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    rxpackethumansize = subprocess.Popen("ifconfig " + intname + " | grep 'RX packets' | awk {'print$6'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    rxerrorcount = subprocess.Popen("ifconfig " + intname + " | grep 'RX Errors' | awk {'print$3'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    rxdroppedcount = subprocess.Popen("ifconfig " + intname + " | grep 'RX Errors' | awk {'print$5'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    rxoverrunscount = subprocess.Popen("ifconfig " + intname + " | grep 'RX Errors' | awk {'print$7'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    rxframecount = subprocess.Popen("ifconfig " + intname + " | grep 'RX Errors' | awk {'print$9'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    txpacketcount = subprocess.Popen("ifconfig " + intname + " | grep 'TX packets' | awk {'print$3'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    txpacketbytecount = subprocess.Popen("ifconfig " + intname + " | grep 'TX packets' | awk {'print$5'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    txpackethumansize = subprocess.Popen("ifconfig " + intname + " | grep 'TX packets' | awk {'print$6'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    txerrorcount = subprocess.Popen("ifconfig " + intname + " | grep 'TX errors' | awk {'print$3'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    txdroppedcount = subprocess.Popen("ifconfig " + intname + " | grep 'TX errors' | awk {'print$5'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    txoverrunscount = subprocess.Popen("ifconfig " + intname + " | grep 'TX errors' | awk {'print$7'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    txcarrier = subprocess.Popen("ifconfig " + intname + " | grep 'TX errors' | awk {'print$9'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    txcollisions = subprocess.Popen("ifconfig " + intname + " | grep 'TX errors' | awk {'print$11'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    LSTLOGGER.debug(intname)
    LSTLOGGER.debug(intstatus)
    LSTLOGGER.debug(intmacaddress)
    LSTLOGGER.debug(intmtu)
    LSTLOGGER.debug(intipaddress)
    LSTLOGGER.debug(intsubnetmask)
    LSTLOGGER.debug(intdefaultgw)
    LSTLOGGER.debug(intbroadcastaddress)
    for server in dnsserveraddresses:
        LSTLOGGER.debug(server)
    LSTLOGGER.debug(inthostname)
    LSTLOGGER.debug(intdnsdomainname)
    LSTLOGGER.debug(rxpacketcount)
    LSTLOGGER.debug(rxpacketbytecount)
    LSTLOGGER.debug(rxpackethumansize)
    LSTLOGGER.debug(rxerrorcount)
    LSTLOGGER.debug(rxdroppedcount)
    LSTLOGGER.debug(rxoverrunscount)
    LSTLOGGER.debug(rxframecount)
    LSTLOGGER.debug(txpacketcount)
    LSTLOGGER.debug(txpacketbytecount)
    LSTLOGGER.debug(txpackethumansize)
    LSTLOGGER.debug(txerrorcount)
    LSTLOGGER.debug(txdroppedcount)
    LSTLOGGER.debug(txoverrunscount)
    LSTLOGGER.debug(txcarrier)
    LSTLOGGER.debug(txcollisions)

def getroutetable():
    LSTLOGGER.debug("Get route table.")
    try:
        introutetable = subprocess.Popen("netstat -r | tail -n +3", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    except:
        LSTLOGGER.error("Unable to retrieve route table.")
    introutetable = introutetable.split()
    count = 0
    rowcount = 1
    for x in introutetable:
        if count == 8:
            count = 0
            rowcount = rowcount + 1
            routetablecontentry = tk.Label(routetblfrm, text = x).grid(column = count, row = rowcount, padx = NARROWPAD, pady = NARROWPAD, sticky = STATICSTICKY)
            count = count + 1
        elif count < 8:
            routetablecontentry = tk.Label(routetblfrm, text = x).grid(column = count, row = rowcount, padx = NARROWPAD, pady = NARROWPAD, sticky = STATICSTICKY)
            count = count + 1

def exitapp():
    LSTLOGGER.debug("Exiting LST.")
    root.quit()


"""Get lst Info"""
#Get NIC list
intlist = subprocess.Popen("ifconfig -s | tail -n +2 | awk '{print$1}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
intlist = intlist.split()

""" This section of code left remarked intentionally
#Get Default Gateway
#defGateway = subprocess.Popen("netstat -r | tail -n +3 | awk '{print$2}' | head -n +1", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]

#Get DNS Server Addresses
#dnsServerAddresses = subprocess.Popen("cat /etc/resolv.conf | tail -n +3 | awk '{print$2}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
#dnsServerAddresses = dnsServerAddresses.split()

#Get DNS Hostname
#dnsHostname = subprocess.Popen("hostname", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]

#Get DNS Domain
#dnsDomain = subprocess.Popen("cat /etc/resolv.conf | tail -n +2 | awk '{print$2}' | head -n +1", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
"""

"""Setup Main Window"""
root = tk.Tk()
root.title(LSTNAME)                                                     #Define App title
root.geometry("590x675")                                                #Define default app size
lst = ttk.Notebook(root)                                                #Nest the lst Notebook into the root tkWindow

"""Setup File Menu"""
menubar = Menu(lst)
filemenu = Menu(menubar, tearoff=0)                                     #Setup File submenu
filemenu.add_command(label="Reports", command=runreports)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exitapp)
menubar.add_cascade(label="File", menu=filemenu)
toolsmenu = Menu(menubar, tearoff=0)                                    #Setup Tools submenu
toolsmenu.add_command(label="Open Toolbox", command=opennettoolbox)
toolsmenu.add_separator()
toolsmenu.add_command(label="Switch User", command=switchuser)
toolsmenu.add_command(label="Logout", command=logout)
toolsmenu.add_command(label="Restart", command=restart)
toolsmenu.add_command(label="Shutdown", command=shutdown)
menubar.add_cascade(label="Tools", menu=toolsmenu)
helpmenu = Menu(menubar, tearoff=0)                                     #Setup Help submenu
helpmenu.add_command(label="Help", command=openhelp)
helpmenu.add_separator()
helpmenu.add_command(label="About", command=openabout)
menubar.add_cascade(label="Help", menu=helpmenu)

"""Define tabs in the root window (root)"""
proctab = ttk.Frame(lst)
servicestab = ttk.Frame(lst)
userstab = ttk.Frame(lst)
nettab = ttk.Frame(lst)
perftab = ttk.Frame(lst)
wirelesstab = ttk.Frame(lst)

"""Define tab names"""
lst.add(proctab, text ='Processes')
lst.add(servicestab, text ='Services')
lst.add(userstab, text ='Users')
lst.add(nettab, text ='Networking')
lst.add(perftab, text ='Performance')
lst.add(wirelesstab, text = 'Wireless')
lst.pack(expand = 1, fill ="both")
#lst.grid(column = 0, row = 0)

"""Tab Layout"""
"""procTab Layout"""
proctabttlfrm = tk.LabelFrame(proctab, text="Running Processes:")
proctabttlfrm.grid(column = 0, row = 0, padx = DEFPADX, pady = (10, 5), sticky=STATICFULLFRMSTICKY, columnspan=2)
proctabttllbl = tk.Label(proctabttlfrm, text="Test Label")
proctabttllbl.grid(column = 0, row = 0, padx = DEFPADX, pady = (10, 5), sticky=STATICSTICKY)
proctabbtnfrm = tk.Frame(proctab)
proctabbtnfrm.grid(column = 2, row = 0, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
killprocbtn = tk.Button(proctabbtnfrm, text="Kill Process")
killprocbtn.grid(column = 0, row = 0, padx = DEFPADX, pady = DEFPADY, sticky=N)
spawnprocbtn = tk.Button(proctabbtnfrm, text="Spawn Process")
spawnprocbtn.grid(column = 0, row = 1, padx = DEFPADX, pady = DEFPADY, sticky=N)

"""servicesTab Layout"""
svcstabttlfrm = tk.LabelFrame(servicestab, text="System Services:")
svcstabttlfrm.grid(column = 0, row = 0, padx = DEFPADX, pady = (10, 5), sticky=STATICFULLFRMSTICKY, columnspan=2)
svcstabttllbl = tk.Label(svcstabttlfrm, text="Test Label")
svcstabttllbl.grid(column = 0, row = 0, padx = DEFPADX, pady = (10, 5), sticky=STATICSTICKY)
svcstabbtnfrm = tk.Frame(servicestab)
svcstabbtnfrm.grid(column = 2, row = 0, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
enablesvcbtn = tk.Button(svcstabbtnfrm, text="Enable Service")
enablesvcbtn.grid(column = 0, row = 0, padx = DEFPADX, pady = DEFPADY, sticky=N)
disablesvcbtn = tk.Button(svcstabbtnfrm, text="Disable Service")
disablesvcbtn.grid(column = 0, row = 1, padx = DEFPADX, pady = DEFPADY, sticky=N)
startsvcbtn = tk.Button(svcstabbtnfrm, text="Start Service")
startsvcbtn.grid(column = 0, row = 2, padx = DEFPADX, pady = DEFPADY, sticky=N)
stopsvcbtn = tk.Button(svcstabbtnfrm, text="Stop Service")
stopsvcbtn.grid(column = 0, row = 3, padx = DEFPADX, pady = DEFPADY, sticky=N)

"""userTab Layout"""
usrtabttlfrm = tk.LabelFrame(userstab, text="Logged In Users:")
usrtabttlfrm.grid(column = 0, row = 0, padx = DEFPADX, pady = (10, 5), sticky=STATICFULLFRMSTICKY, columnspan=2)
usrtabttllbl = tk.Label(usrtabttlfrm, text="Test Label")
usrtabttllbl.grid(column = 0, row = 0, padx = DEFPADX, pady = (10, 5), sticky=STATICSTICKY)
usrtabttlfrm = tk.LabelFrame(userstab, text="Local Users:")
usrtabttlfrm.grid(column = 0, row = 1, padx = DEFPADX, pady = (10, 5), sticky=STATICFULLFRMSTICKY, columnspan=2)
usrtabttllbl = tk.Label(usrtabttlfrm, text="Test Label")
usrtabttllbl.grid(column = 0, row = 0, padx = DEFPADX, pady = (10, 5), sticky=STATICSTICKY)
usrtabbtnfrm = tk.Frame(userstab)
usrtabbtnfrm.grid(column = 2, row = 0, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
newuserbtn = tk.Button(usrtabbtnfrm, text="New User")
newuserbtn.grid(column = 0, row = 0, padx = DEFPADX, pady = DEFPADY, sticky=N)

"""nettab Layout"""
nettabcontfrm = tk.Frame(nettab)
nettabcontfrm.grid(column = 0, row = 0, padx = DEFPADX, pady = (10, 5), sticky=STATICSTICKY)
nettabbtnfrm = tk.Frame(nettab)
nettabbtnfrm.grid(column = 1, row = 0, padx = 0, pady = (10, 5), sticky='N')
intstatsfrm = tk.LabelFrame(nettab, text="Interface Statistics:")
intstatsfrm.grid(column = 0, row = 1, padx = DEFPADX, pady = DEFPADY, sticky = STATICFULLFRMSTICKY, columnspan = 2)
routetblfrm = tk.LabelFrame(nettab, text="Routing Table:")
routetblfrm.grid(column = 0, row = 2, padx = DEFPADX, pady = DEFPADY, sticky = STATICFULLFRMSTICKY, columnspan = 2)
disableintbtn = ttk.Button(nettabbtnfrm, text ="Disable", width = BTNSIZE, command=toggleinterface)
disableintbtn.grid(column = 0, row = 0, padx = DEFPADX, pady = DEFPADY, sticky='N')
dhcpreleasebtn = ttk.Button(nettabbtnfrm, text ="DHCP Release", width = BTNSIZE, command=dhcprelease)
dhcpreleasebtn.grid(column = 0, row = 1, padx = DEFPADX, pady = DEFPADY, sticky='N')
dhcprenewbtn = ttk.Button(nettabbtnfrm, text ="DHCP Renew", width = BTNSIZE, command=dhcprenew)
dhcprenewbtn.grid(column = 0, row = 2, padx = DEFPADX, pady = DEFPADY, sticky='N')
nettoolboxbtn = ttk.Button(nettabbtnfrm, text ="Toolbox", width= BTNSIZE, command=opennettoolbox)
nettoolboxbtn.grid(column = 0, row = 3, padx = DEFPADX, pady = DEFPADY, sticky='N')

#Interface Info
selintname = tk.StringVar()
intlbl = ttk.Label(nettabcontfrm, text ="Select Interface:")
intlbl.grid(column = 0, row = 0, padx = DEFPADX, pady = (10, 5), sticky=STATICSTICKY)
intcombo = ttk.Combobox(nettabcontfrm, values = intlist)
intcombo.grid(column = 1, row = 0, padx = DEFPADX, pady = (10, 5), sticky=STATICSTICKY)
intcombo.set("Select Interface:")
intcombo.bind('<<ComboboxSelected>>', lambda event: selectinterface())
macaddrlbl = ttk.Label(nettabcontfrm, text="Mac Address:")
macaddrlbl.grid(column = 0, row = 1, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
macaddr = ttk.Label(nettabcontfrm, text="")
macaddr.grid(column = 1, row = 1, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
mtulbl = ttk.Label(nettabcontfrm, text ="MTU:")
mtulbl.grid(column = 0, row = 2, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
mtu = ttk.Label(nettabcontfrm, text = "")
mtu.grid(column = 1, row = 2, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
ipaddrlbl = ttk.Label(nettabcontfrm, text="IP Address:")
ipaddrlbl.grid(column = 0, row = 3, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
ipaddr = ttk.Label(nettabcontfrm, text="")
ipaddr.grid(column = 1, row = 3, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
submasklbl = ttk.Label(nettabcontfrm, text="Subnet Mask:")
submasklbl.grid(column = 0, row = 4, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
submask = ttk.Label(nettabcontfrm, text="")
submask.grid(column = 1, row = 4, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
defgwlbl = ttk.Label(nettabcontfrm, text="Default Gateway:")
defgwlbl.grid(column = 0, row = 5, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
defgw = ttk.Label(nettabcontfrm, text="")
defgw.grid(column = 1, row = 5, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
bcastaddrlbl = ttk.Label(nettabcontfrm, text="Broadcast Address:")
bcastaddrlbl.grid(column = 0, row = 6, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
bcastaddr = ttk.Label(nettabcontfrm, text="")
bcastaddr.grid(column = 1, row = 6, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
dnsserverslbl = ttk.Label(nettabcontfrm, text="DNS Servers:")
dnsserverslbl.grid(column = 0, row = 7, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
#rowcount = 7
# for x in dnsServerAddresses:
#     if rowcount < 9:
#         netTabDNSServer = ttk.Label(nettabcontfrm, text=x).grid(column = 1, row = rowcount, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
#         rowcount = rowcount + 1
dnshostnamelbl = ttk.Label(nettabcontfrm, text="DNS Hostname:")
dnshostnamelbl.grid(column = 0, row = 9, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
dnshostname = ttk.Label(nettabcontfrm, text="")
dnshostname.grid(column = 1, row = 9, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
dnsdomainlbl = ttk.Label(nettabcontfrm, text="DNS Domain:")
dnsdomainlbl.grid(column = 0, row = 10, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
dnsdomain = ttk.Label(nettabcontfrm, text="")
dnsdomain.grid(column = 1, row = 10, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)

#Interface Stats
rxpacketlbl = tk.Label(intstatsfrm, text="RX packets")
rxpacketlbl.grid(column = 0, row = 0, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
rxpacketcntlbl = tk.Label(intstatsfrm, text="")
rxpacketcntlbl.grid(column = 1, row = 0, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
rxpacketbyteslbl = tk.Label(intstatsfrm, text="bytes")
rxpacketbyteslbl.grid(column = 2, row = 0, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
rxpacketbytescntlbl = tk.Label(intstatsfrm, text="")
rxpacketbytescntlbl.grid(column = 3, row = 0, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
rxpacketbyteshumancntlbl = tk.Label(intstatsfrm, text="")
rxpacketbyteshumancntlbl.grid(column = 3, row = 0, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
rxerrorslbl = tk.Label(intstatsfrm, text="RX errors")
rxerrorslbl.grid(column = 0, row = 1, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
rxerrorscntlbl = tk.Label(intstatsfrm, text="")
rxerrorscntlbl.grid(column = 1, row = 1, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
rxdroppedlbl = tk.Label(intstatsfrm, text="dropped")
rxdroppedlbl.grid(column = 2, row = 1, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
rxdroppedcntlbl = tk.Label(intstatsfrm, text="")
rxdroppedcntlbl.grid(column = 3, row = 1, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
rxoverrunslbl = tk.Label(intstatsfrm, text="overruns")
rxoverrunslbl.grid(column = 4, row = 1, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
rxoverrunscntlbl = tk.Label(intstatsfrm, text="")
rxoverrunscntlbl.grid(column = 5, row = 1, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
rxframelbl = tk.Label(intstatsfrm, text="frame")
rxframelbl.grid(column = 6, row = 1, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
rxframecntlbl = tk.Label(intstatsfrm, text="")
rxframecntlbl.grid(column = 7, row = 1, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
txpacketlbl = tk.Label(intstatsfrm, text="TX packets")
txpacketlbl.grid(column = 0, row = 2, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
txpacketcntlbl = tk.Label(intstatsfrm, text="")
txpacketcntlbl.grid(column = 1, row = 2, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
txpacketbyteslbl = tk.Label(intstatsfrm, text="bytes")
txpacketbyteslbl.grid(column = 2, row = 2, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
txpacketbytescntlbl = tk.Label(intstatsfrm, text="")
txpacketbytescntlbl.grid(column = 3, row = 2, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
txpacketbyteshumcntlbl = tk.Label(intstatsfrm, text="")
txpacketbyteshumcntlbl.grid(column = 3, row = 2, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
txerrorslbl = tk.Label(intstatsfrm, text="TX errors")
txerrorslbl.grid(column = 0, row = 3, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
txerrorscntlbl = tk.Label(intstatsfrm, text="")
txerrorscntlbl.grid(column = 1, row = 3, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
txdroppedlbl = tk.Label(intstatsfrm, text="dropped")
txdroppedlbl.grid(column = 2, row = 3, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
txdroppedcntlbl = tk.Label(intstatsfrm, text="")
txdroppedcntlbl.grid(column = 3, row = 3, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
txoverrunslbl = tk.Label(intstatsfrm, text="overruns")
txoverrunslbl.grid(column = 4, row = 3, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
txoverrunscntlbl = tk.Label(intstatsfrm, text="")
txoverrunscntlbl.grid(column = 5, row = 3, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
txfrmlbl = tk.Label(intstatsfrm, text="carrier")
txfrmlbl.grid(column = 6, row = 3, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
txfrmcntlbl = tk.Label(intstatsfrm, text="")
txfrmcntlbl.grid(column = 7, row = 3, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
txcolslbl = tk.Label(intstatsfrm, text="collisions")
txcolslbl.grid(column = 8, row = 3, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
txcolscntlbl = tk.Label(intstatsfrm, text="")
txcolscntlbl.grid(column = 9, row = 3, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)

#Routing Table
routetablecontlbl = tk.Label(routetblfrm, text = "Destination")
routetablecontlbl.grid(column = 0, row = 0, padx = NARROWPAD, pady = NARROWPAD, sticky = STATICSTICKY)
routetablecontlbl2 = tk.Label(routetblfrm, text = "Gateway")
routetablecontlbl2.grid(column = 1, row = 0, padx = NARROWPAD, pady = NARROWPAD, sticky = STATICSTICKY)
routetablecontlbl3 = tk.Label(routetblfrm, text = "Genmask")
routetablecontlbl3.grid(column = 2, row = 0, padx = NARROWPAD, pady = NARROWPAD, sticky = STATICSTICKY)
routetablecontlbl4 = tk.Label(routetblfrm, text = "Flags")
routetablecontlbl4.grid(column = 3, row = 0, padx = NARROWPAD, pady = NARROWPAD, sticky = STATICSTICKY)
routetablecontlbl5 = tk.Label(routetblfrm, text = "MSS")
routetablecontlbl5.grid(column = 4, row = 0, padx = NARROWPAD, pady = NARROWPAD, sticky = STATICSTICKY)
routetablecontlbl6 = tk.Label(routetblfrm, text = "Window")
routetablecontlbl6.grid(column = 5, row = 0, padx = NARROWPAD, pady = NARROWPAD, sticky = STATICSTICKY)
routetablecontlbl7 = tk.Label(routetblfrm, text = "irtt")
routetablecontlbl7.grid(column = 6, row = 0, padx = NARROWPAD, pady = NARROWPAD, sticky = STATICSTICKY)
routetablecontlbl8 = tk.Label(routetblfrm, text = "Iface")
routetablecontlbl8.grid(column = 7, row = 0, padx = NARROWPAD, pady = NARROWPAD, sticky = STATICSTICKY)

"""Run System"""
root.config(menu=menubar)
root.mainloop()
