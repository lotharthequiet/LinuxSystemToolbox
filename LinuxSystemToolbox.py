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
proctabtitleframe = tk.LabelFrame(proctab, text="Running Processes:")
proctabtitleframe.grid(column = 0, row = 0, padx = staticpadx, pady = (10, 5), sticky=staticfullframesticky, columnspan=2)
#proctabtitlelbl = tk.Label(proctabtitleframe, text="Test Label")
#proctabtitlelbl.grid(column = 0, row = 0, padx = staticpadx, pady = (10, 5), sticky=staticsticky)
proctabbuttonframe = tk.Frame(proctab)
proctabbuttonframe.grid(column = 2, row = 0, padx = staticpadx, pady = staticpady, sticky=staticsticky)
proctabkillprocessBtn = tk.Button(proctabbuttonframe, text="Kill Process")
proctabkillprocessBtn.grid(column = 0, row = 0, padx = staticpadx, pady = staticpady, sticky=N)
proctabspawnprocessBtn = tk.Button(proctabbuttonframe, text="Spawn Process")
proctabspawnprocessBtn.grid(column = 0, row = 1, padx = staticpadx, pady = staticpady, sticky=N)

"""servicesTab Layout"""
servicestabtitleframe = tk.LabelFrame(servicestab, text="System Services:")
servicestabtitleframe.grid(column = 0, row = 0, padx = staticpadx, pady = (10, 5), sticky=staticfullframesticky, columnspan=2)
servicestabtitlelbl = tk.Label(proctabbuttonframe, text="Test Label")
servicestabtitlelbl.grid(column = 0, row = 0, padx = staticpadx, pady = (10, 5), sticky=staticsticky)
servicestabbuttonframe = tk.Frame(servicestab)
servicestabbuttonframe.grid(column = 2, row = 0, padx = staticpadx, pady = staticpady, sticky=staticsticky)
servicestabenableprocessbtn = tk.Button(servicestabbuttonframe, text="Enable Service")
servicestabenableprocessbtn.grid(column = 0, row = 0, padx = staticpadx, pady = staticpady, sticky=N)
servicestabdisableprocessbtn = tk.Button(servicestabbuttonframe, text="Disable Service")
servicestabdisableprocessbtn.grid(column = 0, row = 1, padx = staticpadx, pady = staticpady, sticky=N)
servicestabstartprocessbtn = tk.Button(servicestabbuttonframe, text="Start Service")
servicestabstartprocessbtn.grid(column = 0, row = 2, padx = staticpadx, pady = staticpady, sticky=N)
servicestabstopprocessbtn = tk.Button(servicestabbuttonframe, text="Stop Service")
servicestabstopprocessbtn.grid(column = 0, row = 3, padx = staticpadx, pady = staticpady, sticky=N)

"""userTab Layout"""
userstabtitleframe = tk.LabelFrame(userstab, text="Logged In Users:")
userstabtitleframe.grid(column = 0, row = 0, padx = staticpadx, pady = (10, 5), sticky=staticfullframesticky, columnspan=2)
userstabtitlelbl = tk.Label(userstabtitleframe, text="Test Label")
userstabtitlelbl.grid(column = 0, row = 0, padx = staticpadx, pady = (10, 5), sticky=staticsticky)
userstabtitleframe = tk.LabelFrame(userstab, text="Local Users:")
userstabtitleframe.grid(column = 0, row = 1, padx = staticpadx, pady = (10, 5), sticky=staticfullframesticky, columnspan=2)
userstabtitlelbl = tk.Label(userstabtitleframe, text="Test Label")
userstabtitlelbl.grid(column = 0, row = 0, padx = staticpadx, pady = (10, 5), sticky=staticsticky)
userstabbuttonframe = tk.Frame(userstab)
userstabbuttonframe.grid(column = 2, row = 0, padx = staticpadx, pady = staticpady, sticky=staticsticky)
userstabkillprocessbtn = tk.Button(userstabbuttonframe, text="Kill Process")
userstabkillprocessbtn.grid(column = 0, row = 0, padx = staticpadx, pady = staticpady, sticky=N)

"""netTab Layout"""
#netTab - Row 1
#Setup nettabcontentframe Frame
nettabcontentframe = tk.Frame(nettab)
nettabcontentframe.grid(column = 0, row = 0, padx = staticpadx, pady = (10, 5), sticky=staticsticky)

#Setup nettabbuttonframe Frame
nettabbuttonframe = tk.Frame(nettab)
nettabbuttonframe.grid(column = 1, row = 0, padx = 0, pady = (10, 5), sticky='N')

#Setup nettabintstatsframe Frame
nettabintstatsframe = tk.LabelFrame(nettab, text="Interface Statistics:")
nettabintstatsframe.grid(column = 0, row = 1, padx = staticpadx, pady = staticpady, sticky = staticfullframesticky, columnspan = 2) 

#Setup netabroutingtableframe
nettabroutingtableframe = tk.LabelFrame(nettab, text="Routing Table:")
nettabroutingtableframe.grid(column = 0, row = 2, padx = staticpadx, pady = staticpady, sticky = staticfullframesticky, columnspan = 2)

#nettabbuttonframe - Buttons
nettabdisableintbtn = ttk.Button(nettabbuttonframe, text ="Disable", width = staticbuttonsize, command=toggleinterface).grid(column = 0, row = 0, padx = staticpadx, pady = staticpady, sticky='N')
nettabdhcpreleasebtn = ttk.Button(nettabbuttonframe, text ="DHCP Release", width = staticbuttonsize, command=dhcprelease).grid(column = 0, row = 1, padx = staticpadx, pady = staticpady, sticky='N')
nettabdhcprenewbtn = ttk.Button(nettabbuttonframe, text ="DHCP Renew", width = staticbuttonsize, command=dhcprenew).grid(column = 0, row = 2, padx = staticpadx, pady = staticpady, sticky='N')
nettabnettoolboxbtn = ttk.Button(nettabbuttonframe, text ="Toolbox", width= staticbuttonsize, command=opennettoolbox).grid(column = 0, row = 3, padx = staticpadx, pady = staticpady, sticky='N')

#nettabcontentframe - Row 1
selintname = tk.StringVar()
nettabintlbl = ttk.Label(nettabcontentframe, text ="Select Interface:").grid(column = 0, row = 0, padx = staticpadx, pady = (10, 5), sticky=staticsticky)
nettabintcombo = ttk.Combobox(nettabcontentframe, values = intlist)
nettabintcombo.set("Select Interface:")
nettabintcombo.grid(column = 1, row = 0, padx = staticpadx, pady = (10, 5), sticky=staticsticky)
nettabintcombo.bind('<<ComboboxSelected>>', lambda event: selectinterface())

#netTab - Row 2
nettabmacaddrlbl = ttk.Label(nettabcontentframe, text="Mac Address:").grid(column = 0, row = 1, padx = staticpadx, pady = staticpady, sticky=staticsticky)
nettabmacaddr = ttk.Label(nettabcontentframe, text="").grid(column = 1, row = 1, padx = staticpadx, pady = staticpady, sticky=staticsticky)

#netTab - Row 3
nettabmtulbl = ttk.Label(nettabcontentframe, text ="MTU:").grid(column = 0, row = 2, padx = staticpadx, pady = staticpady, sticky=staticsticky)
nettabmtu = ttk.Label(nettabcontentframe, text = "").grid(column = 1, row = 2, padx = staticpadx, pady = staticpady, sticky=staticsticky)

#netTab - Row 4
nettabipaddrlbl = ttk.Label(nettabcontentframe, text="IP Address:").grid(column = 0, row = 3, padx = staticpadx, pady = staticpady, sticky=staticsticky)
nettabipaddr = ttk.Label(nettabcontentframe, text="").grid(column = 1, row = 3, padx = staticpadx, pady = staticpady, sticky=staticsticky)

#netTab - Row 5
nettabsubmasklbl = ttk.Label(nettabcontentframe, text="Subnet Mask:").grid(column = 0, row = 4, padx = staticpadx, pady = staticpady, sticky=staticsticky)
nettabsubmask = ttk.Label(nettabcontentframe, text="").grid(column = 1, row = 4, padx = staticpadx, pady = staticpady, sticky=staticsticky)

#netTab - Row 6
nettabdefgwlbl = ttk.Label(nettabcontentframe, text="Default Gateway:").grid(column = 0, row = 5, padx = staticpadx, pady = staticpady, sticky=staticsticky)
nettabdefgw = ttk.Label(nettabcontentframe, text="").grid(column = 1, row = 5, padx = staticpadx, pady = staticpady, sticky=staticsticky)

#netTab - Row 7
nettabbcastaddrlbl = ttk.Label(nettabcontentframe, text="Broadcast Address:").grid(column = 0, row = 6, padx = staticpadx, pady = staticpady, sticky=staticsticky)
nettabbcastaddr = ttk.Label(nettabcontentframe, text="").grid(column = 1, row = 6, padx = staticpadx, pady = staticpady, sticky=staticsticky)

#netTab - Row 8
nettabdnsserverslbl = ttk.Label(nettabcontentframe, text="DNS Servers:").grid(column = 0, row = 7, padx = staticpadx, pady = staticpady, sticky=staticsticky)
#rowcount = 7
# for x in dnsServerAddresses:
#     if rowcount < 9:
#         netTabDNSServer = ttk.Label(nettabcontentframe, text=x).grid(column = 1, row = rowcount, padx = staticpadx, pady = staticpady, sticky=staticsticky)
#         rowcount = rowcount + 1

#netTab - Row 10
nettabdnshostnamelbl = ttk.Label(nettabcontentframe, text="DNS Hostname:").grid(column = 0, row = 9, padx = staticpadx, pady = staticpady, sticky=staticsticky)
nettabdnshostname = ttk.Label(nettabcontentframe, text="").grid(column = 1, row = 9, padx = staticpadx, pady = staticpady, sticky=staticsticky)

#netTab - Row 11
nettabdnsdomainlbl = ttk.Label(nettabcontentframe, text="DNS Domain:").grid(column = 0, row = 10, padx = staticpadx, pady = staticpady, sticky=staticsticky)
nettabdnsdomain = ttk.Label(nettabcontentframe, text="").grid(column = 1, row = 10, padx = staticpadx, pady = staticpady, sticky=staticsticky)

#netTab - Interface Stats
#Row 1
netTabIntStatsRxPacketLbl = tk.Label(nettabintstatsframe, text="RX packets")
netTabIntStatsRxPacketLbl.grid(column = 0, row = 0, padx = staticpadx, pady = staticpady, sticky = staticsticky)
netTabIntStatsRxPacketCountLbl = tk.Label(nettabintstatsframe, text="")
netTabIntStatsRxPacketCountLbl.grid(column = 1, row = 0, padx = staticpadx, pady = staticpady, sticky = staticsticky)
netTabIntStatsRxPacketBytesLbl = tk.Label(nettabintstatsframe, text="bytes")
netTabIntStatsRxPacketBytesLbl.grid(column = 2, row = 0, padx = staticpadx, pady = staticpady, sticky = staticsticky)
netTabIntStatsRxPacketBytesCountLbl = tk.Label(nettabintstatsframe, text="")
netTabIntStatsRxPacketBytesLbl.grid(column = 3, row = 0, padx = staticpadx, pady = staticpady, sticky = staticsticky)
netTabIntStatsRxPacketBytesHumanCountLbl = tk.Label(nettabintstatsframe, text="")
netTabIntStatsRxPacketBytesHumanCountLbl.grid(column = 3, row = 0, padx = staticpadx, pady = staticpady, sticky = staticsticky)
#Row 2
netTabIntStatsRxErrorsLbl = tk.Label(nettabintstatsframe, text="RX errors")
netTabIntStatsRxErrorsLbl.grid(column = 0, row = 1, padx = staticpadx, pady = staticpady, sticky = staticsticky)
netTabIntStatsRxErrorsCountLbl = tk.Label(nettabintstatsframe, text="")
netTabIntStatsRxErrorsCountLbl.grid(column = 1, row = 1, padx = staticpadx, pady = staticpady, sticky = staticsticky)
netTabIntStatsRxDroppedLbl = tk.Label(nettabintstatsframe, text="dropped")
netTabIntStatsRxDroppedLbl.grid(column = 2, row = 1, padx = staticpadx, pady = staticpady, sticky = staticsticky)
netTabIntStatsRxDroppedCountLbl = tk.Label(nettabintstatsframe, text="")
netTabIntStatsRxDroppedCountLbl.grid(column = 3, row = 1, padx = staticpadx, pady = staticpady, sticky = staticsticky)
netTabIntStatsRxOverrunsLbl = tk.Label(nettabintstatsframe, text="overruns")
netTabIntStatsRxOverrunsLbl.grid(column = 4, row = 1, padx = staticpadx, pady = staticpady, sticky = staticsticky)
netTabIntStatsRxOverrunsCountLbl = tk.Label(nettabintstatsframe, text="")
netTabIntStatsRxOverrunsCountLbl.grid(column = 5, row = 1, padx = staticpadx, pady = staticpady, sticky = staticsticky)
netTabIntStatsRxFrameLbl = tk.Label(nettabintstatsframe, text="frame")
netTabIntStatsRxFrameLbl.grid(column = 6, row = 1, padx = staticpadx, pady = staticpady, sticky = staticsticky)
netTabIntStatsRxFrameCountLbl = tk.Label(nettabintstatsframe, text="")
netTabIntStatsRxFrameCountLbl.grid(column = 7, row = 1, padx = staticpadx, pady = staticpady, sticky = staticsticky)
#Row 3
netTabIntStatsTxPacketLbl = tk.Label(nettabintstatsframe, text="TX packets")
netTabIntStatsTxPacketLbl.grid(column = 0, row = 2, padx = staticpadx, pady = staticpady, sticky = staticsticky)
netTabIntStatsTxPacketCountLbl = tk.Label(nettabintstatsframe, text="")
netTabIntStatsTxPacketCountLbl.grid(column = 1, row = 2, padx = staticpadx, pady = staticpady, sticky = staticsticky)
netTabIntStatsTxPacketBytesLbl = tk.Label(nettabintstatsframe, text="bytes")
netTabIntStatsTxPacketBytesLbl.grid(column = 2, row = 2, padx = staticpadx, pady = staticpady, sticky = staticsticky)
netTabIntStatsTxPacketBytesCountLbl = tk.Label(nettabintstatsframe, text="")
netTabIntStatsTxPacketBytesLbl.grid(column = 3, row = 2, padx = staticpadx, pady = staticpady, sticky = staticsticky)
netTabIntStatsTxPacketBytesHumanCountLbl = tk.Label(nettabintstatsframe, text="")
netTabIntStatsTxPacketBytesHumanCountLbl.grid(column = 3, row = 2, padx = staticpadx, pady = staticpady, sticky = staticsticky)
#Row 4
netTabIntStatsTxErrorsLbl = tk.Label(nettabintstatsframe, text="RX errors")
netTabIntStatsTxErrorsLbl.grid(column = 0, row = 3, padx = staticpadx, pady = staticpady, sticky = staticsticky)
netTabIntStatsTxErrorsCountLbl = tk.Label(nettabintstatsframe, text="")
netTabIntStatsTxErrorsCountLbl.grid(column = 1, row = 3, padx = staticpadx, pady = staticpady, sticky = staticsticky)
netTabIntStatsTxDroppedLbl = tk.Label(nettabintstatsframe, text="dropped")
netTabIntStatsTxDroppedLbl.grid(column = 2, row = 3, padx = staticpadx, pady = staticpady, sticky = staticsticky)
netTabIntStatsTxDroppedCountLbl = tk.Label(nettabintstatsframe, text="")
netTabIntStatsTxDroppedCountLbl.grid(column = 3, row = 3, padx = staticpadx, pady = staticpady, sticky = staticsticky)
netTabIntStatsTxOverrunsLbl = tk.Label(nettabintstatsframe, text="overruns")
netTabIntStatsTxOverrunsLbl.grid(column = 4, row = 3, padx = staticpadx, pady = staticpady, sticky = staticsticky)
netTabIntStatsTxOverrunsCountLbl = tk.Label(nettabintstatsframe, text="")
netTabIntStatsTxOverrunsCountLbl.grid(column = 5, row = 3, padx = staticpadx, pady = staticpady, sticky = staticsticky)
netTabIntStatsTxFrameLbl = tk.Label(nettabintstatsframe, text="carrier")
netTabIntStatsTxFrameLbl.grid(column = 6, row = 3, padx = staticpadx, pady = staticpady, sticky = staticsticky)
netTabIntStatsTxFrameCountLbl = tk.Label(nettabintstatsframe, text="")
netTabIntStatsTxFrameCountLbl.grid(column = 7, row = 3, padx = staticpadx, pady = staticpady, sticky = staticsticky)
netTabIntStatsTxCollisionsLbl = tk.Label(nettabintstatsframe, text="collisions")
netTabIntStatsTxCollisionsLbl.grid(column = 8, row = 3, padx = staticpadx, pady = staticpady, sticky = staticsticky)
netTabIntStatsTxCollisionsCountLbl = tk.Label(nettabintstatsframe, text="")
netTabIntStatsTxCollisionsCountLbl.grid(column = 9, row = 3, padx = staticpadx, pady = staticpady, sticky = staticsticky)
#netTab - Routing Table
nettabroutingtablecontentlabel = tk.Label(nettabroutingtableframe, text = "Destination").grid(column = 0, row = 0, padx = staticnarrowpad, pady = staticnarrowpad, sticky = staticsticky)
nettabroutingtablecontentlabel = tk.Label(nettabroutingtableframe, text = "Gateway").grid(column = 1, row = 0, padx = staticnarrowpad, pady = staticnarrowpad, sticky = staticsticky)
nettabroutingtablecontentlabel = tk.Label(nettabroutingtableframe, text = "Genmask").grid(column = 2, row = 0, padx = staticnarrowpad, pady = staticnarrowpad, sticky = staticsticky)
nettabroutingtablecontentlabel = tk.Label(nettabroutingtableframe, text = "Flags").grid(column = 3, row = 0, padx = staticnarrowpad, pady = staticnarrowpad, sticky = staticsticky)
nettabroutingtablecontentlabel = tk.Label(nettabroutingtableframe, text = "MSS").grid(column = 4, row = 0, padx = staticnarrowpad, pady = staticnarrowpad, sticky = staticsticky)
nettabroutingtablecontentlabel = tk.Label(nettabroutingtableframe, text = "Window").grid(column = 5, row = 0, padx = staticnarrowpad, pady = staticnarrowpad, sticky = staticsticky)
nettabroutingtablecontentlabel = tk.Label(nettabroutingtableframe, text = "irtt").grid(column = 6, row = 0, padx = staticnarrowpad, pady = staticnarrowpad, sticky = staticsticky)
nettabroutingtablecontentlabel = tk.Label(nettabroutingtableframe, text = "Iface").grid(column = 7, row = 0, padx = staticnarrowpad, pady = staticnarrowpad, sticky = staticsticky)
count = 0
rowcount = 1
for x in introutetable:
	if count == 8:
		count = 0
		rowcount = rowcount + 1
		nettabroutingtablecontentlabel = tk.Label(nettabroutingtableframe, text = x).grid(column = count, row = rowcount, padx = staticnarrowpad, pady = staticnarrowpad, sticky = staticsticky)
		count = count + 1
	elif count < 8:
		nettabroutingtablecontentlabel = tk.Label(nettabroutingtableframe, text = x).grid(column = count, row = rowcount, padx = staticnarrowpad, pady = staticnarrowpad, sticky = staticsticky)
		count = count + 1

#aboutTab Layout
abouttabtitleframe = tk.LabelFrame(abouttab, text = lstname)
abouttabtitleframe.grid(column = 0, row = 0, padx = staticpadx, pady = staticpady, sticky=staticfullframesticky, columnspan=3)
aboutauthorlbl = ttk.Label(abouttabtitleframe,
          text ="Written By:").grid(column = 0, row = 1, padx = staticpadx, pady = staticpady, sticky=staticsticky)
aboutauthor = ttk.Label(abouttabtitleframe,
          text =lstauthor).grid(column = 1, row = 1, padx = staticpadx, pady = staticpady, sticky=staticsticky)
aboutcontactlbl = ttk.Label(abouttabtitleframe,
          text ="Contact:").grid(column = 0, row = 2, padx = staticpadx, pady = staticpady, sticky=staticsticky)
aboutcontact = ttk.Label(abouttabtitleframe,
          text =lstcontact).grid(column = 1, row = 2, padx = staticpadx, pady = staticpady, sticky=staticsticky)
aboutgithubrepolbl = ttk.Label(abouttabtitleframe, 
          text ="GitHub Repository:").grid(column = 0, row = 3, padx = staticpadx, pady = staticpady, sticky=staticsticky)
aboutgithubrepo = ttk.Label(abouttabtitleframe,
          text =lstgithubrepo).grid(column = 1, row = 3, padx = staticpadx, pady = staticpady, sticky=staticsticky)
aboutgitlbl = ttk.Label(abouttabtitleframe,
          text ="Git Link:").grid(column = 0, row = 4, padx = staticpadx, pady = staticpady, sticky=staticsticky)
aboutgithubgit = ttk.Label(abouttabtitleframe,
          text =lstgithubgit).grid(column = 1, row = 4, padx = staticpadx, pady = staticpady, sticky=staticsticky)

"""Run System"""
root.config(menu=menubar)
root.mainloop()
