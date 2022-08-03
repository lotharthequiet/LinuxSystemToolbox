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

"""Define System Variables"""
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
CURRENTINT = ""
CURRENTINTSTAT = ""


class App():
    root = tk.Tk()
    root.title(LSTFULLNAME)
    def __init__(self):
        currentdns = tk.StringVar()
        
        App.root.geometry("590x675")
        LSTnb = ttk.Notebook(App.root)
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
        proctabttlfrm.grid(column = 0, row = 0, padx = DEFPADX, pady = (10, 5), sticky=STATICFULLFRMSTICKY, columnspan=2)
        proctabttllbl = tk.Label(proctabttlfrm, text="Test Label")
        proctabttllbl.grid(column = 0, row = 0, padx = DEFPADX, pady = (10, 5), sticky=STATICSTICKY)
        proctabbtnfrm = tk.Frame(proctab)
        proctabbtnfrm.grid(column = 2, row = 0, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
        killprocbtn = tk.Button(proctabbtnfrm, text="Kill Process", width = BTNSIZE)
        killprocbtn.grid(column = 0, row = 0, padx = DEFPADX, pady = DEFPADY, sticky='N')
        spawnprocbtn = tk.Button(proctabbtnfrm, text="Spawn Process", width = BTNSIZE)
        spawnprocbtn.grid(column = 0, row = 1, padx = DEFPADX, pady = DEFPADY, sticky='N')

        svcstabttlfrm = tk.LabelFrame(servicestab, text="System Services:")
        svcstabttlfrm.grid(column = 0, row = 0, padx = DEFPADX, pady = (10, 5), sticky=STATICFULLFRMSTICKY, columnspan=2)
        svcstabttllbl = tk.Label(svcstabttlfrm, text="Test Label")
        svcstabttllbl.grid(column = 0, row = 0, padx = DEFPADX, pady = (10, 5), sticky=STATICSTICKY)
        svcstabbtnfrm = tk.Frame(servicestab)
        svcstabbtnfrm.grid(column = 2, row = 0, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
        enablesvcbtn = tk.Button(svcstabbtnfrm, text="Enable Service", width = BTNSIZE)
        enablesvcbtn.grid(column = 0, row = 0, padx = DEFPADX, pady = DEFPADY, sticky='N')
        disablesvcbtn = tk.Button(svcstabbtnfrm, text="Disable Service", width = BTNSIZE)
        disablesvcbtn.grid(column = 0, row = 1, padx = DEFPADX, pady = DEFPADY, sticky='N')
        startsvcbtn = tk.Button(svcstabbtnfrm, text="Start Service", width = BTNSIZE)
        startsvcbtn.grid(column = 0, row = 2, padx = DEFPADX, pady = DEFPADY, sticky='N')
        stopsvcbtn = tk.Button(svcstabbtnfrm, text="Stop Service", width = BTNSIZE)
        stopsvcbtn.grid(column = 0, row = 3, padx = DEFPADX, pady = DEFPADY, sticky='N')

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
        newuserbtn = tk.Button(usrtabbtnfrm, text="New User", width = BTNSIZE)
        newuserbtn.grid(column = 0, row = 0, padx = DEFPADX, pady = DEFPADY, sticky='N')

        nettabcontfrm = tk.Frame(nettab)
        nettabcontfrm.grid(column = 0, row = 0, padx = DEFPADX, pady = (10, 5), sticky=STATICSTICKY)
        nettabbtnfrm = tk.Frame(nettab)
        nettabbtnfrm.grid(column = 1, row = 0, padx = 0, pady = (10, 5), sticky='N')
        intstatsfrm = tk.LabelFrame(nettab, text="Interface Statistics:")
        intstatsfrm.grid(column = 0, row = 1, padx = DEFPADX, pady = DEFPADY, sticky = STATICFULLFRMSTICKY, columnspan = 2)
        routetblfrm = tk.LabelFrame(nettab, text="Routing Table:")
        routetblfrm.grid(column = 0, row = 2, padx = DEFPADX, pady = DEFPADY, sticky = STATICFULLFRMSTICKY, columnspan = 2)
        self.disableintbtn = tk.Button(nettabbtnfrm, text ="Disable", width = BTNSIZE, command=self.toggleinterface)
        self.disableintbtn.grid(column = 0, row = 0, padx = DEFPADX, pady = DEFPADY, sticky='N')
        dhcpreleasebtn = tk.Button(nettabbtnfrm, text ="DHCP Release", width = BTNSIZE, command=self.dhcprelease)
        dhcpreleasebtn.grid(column = 0, row = 1, padx = DEFPADX, pady = DEFPADY, sticky='N')
        dhcprenewbtn = tk.Button(nettabbtnfrm, text ="DHCP Renew", width = BTNSIZE, command=self.dhcprenew)
        dhcprenewbtn.grid(column = 0, row = 2, padx = DEFPADX, pady = DEFPADY, sticky='N')
        nettoolboxbtn = tk.Button(nettabbtnfrm, text ="Toolbox", width = BTNSIZE, command=self.opennettoolbox)
        nettoolboxbtn.grid(column = 0, row = 3, padx = DEFPADX, pady = DEFPADY, sticky='N')
        selintname = tk.StringVar()
        intlbl = tk.Label(nettabcontfrm, text ="Select Interface:")
        intlbl.grid(column = 0, row = 0, padx = DEFPADX, pady = (10, 5), sticky=STATICSTICKY)
        self.intcombo = ttk.Combobox(nettabcontfrm, values = INTLIST)
        self.intcombo.grid(column = 1, row = 0, padx = DEFPADX, pady = (10, 5), sticky=STATICSTICKY)
        self.intcombo.set("Select Interface:")
        self.intcombo.bind('<<ComboboxSelected>>', lambda event: self.selectinterface())
        intstatuslbl = tk.Label(nettabcontfrm, text="Interface Status:")
        intstatuslbl.grid(column = 0, row = 1, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
        intstatus = tk.Label(nettabcontfrm, text = CURRENTINTSTAT)
        intstatus.grid(column = 1, row = 1, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
        macaddrlbl = tk.Label(nettabcontfrm, text="Mac Address:")
        macaddrlbl.grid(column = 0, row = 2, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
        macaddr = tk.Label(nettabcontfrm, text="", width = 18)
        macaddr.grid(column = 1, row = 2, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
        mtulbl = tk.Label(nettabcontfrm, text ="MTU:")
        mtulbl.grid(column = 0, row = 3, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
        mtu = tk.Label(nettabcontfrm, text = "", width = 5)
        mtu.grid(column = 1, row = 3, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
        ipaddrlbl = tk.Label(nettabcontfrm, text="IP Address:")
        ipaddrlbl.grid(column = 0, row = 4, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
        ipaddr = tk.Label(nettabcontfrm, text="", width = 16)
        ipaddr.grid(column = 1, row = 4, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
        submasklbl = tk.Label(nettabcontfrm, text="Subnet Mask:")
        submasklbl.grid(column = 0, row = 5, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
        submask = tk.Label(nettabcontfrm, text="", width = 16)
        submask.grid(column = 1, row = 5, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
        defgwlbl = tk.Label(nettabcontfrm, text="Default Gateway:")
        defgwlbl.grid(column = 0, row = 6, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
        defgw = tk.Label(nettabcontfrm, text="", width = 18)
        defgw.grid(column = 1, row = 6, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
        bcastaddrlbl = tk.Label(nettabcontfrm, text="Broadcast Address:")
        bcastaddrlbl.grid(column = 0, row = 7, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
        bcastaddr = tk.Label(nettabcontfrm, text="", width = 18)
        bcastaddr.grid(column = 1, row = 7, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
        dnsserverslbl = tk.Label(nettabcontfrm, text="DNS Servers:")
        dnsserverslbl.grid(column = 0, row = 8, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
        dnsserveraddr = tk.Label(nettabcontfrm, textvariable=currentdns).grid(column = 1, row = 8, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
        dnshostnamelbl = tk.Label(nettabcontfrm, text="DNS Hostname:")
        dnshostnamelbl.grid(column = 0, row = 9, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
        dnshostname = tk.Label(nettabcontfrm, text="", width = 25)
        dnshostname.grid(column = 1, row = 9, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
        dnsdomainlbl = tk.Label(nettabcontfrm, text="DNS Domain:")
        dnsdomainlbl.grid(column = 0, row = 10, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
        dnsdomain = tk.Label(nettabcontfrm, text="", width = 25)
        dnsdomain.grid(column = 1, row = 10, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
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

        wrlsstabttlfrm = tk.LabelFrame(wrlsstab, text="Connection Status:")
        wrlsstabttlfrm.grid(column = 0, row = 0, padx = DEFPADX, pady = (10, 5), sticky=STATICFULLFRMSTICKY, columnspan=2)
        wrlsstabttllbl = tk.Label(wrlsstabttlfrm, text="Test Label")
        wrlsstabttllbl.grid(column = 0, row = 0, padx = DEFPADX, pady = (10, 5), sticky=STATICSTICKY)
        wrlsstabttlfrm = tk.LabelFrame(wrlsstab, text="Available Networks:")
        wrlsstabttlfrm.grid(column = 0, row = 1, padx = DEFPADX, pady = (10, 5), sticky=STATICFULLFRMSTICKY, columnspan=2)
        wrlsstabttllbl = tk.Label(wrlsstabttlfrm, text="Test Label")
        wrlsstabttllbl.grid(column = 0, row = 0, padx = DEFPADX, pady = (10, 5), sticky=STATICSTICKY)
        wrlsstabbtnfrm = tk.Frame(wrlsstab)
        wrlsstabbtnfrm.grid(column = 2, row = 0, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
        rfwrlssbtn = tk.Button(wrlsstabbtnfrm, text="New User", width = BTNSIZE)
        rfwrlssbtn.grid(column = 0, row = 0, padx = DEFPADX, pady = DEFPADY, sticky='N')

        App.root.config(menu=menubar)
        App.root.mainloop()

    def runreports(self):
        LSTLOGGER.debug("Open System Reports Window.")
        reportwindow = tk.Toplevel(self.root)
        reportwindow.title(LSTFULLNAME)
        reportwinttlfrm = tk.LabelFrame(reportwindow, text = "System Reports")
        reportwinttlfrm.grid(column = 0, row = 0, padx = DEFPADX, pady = DEFPADY, sticky=STATICFULLFRMSTICKY, columnspan=3)
        reportauthorlbl = tk.Label(reportwinttlfrm, text ="Written By:")
        reportauthorlbl.grid(column= 0, row = 0, padx = DEFPADX, pady = DEFPADY, sticky=STATICFULLFRMSTICKY)

    def exitapp(self):
        LSTLOGGER.debug("Exiting LST.")
        self.quit()

    def opennettoolbox(self):
        LSTLOGGER.debug("Open Network Toolbox Window.")
        toolboxwindow = tk.Toplevel(self.root)
        toolboxwindow.title(LSTFULLNAME)
        toolboxwinttlfrm = tk.LabelFrame(toolboxwindow, text = "Network Toolbox")
        toolboxwinttlfrm.grid(column = 0, row = 0, padx = DEFPADX, pady = DEFPADY, sticky=STATICFULLFRMSTICKY, columnspan=3)
        toolboxlbl = tk.Label(toolboxwinttlfrm, text ="Written By:")
        toolboxlbl.grid(column= 0, row = 0, padx = DEFPADX, pady = DEFPADY, sticky=STATICFULLFRMSTICKY)

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
        helpwindow.title(LSTFULLNAME)
        helpwinttlfrm = tk.LabelFrame(helpwindow, text = "Help")
        helpwinttlfrm.grid(column = 0, row = 0, padx = DEFPADX, pady = DEFPADY, sticky=STATICFULLFRMSTICKY)
        helpauthorlbl = tk.Label(helpwinttlfrm, text ="Written By:")
        helpauthorlbl.grid(column= 0, row = 0, padx = DEFPADX, pady = DEFPADY, sticky=STATICFULLFRMSTICKY)

    def openabout(self):
        LSTLOGGER.debug(LSTFULLNAME)
        aboutwindow = tk.Toplevel(self.root)
        aboutwindow.title(LSTNAME)
        aboutwinttlfrm = tk.LabelFrame(aboutwindow, text = "About")
        aboutwinttlfrm.grid(column = 0, row = 0, padx = DEFPADX, pady = DEFPADY, sticky=STATICFULLFRMSTICKY)
        aboutauthorlbl = tk.Label(aboutwinttlfrm, text ="Written By:")
        aboutauthorlbl.grid(column = 0, row = 1, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
        aboutauthor = tk.Label(aboutwinttlfrm, text = LSTAUTHOR)
        aboutauthor.grid(column = 1, row = 1, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
        aboutcontactlbl = tk.Label(aboutwinttlfrm, text ="Contact:")
        aboutcontactlbl.grid(column = 0, row = 2, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
        aboutcontact = tk.Label(aboutwinttlfrm, text = LSTCONTACT)
        aboutcontact.grid(column = 1, row = 2, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
        aboutgithubrepolbl = tk.Label(aboutwinttlfrm, text ="GitHub Repository:")
        aboutgithubrepolbl.grid(column = 0, row = 3, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
        aboutgithubrepo = tk.Label(aboutwinttlfrm, text = LSTGITHUBREPO)
        aboutgithubrepo.grid(column = 1, row = 3, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
        aboutgitlbl = tk.Label(aboutwinttlfrm, text ="Git Link:")
        aboutgitlbl.grid(column = 0, row = 4, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
        aboutgithubgit = tk.Label(aboutwinttlfrm, text = LSTGITHUB)
        aboutgithubgit.grid(column = 1, row = 4, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
        aboutverlbl = tk.Label(aboutwinttlfrm, text = "Version:")
        aboutverlbl.grid(column = 0, row = 5, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)
        aboutver = tk.Label(aboutwinttlfrm, text = LSTVER)
        aboutver.grid(column = 1, row = 5, padx = DEFPADX, pady = DEFPADY, sticky=STATICSTICKY)

    def toggleinterface(self):
        LSTLOGGER.debug("Toggle Interface")
        LSTLOGGER.debug(CURRENTINTSTAT)
        if CURRENTINTSTAT == "UP":
            try:
                subprocess.Popen("sudo ifconfig ", CURRENTINT, " down", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
                LSTLOGGER.debug("")
            except Exception as e:
                LSTLOGGER.error("Unable to disable interface: ", CURRENTINT, e)
        else:
            try:
                subprocess.Popen("sudo ifconfig ", CURRENTINT, " up", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
            except Exception as e:
                LSTLOGGER.error("Unable to enable interface: ", CURRENTINT, e)

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
            self.disableintbtn.config(state="ACTIVE")
            CURRENTINTSTAT == "UP"
        else:
            if search("DOWN", intstatus):
                LSTLOGGER.info("Interface DOWN")
                self.disableintbtn.config(text="Enable")
                self.disableintbtn.config(state="ACTIVE")    
                CURRENTINTSTAT == "DOWN"
            else:
                if CURRENTINT == "lo":
                    self.disableintbtn.config(text="Disable")
                    self.disableintbtn.config(state="DISABLED")
                else:
                    self.disableintbtn.config(text="Disable")
                    self.disableintbtn.config(state="ACTIVE")

        #Get add info
        intmacaddress = subprocess.Popen("ifconfig " + CURRENTINT + " | grep ether | awk '{print$2}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
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
        LSTLOGGER.debug(CURRENTINTSTAT)
        LSTLOGGER.debug(intmacaddress)
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
            
app=App()