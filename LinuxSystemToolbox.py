"""
*********************************************************************************
|                                                                               |
|                             Linux System Toolbox                              |
|                 -------------------------------------------                   |   
|                         Written by: Lothar TheQuiet                           |
|                          lotharthequiet@gmail.com                             |
|                   Graphing Logic Assitance: Tai Gong Quan                     |
|                                                                               |
*********************************************************************************

"""

#load necessary modules
from ctypes import alignment
import sys
import tkinter as tk                    
from tkinter import ttk
import os
from tkinter import *
import webbrowser
import subprocess
from pyparsing import col

"""Define System Variables"""
lstver = "0.1a"                                                                  #Sytem Version number
lstname = "Linux System Toolbox"                                                 #Application Name
lstauthor = "Lothar TheQuiet"                                                    #Application Author
lstcontact = "lotharthequiet@gmail.com"                                          #Application Author Contact
lstgithubrepo = "https://github.com/lotharthequiet/LinuxSystemToolbox"           #GitHub Repository
lstgithubgit = "https://github.com/lotharthequiet/LinuxSystemToolbox.git"        #GitHub Direct Link
staticpadx = 10                                                                     #Static X Padding Value
staticpady = 5                                                                      #Static Y Padding Value
staticnarrowpad = 5                                                                 #Static Narrow Pad Value
staticbuttonsize = 12                                                               #Static button size value
staticsticky = W                                                                    #Static sticky direction
staticfullframesticky = NSEW                                                        #Static full sticky for label frames

"""  ***** Define routines/gather info *****  """
def toggleinterface():
    print("Toggle Interface")

def dhcprelease():
    print("DHCP Release")

def dhcprenew():
    print("DHCP Renew")

def opennettoolbox():
    print("Open Toolbox")

def switchuser():
    print("Switch User")

def logout():
    print("Logout")

def restart():
    print("Restart")

def shutdown():
    print("Shutdown")

def openmanpage():
    print("Open Man Pages.")

def openabout():
    print("Open About Tab.")

def runreports():
    print("Run reports.")

def selectinterface():
    print("Select Interface Function.")
    print(nettabintcombo.get())
    #Get selected interface name
    intname = nettabintcombo.get()
    #Get interface status
    intstatus = subprocess.Popen("ifconfig " + intname + " | head -n 1 | awk {'print$2'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    print(intstatus)
    intstatusStr = "UP"
    connectedStatusStr = "RUNNING"
    if intstatusStr in intstatus:                       #iterate through raw int status and find UP L1 status
        if connectedStatusStr in intstatus:             #iterate through raw int status and find RUNNING L2 status
            intstatusResult = True
    else:
            intstatusResult = False
    #Set button label
    if intstatusResult:
        nettabdisableintbtn.config(text="Disable")      #Change the button text to disable if interface is enabled
    else:
        nettabdisableintbtn.config(text="Enable")       #Change the button text to enable if interface is disabled
    #Get mac address
    intmacaddress = subprocess.Popen("ifconfig " + intname + " | grep ether | awk '{print$2}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    #Get MTU
    intmtu = subprocess.Popen("ifconfig " + intname + " | head -n +1 | awk '{print$4}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    #Get IP address
    intipaddress = subprocess.Popen("ifconfig " + intname + " | grep inet | head -n +1 | awk '{print$2}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    #Get subnet mask
    intsubnetmask = subprocess.Popen("ifconfig " + intname + " | grep inet | head -n +1 | awk '{print$4}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    #Get def gw
    intdefaultgw = subprocess.Popen("netstat -r | tail -n +3 | awk '{print$2}' | head -n +1", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    #Get broadcast address
    intbroadcastaddress = subprocess.Popen("ifconfig " + intname + " | grep inet | head -n +1 | awk '{print$6}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    #Get DNS server addresses (qty 2)
    dnsserveraddresses = subprocess.Popen("cat /etc/resolv.conf | tail -n +3 | awk '{print$2}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    dnsserveraddresses = dnsserveraddresses.split()
    #Get DNS hostname
    inthostname = subprocess.Popen("hostname", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    #Get DNS domain name
    intdnsdomainname = subprocess.Popen("cat /etc/resolv.conf | tail -n +2 | awk '{print$2}' | head -n +1", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    #Get interface stats
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
    print(intname)
    print(intstatus)
    print(intmacaddress)
    print(intmtu)
    print(intipaddress)
    print(intsubnetmask)
    print(intdefaultgw)
    print(intbroadcastaddress)
    for server in dnsserveraddresses:
        print(server)
    print(inthostname)
    print(intdnsdomainname)
    print(rxpacketcount)
    print(rxpacketbytecount)
    print(rxpackethumansize)
    print(rxerrorcount)
    print(rxdroppedcount)
    print(rxoverrunscount)
    print(rxframecount)
    print(txpacketcount)
    print(txpacketbytecount)
    print(txpackethumansize)
    print(txerrorcount)
    print(txdroppedcount)
    print(txoverrunscount)
    print(txcarrier)
    print(txcollisions)


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

#Get Route Table
introutetable = subprocess.Popen("netstat -r | tail -n +3", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
introutetable = introutetable.split()

"""Setup Main Window"""
root = tk.Tk()
root.title(lstname)                                                     #Define App title
root.geometry("590x675")                                                #Define default app size
lst = ttk.Notebook(root)                                                #Nest the lst Notebook into the root tkWindow

"""Setup File Menu"""
menubar = Menu(lst)
filemenu = Menu(menubar, tearoff=0)                                     #Setup File submenu
filemenu.add_command(label="Reports", command=runreports)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
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
helpmenu.add_command(label="Help", command=openmanpage)
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
abouttab = ttk.Frame(lst)

"""Define tab names"""
lst.add(proctab, text ='Processes')
lst.add(servicestab, text ='Services')
lst.add(userstab, text ='Users')
lst.add(nettab, text ='Networking')
lst.add(perftab, text ='Performance')
lst.add(wirelesstab, text = 'Wireless')
lst.add(abouttab, text ='About')
lst.pack(expand = 1, fill ="both")

"""Tab Layout"""
"""procTab Layout"""
proctabttlfrm = tk.LabelFrame(proctab, text="Running Processes:").grid(column = 0, row = 0, padx = staticpadx, pady = (10, 5), sticky=staticfullframesticky, columnspan=2)
proctabttllbl = tk.Label(proctabttlfrm, text="Test Label").grid(column = 0, row = 0, padx = staticpadx, pady = (10, 5), sticky=staticsticky)
proctabbtnfrm = tk.Frame(proctab).grid(column = 2, row = 0, padx = staticpadx, pady = staticpady, sticky=staticsticky)
killprocBtn = tk.Button(proctabbtnfrm, text="Kill Process").grid(column = 0, row = 0, padx = staticpadx, pady = staticpady, sticky=N)
spawnprocBtn = tk.Button(proctabbtnfrm, text="Spawn Process").grid(column = 0, row = 1, padx = staticpadx, pady = staticpady, sticky=N)


"""servicesTab Layout"""
svcstabttlfrm = tk.LabelFrame(servicestab, text="System Services:").grid(column = 0, row = 0, padx = staticpadx, pady = (10, 5), sticky=staticfullframesticky, columnspan=2)
svcstabttllbl = tk.Label(svcstabttlfrm, text="Test Label").grid(column = 0, row = 0, padx = staticpadx, pady = (10, 5), sticky=staticsticky)
svcstabbtnfrm = tk.Frame(servicestab).grid(column = 2, row = 0, padx = staticpadx, pady = staticpady, sticky=staticsticky)
enablesvcbtn = tk.Button(svcstabbtnfrm, text="Enable Service").grid(column = 0, row = 0, padx = staticpadx, pady = staticpady, sticky=N)
disablesvcbtn = tk.Button(svcstabbtnfrm, text="Disable Service").grid(column = 0, row = 1, padx = staticpadx, pady = staticpady, sticky=N)
startsvcbtn = tk.Button(svcstabbtnfrm, text="Start Service").grid(column = 0, row = 2, padx = staticpadx, pady = staticpady, sticky=N)
stopsvcbtn = tk.Button(svcstabbtnfrm, text="Stop Service").grid(column = 0, row = 3, padx = staticpadx, pady = staticpady, sticky=N)

"""userTab Layout"""
usrtabttlfrm = tk.LabelFrame(userstab, text="Logged In Users:").grid(column = 0, row = 0, padx = staticpadx, pady = (10, 5), sticky=staticfullframesticky, columnspan=2)
usrtabttllbl = tk.Label(usrtabttlfrm, text="Test Label").grid(column = 0, row = 0, padx = staticpadx, pady = (10, 5), sticky=staticsticky)
usrtabttlfrm = tk.LabelFrame(userstab, text="Local Users:").grid(column = 0, row = 1, padx = staticpadx, pady = (10, 5), sticky=staticfullframesticky, columnspan=2)
usrtabttllbl = tk.Label(usrtabttlfrm, text="Test Label").grid(column = 0, row = 0, padx = staticpadx, pady = (10, 5), sticky=staticsticky)
usrtabbtnfrm = tk.Frame(userstab).grid(column = 2, row = 0, padx = staticpadx, pady = staticpady, sticky=staticsticky)
newuserbtn = tk.Button(usrtabbtnfrm, text="New User").grid(column = 0, row = 0, padx = staticpadx, pady = staticpady, sticky=N)

"""nettab Layout"""
#Setup frames and buttons for nettab
nettabcontfrm = tk.Frame(nettab).grid(column = 0, row = 0, padx = staticpadx, pady = (10, 5), sticky=staticsticky)
nettabbtnfrm = tk.Frame(nettab).grid(column = 1, row = 0, padx = 0, pady = (10, 5), sticky='N')
intstatsfrm = tk.LabelFrame(nettab, text="Interface Statistics:").grid(column = 0, row = 1, padx = staticpadx, pady = staticpady, sticky = staticfullframesticky, columnspan = 2)
routetblfrm = tk.LabelFrame(nettab, text="Routing Table:").grid(column = 0, row = 2, padx = staticpadx, pady = staticpady, sticky = staticfullframesticky, columnspan = 2)
disableintbtn = ttk.Button(nettabbtnfrm, text ="Disable", width = staticbuttonsize, command=toggleinterface).grid(column = 0, row = 0, padx = staticpadx, pady = staticpady, sticky='N')
dhcpreleasebtn = ttk.Button(nettabbtnfrm, text ="DHCP Release", width = staticbuttonsize, command=dhcprelease).grid(column = 0, row = 1, padx = staticpadx, pady = staticpady, sticky='N')
dhcprenewbtn = ttk.Button(nettabbtnfrm, text ="DHCP Renew", width = staticbuttonsize, command=dhcprenew).grid(column = 0, row = 2, padx = staticpadx, pady = staticpady, sticky='N')
nettoolboxbtn = ttk.Button(nettabbtnfrm, text ="Toolbox", width= staticbuttonsize, command=opennettoolbox).grid(column = 0, row = 3, padx = staticpadx, pady = staticpady, sticky='N')

#nettab - Interface Info
selintname = tk.StringVar()
intlbl = ttk.Label(nettabcontfrm, text ="Select Interface:").grid(column = 0, row = 0, padx = staticpadx, pady = (10, 5), sticky=staticsticky)
intcombo = ttk.Combobox(nettabcontfrm, values = intlist).grid(column = 1, row = 0, padx = staticpadx, pady = (10, 5), sticky=staticsticky)
intcombo.set("Select Interface:")
intcombo.bind('<<ComboboxSelected>>', lambda event: selectinterface())
macaddrlbl = ttk.Label(nettabcontfrm, text="Mac Address:").grid(column = 0, row = 1, padx = staticpadx, pady = staticpady, sticky=staticsticky)
macaddr = ttk.Label(nettabcontfrm, text="").grid(column = 1, row = 1, padx = staticpadx, pady = staticpady, sticky=staticsticky)
mtulbl = ttk.Label(nettabcontfrm, text ="MTU:").grid(column = 0, row = 2, padx = staticpadx, pady = staticpady, sticky=staticsticky)
mtu = ttk.Label(nettabcontfrm, text = "").grid(column = 1, row = 2, padx = staticpadx, pady = staticpady, sticky=staticsticky)
ipaddrlbl = ttk.Label(nettabcontfrm, text="IP Address:").grid(column = 0, row = 3, padx = staticpadx, pady = staticpady, sticky=staticsticky)
ipaddr = ttk.Label(nettabcontfrm, text="").grid(column = 1, row = 3, padx = staticpadx, pady = staticpady, sticky=staticsticky)
submasklbl = ttk.Label(nettabcontfrm, text="Subnet Mask:").grid(column = 0, row = 4, padx = staticpadx, pady = staticpady, sticky=staticsticky)
submask = ttk.Label(nettabcontfrm, text="").grid(column = 1, row = 4, padx = staticpadx, pady = staticpady, sticky=staticsticky)
defgwlbl = ttk.Label(nettabcontfrm, text="Default Gateway:").grid(column = 0, row = 5, padx = staticpadx, pady = staticpady, sticky=staticsticky)
defgw = ttk.Label(nettabcontfrm, text="").grid(column = 1, row = 5, padx = staticpadx, pady = staticpady, sticky=staticsticky)
bcastaddrlbl = ttk.Label(nettabcontfrm, text="Broadcast Address:").grid(column = 0, row = 6, padx = staticpadx, pady = staticpady, sticky=staticsticky)
bcastaddr = ttk.Label(nettabcontfrm, text="").grid(column = 1, row = 6, padx = staticpadx, pady = staticpady, sticky=staticsticky)
dnsserverslbl = ttk.Label(nettabcontfrm, text="DNS Servers:").grid(column = 0, row = 7, padx = staticpadx, pady = staticpady, sticky=staticsticky)
#rowcount = 7
# for x in dnsServerAddresses:
#     if rowcount < 9:
#         netTabDNSServer = ttk.Label(nettabcontfrm, text=x).grid(column = 1, row = rowcount, padx = staticpadx, pady = staticpady, sticky=staticsticky)
#         rowcount = rowcount + 1
dnshostnamelbl = ttk.Label(nettabcontfrm, text="DNS Hostname:").grid(column = 0, row = 9, padx = staticpadx, pady = staticpady, sticky=staticsticky)
dnshostname = ttk.Label(nettabcontfrm, text="").grid(column = 1, row = 9, padx = staticpadx, pady = staticpady, sticky=staticsticky)
dnsdomainlbl = ttk.Label(nettabcontfrm, text="DNS Domain:").grid(column = 0, row = 10, padx = staticpadx, pady = staticpady, sticky=staticsticky)
dnsdomain = ttk.Label(nettabcontfrm, text="").grid(column = 1, row = 10, padx = staticpadx, pady = staticpady, sticky=staticsticky)

#netTab - Interface Stats
IntStatsRxPacketLbl = tk.Label(intstatsfrm, text="RX packets").grid(column = 0, row = 0, padx = staticpadx, pady = staticpady, sticky = staticsticky)
IntStatsRxPacketCountLbl = tk.Label(intstatsfrm, text="").grid(column = 1, row = 0, padx = staticpadx, pady = staticpady, sticky = staticsticky)
IntStatsRxPacketBytesLbl = tk.Label(intstatsfrm, text="bytes").grid(column = 2, row = 0, padx = staticpadx, pady = staticpady, sticky = staticsticky)
IntStatsRxPacketBytesCountLbl = tk.Label(intstatsfrm, text="").grid(column = 3, row = 0, padx = staticpadx, pady = staticpady, sticky = staticsticky)
IntStatsRxPacketBytesHumanCountLbl = tk.Label(intstatsfrm, text="").grid(column = 3, row = 0, padx = staticpadx, pady = staticpady, sticky = staticsticky)
IntStatsRxErrorsLbl = tk.Label(intstatsfrm, text="RX errors").grid(column = 0, row = 1, padx = staticpadx, pady = staticpady, sticky = staticsticky)
IntStatsRxErrorsCountLbl = tk.Label(intstatsfrm, text="").grid(column = 1, row = 1, padx = staticpadx, pady = staticpady, sticky = staticsticky)
IntStatsRxDroppedLbl = tk.Label(intstatsfrm, text="dropped").grid(column = 2, row = 1, padx = staticpadx, pady = staticpady, sticky = staticsticky)
IntStatsRxDroppedCountLbl = tk.Label(intstatsfrm, text="").grid(column = 3, row = 1, padx = staticpadx, pady = staticpady, sticky = staticsticky)
IntStatsRxOverrunsLbl = tk.Label(intstatsfrm, text="overruns").grid(column = 4, row = 1, padx = staticpadx, pady = staticpady, sticky = staticsticky)
IntStatsRxOverrunsCountLbl = tk.Label(intstatsfrm, text="").grid(column = 5, row = 1, padx = staticpadx, pady = staticpady, sticky = staticsticky)
IntStatsRxFrameLbl = tk.Label(intstatsfrm, text="frame").grid(column = 6, row = 1, padx = staticpadx, pady = staticpady, sticky = staticsticky)
IntStatsRxFrameCountLbl = tk.Label(intstatsfrm, text="").grid(column = 7, row = 1, padx = staticpadx, pady = staticpady, sticky = staticsticky)
IntStatsTxPacketLbl = tk.Label(intstatsfrm, text="TX packets").grid(column = 0, row = 2, padx = staticpadx, pady = staticpady, sticky = staticsticky)
IntStatsTxPacketCountLbl = tk.Label(intstatsfrm, text="").grid(column = 1, row = 2, padx = staticpadx, pady = staticpady, sticky = staticsticky)
IntStatsTxPacketBytesLbl = tk.Label(intstatsfrm, text="bytes").grid(column = 2, row = 2, padx = staticpadx, pady = staticpady, sticky = staticsticky)
IntStatsTxPacketBytesCountLbl = tk.Label(intstatsfrm, text="").grid(column = 3, row = 2, padx = staticpadx, pady = staticpady, sticky = staticsticky)
IntStatsTxPacketBytesHumanCountLbl = tk.Label(intstatsfrm, text="").grid(column = 3, row = 2, padx = staticpadx, pady = staticpady, sticky = staticsticky)
IntStatsTxErrorsLbl = tk.Label(intstatsfrm, text="RX errors").grid(column = 0, row = 3, padx = staticpadx, pady = staticpady, sticky = staticsticky)
IntStatsTxErrorsCountLbl = tk.Label(intstatsfrm, text="").grid(column = 1, row = 3, padx = staticpadx, pady = staticpady, sticky = staticsticky)
IntStatsTxDroppedLbl = tk.Label(intstatsfrm, text="dropped").grid(column = 2, row = 3, padx = staticpadx, pady = staticpady, sticky = staticsticky)
IntStatsTxDroppedCountLbl = tk.Label(intstatsfrm, text="").grid(column = 3, row = 3, padx = staticpadx, pady = staticpady, sticky = staticsticky)
IntStatsTxOverrunsLbl = tk.Label(intstatsfrm, text="overruns").grid(column = 4, row = 3, padx = staticpadx, pady = staticpady, sticky = staticsticky)
IntStatsTxOverrunsCountLbl = tk.Label(intstatsfrm, text="").grid(column = 5, row = 3, padx = staticpadx, pady = staticpady, sticky = staticsticky)
IntStatsTxFrameLbl = tk.Label(intstatsfrm, text="carrier").grid(column = 6, row = 3, padx = staticpadx, pady = staticpady, sticky = staticsticky)
IntStatsTxFrameCountLbl = tk.Label(intstatsfrm, text="").grid(column = 7, row = 3, padx = staticpadx, pady = staticpady, sticky = staticsticky)
IntStatsTxCollisionsLbl = tk.Label(intstatsfrm, text="collisions").grid(column = 8, row = 3, padx = staticpadx, pady = staticpady, sticky = staticsticky)
IntStatsTxCollisionsCountLbl = tk.Label(intstatsfrm, text="").grid(column = 9, row = 3, padx = staticpadx, pady = staticpady, sticky = staticsticky)

#netTab - Routing Table
routingtablecontlbl = tk.Label(routetblfrm, text = "Destination").grid(column = 0, row = 0, padx = staticnarrowpad, pady = staticnarrowpad, sticky = staticsticky)
routingtablecontlbl = tk.Label(routetblfrm, text = "Gateway").grid(column = 1, row = 0, padx = staticnarrowpad, pady = staticnarrowpad, sticky = staticsticky)
routingtablecontlbl = tk.Label(routetblfrm, text = "Genmask").grid(column = 2, row = 0, padx = staticnarrowpad, pady = staticnarrowpad, sticky = staticsticky)
routingtablecontlbl = tk.Label(routetblfrm, text = "Flags").grid(column = 3, row = 0, padx = staticnarrowpad, pady = staticnarrowpad, sticky = staticsticky)
routingtablecontlbl = tk.Label(routetblfrm, text = "MSS").grid(column = 4, row = 0, padx = staticnarrowpad, pady = staticnarrowpad, sticky = staticsticky)
routingtablecontlbl = tk.Label(routetblfrm, text = "Window").grid(column = 5, row = 0, padx = staticnarrowpad, pady = staticnarrowpad, sticky = staticsticky)
routingtablecontlbl = tk.Label(routetblfrm, text = "irtt").grid(column = 6, row = 0, padx = staticnarrowpad, pady = staticnarrowpad, sticky = staticsticky)
routingtablecontlbl = tk.Label(routetblfrm, text = "Iface").grid(column = 7, row = 0, padx = staticnarrowpad, pady = staticnarrowpad, sticky = staticsticky)
count = 0
rowcount = 1
for x in introutetable:
	if count == 8:
		count = 0
		rowcount = rowcount + 1
		routingtablecontlbl = tk.Label(routetblfrm, text = x).grid(column = count, row = rowcount, padx = staticnarrowpad, pady = staticnarrowpad, sticky = staticsticky)
		count = count + 1
	elif count < 8:
		routingtablecontlbl = tk.Label(routetblfrm, text = x).grid(column = count, row = rowcount, padx = staticnarrowpad, pady = staticnarrowpad, sticky = staticsticky)
		count = count + 1

#aboutTab Layout
abouttabttlfrm = tk.LabelFrame(abouttab, text = lstname).grid(column = 0, row = 0, padx = staticpadx, pady = staticpady, sticky=staticfullframesticky, columnspan=3)
aboutauthorlbl = ttk.Label(abouttabttlfrm, text ="Written By:").grid(column = 0, row = 1, padx = staticpadx, pady = staticpady, sticky=staticsticky)
aboutauthor = ttk.Label(abouttabttlfrm, text =lstauthor).grid(column = 1, row = 1, padx = staticpadx, pady = staticpady, sticky=staticsticky)
aboutcontactlbl = ttk.Label(abouttabttlfrm, text ="Contact:").grid(column = 0, row = 2, padx = staticpadx, pady = staticpady, sticky=staticsticky)
aboutcontact = ttk.Label(abouttabttlfrm, text =lstcontact).grid(column = 1, row = 2, padx = staticpadx, pady = staticpady, sticky=staticsticky)
aboutgithubrepolbl = ttk.Label(abouttabttlfrm, text ="GitHub Repository:").grid(column = 0, row = 3, padx = staticpadx, pady = staticpady, sticky=staticsticky)
aboutgithubrepo = ttk.Label(abouttabttlfrm, text =lstgithubrepo).grid(column = 1, row = 3, padx = staticpadx, pady = staticpady, sticky=staticsticky)
aboutgitlbl = ttk.Label(abouttabttlfrm, text ="Git Link:").grid(column = 0, row = 4, padx = staticpadx, pady = staticpady, sticky=staticsticky)
aboutgithubgit = ttk.Label(abouttabttlfrm, text =lstgithubgit).grid(column = 1, row = 4, padx = staticpadx, pady = staticpady, sticky=staticsticky)

"""Run System"""
root.config(menu=menubar)
root.mainloop()
