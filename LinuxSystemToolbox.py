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
sysMgrVer = "0.1a"                                                                  #Sytem Version number
sysMgrName = "Linux System Toolbox"                                                 #Application Name
sysMgrAuthor = "Lothar TheQuiet"                                                    #Application Author
sysMgrContact = "lotharthequiet@gmail.com"                                          #Application Author Contact
sysMgrGitHubRepo = "https://github.com/lotharthequiet/LinuxSystemToolbox"           #GitHub Repository
sysMgrGitHubGit = "https://github.com/lotharthequiet/LinuxSystemToolbox.git"        #GitHub Direct Link
staticPadX = 10                                                                     #Static X Padding Value
staticPadY = 5                                                                      #Static Y Padding Value
staticNarrowPad = 5                                                                 #Static Narrow Pad Value
staticButtonSize = 12                                                               #Static button size value
staticSticky = W                                                                    #Static sticky direction
staticFullFrameSticky = NSEW                                                        #Static full sticky for label frames

"""  ***** Define routines/gather info *****  """
def toggleInterface():
    print("Toggle Interface")

def dhcpRelease():
    print("DHCP Release")

def dhcpRenew():
    print("DHCP Renew")

def openNetToolbox():
    print("Open Toolbox")

def switchUser():
    print("Switch User")

def logout():
    print("Logout")

def restart():
    print("Restart")

def shutdown():
    print("Shutdown")

def openManPage():
    print("Open Man Pages.")

def openAboutTab():
    print("Open About Tab.")

def runReports():
    print("Run reports.")

def selectInterface():
    print("Select Interface Function.")
    print(netTabIntCombo.get())
    #Get selected interface name
    intName = netTabIntCombo.get()
    #Get interface status
    intStatus = subprocess.Popen("ifconfig " + intName + " | head -n 1 | awk {'print$2'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    print(intStatus)
    intStatusStr = "UP"
    connectedStatusStr = "RUNNING"
    if intStatusStr in intStatus:                       #iterate through raw int status and find UP L1 status
        if connectedStatusStr in intStatus:             #iterate through raw int status and find RUNNING L2 status
            intStatusResult = True
    else:
            intStatusResult = False
    #Set button label
    if intStatusResult:
        netTabDisableIntBtn.config(text="Disable")      #Change the button text to disable if interface is enabled
    else:
        netTabDisableIntBtn.config(text="Enable")       #Change the button text to enable if interface is disabled
    #Get mac address
    intMacAddress = subprocess.Popen("ifconfig " + intName + " | grep ether | awk '{print$2}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    #Get MTU
    intMTU = subprocess.Popen("ifconfig " + intName + " | head -n +1 | awk '{print$4}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    #Get IP address
    intIPAddress = subprocess.Popen("ifconfig " + intName + " | grep inet | head -n +1 | awk '{print$2}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    #Get subnet mask
    intSubnetMask = subprocess.Popen("ifconfig " + intName + " | grep inet | head -n +1 | awk '{print$4}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    #Get def gw
    intDefaultGW = subprocess.Popen("netstat -r | tail -n +3 | awk '{print$2}' | head -n +1", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    #Get broadcast address
    intBroadcastAddress = subprocess.Popen("ifconfig " + intName + " | grep inet | head -n +1 | awk '{print$6}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    #Get DNS server addresses (qty 2)
    dnsServerAddresses = subprocess.Popen("cat /etc/resolv.conf | tail -n +3 | awk '{print$2}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    dnsServerAddresses = dnsServerAddresses.split()
    #Get DNS hostname
    intHostname = subprocess.Popen("hostname", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    #Get DNS domain name
    intDNSDomainName = subprocess.Popen("cat /etc/resolv.conf | tail -n +2 | awk '{print$2}' | head -n +1", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    #Get interface stats
    rxPacketCount = subprocess.Popen("ifconfig " + intName + " | grep 'RX packets' | awk {'print$3'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    rxPacketByteCount = subprocess.Popen("ifconfig " + intName + " | grep 'RX packets' | awk {'print$5'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    rxPacketHumanSize = subprocess.Popen("ifconfig " + intName + " | grep 'RX packets' | awk {'print$6'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    rxErrorCount = subprocess.Popen("ifconfig " + intName + " | grep 'RX Errors' | awk {'print$3'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    rxDroppedCount = subprocess.Popen("ifconfig " + intName + " | grep 'RX Errors' | awk {'print$5'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    rxOverrunsCount = subprocess.Popen("ifconfig " + intName + " | grep 'RX Errors' | awk {'print$7'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    rxFrameCount = subprocess.Popen("ifconfig " + intName + " | grep 'RX Errors' | awk {'print$9'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    txPacketCount = subprocess.Popen("ifconfig " + intName + " | grep 'TX packets' | awk {'print$3'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    txPacketByteCount = subprocess.Popen("ifconfig " + intName + " | grep 'TX packets' | awk {'print$5'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    txPacketHumanSize = subprocess.Popen("ifconfig " + intName + " | grep 'TX packets' | awk {'print$6'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    txErrorCount = subprocess.Popen("ifconfig " + intName + " | grep 'TX errors' | awk {'print$3'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    txDroppedCount = subprocess.Popen("ifconfig " + intName + " | grep 'TX errors' | awk {'print$5'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    txOverrunsCount = subprocess.Popen("ifconfig " + intName + " | grep 'TX errors' | awk {'print$7'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    txCarrier = subprocess.Popen("ifconfig " + intName + " | grep 'TX errors' | awk {'print$9'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    txCollisions = subprocess.Popen("ifconfig " + intName + " | grep 'TX errors' | awk {'print$11'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
    print(intName)
    print(intStatus)
    print(intMacAddress)
    print(intMTU)
    print(intIPAddress)
    print(intSubnetMask)
    print(intDefaultGW)
    print(intBroadcastAddress)
    for server in dnsServerAddresses:
        print(server)
    print(intHostname)
    print(intDNSDomainName)
    print(rxPacketCount)
    print(rxPacketByteCount)
    print(rxPacketHumanSize)
    print(rxErrorCount)
    print(rxDroppedCount)
    print(rxOverrunsCount)
    print(rxFrameCount)
    print(txPacketCount)
    print(txPacketByteCount)
    print(txPacketHumanSize)
    print(txErrorCount)
    print(txDroppedCount)
    print(txOverrunsCount)
    print(txCarrier)
    print(txCollisions)


"""Get sysMgr Info"""
#Get NIC list
intList = subprocess.Popen("ifconfig -s | tail -n +2 | awk '{print$1}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
intList = intList.split()

#Get Default Gateway
#defGateway = subprocess.Popen("netstat -r | tail -n +3 | awk '{print$2}' | head -n +1", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]

#Get DNS Server Addresses
#dnsServerAddresses = subprocess.Popen("cat /etc/resolv.conf | tail -n +3 | awk '{print$2}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
#dnsServerAddresses = dnsServerAddresses.split()

#Get DNS Hostname
#dnsHostname = subprocess.Popen("hostname", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]

#Get DNS Domain
#dnsDomain = subprocess.Popen("cat /etc/resolv.conf | tail -n +2 | awk '{print$2}' | head -n +1", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]

#Get Route Table
intRouteTable = subprocess.Popen("netstat -r | tail -n +3", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
intRouteTable = intRouteTable.split()

"""Setup Main Window"""
root = tk.Tk()
root.title(sysMgrName)                                                  #Define App title
root.geometry("590x675")                                                #Define default app size
sysMgr = ttk.Notebook(root)                                             #Nest the sysMgr Notebook into the root tkWindow

"""Setup File Menu"""
menubar = Menu(sysMgr)
filemenu = Menu(menubar, tearoff=0)                                     #Setup File submenu
filemenu.add_command(label="Reports", command=runReports)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
toolsmenu = Menu(menubar, tearoff=0)                                    #Setup Tools submenu
toolsmenu.add_command(label="Open Toolbox", command=openNetToolbox)
toolsmenu.add_separator()
toolsmenu.add_command(label="Switch User", command=switchUser)
toolsmenu.add_command(label="Logout", command=logout)
toolsmenu.add_command(label="Restart", command=restart)
toolsmenu.add_command(label="Shutdown", command=shutdown)
menubar.add_cascade(label="Tools", menu=toolsmenu)
helpmenu = Menu(menubar, tearoff=0)                                     #Setup Help submenu
helpmenu.add_command(label="Help", command=openManPage)
helpmenu.add_separator()
helpmenu.add_command(label="About", command=openAboutTab)
menubar.add_cascade(label="Help", menu=helpmenu)

"""Define tabs in the root window (root)"""
procTab = ttk.Frame(sysMgr)
servicesTab = ttk.Frame(sysMgr)
usersTab = ttk.Frame(sysMgr)
netTab = ttk.Frame(sysMgr)
perfTab = ttk.Frame(sysMgr)
wirelessTab = ttk.Frame(sysMgr)
aboutTab = ttk.Frame(sysMgr)

"""Define tab names"""
sysMgr.add(procTab, text ='Processes')
sysMgr.add(servicesTab, text ='Services')
sysMgr.add(usersTab, text ='Users')
sysMgr.add(netTab, text ='Networking')
sysMgr.add(perfTab, text ='Performance')
sysMgr.add(wirelessTab, text = 'Wireless')
sysMgr.add(aboutTab, text ='About')
sysMgr.pack(expand = 1, fill ="both")

"""Tab Layout"""
"""procTab Layout"""
procTabTitleFrame = tk.LabelFrame(procTab, text="Running Processes:")
procTabTitleFrame.grid(column = 0, row = 0, padx = staticPadX, pady = (10, 5), sticky=staticFullFrameSticky, columnspan=2)
procTabTitleLbl = tk.Label(procTabTitleFrame, text="Test Label")
procTabTitleLbl.grid(column = 0, row = 0, padx = staticPadX, pady = (10, 5), sticky=staticSticky)
procTabButtonFrame = tk.Frame(procTab)
procTabButtonFrame.grid(column = 2, row = 0, padx = staticPadX, pady = staticPadY, sticky=staticSticky)
procTabKillProcessBtn = tk.Button(procTabButtonFrame, text="Kill Process")
procTabKillProcessBtn.grid(column = 0, row = 0, padx = staticPadX, pady = staticPadY, sticky=N)
procTabSpawnProcessBtn = tk.Button(procTabButtonFrame, text="Spawn Process")
procTabSpawnProcessBtn.grid(column = 0, row = 1, padx = staticPadX, pady = staticPadY, sticky=N)
"""servicesTab Layout"""
servicesTabTitleFrame = tk.LabelFrame(servicesTab, text="System Services:")
servicesTabTitleFrame.grid(column = 0, row = 0, padx = staticPadX, pady = (10, 5), sticky=staticFullFrameSticky, columnspan=2)
servicesTabTitleLbl = tk.Label(servicesTabTitleFrame, text="Test Label")
servicesTabTitleLbl.grid(column = 0, row = 0, padx = staticPadX, pady = (10, 5), sticky=staticSticky)
servicesTabButtonFrame = tk.Frame(servicesTab)
servicesTabButtonFrame.grid(column = 2, row = 0, padx = staticPadX, pady = staticPadY, sticky=staticSticky)
servicesTabEnableProcessBtn = tk.Button(servicesTabButtonFrame, text="Enable Service")
servicesTabEnableProcessBtn.grid(column = 0, row = 0, padx = staticPadX, pady = staticPadY, sticky=N)
servicesTabDisableProcessBtn = tk.Button(servicesTabButtonFrame, text="Disable Service")
servicesTabDisableProcessBtn.grid(column = 0, row = 1, padx = staticPadX, pady = staticPadY, sticky=N)
servicesTabStartProcessBtn = tk.Button(servicesTabButtonFrame, text="Start Service")
servicesTabStartProcessBtn.grid(column = 0, row = 2, padx = staticPadX, pady = staticPadY, sticky=N)
servicesTabStopProcessBtn = tk.Button(servicesTabButtonFrame, text="Stop Service")
servicesTabStopProcessBtn.grid(column = 0, row = 3, padx = staticPadX, pady = staticPadY, sticky=N)
"""userTab Layout"""
usersTabTitleFrame = tk.LabelFrame(usersTab, text="Logged In Users:")
usersTabTitleFrame.grid(column = 0, row = 0, padx = staticPadX, pady = (10, 5), sticky=staticFullFrameSticky, columnspan=2)
usersTabTitleLbl = tk.Label(usersTabTitleFrame, text="Test Label")
usersTabTitleLbl.grid(column = 0, row = 0, padx = staticPadX, pady = (10, 5), sticky=staticSticky)
usersTabTitleFrame = tk.LabelFrame(usersTab, text="Local Users:")
usersTabTitleFrame.grid(column = 0, row = 1, padx = staticPadX, pady = (10, 5), sticky=staticFullFrameSticky, columnspan=2)
usersTabTitleLbl = tk.Label(usersTabTitleFrame, text="Test Label")
usersTabTitleLbl.grid(column = 0, row = 0, padx = staticPadX, pady = (10, 5), sticky=staticSticky)
usersTabButtonFrame = tk.Frame(usersTab)
usersTabButtonFrame.grid(column = 2, row = 0, padx = staticPadX, pady = staticPadY, sticky=staticSticky)
usersTabKillProcessBtn = tk.Button(usersTabButtonFrame, text="Kill Process")
usersTabKillProcessBtn.grid(column = 0, row = 0, padx = staticPadX, pady = staticPadY, sticky=N)

"""netTab Layout"""

#netTab - Row 1
#Setup netTabContentFrame Frame
netTabContentFrame = tk.Frame(netTab)
netTabContentFrame.grid(column = 0, row = 0, padx = staticPadX, pady = (10, 5), sticky=staticSticky)

#Setup netTabButtonFrame Frame
netTabButtonFrame = tk.Frame(netTab)
netTabButtonFrame.grid(column = 1, row = 0, padx = 0, pady = (10, 5), sticky='N')

#Setup netTabIntStatsFrame Frame
netTabIntStatsFrame = tk.LabelFrame(netTab, text="Interface Statistics:")
netTabIntStatsFrame.grid(column = 0, row = 1, padx = staticPadX, pady = staticPadY, sticky = staticFullFrameSticky, columnspan = 2) 

#Setup netTabRoutingTableFrame
netTabRoutingTableFrame = tk.LabelFrame(netTab, text="Routing Table:")
netTabRoutingTableFrame.grid(column = 0, row = 2, padx = staticPadX, pady = staticPadY, sticky = staticFullFrameSticky, columnspan = 2)

#netTabButtonFrame - Buttons
netTabDisableIntBtn = ttk.Button(netTabButtonFrame, text ="Disable", width = staticButtonSize, command=toggleInterface).grid(column = 0, row = 0, padx = staticPadX, pady = staticPadY, sticky='N')
netTabDHCPReleaseBtn = ttk.Button(netTabButtonFrame, text ="DHCP Release", width = staticButtonSize, command=dhcpRelease).grid(column = 0, row = 1, padx = staticPadX, pady = staticPadY, sticky='N')
netTabDHCPRenewBtn = ttk.Button(netTabButtonFrame, text ="DHCP Renew", width = staticButtonSize, command=dhcpRenew).grid(column = 0, row = 2, padx = staticPadX, pady = staticPadY, sticky='N')
netTabNetToolboxBtn = ttk.Button(netTabButtonFrame, text ="Toolbox", width= staticButtonSize, command=openNetToolbox).grid(column = 0, row = 3, padx = staticPadX, pady = staticPadY, sticky='N')

#netTabContentFrame - Row 1
selIntName = tk.StringVar()
netTabIntLbl = ttk.Label(netTabContentFrame, text ="Select Interface:").grid(column = 0, row = 0, padx = staticPadX, pady = (10, 5), sticky=staticSticky)
netTabIntCombo = ttk.Combobox(netTabContentFrame, values = intList)
netTabIntCombo.set("Select Interface:")
netTabIntCombo.grid(column = 1, row = 0, padx = staticPadX, pady = (10, 5), sticky=staticSticky)
netTabIntCombo.bind('<<ComboboxSelected>>', lambda event: selectInterface())

#netTab - Row 2
netTabMacAddrLbl = ttk.Label(netTabContentFrame, text="Mac Address:").grid(column = 0, row = 1, padx = staticPadX, pady = staticPadY, sticky=staticSticky)
netTabMacAddr = ttk.Label(netTabContentFrame, text="").grid(column = 1, row = 1, padx = staticPadX, pady = staticPadY, sticky=staticSticky)

#netTab - Row 3
netTabMTULbl = ttk.Label(netTabContentFrame, text ="MTU:").grid(column = 0, row = 2, padx = staticPadX, pady = staticPadY, sticky=staticSticky)
netTabMTU = ttk.Label(netTabContentFrame, text = "").grid(column = 1, row = 2, padx = staticPadX, pady = staticPadY, sticky=staticSticky)

#netTab - Row 4
netTabIPAddrLbl = ttk.Label(netTabContentFrame, text="IP Address:").grid(column = 0, row = 3, padx = staticPadX, pady = staticPadY, sticky=staticSticky)
netTabIPAddr = ttk.Label(netTabContentFrame, text="").grid(column = 1, row = 3, padx = staticPadX, pady = staticPadY, sticky=staticSticky)

#netTab - Row 5
netTabSubMaskLbl = ttk.Label(netTabContentFrame, text="Subnet Mask:").grid(column = 0, row = 4, padx = staticPadX, pady = staticPadY, sticky=staticSticky)
netTabSubMask = ttk.Label(netTabContentFrame, text="").grid(column = 1, row = 4, padx = staticPadX, pady = staticPadY, sticky=staticSticky)

#netTab - Row 6
netTabDefGWLbl = ttk.Label(netTabContentFrame, text="Default Gateway:").grid(column = 0, row = 5, padx = staticPadX, pady = staticPadY, sticky=staticSticky)
netTabDefGW = ttk.Label(netTabContentFrame, text="").grid(column = 1, row = 5, padx = staticPadX, pady = staticPadY, sticky=staticSticky)

#netTab - Row 7
netTabBCastAddrLbl = ttk.Label(netTabContentFrame, text="Broadcast Address:").grid(column = 0, row = 6, padx = staticPadX, pady = staticPadY, sticky=staticSticky)
netTabBCastAddr = ttk.Label(netTabContentFrame, text="").grid(column = 1, row = 6, padx = staticPadX, pady = staticPadY, sticky=staticSticky)

#netTab - Row 8
netTabDNSServersLbl = ttk.Label(netTabContentFrame, text="DNS Servers:").grid(column = 0, row = 7, padx = staticPadX, pady = staticPadY, sticky=staticSticky)
rowcount = 7
# for x in dnsServerAddresses:
#     if rowcount < 9:
#         netTabDNSServer = ttk.Label(netTabContentFrame, text=x).grid(column = 1, row = rowcount, padx = staticPadX, pady = staticPadY, sticky=staticSticky)
#         rowcount = rowcount + 1

#netTab - Row 10
netTabDNSHostnameLbl = ttk.Label(netTabContentFrame, text="DNS Hostname:").grid(column = 0, row = 9, padx = staticPadX, pady = staticPadY, sticky=staticSticky)
netTabDNSHostname = ttk.Label(netTabContentFrame, text="").grid(column = 1, row = 9, padx = staticPadX, pady = staticPadY, sticky=staticSticky)

#netTab - Row 11
netTabDNSDomainLbl = ttk.Label(netTabContentFrame, text="DNS Domain:").grid(column = 0, row = 10, padx = staticPadX, pady = staticPadY, sticky=staticSticky)
netTabDNSDomain = ttk.Label(netTabContentFrame, text="").grid(column = 1, row = 10, padx = staticPadX, pady = staticPadY, sticky=staticSticky)

#netTab - Interface Stats
#Row 1
netTabIntStatsRxPacketLbl = tk.Label(netTabIntStatsFrame, text="RX packets")
netTabIntStatsRxPacketLbl.grid(column = 0, row = 0, padx = staticPadX, pady = staticPadY, sticky = staticSticky)
netTabIntStatsRxPacketCountLbl = tk.Label(netTabIntStatsFrame, text="")
netTabIntStatsRxPacketCountLbl.grid(column = 1, row = 0, padx = staticPadX, pady = staticPadY, sticky = staticSticky)
netTabIntStatsRxPacketBytesLbl = tk.Label(netTabIntStatsFrame, text="bytes")
netTabIntStatsRxPacketBytesLbl.grid(column = 2, row = 0, padx = staticPadX, pady = staticPadY, sticky = staticSticky)
netTabIntStatsRxPacketBytesCountLbl = tk.Label(netTabIntStatsFrame, text="")
netTabIntStatsRxPacketBytesLbl.grid(column = 3, row = 0, padx = staticPadX, pady = staticPadY, sticky = staticSticky)
netTabIntStatsRxPacketBytesHumanCountLbl = tk.Label(netTabIntStatsFrame, text="")
netTabIntStatsRxPacketBytesHumanCountLbl.grid(column = 3, row = 0, padx = staticPadX, pady = staticPadY, sticky = staticSticky)
#Row 2
netTabIntStatsRxErrorsLbl = tk.Label(netTabIntStatsFrame, text="RX errors")
netTabIntStatsRxErrorsLbl.grid(column = 0, row = 1, padx = staticPadX, pady = staticPadY, sticky = staticSticky)
netTabIntStatsRxErrorsCountLbl = tk.Label(netTabIntStatsFrame, text="")
netTabIntStatsRxErrorsCountLbl.grid(column = 1, row = 1, padx = staticPadX, pady = staticPadY, sticky = staticSticky)
netTabIntStatsRxDroppedLbl = tk.Label(netTabIntStatsFrame, text="dropped")
netTabIntStatsRxDroppedLbl.grid(column = 2, row = 1, padx = staticPadX, pady = staticPadY, sticky = staticSticky)
netTabIntStatsRxDroppedCountLbl = tk.Label(netTabIntStatsFrame, text="")
netTabIntStatsRxDroppedCountLbl.grid(column = 3, row = 1, padx = staticPadX, pady = staticPadY, sticky = staticSticky)
netTabIntStatsRxOverrunsLbl = tk.Label(netTabIntStatsFrame, text="overruns")
netTabIntStatsRxOverrunsLbl.grid(column = 4, row = 1, padx = staticPadX, pady = staticPadY, sticky = staticSticky)
netTabIntStatsRxOverrunsCountLbl = tk.Label(netTabIntStatsFrame, text="")
netTabIntStatsRxOverrunsCountLbl.grid(column = 5, row = 1, padx = staticPadX, pady = staticPadY, sticky = staticSticky)
netTabIntStatsRxFrameLbl = tk.Label(netTabIntStatsFrame, text="frame")
netTabIntStatsRxFrameLbl.grid(column = 6, row = 1, padx = staticPadX, pady = staticPadY, sticky = staticSticky)
netTabIntStatsRxFrameCountLbl = tk.Label(netTabIntStatsFrame, text="")
netTabIntStatsRxFrameCountLbl.grid(column = 7, row = 1, padx = staticPadX, pady = staticPadY, sticky = staticSticky)
#Row 3
netTabIntStatsTxPacketLbl = tk.Label(netTabIntStatsFrame, text="TX packets")
netTabIntStatsTxPacketLbl.grid(column = 0, row = 2, padx = staticPadX, pady = staticPadY, sticky = staticSticky)
netTabIntStatsTxPacketCountLbl = tk.Label(netTabIntStatsFrame, text="")
netTabIntStatsTxPacketCountLbl.grid(column = 1, row = 2, padx = staticPadX, pady = staticPadY, sticky = staticSticky)
netTabIntStatsTxPacketBytesLbl = tk.Label(netTabIntStatsFrame, text="bytes")
netTabIntStatsTxPacketBytesLbl.grid(column = 2, row = 2, padx = staticPadX, pady = staticPadY, sticky = staticSticky)
netTabIntStatsTxPacketBytesCountLbl = tk.Label(netTabIntStatsFrame, text="")
netTabIntStatsTxPacketBytesLbl.grid(column = 3, row = 2, padx = staticPadX, pady = staticPadY, sticky = staticSticky)
netTabIntStatsTxPacketBytesHumanCountLbl = tk.Label(netTabIntStatsFrame, text="")
netTabIntStatsTxPacketBytesHumanCountLbl.grid(column = 3, row = 2, padx = staticPadX, pady = staticPadY, sticky = staticSticky)
#Row 4
netTabIntStatsTxErrorsLbl = tk.Label(netTabIntStatsFrame, text="RX errors")
netTabIntStatsTxErrorsLbl.grid(column = 0, row = 3, padx = staticPadX, pady = staticPadY, sticky = staticSticky)
netTabIntStatsTxErrorsCountLbl = tk.Label(netTabIntStatsFrame, text="")
netTabIntStatsTxErrorsCountLbl.grid(column = 1, row = 3, padx = staticPadX, pady = staticPadY, sticky = staticSticky)
netTabIntStatsTxDroppedLbl = tk.Label(netTabIntStatsFrame, text="dropped")
netTabIntStatsTxDroppedLbl.grid(column = 2, row = 3, padx = staticPadX, pady = staticPadY, sticky = staticSticky)
netTabIntStatsTxDroppedCountLbl = tk.Label(netTabIntStatsFrame, text="")
netTabIntStatsTxDroppedCountLbl.grid(column = 3, row = 3, padx = staticPadX, pady = staticPadY, sticky = staticSticky)
netTabIntStatsTxOverrunsLbl = tk.Label(netTabIntStatsFrame, text="overruns")
netTabIntStatsTxOverrunsLbl.grid(column = 4, row = 3, padx = staticPadX, pady = staticPadY, sticky = staticSticky)
netTabIntStatsTxOverrunsCountLbl = tk.Label(netTabIntStatsFrame, text="")
netTabIntStatsTxOverrunsCountLbl.grid(column = 5, row = 3, padx = staticPadX, pady = staticPadY, sticky = staticSticky)
netTabIntStatsTxFrameLbl = tk.Label(netTabIntStatsFrame, text="carrier")
netTabIntStatsTxFrameLbl.grid(column = 6, row = 3, padx = staticPadX, pady = staticPadY, sticky = staticSticky)
netTabIntStatsTxFrameCountLbl = tk.Label(netTabIntStatsFrame, text="")
netTabIntStatsTxFrameCountLbl.grid(column = 7, row = 3, padx = staticPadX, pady = staticPadY, sticky = staticSticky)
netTabIntStatsTxCollisionsLbl = tk.Label(netTabIntStatsFrame, text="collisions")
netTabIntStatsTxCollisionsLbl.grid(column = 8, row = 3, padx = staticPadX, pady = staticPadY, sticky = staticSticky)
netTabIntStatsTxCollisionsCountLbl = tk.Label(netTabIntStatsFrame, text="")
netTabIntStatsTxCollisionsCountLbl.grid(column = 9, row = 3, padx = staticPadX, pady = staticPadY, sticky = staticSticky)
#netTab - Routing Table
netTabRoutingTableContentLabel = tk.Label(netTabRoutingTableFrame, text = "Destination").grid(column = 0, row = 0, padx = staticNarrowPad, pady = staticNarrowPad, sticky = staticSticky)
netTabRoutingTableContentLabel = tk.Label(netTabRoutingTableFrame, text = "Gateway").grid(column = 1, row = 0, padx = staticNarrowPad, pady = staticNarrowPad, sticky = staticSticky)
netTabRoutingTableContentLabel = tk.Label(netTabRoutingTableFrame, text = "Genmask").grid(column = 2, row = 0, padx = staticNarrowPad, pady = staticNarrowPad, sticky = staticSticky)
netTabRoutingTableContentLabel = tk.Label(netTabRoutingTableFrame, text = "Flags").grid(column = 3, row = 0, padx = staticNarrowPad, pady = staticNarrowPad, sticky = staticSticky)
netTabRoutingTableContentLabel = tk.Label(netTabRoutingTableFrame, text = "MSS").grid(column = 4, row = 0, padx = staticNarrowPad, pady = staticNarrowPad, sticky = staticSticky)
netTabRoutingTableContentLabel = tk.Label(netTabRoutingTableFrame, text = "Window").grid(column = 5, row = 0, padx = staticNarrowPad, pady = staticNarrowPad, sticky = staticSticky)
netTabRoutingTableContentLabel = tk.Label(netTabRoutingTableFrame, text = "irtt").grid(column = 6, row = 0, padx = staticNarrowPad, pady = staticNarrowPad, sticky = staticSticky)
netTabRoutingTableContentLabel = tk.Label(netTabRoutingTableFrame, text = "Iface").grid(column = 7, row = 0, padx = staticNarrowPad, pady = staticNarrowPad, sticky = staticSticky)
count = 0
rowcount = 1
for x in intRouteTable:
	if count == 8:
		count = 0
		rowcount = rowcount + 1
		netTabRoutingTableContentLabel = tk.Label(netTabRoutingTableFrame, text = x).grid(column = count, row = rowcount, padx = staticNarrowPad, pady = staticNarrowPad, sticky = staticSticky)
		count = count + 1
	elif count < 8:
		netTabRoutingTableContentLabel = tk.Label(netTabRoutingTableFrame, text = x).grid(column = count, row = rowcount, padx = staticNarrowPad, pady = staticNarrowPad, sticky = staticSticky)
		count = count + 1

#aboutTab Layout
aboutTabTitleFrame = tk.LabelFrame(aboutTab, text = sysMgrName)
aboutTabTitleFrame.grid(column = 0, row = 0, padx = staticPadX, pady = staticPadY, sticky=staticFullFrameSticky, columnspan=3)
aboutAuthorLbl = ttk.Label(aboutTabTitleFrame,
          text ="Written By:").grid(column = 0, row = 1, padx = staticPadX, pady = staticPadY, sticky=staticSticky)
aboutAuthor = ttk.Label(aboutTabTitleFrame,
          text =sysMgrAuthor).grid(column = 1, row = 1, padx = staticPadX, pady = staticPadY, sticky=staticSticky)
aboutContactLbl = ttk.Label(aboutTabTitleFrame,
          text ="Contact:").grid(column = 0, row = 2, padx = staticPadX, pady = staticPadY, sticky=staticSticky)
aboutContact = ttk.Label(aboutTabTitleFrame,
          text =sysMgrContact).grid(column = 1, row = 2, padx = staticPadX, pady = staticPadY, sticky=staticSticky)
aboutGitHubRepoLbl = ttk.Label(aboutTabTitleFrame, 
          text ="GitHub Repository:").grid(column = 0, row = 3, padx = staticPadX, pady = staticPadY, sticky=staticSticky)
aboutGitHubRepo = ttk.Label(aboutTabTitleFrame,
          text =sysMgrGitHubRepo).grid(column = 1, row = 3, padx = staticPadX, pady = staticPadY, sticky=staticSticky)
aboutGitGitLbl = ttk.Label(aboutTabTitleFrame,
          text ="Git Link:").grid(column = 0, row = 4, padx = staticPadX, pady = staticPadY, sticky=staticSticky)
aboutGitHubGit = ttk.Label(aboutTabTitleFrame,
          text =sysMgrGitHubGit).grid(column = 1, row = 4, padx = staticPadX, pady = staticPadY, sticky=staticSticky)

"""Run System"""
root.config(menu=menubar)
root.mainloop()
