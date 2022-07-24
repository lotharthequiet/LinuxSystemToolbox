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
LSTVER = "0.1a"                                                                         #Sytem Version number
LSTNAME = "Linux System Toolbox"                                                        #Application Name
LSTAUTHOR = "Lothar TheQuiet"                                                           #Application Author
LSTCONTACT = "lotharthequiet@gmail.com"                                                 #Application Author Contact
LSTGITHUBREPO = "https://github.com/lotharthequiet/LinuxSystemToolbox"                  #GitHub Repository
LSTGITHUB = "https://github.com/lotharthequiet/LinuxSystemToolbox.git"                  #GitHub Direct Link
DEFPADX = 10                                                                               #Static X Padding Value
DEFPADY = 5                                                                                #Static Y Padding Value
NARROWPAD = 5                                                                           #Static Narrow Pad Value
BTNSIZE = 12                                                                            #Static button size value
STATICSTICKY = W                                                                        #Static sticky direction
STATICFULLFRMSTICKY = NSEW                                                              #Static full sticky for label frames

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
    print(intcombo.get())
    #Get selected interface name
    intname = intcombo.get()
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
        disableintbtn.config(text="Disable")      #Change the button text to disable if interface is enabled
    else:
        disableintbtn.config(text="Enable")       #Change the button text to enable if interface is disabled
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
root.title(LSTNAME)                                                     #Define App title
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
proctabttlfrm = tk.LabelFrame(proctab, text="Running Processes:").grid(column = 0, row = 0, padx = DEFPADX, pady = (10, 5), sticky=STATICFULLFRMSTICKY, columnspan=2)
proctabttllbl = tk.Label(proctabttlfrm, text="Test Label").grid(column = 0, row = 0, padx = DEFPADX, pady = (10, 5), sticky=STATICSTICKY)
proctabbtnfrm = tk.Frame(proctab).grid(column = 2, row = 0, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
killprocBtn = tk.Button(proctabbtnfrm, text="Kill Process").grid(column = 0, row = 0, padx = DEFPADX, pady = DEFPADY, sticky=N)
spawnprocBtn = tk.Button(proctabbtnfrm, text="Spawn Process").grid(column = 0, row = 1, padx = DEFPADX, pady = DEFPADY, sticky=N)


"""servicesTab Layout"""
svcstabttlfrm = tk.LabelFrame(servicestab, text="System Services:").grid(column = 0, row = 0, padx = DEFPADX, pady = (10, 5), sticky=STATICFULLFRMSTICKY, columnspan=2)
svcstabttllbl = tk.Label(svcstabttlfrm, text="Test Label").grid(column = 0, row = 0, padx = DEFPADX, pady = (10, 5), sticky=STATICSTICKY)
svcstabbtnfrm = tk.Frame(servicestab).grid(column = 2, row = 0, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
enablesvcbtn = tk.Button(svcstabbtnfrm, text="Enable Service").grid(column = 0, row = 0, padx = DEFPADX, pady = DEFPADY, sticky=N)
disablesvcbtn = tk.Button(svcstabbtnfrm, text="Disable Service").grid(column = 0, row = 1, padx = DEFPADX, pady = DEFPADY, sticky=N)
startsvcbtn = tk.Button(svcstabbtnfrm, text="Start Service").grid(column = 0, row = 2, padx = DEFPADX, pady = DEFPADY, sticky=N)
stopsvcbtn = tk.Button(svcstabbtnfrm, text="Stop Service").grid(column = 0, row = 3, padx = DEFPADX, pady = DEFPADY, sticky=N)

"""userTab Layout"""
usrtabttlfrm = tk.LabelFrame(userstab, text="Logged In Users:").grid(column = 0, row = 0, padx = DEFPADX, pady = (10, 5), sticky=STATICFULLFRMSTICKY, columnspan=2)
usrtabttllbl = tk.Label(usrtabttlfrm, text="Test Label").grid(column = 0, row = 0, padx = DEFPADX, pady = (10, 5), sticky=STATICSTICKY)
usrtabttlfrm = tk.LabelFrame(userstab, text="Local Users:").grid(column = 0, row = 1, padx = DEFPADX, pady = (10, 5), sticky=STATICFULLFRMSTICKY, columnspan=2)
usrtabttllbl = tk.Label(usrtabttlfrm, text="Test Label").grid(column = 0, row = 0, padx = DEFPADX, pady = (10, 5), sticky=STATICSTICKY)
usrtabbtnfrm = tk.Frame(userstab).grid(column = 2, row = 0, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
newuserbtn = tk.Button(usrtabbtnfrm, text="New User").grid(column = 0, row = 0, padx = DEFPADX, pady = DEFPADY, sticky=N)

"""nettab Layout"""
#Setup frames and buttons for nettab
nettabcontfrm = tk.Frame(nettab).grid(column = 0, row = 0, padx = DEFPADX, pady = (10, 5), sticky=STATICSTICKY)
nettabbtnfrm = tk.Frame(nettab).grid(column = 1, row = 0, padx = 0, pady = (10, 5), sticky='N')
intstatsfrm = tk.LabelFrame(nettab, text="Interface Statistics:").grid(column = 0, row = 1, padx = DEFPADX, pady = DEFPADY, sticky = STATICFULLFRMSTICKY, columnspan = 2)
routetblfrm = tk.LabelFrame(nettab, text="Routing Table:").grid(column = 0, row = 2, padx = DEFPADX, pady = DEFPADY, sticky = STATICFULLFRMSTICKY, columnspan = 2)
disableintbtn = ttk.Button(nettabbtnfrm, text ="Disable", width = BTNSIZE, command=toggleinterface).grid(column = 0, row = 0, padx = DEFPADX, pady = DEFPADY, sticky='N')
dhcpreleasebtn = ttk.Button(nettabbtnfrm, text ="DHCP Release", width = BTNSIZE, command=dhcprelease).grid(column = 0, row = 1, padx = DEFPADX, pady = DEFPADY, sticky='N')
dhcprenewbtn = ttk.Button(nettabbtnfrm, text ="DHCP Renew", width = BTNSIZE, command=dhcprenew).grid(column = 0, row = 2, padx = DEFPADX, pady = DEFPADY, sticky='N')
nettoolboxbtn = ttk.Button(nettabbtnfrm, text ="Toolbox", width= BTNSIZE, command=opennettoolbox).grid(column = 0, row = 3, padx = DEFPADX, pady = DEFPADY, sticky='N')

#nettab - Interface Info
selintname = tk.StringVar()
intlbl = ttk.Label(nettabcontfrm, text ="Select Interface:").grid(column = 0, row = 0, padx = DEFPADX, pady = (10, 5), sticky=STATICSTICKY)
intcombo = ttk.Combobox(nettabcontfrm, values = intlist).grid(column = 1, row = 0, padx = DEFPADX, pady = (10, 5), sticky=STATICSTICKY)
intcombo.set("Select Interface:")
intcombo.bind('<<ComboboxSelected>>', lambda event: selectinterface())
macaddrlbl = ttk.Label(nettabcontfrm, text="Mac Address:").grid(column = 0, row = 1, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
macaddr = ttk.Label(nettabcontfrm, text="").grid(column = 1, row = 1, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
mtulbl = ttk.Label(nettabcontfrm, text ="MTU:").grid(column = 0, row = 2, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
mtu = ttk.Label(nettabcontfrm, text = "").grid(column = 1, row = 2, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
ipaddrlbl = ttk.Label(nettabcontfrm, text="IP Address:").grid(column = 0, row = 3, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
ipaddr = ttk.Label(nettabcontfrm, text="").grid(column = 1, row = 3, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
submasklbl = ttk.Label(nettabcontfrm, text="Subnet Mask:").grid(column = 0, row = 4, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
submask = ttk.Label(nettabcontfrm, text="").grid(column = 1, row = 4, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
defgwlbl = ttk.Label(nettabcontfrm, text="Default Gateway:").grid(column = 0, row = 5, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
defgw = ttk.Label(nettabcontfrm, text="").grid(column = 1, row = 5, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
bcastaddrlbl = ttk.Label(nettabcontfrm, text="Broadcast Address:").grid(column = 0, row = 6, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
bcastaddr = ttk.Label(nettabcontfrm, text="").grid(column = 1, row = 6, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
dnsserverslbl = ttk.Label(nettabcontfrm, text="DNS Servers:").grid(column = 0, row = 7, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
#rowcount = 7
# for x in dnsServerAddresses:
#     if rowcount < 9:
#         netTabDNSServer = ttk.Label(nettabcontfrm, text=x).grid(column = 1, row = rowcount, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
#         rowcount = rowcount + 1
dnshostnamelbl = ttk.Label(nettabcontfrm, text="DNS Hostname:").grid(column = 0, row = 9, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
dnshostname = ttk.Label(nettabcontfrm, text="").grid(column = 1, row = 9, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
dnsdomainlbl = ttk.Label(nettabcontfrm, text="DNS Domain:").grid(column = 0, row = 10, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
dnsdomain = ttk.Label(nettabcontfrm, text="").grid(column = 1, row = 10, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)

#netTab - Interface Stats
rxpacketlbl = tk.Label(intstatsfrm, text="RX packets").grid(column = 0, row = 0, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
rxpacketcntlbl = tk.Label(intstatsfrm, text="").grid(column = 1, row = 0, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
rxpacketbyteslbl = tk.Label(intstatsfrm, text="bytes").grid(column = 2, row = 0, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
rxpacketbytescntlbl = tk.Label(intstatsfrm, text="").grid(column = 3, row = 0, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
rxpacketbytesHumancntlbl = tk.Label(intstatsfrm, text="").grid(column = 3, row = 0, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
rxerrorslbl = tk.Label(intstatsfrm, text="RX errors").grid(column = 0, row = 1, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
rxerrorscntlbl = tk.Label(intstatsfrm, text="").grid(column = 1, row = 1, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
rxdroppedlbl = tk.Label(intstatsfrm, text="dropped").grid(column = 2, row = 1, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
rxdroppedcntlbl = tk.Label(intstatsfrm, text="").grid(column = 3, row = 1, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
rxoverrunslbl = tk.Label(intstatsfrm, text="overruns").grid(column = 4, row = 1, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
rxoverrunscntLbl = tk.Label(intstatsfrm, text="").grid(column = 5, row = 1, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
rxframeLbl = tk.Label(intstatsfrm, text="frame").grid(column = 6, row = 1, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
rxframeCountLbl = tk.Label(intstatsfrm, text="").grid(column = 7, row = 1, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
txpacketLbl = tk.Label(intstatsfrm, text="TX packets").grid(column = 0, row = 2, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
txpacketcountlbl = tk.Label(intstatsfrm, text="").grid(column = 1, row = 2, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
txpacketbyteslbl = tk.Label(intstatsfrm, text="bytes").grid(column = 2, row = 2, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
txpacketbytescntlbl = tk.Label(intstatsfrm, text="").grid(column = 3, row = 2, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
txpacketbyteshumancntlbl = tk.Label(intstatsfrm, text="").grid(column = 3, row = 2, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
txerrorslbl = tk.Label(intstatsfrm, text="RX errors").grid(column = 0, row = 3, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
txerrorscntlbl = tk.Label(intstatsfrm, text="").grid(column = 1, row = 3, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
txdroppedlbl = tk.Label(intstatsfrm, text="dropped").grid(column = 2, row = 3, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
txdroppedcntlbl = tk.Label(intstatsfrm, text="").grid(column = 3, row = 3, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
txoverrunslbl = tk.Label(intstatsfrm, text="overruns").grid(column = 4, row = 3, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
txoverrunscountlbl = tk.Label(intstatsfrm, text="").grid(column = 5, row = 3, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
txframelbl = tk.Label(intstatsfrm, text="carrier").grid(column = 6, row = 3, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
txframecountlbl = tk.Label(intstatsfrm, text="").grid(column = 7, row = 3, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
txcollisionslbl = tk.Label(intstatsfrm, text="collisions").grid(column = 8, row = 3, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)
txcollisionscountlbl = tk.Label(intstatsfrm, text="").grid(column = 9, row = 3, padx = DEFPADX, pady = DEFPADY, sticky = STATICSTICKY)

#netTab - Routing Table
routingtablecontlbl = tk.Label(routetblfrm, text = "Destination").grid(column = 0, row = 0, padx = NARROWPAD, pady = NARROWPAD, sticky = STATICSTICKY)
routingtablecontlbl = tk.Label(routetblfrm, text = "Gateway").grid(column = 1, row = 0, padx = NARROWPAD, pady = NARROWPAD, sticky = STATICSTICKY)
routingtablecontlbl = tk.Label(routetblfrm, text = "Genmask").grid(column = 2, row = 0, padx = NARROWPAD, pady = NARROWPAD, sticky = STATICSTICKY)
routingtablecontlbl = tk.Label(routetblfrm, text = "Flags").grid(column = 3, row = 0, padx = NARROWPAD, pady = NARROWPAD, sticky = STATICSTICKY)
routingtablecontlbl = tk.Label(routetblfrm, text = "MSS").grid(column = 4, row = 0, padx = NARROWPAD, pady = NARROWPAD, sticky = STATICSTICKY)
routingtablecontlbl = tk.Label(routetblfrm, text = "Window").grid(column = 5, row = 0, padx = NARROWPAD, pady = NARROWPAD, sticky = STATICSTICKY)
routingtablecontlbl = tk.Label(routetblfrm, text = "irtt").grid(column = 6, row = 0, padx = NARROWPAD, pady = NARROWPAD, sticky = STATICSTICKY)
routingtablecontlbl = tk.Label(routetblfrm, text = "Iface").grid(column = 7, row = 0, padx = NARROWPAD, pady = NARROWPAD, sticky = STATICSTICKY)
count = 0
rowcount = 1
for x in introutetable:
	if count == 8:
		count = 0
		rowcount = rowcount + 1
		routingtablecontlbl = tk.Label(routetblfrm, text = x).grid(column = count, row = rowcount, padx = NARROWPAD, pady = NARROWPAD, sticky = STATICSTICKY)
		count = count + 1
	elif count < 8:
		routingtablecontlbl = tk.Label(routetblfrm, text = x).grid(column = count, row = rowcount, padx = NARROWPAD, pady = NARROWPAD, sticky = STATICSTICKY)
		count = count + 1

#aboutTab Layout
abouttabttlfrm = tk.LabelFrame(abouttab, text = LSTNAME).grid(column = 0, row = 0, padx = DEFPADX, pady = DEFPADY, sticky=STATICFULLFRMSTICKY, columnspan=3)
aboutauthorlbl = ttk.Label(abouttabttlfrm, text ="Written By:").grid(column = 0, row = 1, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
aboutauthor = ttk.Label(abouttabttlfrm, text = LSTAUTHOR).grid(column = 1, row = 1, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
aboutcontactlbl = ttk.Label(abouttabttlfrm, text ="Contact:").grid(column = 0, row = 2, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
aboutcontact = ttk.Label(abouttabttlfrm, text = LSTCONTACT).grid(column = 1, row = 2, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
aboutgithubrepolbl = ttk.Label(abouttabttlfrm, text ="GitHub Repository:").grid(column = 0, row = 3, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
aboutgithubrepo = ttk.Label(abouttabttlfrm, text = LSTGITHUBREPO).grid(column = 1, row = 3, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
aboutgitlbl = ttk.Label(abouttabttlfrm, text ="Git Link:").grid(column = 0, row = 4, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
aboutgithubgit = ttk.Label(abouttabttlfrm, text = LSTGITHUB).grid(column = 1, row = 4, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)

"""Run System"""
root.config(menu=menubar)
root.mainloop()
