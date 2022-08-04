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
import tkinter as tk
import logging
import subprocess

from tkinter import ttk
from re import search

LSTLOGGER = logging.getLogger(__name__) 
LSTLOGGER.setLevel(logging.DEBUG)
LSTLOGGERFMT = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
LSTLOGHANDLER = logging.FileHandler('LinuxSystemToolbox.log')
LSTLOGHANDLER.setFormatter(LSTLOGGERFMT)
LSTLOGGER.addHandler(LSTLOGHANDLER)
LSTLOGGERSTRM = logging.StreamHandler()
LSTLOGGERSTRM.setFormatter(LSTLOGGERFMT)
LSTLOGGER.addHandler(LSTLOGGERSTRM)
LSTLOGGER.debug("Starting LST...")
try:
    INTLIST = subprocess.Popen("ifconfig -s -a | tail -n +2 | awk '{print$1}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
except Exception as e:
    LSTLOGGER.error("Unable to retrieve interface list.", e)
INTLIST = INTLIST.split()
root = tk.Tk()

class GlobalVars(object):
    LSTVER = "0.1b"                                                                         #Sytem Version number
    LSTNAME = "Linux System Toolbox"                                                        #Application Name
    LSTFULLNAME = (LSTNAME + " " + LSTVER)
    LSTAUTHOR = "Lothar TheQuiet"                                                           #Application Author
    LSTCONTACT = "lotharthequiet@gmail.com"                                                 #Application Author Contact
    LSTGITHUBREPO = "https://github.com/lotharthequiet/LinuxSystemToolbox"                  #GitHub Repository
    LSTGITHUB = "https://github.com/lotharthequiet/LinuxSystemToolbox.git"                  #GitHub Direct Link
    DEFPADX = 10                                                                            #Static X Padding Value
    DEFPADY = 5                                                                             #Static Y Padding Value
    NARROWPAD = 5                                                                           #Static Narrow Pad Value
    BTNSIZE = 12                                                                            #Static button size value
    STATICSTICKY = "W"                                                                        #Static sticky direction
    STATICFULLFRMSTICKY = "NSEW"                                                              #Static full sticky for label frames
    CURRENTINT = ""
    CURRENTINTSTAT = ""
    Currentdns = tk.StringVar()
    Currentmacaddr = tk.StringVar()

class App():
    root.title(GlobalVars.LSTFULLNAME)
    def __init__(self):
        root.geometry("590x675")
        LSTnb = ttk.Notebook(root)
        menubar = tk.Menu(LSTnb)
        menubar = tk.Menu(LSTnb)
        filemenu = tk.Menu(menubar, tearoff=0)                                     
        filemenu.add_command(label="Reports", command=self.runreports)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.exitapp)
        menubar.add_cascade(label="File", menu=filemenu)
        toolsmenu = tk.Menu(menubar, tearoff=0)                                    
        toolsmenu.add_command(label="Open Toolbox", command=self.opennettoolbox)
        toolsmenu.add_separator()
        toolsmenu.add_command(label="Switch User", command=self.switchuser)
        toolsmenu.add_command(label="Logout", command=self.logout)
        toolsmenu.add_command(label="Restart", command=self.restart)
        toolsmenu.add_command(label="Shutdown", command=self.shutdown)
        menubar.add_cascade(label="Tools", menu=toolsmenu)
        helpmenu = tk.Menu(menubar, tearoff=0)                                     
        helpmenu.add_command(label="Help", command=self.openhelp)
        helpmenu.add_separator()
        helpmenu.add_command(label="About", command=self.openabout)
        menubar.add_cascade(label="Help", menu=helpmenu)
        proctab = tk.Frame(LSTnb)
        servicestab = tk.Frame(LSTnb)
        userstab = tk.Frame(LSTnb)
        nettab = tk.Frame(LSTnb)
        perftab = tk.Frame(LSTnb)
        wrlsstab = tk.Frame(LSTnb)
        LSTnb.add(proctab, text ='Processes')
        LSTnb.add(servicestab, text ='Services')
        LSTnb.add(userstab, text ='Users')
        LSTnb.add(nettab, text ='Networking')
        LSTnb.add(perftab, text ='Performance')
        LSTnb.add(wrlsstab, text = 'Wireless')
        LSTnb.pack(expand = 1, fill ="both")

        proctabttlfrm = tk.LabelFrame(proctab, text="Running Processes:")
        proctabttlfrm.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICFULLFRMSTICKY, columnspan=2)
        proctabttllbl = tk.Label(proctabttlfrm, text="Test Label")
        proctabttllbl.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICSTICKY)
        proctabbtnfrm = tk.Frame(proctab)
        proctabbtnfrm.grid(column = 2, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        killprocbtn = tk.Button(proctabbtnfrm, text="Kill Process", width = GlobalVars.BTNSIZE)
        killprocbtn.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
        spawnprocbtn = tk.Button(proctabbtnfrm, text="Spawn Process", width = GlobalVars.BTNSIZE)
        spawnprocbtn.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')

        svcstabttlfrm = tk.LabelFrame(servicestab, text="System Services:")
        svcstabttlfrm.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICFULLFRMSTICKY, columnspan=2)
        svcstabttllbl = tk.Label(svcstabttlfrm, text="Test Label")
        svcstabttllbl.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICSTICKY)
        svcstabbtnfrm = tk.Frame(servicestab)
        svcstabbtnfrm.grid(column = 2, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        enablesvcbtn = tk.Button(svcstabbtnfrm, text="Enable Service", width = GlobalVars.BTNSIZE)
        enablesvcbtn.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
        disablesvcbtn = tk.Button(svcstabbtnfrm, text="Disable Service", width = GlobalVars.BTNSIZE)
        disablesvcbtn.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
        startsvcbtn = tk.Button(svcstabbtnfrm, text="Start Service", width = GlobalVars.BTNSIZE)
        startsvcbtn.grid(column = 0, row = 2, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
        stopsvcbtn = tk.Button(svcstabbtnfrm, text="Stop Service", width = GlobalVars.BTNSIZE)
        stopsvcbtn.grid(column = 0, row = 3, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')

        usrtabttlfrm = tk.LabelFrame(userstab, text="Logged In Users:")
        usrtabttlfrm.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICFULLFRMSTICKY, columnspan=2)
        usrtabttllbl = tk.Label(usrtabttlfrm, text="Test Label")
        usrtabttllbl.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICSTICKY)
        usrtabttlfrm = tk.LabelFrame(userstab, text="Local Users:")
        usrtabttlfrm.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICFULLFRMSTICKY, columnspan=2)
        usrtabttllbl = tk.Label(usrtabttlfrm, text="Test Label")
        usrtabttllbl.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICSTICKY)
        usrtabbtnfrm = tk.Frame(userstab)
        usrtabbtnfrm.grid(column = 2, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        newuserbtn = tk.Button(usrtabbtnfrm, text="New User", width = GlobalVars.BTNSIZE)
        newuserbtn.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')

        nettabcontfrm = tk.Frame(nettab)
        nettabcontfrm.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICSTICKY)
        nettabbtnfrm = tk.Frame(nettab)
        nettabbtnfrm.grid(column = 1, row = 0, padx = 0, pady = (10, 5), sticky='N')
        intstatsfrm = tk.LabelFrame(nettab, text="Interface Statistics:")
        intstatsfrm.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICFULLFRMSTICKY, columnspan = 2)
        routetblfrm = tk.LabelFrame(nettab, text="Routing Table:")
        routetblfrm.grid(column = 0, row = 2, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICFULLFRMSTICKY, columnspan = 2)
        self.disableintbtn = tk.Button(nettabbtnfrm, text ="Disable", width = GlobalVars.BTNSIZE, command=self.toggleinterface)
        self.disableintbtn.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
        dhcpreleasebtn = tk.Button(nettabbtnfrm, text ="DHCP Release", width = GlobalVars.BTNSIZE, command=self.dhcprelease)
        dhcpreleasebtn.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
        dhcprenewbtn = tk.Button(nettabbtnfrm, text ="DHCP Renew", width = GlobalVars.BTNSIZE, command=self.dhcprenew)
        dhcprenewbtn.grid(column = 0, row = 2, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
        nettoolboxbtn = tk.Button(nettabbtnfrm, text ="Toolbox", width = GlobalVars.BTNSIZE, command=self.opennettoolbox)
        nettoolboxbtn.grid(column = 0, row = 3, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
        selintname = tk.StringVar()
        intlbl = tk.Label(nettabcontfrm, text ="Select Interface:")
        intlbl.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICSTICKY)
        self.intcombo = ttk.Combobox(nettabcontfrm, values = INTLIST)
        self.intcombo.grid(column = 1, row = 0, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICSTICKY)
        self.intcombo.set("Select Interface:")
        self.intcombo.bind('<<ComboboxSelected>>', lambda event: self.selectinterface())
        intstatuslbl = tk.Label(nettabcontfrm, text="Interface Status:")
        intstatuslbl.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        intstatus = tk.Label(nettabcontfrm, text = GlobalVars.CURRENTINTSTAT)
        intstatus.grid(column = 1, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        macaddrlbl = tk.Label(nettabcontfrm, text="Mac Address:")
        macaddrlbl.grid(column = 0, row = 2, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        macaddr = tk.Label(nettabcontfrm, textvariable=GlobalVars.Currentmacaddr, width = 18)
        macaddr.grid(column = 1, row = 2, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        mtulbl = tk.Label(nettabcontfrm, text ="MTU:")
        mtulbl.grid(column = 0, row = 3, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        mtu = tk.Label(nettabcontfrm, text = "", width = 5)
        mtu.grid(column = 1, row = 3, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        ipaddrlbl = tk.Label(nettabcontfrm, text="IP Address:")
        ipaddrlbl.grid(column = 0, row = 4, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        ipaddr = tk.Label(nettabcontfrm, text="", width = 16)
        ipaddr.grid(column = 1, row = 4, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        submasklbl = tk.Label(nettabcontfrm, text="Subnet Mask:")
        submasklbl.grid(column = 0, row = 5, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        submask = tk.Label(nettabcontfrm, text="", width = 16)
        submask.grid(column = 1, row = 5, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        defgwlbl = tk.Label(nettabcontfrm, text="Default Gateway:")
        defgwlbl.grid(column = 0, row = 6, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        defgw = tk.Label(nettabcontfrm, text="", width = 18)
        defgw.grid(column = 1, row = 6, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        bcastaddrlbl = tk.Label(nettabcontfrm, text="Broadcast Address:")
        bcastaddrlbl.grid(column = 0, row = 7, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        bcastaddr = tk.Label(nettabcontfrm, text="", width = 18)
        bcastaddr.grid(column = 1, row = 7, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        dnsserverslbl = tk.Label(nettabcontfrm, text="DNS Servers:")
        dnsserverslbl.grid(column = 0, row = 8, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        dnsserveraddr = tk.Label(nettabcontfrm, textvariable=GlobalVars.Currentdns).grid(column = 1, row = 8, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        dnshostnamelbl = tk.Label(nettabcontfrm, text="DNS Hostname:")
        dnshostnamelbl.grid(column = 0, row = 9, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        dnshostname = tk.Label(nettabcontfrm, text="", width = 25)
        dnshostname.grid(column = 1, row = 9, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        dnsdomainlbl = tk.Label(nettabcontfrm, text="DNS Domain:")
        dnsdomainlbl.grid(column = 0, row = 10, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        dnsdomain = tk.Label(nettabcontfrm, text="", width = 25)
        dnsdomain.grid(column = 1, row = 10, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        rxpacketlbl = tk.Label(intstatsfrm, text="RX packets")
        rxpacketlbl.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
        rxpacketcntlbl = tk.Label(intstatsfrm, text="")
        rxpacketcntlbl.grid(column = 1, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
        rxpacketbyteslbl = tk.Label(intstatsfrm, text="bytes")
        rxpacketbyteslbl.grid(column = 2, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
        rxpacketbytescntlbl = tk.Label(intstatsfrm, text="")
        rxpacketbytescntlbl.grid(column = 3, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
        rxpacketbyteshumancntlbl = tk.Label(intstatsfrm, text="")
        rxpacketbyteshumancntlbl.grid(column = 3, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
        rxerrorslbl = tk.Label(intstatsfrm, text="RX errors")
        rxerrorslbl.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
        rxerrorscntlbl = tk.Label(intstatsfrm, text="")
        rxerrorscntlbl.grid(column = 1, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
        rxdroppedlbl = tk.Label(intstatsfrm, text="dropped")
        rxdroppedlbl.grid(column = 2, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
        rxdroppedcntlbl = tk.Label(intstatsfrm, text="")
        rxdroppedcntlbl.grid(column = 3, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
        rxoverrunslbl = tk.Label(intstatsfrm, text="overruns")
        rxoverrunslbl.grid(column = 4, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
        rxoverrunscntlbl = tk.Label(intstatsfrm, text="")
        rxoverrunscntlbl.grid(column = 5, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
        rxframelbl = tk.Label(intstatsfrm, text="frame")
        rxframelbl.grid(column = 6, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
        rxframecntlbl = tk.Label(intstatsfrm, text="")
        rxframecntlbl.grid(column = 7, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
        txpacketlbl = tk.Label(intstatsfrm, text="TX packets")
        txpacketlbl.grid(column = 0, row = 2, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
        txpacketcntlbl = tk.Label(intstatsfrm, text="")
        txpacketcntlbl.grid(column = 1, row = 2, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
        txpacketbyteslbl = tk.Label(intstatsfrm, text="bytes")
        txpacketbyteslbl.grid(column = 2, row = 2, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
        txpacketbytescntlbl = tk.Label(intstatsfrm, text="")
        txpacketbytescntlbl.grid(column = 3, row = 2, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
        txpacketbyteshumcntlbl = tk.Label(intstatsfrm, text="")
        txpacketbyteshumcntlbl.grid(column = 3, row = 2, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
        txerrorslbl = tk.Label(intstatsfrm, text="TX errors")
        txerrorslbl.grid(column = 0, row = 3, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
        txerrorscntlbl = tk.Label(intstatsfrm, text="")
        txerrorscntlbl.grid(column = 1, row = 3, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
        txdroppedlbl = tk.Label(intstatsfrm, text="dropped")
        txdroppedlbl.grid(column = 2, row = 3, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
        txdroppedcntlbl = tk.Label(intstatsfrm, text="")
        txdroppedcntlbl.grid(column = 3, row = 3, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
        txoverrunslbl = tk.Label(intstatsfrm, text="overruns")
        txoverrunslbl.grid(column = 4, row = 3, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
        txoverrunscntlbl = tk.Label(intstatsfrm, text="")
        txoverrunscntlbl.grid(column = 5, row = 3, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
        txfrmlbl = tk.Label(intstatsfrm, text="carrier")
        txfrmlbl.grid(column = 6, row = 3, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
        txfrmcntlbl = tk.Label(intstatsfrm, text="")
        txfrmcntlbl.grid(column = 7, row = 3, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
        txcolslbl = tk.Label(intstatsfrm, text="collisions")
        txcolslbl.grid(column = 8, row = 3, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
        txcolscntlbl = tk.Label(intstatsfrm, text="")
        txcolscntlbl.grid(column = 9, row = 3, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
        routetablecontlbl = tk.Label(routetblfrm, text = "Destination")
        routetablecontlbl.grid(column = 0, row = 0, padx = GlobalVars.NARROWPAD, pady = GlobalVars.NARROWPAD, sticky = GlobalVars.STATICSTICKY)
        routetablecontlbl2 = tk.Label(routetblfrm, text = "Gateway")
        routetablecontlbl2.grid(column = 1, row = 0, padx = GlobalVars.NARROWPAD, pady = GlobalVars.NARROWPAD, sticky = GlobalVars.STATICSTICKY)
        routetablecontlbl3 = tk.Label(routetblfrm, text = "Genmask")
        routetablecontlbl3.grid(column = 2, row = 0, padx = GlobalVars.NARROWPAD, pady = GlobalVars.NARROWPAD, sticky = GlobalVars.STATICSTICKY)
        routetablecontlbl4 = tk.Label(routetblfrm, text = "Flags")
        routetablecontlbl4.grid(column = 3, row = 0, padx = GlobalVars.NARROWPAD, pady = GlobalVars.NARROWPAD, sticky = GlobalVars.STATICSTICKY)
        routetablecontlbl5 = tk.Label(routetblfrm, text = "MSS")
        routetablecontlbl5.grid(column = 4, row = 0, padx = GlobalVars.NARROWPAD, pady = GlobalVars.NARROWPAD, sticky = GlobalVars.STATICSTICKY)
        routetablecontlbl6 = tk.Label(routetblfrm, text = "Window")
        routetablecontlbl6.grid(column = 5, row = 0, padx = GlobalVars.NARROWPAD, pady = GlobalVars.NARROWPAD, sticky = GlobalVars.STATICSTICKY)
        routetablecontlbl7 = tk.Label(routetblfrm, text = "irtt")
        routetablecontlbl7.grid(column = 6, row = 0, padx = GlobalVars.NARROWPAD, pady = GlobalVars.NARROWPAD, sticky = GlobalVars.STATICSTICKY)
        routetablecontlbl8 = tk.Label(routetblfrm, text = "Iface")
        routetablecontlbl8.grid(column = 7, row = 0, padx = GlobalVars.NARROWPAD, pady = GlobalVars.NARROWPAD, sticky = GlobalVars.STATICSTICKY)

        perftabttlfrm = tk.LabelFrame(perftab, text="CPU Usage")
        perftabttlfrm.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICFULLFRMSTICKY, columnspan=2)
        perftabttllbl = tk.Label(perftabttlfrm, text="Test Label")
        perftabttllbl.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICSTICKY)
        perftabttlfrm = tk.LabelFrame(perftab, text="Memory")
        perftabttlfrm.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICFULLFRMSTICKY, columnspan=2)
        perftabttllbl = tk.Label(perftabttlfrm, text="Test Label")
        perftabttllbl.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICSTICKY)
        perftabbtnfrm = tk.Frame(perftab)
        perftabbtnfrm.grid(column = 2, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        perftabbtn = tk.Button(perftabbtnfrm, text="New User", width = GlobalVars.BTNSIZE)
        perftabbtn.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')

        wrlsstabttlfrm = tk.LabelFrame(wrlsstab, text="Connection Status:")
        wrlsstabttlfrm.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICFULLFRMSTICKY, columnspan=2)
        wrlsstabttllbl = tk.Label(wrlsstabttlfrm, text="Test Label")
        wrlsstabttllbl.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICSTICKY)
        wrlsstabttlfrm = tk.LabelFrame(wrlsstab, text="Available Networks:")
        wrlsstabttlfrm.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICFULLFRMSTICKY, columnspan=2)
        wrlsstabttllbl = tk.Label(wrlsstabttlfrm, text="Test Label")
        wrlsstabttllbl.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICSTICKY)
        wrlsstabbtnfrm = tk.Frame(wrlsstab)
        wrlsstabbtnfrm.grid(column = 2, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        rfwrlssbtn = tk.Button(wrlsstabbtnfrm, text="Refresh", width = GlobalVars.BTNSIZE)
        rfwrlssbtn.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')

        root.config(menu=menubar)

    def runreports(self):
        LSTLOGGER.debug("Open System Reports Window.")
        reportwindow = tk.Toplevel(self.root)
        reportwindow.title(GlobalVars.LSTFULLNAME)
        reportwinttlfrm = tk.LabelFrame(reportwindow, text = "System Reports")
        reportwinttlfrm.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICFULLFRMSTICKY, columnspan=3)
        reportauthorlbl = tk.Label(reportwinttlfrm, text ="Written By:")
        reportauthorlbl.grid(column= 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICFULLFRMSTICKY)

    def exitapp(self):
        LSTLOGGER.debug("Exiting LST.")
        self.quit()

    def opennettoolbox(self):
        LSTLOGGER.debug("Open Network Toolbox Window.")
        toolboxwindow = tk.Toplevel(self.root)
        toolboxwindow.title(GlobalVars.LSTFULLNAME)
        toolboxwinttlfrm = tk.LabelFrame(toolboxwindow, text = "Network Toolbox")
        toolboxwinttlfrm.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICFULLFRMSTICKY, columnspan=3)
        toolboxlbl = tk.Label(toolboxwinttlfrm, text ="Written By:")
        toolboxlbl.grid(column= 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICFULLFRMSTICKY)

    def switchuser(self):
        LSTLOGGER.debug("Switch User.")

    def logout(self):
        LSTLOGGER.debug("Logout.")

    def restart(self):
        LSTLOGGER.debug("Restart.")

    def shutdown(self):
        LSTLOGGER.debug("Shutdown.")

    def openhelp(self):
        LSTLOGGER.debug("Open Help Window.")
        helpwindow = tk.Toplevel(self.root)
        helpwindow.title(GlobalVars.LSTFULLNAME)
        helpwinttlfrm = tk.LabelFrame(helpwindow, text = "Help")
        helpwinttlfrm.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICFULLFRMSTICKY)
        helpauthorlbl = tk.Label(helpwinttlfrm, text ="Written By:")
        helpauthorlbl.grid(column= 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICFULLFRMSTICKY)

    def openabout(self):
        LSTLOGGER.debug(GlobalVars.LSTFULLNAME)
        aboutwindow = tk.Toplevel(self.root)
        aboutwindow.title(GlobalVars.LSTFULLNAME)
        aboutwinttlfrm = tk.LabelFrame(aboutwindow, text = "About")
        aboutwinttlfrm.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICFULLFRMSTICKY)
        aboutauthorlbl = tk.Label(aboutwinttlfrm, text ="Written By:")
        aboutauthorlbl.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        aboutauthor = tk.Label(aboutwinttlfrm, text = GlobalVars.LSTAUTHOR)
        aboutauthor.grid(column = 1, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        aboutcontactlbl = tk.Label(aboutwinttlfrm, text ="Contact:")
        aboutcontactlbl.grid(column = 0, row = 2, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        aboutcontact = tk.Label(aboutwinttlfrm, text = GlobalVars.LSTCONTACT)
        aboutcontact.grid(column = 1, row = 2, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        aboutgithubrepolbl = tk.Label(aboutwinttlfrm, text ="GitHub Repository:")
        aboutgithubrepolbl.grid(column = 0, row = 3, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        aboutgithubrepo = tk.Label(aboutwinttlfrm, text = GlobalVars.LSTGITHUBREPO)
        aboutgithubrepo.grid(column = 1, row = 3, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        aboutgitlbl = tk.Label(aboutwinttlfrm, text ="Git Link:")
        aboutgitlbl.grid(column = 0, row = 4, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        aboutgithubgit = tk.Label(aboutwinttlfrm, text = GlobalVars.LSTGITHUB)
        aboutgithubgit.grid(column = 1, row = 4, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        aboutverlbl = tk.Label(aboutwinttlfrm, text = "Version:")
        aboutverlbl.grid(column = 0, row = 5, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        aboutver = tk.Label(aboutwinttlfrm, text = GlobalVars.LSTVER)
        aboutver.grid(column = 1, row = 5, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)

    def toggleinterface(self):
        LSTLOGGER.debug("Toggle Interface")
        LSTLOGGER.debug(GlobalVars.CURRENTINTSTAT)
        if GlobalVars.CURRENTINTSTAT == "UP":
            try:
                subprocess.Popen("sudo ifconfig ", GlobalVars.CURRENTINT, " down", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
                LSTLOGGER.debug("")
            except Exception as e:
                LSTLOGGER.error("Unable to disable interface: ", GlobalVars.CURRENTINT, e)
        else:
            try:
                subprocess.Popen("sudo ifconfig ", GlobalVars.CURRENTINT, " up", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
            except Exception as e:
                LSTLOGGER.error("Unable to enable interface: ", GlobalVars.CURRENTINT, e)

    def dhcprelease(self):
        LSTLOGGER.debug("DHCP Release")

    def dhcprenew(self):
        LSTLOGGER.debug("DHCP Renew")

    def selectinterface(self):
        LSTLOGGER.debug("Select Interface Function.")
        LSTLOGGER.debug(self.intcombo.get())
        CURRENTINT = self.intcombo.get()
        try:
            intstatus = subprocess.Popen("ip a sh dev " + CURRENTINT + " | head -n 1 | awk {'print$9'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        except Exception as e: 
            LSTLOGGER.error("Unable to retrieve current interface status. ", e)
        LSTLOGGER.debug(intstatus)
        intstatstr = "UP"
        if search(intstatstr, intstatus):
            LSTLOGGER.info("Interface UP")
            self.disableintbtn.config(text="Disable")
            self.disableintbtn.config(state="normal")
            GlobalVars.CURRENTINTSTAT == "UP"
        else:
            if search("DOWN", intstatus):
                LSTLOGGER.info("Interface DOWN")
                self.disableintbtn.config(text="Enable")
                self.disableintbtn.config(state="normal")    
                GlobalVars.CURRENTINTSTAT == "DOWN"
            else:
                if CURRENTINT == "lo":
                    self.disableintbtn.config(text="Disable")
                    self.disableintbtn.config(state="disabled")
                else:
                    self.disableintbtn.config(text="Disable")
                    self.disableintbtn.config(state="normal")

        #Get add info
        GlobalVars.Currentmacaddr.set = subprocess.Popen("ifconfig " + CURRENTINT + " | grep ether | awk '{print$2}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        intmtu = subprocess.Popen("ifconfig " + CURRENTINT + " | head -n +1 | awk '{print$4}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        intipaddress = subprocess.Popen("ifconfig " + CURRENTINT + " | grep inet | head -n +1 | awk '{print$2}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        intsubnetmask = subprocess.Popen("ifconfig " + CURRENTINT + " | grep inet | head -n +1 | awk '{print$4}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        intdefaultgw = subprocess.Popen("netstat -r | tail -n +3 | awk '{print$2}' | head -n +1", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        intbroadcastaddress = subprocess.Popen("ifconfig " + CURRENTINT + " | grep inet | head -n +1 | awk '{print$6}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        self.getdnsservers()
        inthostname = subprocess.Popen("hostname", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        intdnsdomainname = subprocess.Popen("cat /etc/resolv.conf | tail -n +2 | awk '{print$2}' | head -n +1", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        #Get int stats
        rxpacketcount = subprocess.Popen("ifconfig " + CURRENTINT + " | grep 'RX packets' | awk {'print$3'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        rxpacketbytecount = subprocess.Popen("ifconfig " + CURRENTINT + " | grep 'RX packets' | awk {'print$5'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        rxpackethumansize = subprocess.Popen("ifconfig " + CURRENTINT + " | grep 'RX packets' | awk {'print$6'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        rxerrorcount = subprocess.Popen("ifconfig " + CURRENTINT + " | grep 'RX Errors' | awk {'print$3'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        rxdroppedcount = subprocess.Popen("ifconfig " + CURRENTINT + " | grep 'RX Errors' | awk {'print$5'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        rxoverrunscount = subprocess.Popen("ifconfig " + CURRENTINT + " | grep 'RX Errors' | awk {'print$7'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        rxframecount = subprocess.Popen("ifconfig " + CURRENTINT + " | grep 'RX Errors' | awk {'print$9'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        txpacketcount = subprocess.Popen("ifconfig " + CURRENTINT + " | grep 'TX packets' | awk {'print$3'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        txpacketbytecount = subprocess.Popen("ifconfig " + CURRENTINT + " | grep 'TX packets' | awk {'print$5'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        txpackethumansize = subprocess.Popen("ifconfig " + CURRENTINT + " | grep 'TX packets' | awk {'print$6'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        txerrorcount = subprocess.Popen("ifconfig " + CURRENTINT + " | grep 'TX errors' | awk {'print$3'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        txdroppedcount = subprocess.Popen("ifconfig " + CURRENTINT + " | grep 'TX errors' | awk {'print$5'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        txoverrunscount = subprocess.Popen("ifconfig " + CURRENTINT + " | grep 'TX errors' | awk {'print$7'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        txcarrier = subprocess.Popen("ifconfig " + CURRENTINT + " | grep 'TX errors' | awk {'print$9'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        txcollisions = subprocess.Popen("ifconfig " + CURRENTINT + " | grep 'TX errors' | awk {'print$11'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        LSTLOGGER.debug(CURRENTINT)
        LSTLOGGER.debug(GlobalVars.CURRENTINTSTAT)
        LSTLOGGER.debug(GlobalVars.Currentmacaddr)
        LSTLOGGER.debug(intmtu)
        LSTLOGGER.debug(intipaddress)
        LSTLOGGER.debug(intsubnetmask)
        LSTLOGGER.debug(intdefaultgw)
        LSTLOGGER.debug(intbroadcastaddress)
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

    def getdnsservers(self):
        LSTLOGGER.debug("getdnsservers function.")
        GlobalVars.Currentdns.set = subprocess.Popen("cat /etc/resolv.conf | tail -n +3 | awk '{print$2}'| head -n +1", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        LSTLOGGER.debug(GlobalVars.Currentdns)
    
    def getroutetable(self):
        LSTLOGGER.debug("Get route table.")
        try:
            introutetable = subprocess.Popen("netstat -r | tail -n +3", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        except Exception as e:
            LSTLOGGER.error("Unable to retrieve route table.", e)
        introutetable = introutetable.split()
        count = 0
        rowcount = 1
        for x in introutetable:
            if count == 8:
                count = 0
                rowcount = rowcount + 1
                routetablecontentry = tk.Label(self.routetblfrm, text = x).grid(column = count, row = rowcount, padx = GlobalVars.NARROWPAD, pady = GlobalVars.NARROWPAD, sticky = GlobalVars.STATICSTICKY)
                count = count + 1
            elif count < 8:
                routetablecontentry = tk.Label(self.routetblfrm, text = x).grid(column = count, row = rowcount, padx = GlobalVars.NARROWPAD, pady = GlobalVars.NARROWPAD, sticky = GlobalVars.STATICSTICKY)
                count = count + 1
                    
app=App()
root.mainloop()