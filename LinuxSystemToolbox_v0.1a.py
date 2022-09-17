#!/bin/python3
"""
*********************************************************************************
|                                                                               |
|                             Linux System Toolbox                              |
|                 --------------------------------------------                  |   
|                         Written by: Lothar TheQuiet                           |
|                          lotharthequiet@gmail.com                             |
|                   Graphing Logic Assitance: Tai Gong Quan                     |
|                      Hounding about caMELCase: Rilvyk                         |
|                 Randomly Odd/Tasteless/Weird Jokes: Rleonekc                  |
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

"""
Perf Graph Color codes:
Green: #66ff33
Green Shade: #1a6600
Yellow: #ffff00
Yellow Shade: #666600
Red: #ff0000
Red Shade: #800000
"""
import tkinter as tk
import os
import tksheet
import logging
import subprocess

from tkinter import DISABLED, Canvas, ttk
from re import search
from PIL import Image, ImageTk

root = tk.Tk()
print(f"Current working dir: {os.getcwd()}")

class GlobalVars(object):
    LSTVER = "0.1a35"
    LSTNAME = "Linux System Toolbox"
    LSTFULLNAME = (LSTNAME + " " + LSTVER)
    LSTAUTHOR = "Lothar TheQuiet"
    LSTCONTACT = "lotharthequiet@gmail.com"
    LSTGITHUBREPO = "https://github.com/lotharthequiet/LinuxSystemToolbox"
    LSTGITHUB = "https://github.com/lotharthequiet/LinuxSystemToolbox.git"
    DEFPADX = 10
    DEFPADY = 5
    NARROWPAD = 5
    BTNSIZE = 12
    STATICSTICKY = "W"
    STATICFULLFRMSTICKY = "NSEW"
    CURRENTINT = None
    CURRENTWRLSSINT = None
    CURRENTINTSTAT = None
    CURRENTWRLSSINTSTAT = None
    PROC = tk.StringVar()
    MAINICO = "tools.png"
    BROWSEICO = "browse.png"
    memused = 0
    totalmem = 0
    cpuidle = 0
    INTLIST = None
    WRLSSINTLIST = None
    proclist = None
    loggedusers = None
    allusers = None

class LSTLog():
    Logger = logging.getLogger(__name__)
    Logger.setLevel(logging.DEBUG)
    Loggerfmt = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
    #Logh = logging.FileHandler('LinuxSystemToolbox.log')
    Logh = logging.StreamHandler()
    Logh.setFormatter(Loggerfmt)
    Logger.addHandler(Logh)

try:
    GlobalVars.INTLIST = subprocess.Popen("ifconfig -s -a | tail -n +2 | awk '{print$1}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
except Exception as e:
    LSTLog.Logger.error("Unable to retrieve interface list.", e)
print(GlobalVars.INTLIST)
GlobalVars.INTLIST = GlobalVars.INTLIST.split()

try: 
    GlobalVars.WRLSSINTLIST = subprocess.Popen("iw dev | awk '$1==\"Interface\"{print$2}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
except Exception as e:
    LSTLog.Logger.error("Unable to retrieve wireless interface list.", e)
GlobalVars.WRLSSINTLIST = GlobalVars.WRLSSINTLIST.split()

try:
    proclist = subprocess.Popen("ps -au | awk '{print$1,$2,$3,$4,$7,$11}' | sed '1d'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
    proclist = proclist[:-1]
    proclist = proclist.split("\n")
    GlobalVars.proclist = [[x for x in line.strip().split(' ')] for line in proclist]
    LSTLog.Logger.debug(GlobalVars.proclist)
except Exception as e:
    LSTLog.Logger.error("Unable to retrieve system process list.", e)

try:
    loggedusers = subprocess.Popen("who | awk '{print$1}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
    loggedusers = loggedusers[:-1]
    loggedusers = loggedusers.split("\n")
    GlobalVars.loggedusers = [[x for x in line.strip().split(' ')] for line in loggedusers]
    LSTLog.Logger.debug(GlobalVars.loggedusers)
except Exception as e:
    LSTLog.Logger.error("Unable to retrieve logged in users.", e)

try: 
    allusers = subprocess.Popen("awk -F: '{print$1}' /etc/passwd", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
    allusers = allusers[:-1]
    allusers = allusers.split("\n")
    GlobalVars.allusers = [[x for x in line.strip().split(' ')] for line in allusers]
    LSTLog.Logger.debug(GlobalVars.allusers)
except Exception as e:
    LSTLog.Logger.error("Unable to retrieve list of system users.")

class GUIActions():
    def runreports():
        LSTLog.Logger.debug("Open System Reports Window.")
        reportwindow = tk.Toplevel(root)
        reportwindow.title(GlobalVars.LSTFULLNAME)
        ico = Image.open(GlobalVars.MAINICO)
        photo = ImageTk.PhotoImage(ico)
        reportwindow.wm_iconphoto(False, photo)
        reportwinttlfrm = tk.LabelFrame(reportwindow, text = "System Reports")
        reportwinttlfrm.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICFULLFRMSTICKY, columnspan=3)
        reportauthorlbl = tk.Label(reportwinttlfrm, text ="Written By:")
        reportauthorlbl.grid(column= 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICFULLFRMSTICKY)

    def exitapp():
        LSTLog.Logger.debug("Exiting LST.")
        root.quit()

    def switchuser():
        LSTLog.Logger.debug("Switch User.")

    def logout():
        LSTLog.Logger.debug("Logout.")

    def restart():
        LSTLog.Logger.debug("Restart.")

    def shutdown():
        LSTLog.Logger.debug("Shutdown.")

    def openhelp():
        LSTLog.Logger.debug("Open Help Window.")
        helpwindow = tk.Toplevel(root)
        helpwindow.title(GlobalVars.LSTFULLNAME)
        ico = Image.open(GlobalVars.MAINICO)
        photo = ImageTk.PhotoImage(ico)
        helpwindow.wm_iconphoto(False, photo)
        helpwinttlfrm = tk.LabelFrame(helpwindow, text = "Help")
        helpwinttlfrm.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICFULLFRMSTICKY)
        helpauthorlbl = tk.Label(helpwinttlfrm, text ="Written By:")
        helpauthorlbl.grid(column= 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICFULLFRMSTICKY)

    def openabout():
        LSTLog.Logger.debug("Open About Window.")
        aboutwindow = tk.Toplevel(root)
        aboutwindow.title(GlobalVars.LSTFULLNAME)
        ico = Image.open(GlobalVars.MAINICO)
        photo = ImageTk.PhotoImage(ico)
        aboutwindow.wm_iconphoto(False, photo)
        aboutwinttlfrm = tk.LabelFrame(aboutwindow, text = "About")
        aboutwinttlfrm.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICFULLFRMSTICKY)
        img = Image.open(GlobalVars.MAINICO)
        image = ImageTk.PhotoImage(img.resize((127, 127)))
        aboutcanvas = Canvas(aboutwinttlfrm, width=128, height=128)
        aboutcanvas.create_image(64, 64, image = image)
        aboutcanvas.grid(column=0, row=0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        aboutttllbl = tk.Label(aboutwinttlfrm, text=GlobalVars.LSTFULLNAME)
        aboutttllbl.grid(column=1, row=0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky="SW")
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
        print(GlobalVars.test)

    def getmacaddr(addr=None):
        LSTLog.Logger.debug("getmacaddr function.")
        try:
            addr = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | grep ether | awk '{print$2}' | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
            LSTLog.Logger.debug(addr)
        except Exception as e:
            LSTLog.Logger.error("Unable to retrive MAC address from interface: ", GlobalVars.CURRENTINT, e)
        return addr

    def getmtu(mtu=None):
        LSTLog.Logger.debug("getmtu function.")
        try:
            mtu = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | head -n +1 | awk '{print$4}' | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
            LSTLog.Logger.debug(mtu)
        except Exception as e:
            LSTLog.Logger.error("Unable to retrive MTU from interface: ", GlobalVars.CURRENTINT, e)
        return mtu

    def getipaddr(ipaddr=None):
        LSTLog.Logger.debug("getipaddr function.")
        try:
            ipaddr = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | grep inet | head -n +1 | awk '{print$2}' | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
            LSTLog.Logger.debug(ipaddr)
        except Exception as e:
            LSTLog.Logger.error("Unable to retrive IP address from interface: ", GlobalVars.CURRENTINT, e)
        return ipaddr

    def getsubmask(submask=None):
        LSTLog.Logger.debug("getsubmask function.")
        try:
            submask = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | grep inet | head -n +1 | awk '{print$4}' | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
            LSTLog.Logger.debug(submask)
        except Exception as e:
            LSTLog.Logger.error("Unable to retrive subnet mask from interface: ", GlobalVars.CURRENTINT, e)
        return submask

    def getdefgw(defgw=None):
        LSTLog.Logger.debug("getdefgw function.")
        try:
            defgw = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | grep inet | head -n +1 | awk '{print$4}' | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
            LSTLog.Logger.debug(defgw)
        except Exception as e:
            LSTLog.Logger.error("Unable to retrive default gateway from interface: ", GlobalVars.CURRENTINT, e)
        return defgw

    def getbcastaddr(bcastaddr=None):
        LSTLog.Logger.debug("getbcastaddr function.")
        try:
            bcastaddr = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | grep inet | head -n +1 | awk '{print$6}' | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
            LSTLog.Logger.debug(bcastaddr)
        except Exception as e:
            LSTLog.Logger.error("Unable to retrive subnet mask from interface: ", GlobalVars.CURRENTINT, e)
        return bcastaddr

    def getdnsserveraddr(dnsserveraddr=None):
        LSTLog.Logger.debug("getdnsserveraddr function.")
        try:
            dnsserveraddr = subprocess.Popen("cat /etc/resolv.conf | tail -n +3 | awk '{print$2}'| head -n +1 | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
            LSTLog.Logger.debug(dnsserveraddr)
        except Exception as e:
            LSTLog.Logger.error("Unable to retrive system DNS address(es).", e)
        return dnsserveraddr

    def gethostname(hostname=None):
        LSTLog.Logger.debug("gethostname function.")
        try:
            hostname = subprocess.Popen("hostname | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
            LSTLog.Logger.debug(hostname)
        except Exception as e:
            LSTLog.Logger.error("Unable to retrive system host name.", e)
        return hostname

    def getdomainname(domainname=None):
        LSTLog.Logger.debug("getdomainname function.")
        try:
            domainname = subprocess.Popen("cat /etc/resolv.conf | tail -n +2 | awk '{print$2}' | head -n +1 | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
            LSTLog.Logger.debug(domainname)
        except Exception as e:
            LSTLog.Logger.error("Unable to retrive system domain name.", e)
        return domainname

    def killproc(proc=None):
        LSTLog.Logger.debug("killproc function.")

    def spawnproc(proc=None):
        LSTLog.Logger.debug("spawnproc function.")
        spawnprocwindow = tk.Toplevel(root)
        spawnprocwindow.title(GlobalVars.LSTFULLNAME)
        ico = Image.open(GlobalVars.MAINICO)
        photo = ImageTk.PhotoImage(ico)
        spawnprocwindow.wm_iconphoto(False, photo)
        spawnprocttlfrm = tk.LabelFrame(spawnprocwindow, text = "Spawn Process")
        spawnprocttlfrm.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICFULLFRMSTICKY, columnspan=3)
        spawnprocauthorlbl = tk.Label(spawnprocttlfrm, text ="Process to Spawn:")
        spawnprocauthorlbl.grid(column= 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICFULLFRMSTICKY)
        spawnprocentry = tk.Entry(spawnprocttlfrm, textvariable=GlobalVars.PROC)
        spawnprocentry.grid(column=1, row=0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICFULLFRMSTICKY)
        spawnprocbrowsebtn = tk.Button(spawnprocttlfrm, image=GlobalVars.BROWSEICO)
        spawnprocbrowsebtn.grid(column=2, row=0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICFULLFRMSTICKY)
        
    def enablesvc(svc=None):
        LSTLog.Logger.debug("enablesvc function.")
    
    def disablesvc(svc=None):
        LSTLog.Logger.debug("disablesvc function.")
    
    def startsvc(svc=None):
        LSTLog.Logger.debug("startsvc function.")
    
    def stopsvc(svc=None):
        LSTLog.Logger.debug("stopsvc function.")

    def newuser(user=None):
        LSTLog.Logger.debug("newuser function.")
    
    def disableuser(user=None):
        LSTLog.Logger.debug("disableuser function.")
    
    def deluser(user=None):
        LSTLog.Logger.debug("deluser function.")

    def toggleinterface():
        LSTLog.Logger.debug("Toggle Interface")
        LSTLog.Logger.debug(GlobalVars.CURRENTINTSTAT)
        if GlobalVars.CURRENTINTSTAT == "UP":
            try:
                subprocess.Popen("sudo ifconfig ", GlobalVars.CURRENTINT, " down", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
                LSTLog.Logger.debug("")
            except Exception as e:
                LSTLog.Logger.error("Unable to disable interface: ", GlobalVars.CURRENTINT, e)
        else:
            try:
                subprocess.Popen("sudo ifconfig ", GlobalVars.CURRENTINT, " up", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
            except Exception as e:
                LSTLog.Logger.error("Unable to enable interface: ", GlobalVars.CURRENTINT, e)

    def dhcprelease():
        LSTLog.Logger.info("DHCP Release")

    def dhcprenew():
        LSTLog.Logger.info("DHCP Renew")

    def refreshintstats(int=None):
        LSTLog.Logger.info("refreshintstats function.")
        LSTLog.Logger.debug(GlobalVars.CURRENTINT)
        intstats = []
        try:
            intstats[1] = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | grep 'RX packets' | awk {'print$3'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
            intstats[2] = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | grep 'RX packets' | awk {'print$5'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
            intstats[3] = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | grep 'RX packets' | awk {'print$6'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
            intstats[4] = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | grep 'RX Errors' | awk {'print$3'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
            intstats[5] = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | grep 'RX Errors' | awk {'print$5'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
            intstats[6] = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | grep 'RX Errors' | awk {'print$7'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
            intstats[7] = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | grep 'RX Errors' | awk {'print$9'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
            intstats[8] = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | grep 'TX packets' | awk {'print$3'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
            intstats[9] = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | grep 'TX packets' | awk {'print$5'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
            intstats[10] = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | grep 'TX packets' | awk {'print$6'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
            intstats[11] = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | grep 'TX errors' | awk {'print$3'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
            intstats[12] = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | grep 'TX errors' | awk {'print$5'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
            intstats[13] = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | grep 'TX errors' | awk {'print$7'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
            intstats[14] = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | grep 'TX errors' | awk {'print$9'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
            intstats[15] = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | grep 'TX errors' | awk {'print$11'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
            LSTLog.Logger.debug(intstats)
        except Exception as e:
            LSTLog.Logger.error("Unable to refresh stats for int", e)
        return intstats

    def selectinterface():
        LSTLog.Logger.info("Select Interface Function.")
        GlobalVars.CURRENTINT = BuildGUI.intcombo.get()
        LSTLog.Logger.debug(GlobalVars.CURRENTINT)
        try:
            intstatus = subprocess.Popen("ip a sh dev " + GlobalVars.CURRENTINT + " | head -n 1 | awk {'print$9'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        except Exception as e: 
            LSTLog.Logger.error("Unable to retrieve current interface status. ", e)
        if search("UP", intstatus):
            LSTLog.Logger.info("Interface UP")
            BuildGUI.disableintbtn.config(text="Disable", state="normal")
            BuildGUI.intstatus['text'] = "Up"
        else:
            if search("DOWN", intstatus):
                LSTLog.Logger.info("Interface DOWN")
                BuildGUI.disableintbtn.config(text="Enable", state="normal")
                BuildGUI.intstatus['text'] = "Down"
            else:
                if GlobalVars.CURRENTINT == "lo":
                    LSTLog.Logger.info("Interface Loopback")
                    BuildGUI.disableintbtn.config(text="Disable", state="disabled")
                    BuildGUI.intstatus['text'] = "Loopback"
                else:
                    LSTLog.Logger.info("Interface Unknown")
                    BuildGUI.disableintbtn.config(text="Disable", state="normal")
                    BuildGUI.intstatus['text'] = "Unknown"
        BuildGUI.macaddr['text'] = GUIActions.getmacaddr()
        BuildGUI.mtu['text'] = GUIActions.getmtu()
        BuildGUI.ipaddr['text'] = GUIActions.getipaddr()
        BuildGUI.submask['text'] = GUIActions.getsubmask()
        BuildGUI.defgw['text'] = GUIActions.getdefgw()
        BuildGUI.bcastaddr['text'] = GUIActions.getbcastaddr()
        BuildGUI.dnsserveraddr['text'] = GUIActions.getdnsserveraddr()
        BuildGUI.dnshostname['text'] = GUIActions.gethostname()
        BuildGUI.dnsdomain['text'] = GUIActions.getdomainname()
        BuildGUI.rxpacketcntlbl['text'] = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | grep 'RX packets' | awk {'print$3'} | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        BuildGUI.rxpacketbytescntlbl['text'] = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | grep 'RX packets' | awk {'print$5'} | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        BuildGUI.rxpacketbyteshumancntlbl['text'] = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | grep 'RX packets' | awk {'print$6,$7'} | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        BuildGUI.rxerrorscntlbl['text'] = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | grep 'RX errors' | awk {'print$3'} | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        BuildGUI.rxdroppedcntlbl['text'] = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | grep 'RX errors' | awk {'print$5'} | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        BuildGUI.rxoverrunscntlbl['text'] = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | grep 'RX errors' | awk {'print$7'} | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        BuildGUI.rxframecntlbl['text'] = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | grep 'RX errors' | awk {'print$9'} | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        BuildGUI.txpacketcntlbl['text'] = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | grep 'TX packets' | awk {'print$3'} | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        BuildGUI.txpacketbytescntlbl['text'] = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | grep 'TX packets' | awk {'print$5'} | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        BuildGUI.txpacketbyteshumcntlbl['text'] = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | grep 'TX packets' | awk {'print$6,$7'} | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        BuildGUI.txerrorscntlbl['text'] = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | grep 'TX errors' | awk {'print$3'} | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        BuildGUI.txdroppedcntlbl['text'] = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | grep 'TX errors' | awk {'print$5'} | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        BuildGUI.txoverrunscntlbl['text'] = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | grep 'TX errors' | awk {'print$7'} | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        BuildGUI.txfrmcntlbl['text'] = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | grep 'TX errors' | awk {'print$9'} | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        BuildGUI.txcolscntlbl['text'] = subprocess.Popen("ifconfig " + GlobalVars.CURRENTINT + " | grep 'TX errors' | awk {'print$11'} | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        GUIActions.getroutetable()
        BuildGUI.dhcpreleasebtn.config(state="normal")
        BuildGUI.dhcprenewbtn.config(state="normal")
        BuildGUI.refreshbtn.config(state="normal")
    
    def getroutetable():
        LSTLog.Logger.debug("Get route table.")
        try:
            introutetable = subprocess.Popen("netstat -r | tail -n +3", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        except Exception as e:
            LSTLog.Logger.error("Unable to retrieve route table.", e)
        introutetable = introutetable.split()
        count = 0
        rowcount = 1
        for x in introutetable:
            if count == 8:
                count = 0
                rowcount = rowcount + 1
                tk.Label(BuildGUI.routetblfrm, text = x).grid(column = count, row = rowcount, padx = GlobalVars.NARROWPAD, pady = GlobalVars.NARROWPAD, sticky = GlobalVars.STATICSTICKY)
                count = count + 1
            elif count < 8:
                tk.Label(BuildGUI.routetblfrm, text = x).grid(column = count, row = rowcount, padx = GlobalVars.NARROWPAD, pady = GlobalVars.NARROWPAD, sticky = GlobalVars.STATICSTICKY)
                count = count + 1
    
    def selwrlssint():
        LSTLog.Logger.debug("selwrlssint function.")
        GlobalVars.CURRENTWRLSSINT = BuildGUI.wrlssintcombo.get()
        LSTLog.Logger.debug(GlobalVars.CURRENTWRLSSINT)

    def getmemoryinfo():
        LSTLog.Logger.debug("getmemoryinfo function")
        BuildGUI.perftabmemtotal['text'] = subprocess.Popen("free | tail -n 2 | head -n 1 | awk {'print$2'} | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        BuildGUI.perftabmemavail['text'] = subprocess.Popen("free | tail -n 2 | head -n 1 | awk {'print$7'} | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        BuildGUI.perftabstatmemuse['text'] = subprocess.Popen("free | tail -n 2 | head -n 1 | awk {'print$3'} | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        GlobalVars.totalmem = subprocess.Popen("free | tail -n 2 | head -n 1 | awk {'print$2'} | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        BuildGUI.perftabstatmemusetotal['text'] = subprocess.Popen("free | tail -n 2 | head -n 1 | awk {'print$2'} | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        BuildGUI.perftabmemcache['text'] = subprocess.Popen("free | tail -n 2 | head -n 1 | awk {'print$6'} | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        BuildGUI.perftabswaptotal['text'] = subprocess.Popen("free | tail -n 1 | awk {'print$2'} | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        GlobalVars.memused = subprocess.Popen("free | tail -n 2 | head -n 1 | awk {'print$3'} | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        GlobalVars.memused = GlobalVars.memused + " MB"
        BuildGUI.memcanvas.create_text(64, 110, text=GlobalVars.memused, fill='#66ff33', font=('Cantarell Regular', 12))
        BuildGUI.perftabswapused['text'] = subprocess.Popen("free | tail -n 2 | head -n 1 | awk {'print$3'} | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        BuildGUI.perftabswapfree['text'] = subprocess.Popen("free | tail -n 1 | awk {'print$4'} | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        
    def getprocinfo():
        LSTLog.Logger.debug("getprocinfo function")
        BuildGUI.perftabstatsproc['text'] = subprocess.Popen("ps -aux | wc -l  | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        BuildGUI.perftabprocs['text'] = subprocess.Popen("ps -aux | wc -l  | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        GlobalVars.cpuidle = subprocess.Popen("iostat -c | tail -n 4 | awk {'print$6'} | tr -d '\n'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0].decode('utf-8')
        cpuused = 100 - float(GlobalVars.cpuidle)
        cpu = str(int(cpuused))
        cpu2 = cpu + " %"
        BuildGUI.perftabstatscpu['text'] = cpu2
        BuildGUI.cpucanvas.create_text(64, 110, text=cpu2, fill='#66ff33', font=('Cantarell Regular', 14))
        GUIActions.drawcpugraph(cpu)

    def drawcpugraph(cpu):
        LSTLog.Logger.debug("drawcpugraph function")
        LSTLog.Logger.debug(cpu)
        if int(cpu) <= 10:
            LSTLog.Logger.debug("Cpu 10% or less") 
            BuildGUI.cpucanvas.create_text(64, 30, text="_______", fill='#800000', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 35, text="_______", fill='#666600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 40, text="_______", fill='#666600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 45, text="_______", fill='#1a6600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 50, text="_______", fill='#1a6600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 55, text="_______", fill='#1a6600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 60, text="_______", fill='#1a6600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 65, text="_______", fill='#1a6600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 70, text="_______", fill='#1a6600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 75, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
        elif int(cpu) <= 20 and int(cpu) > 10:
            LSTLog.Logger.debug("Cpu 20%")
            BuildGUI.cpucanvas.create_text(64, 30, text="_______", fill='#800000', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 35, text="_______", fill='#666600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 40, text="_______", fill='#666600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 45, text="_______", fill='#1a6600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 50, text="_______", fill='#1a6600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 55, text="_______", fill='#1a6600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 60, text="_______", fill='#1a6600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 65, text="_______", fill='#1a6600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 70, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 75, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
        elif int(cpu) <= 30 and int(cpu) > 20:
            LSTLog.Logger.debug("Cpu 30%")
            BuildGUI.cpucanvas.create_text(64, 30, text="_______", fill='#800000', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 35, text="_______", fill='#666600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 40, text="_______", fill='#666600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 45, text="_______", fill='#1a6600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 50, text="_______", fill='#1a6600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 55, text="_______", fill='#1a6600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 60, text="_______", fill='#1a6600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 65, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 70, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 75, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
        elif int(cpu) <= 40 and int(cpu) > 30:
            LSTLog.Logger.debug("Cpu 40%")
            BuildGUI.cpucanvas.create_text(64, 30, text="_______", fill='#800000', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 35, text="_______", fill='#666600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 40, text="_______", fill='#666600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 45, text="_______", fill='#1a6600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 50, text="_______", fill='#1a6600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 55, text="_______", fill='#1a6600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 60, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 65, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 70, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 75, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
        elif int(cpu) <= 50 and int(cpu) > 40:
            LSTLog.Logger.debug("Cpu 50%")
            BuildGUI.cpucanvas.create_text(64, 30, text="_______", fill='#800000', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 35, text="_______", fill='#666600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 40, text="_______", fill='#666600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 45, text="_______", fill='#1a6600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 50, text="_______", fill='#1a6600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 55, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 60, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 65, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 70, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 75, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
        elif int(cpu) <= 60 and int(cpu) > 50:
            LSTLog.Logger.debug("Cpu 60%")
            BuildGUI.cpucanvas.create_text(64, 30, text="_______", fill='#800000', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 35, text="_______", fill='#666600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 40, text="_______", fill='#666600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 45, text="_______", fill='#1a6600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 50, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 55, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 60, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 65, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 70, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 75, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
        elif int(cpu) <= 70 and int(cpu) > 60:
            LSTLog.Logger.debug("Cpu 70%")
            BuildGUI.cpucanvas.create_text(64, 30, text="_______", fill='#800000', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 35, text="_______", fill='#666600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 40, text="_______", fill='#666600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 45, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 50, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 55, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 60, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 65, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 70, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 75, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
        elif int(cpu) <= 80 and int(cpu) > 70:
            LSTLog.Logger.debug("Cpu 80%")
            BuildGUI.cpucanvas.create_text(64, 30, text="_______", fill='#800000', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 35, text="_______", fill='#666600', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 40, text="_______", fill='#ffff00', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 45, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 50, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 55, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 60, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 65, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 70, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 75, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
        elif int(cpu) <= 90 and int(cpu) > 80:
            LSTLog.Logger.debug("Cpu 90%")
            BuildGUI.cpucanvas.create_text(64, 30, text="_______", fill='#800000', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 35, text="_______", fill='#ffff00', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 40, text="_______", fill='#ffff00', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 45, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 50, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 55, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 60, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 65, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 70, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 75, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
        elif int(cpu) <= 100 and int(cpu) > 90:
            LSTLog.Logger.debug("Cpu 100%")
            BuildGUI.cpucanvas.create_text(64, 30, text="_______", fill='#ff0000', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 35, text="_______", fill='#ffff00', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 40, text="_______", fill='#ffff00', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 45, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 50, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 55, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 60, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 65, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 70, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            BuildGUI.cpucanvas.create_text(64, 75, text="_______", fill='#66ff33', font=('Cantarell Regular', 12, 'bold'))
            
class NetToolbox():
    def Open():
        LSTLog.Logger.debug("Open Network Toolbox Window.")
        toolboxwindow = tk.Toplevel(root)
        toolboxwindow.title(GlobalVars.LSTFULLNAME)
        toolboxwindow.geometry("700x500")
        ico = Image.open(GlobalVars.MAINICO)
        photo = ImageTk.PhotoImage(ico)
        toolboxwindow.wm_iconphoto(False, photo)
        Toolboxnb = ttk.Notebook(toolboxwindow)
        configtab = tk.Frame(Toolboxnb)
        dhcptab = tk.Frame(Toolboxnb)
        routingtab = tk.Frame(Toolboxnb)
        pingtab = tk.Frame(Toolboxnb)
        traceroutetab = tk.Frame(Toolboxnb)
        nslookuptab = tk.Frame(Toolboxnb)
        whoistab = tk.Frame(Toolboxnb)
        wgettab = tk.Frame(Toolboxnb)
        tftptab = tk.Frame(Toolboxnb)
        telnettab = tk.Frame(Toolboxnb)
        ftptab = tk.Frame(Toolboxnb)
        sftptab = tk.Frame(Toolboxnb)
        scptab = tk.Frame(Toolboxnb)
        Toolboxnb.add(configtab, text ='Config')
        Toolboxnb.add(dhcptab, text ='DHCP')
        Toolboxnb.add(routingtab, text ='Routing')
        Toolboxnb.add(pingtab, text ='Ping')
        Toolboxnb.add(traceroutetab, text ='Traceroute')
        Toolboxnb.add(nslookuptab, text ='NSLOOKUP')
        Toolboxnb.add(whoistab, text ='WHOIS')
        Toolboxnb.add(wgettab, text = 'WGET')
        Toolboxnb.add(tftptab, text = 'TFTP')
        Toolboxnb.add(telnettab, text = 'Telnet')
        Toolboxnb.add(ftptab, text = 'FTP')
        Toolboxnb.add(sftptab, text = 'SFTP')
        Toolboxnb.add(scptab, text = 'SCP')
        Toolboxnb.pack(expand = 1, fill ="both")
        configtabcontfrm = tk.Frame(configtab)
        configtabcontfrm.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICSTICKY)
        configtabbtnfrm = tk.Frame(configtab)
        configtabbtnfrm.grid(column = 1, row = 0, padx = 0, pady = (10, 5), sticky='N')
        disableintbtn = tk.Button(configtabbtnfrm, text ="Disable", width = GlobalVars.BTNSIZE, command=GUIActions.toggleinterface, state="disabled")
        disableintbtn.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
        intlbl = tk.Label(configtabcontfrm, text ="Select Interface:")
        intlbl.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICSTICKY)
        intcombo = ttk.Combobox(configtabcontfrm, values = GlobalVars.INTLIST)
        intcombo.grid(column = 1, row = 0, pady = (10, 5), sticky=GlobalVars.STATICSTICKY)
        intcombo.set("Select Interface:")
        intcombo.bind('<<ComboboxSelected>>', lambda event: GUIActions.selectinterface())
        intstatuslbl = tk.Label(configtabcontfrm, text="Interface Status:")
        intstatuslbl.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        intstatus = tk.Label(configtabcontfrm, text = GlobalVars.CURRENTINTSTAT)
        intstatus.grid(column = 1, row = 1, sticky=GlobalVars.STATICSTICKY)
        macaddrlbl = tk.Label(configtabcontfrm, text="Mac Address:")
        macaddrlbl.grid(column = 0, row = 2, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        macaddr = tk.Label(configtabcontfrm)
        macaddr.grid(column = 1, row = 2, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        mtulbl = tk.Label(configtabcontfrm, text ="MTU:")
        mtulbl.grid(column = 0, row = 3, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        mtu = tk.Label(configtabcontfrm)
        mtu.grid(column = 1, row = 3, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        ipaddrlbl = tk.Label(configtabcontfrm, text="IP Address:")
        ipaddrlbl.grid(column = 0, row = 4, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        ipaddr = tk.Label(configtabcontfrm)
        ipaddr.grid(column = 1, row = 4, sticky=GlobalVars.STATICSTICKY)
        submasklbl = tk.Label(configtabcontfrm, text="Subnet Mask:")
        submasklbl.grid(column = 0, row = 5, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        submask = tk.Label(configtabcontfrm)
        submask.grid(column = 1, row = 5, sticky=GlobalVars.STATICSTICKY)
        defgwlbl = tk.Label(configtabcontfrm, text="Default Gateway:")
        defgwlbl.grid(column = 0, row = 6, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        defgw = tk.Label(configtabcontfrm)
        defgw.grid(column = 1, row = 6, sticky=GlobalVars.STATICSTICKY)
        bcastaddrlbl = tk.Label(configtabcontfrm, text="Broadcast Address:")
        bcastaddrlbl.grid(column = 0, row = 7, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        bcastaddr = tk.Label(configtabcontfrm)
        bcastaddr.grid(column = 1, row = 7, sticky=GlobalVars.STATICSTICKY)
        dnsserverslbl = tk.Label(configtabcontfrm, text="DNS Servers:")
        dnsserverslbl.grid(column = 0, row = 8, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        dnsserveraddr = tk.Label(configtabcontfrm)
        dnsserveraddr.grid(column = 1, row = 8, sticky=GlobalVars.STATICSTICKY)
        dnshostnamelbl = tk.Label(configtabcontfrm, text="DNS Hostname:")
        dnshostnamelbl.grid(column = 0, row = 9, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        dnshostname = tk.Label(configtabcontfrm)
        dnshostname.grid(column = 1, row = 9, sticky=GlobalVars.STATICSTICKY)
        dnsdomainlbl = tk.Label(configtabcontfrm, text="DNS Domain:")
        dnsdomainlbl.grid(column = 0, row = 10, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        dnsdomain = tk.Label(configtabcontfrm)
        dnsdomain.grid(column = 1, row = 10, sticky=GlobalVars.STATICSTICKY)
        pingtablblfrm = tk.LabelFrame(pingtab, text="Ping")
        pingtablblfrm.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICSTICKY)
        pingoutputlblfrm = tk.LabelFrame(pingtab, text="Output")
        pingoutputlblfrm.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICSTICKY)
        pingtabcontfrm = tk.Frame(pingtablblfrm)
        pingtabcontfrm.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICSTICKY)
        pingtabbtnfrm = tk.Frame(pingtablblfrm)
        pingtabbtnfrm.grid(column = 1, row = 0, padx = 0, pady = (10, 5), sticky='N')
        pingbtn = tk.Button(pingtabbtnfrm, text ="Ping", width = GlobalVars.BTNSIZE, command=GUIActions.toggleinterface)
        pingbtn.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
        pingcancelbtn = tk.Button(pingtabbtnfrm, text ="Cancel", width = GlobalVars.BTNSIZE, command=GUIActions.toggleinterface)
        pingcancelbtn.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
        pingclearbtn = tk.Button(pingtabbtnfrm, text = "Clear", width = GlobalVars.BTNSIZE, command=GUIActions.toggleinterface)
        pingclearbtn.grid(column = 0, row = 2, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
        pinglbl = tk.Label(pingtabcontfrm, text="Address:")
        pinglbl.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        pingaddr = tk.Entry(pingtabcontfrm, width = 35)
        pingaddr.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        pinghelplbl = tk.Label(pingtabcontfrm, text = "(Ie. 10.1.1.10 10.1.1.10-10.1.1.15 10.1.1.*)")
        pinghelplbl.grid(column = 0, row = 2, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        pingoutput = tk.Entry(pingoutputlblfrm, width=60, text="Test text.", state = DISABLED)
        pingoutput.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        traceroutetablblfrm = tk.LabelFrame(traceroutetab, text="Traceroute")
        traceroutetablblfrm.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICSTICKY)
        tracerouteoutputlblfrm = tk.LabelFrame(traceroutetab, text="Output")
        tracerouteoutputlblfrm.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICSTICKY)
        traceroutetabcontfrm = tk.Frame(traceroutetablblfrm)
        traceroutetabcontfrm.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICSTICKY)
        traceroutetabbtnfrm = tk.Frame(traceroutetablblfrm)
        traceroutetabbtnfrm.grid(column = 1, row = 0, padx = 0, pady = (10, 5), sticky='N')
        traceroutebtn = tk.Button(traceroutetabbtnfrm, text ="Traceroute", width = GlobalVars.BTNSIZE, command=GUIActions.toggleinterface)
        traceroutebtn.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
        traceroutecancelbtn = tk.Button(traceroutetabbtnfrm, text ="Cancel", width = GlobalVars.BTNSIZE, command=GUIActions.toggleinterface)
        traceroutecancelbtn.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
        tracerouteclearbtn = tk.Button(traceroutetabbtnfrm, text = "Clear", width = GlobalVars.BTNSIZE, command=GUIActions.toggleinterface)
        tracerouteclearbtn.grid(column = 0, row = 2, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
        traceroutelbl = tk.Label(traceroutetabcontfrm, text="Address:")
        traceroutelbl.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        tracerouteaddr = tk.Entry(traceroutetabcontfrm, width = 35)
        tracerouteaddr.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        traceroutehelplbl = tk.Label(traceroutetabcontfrm, text = "(Ie. 10.1.1.10 10.1.1.10-10.1.1.15 10.1.1.*)")
        traceroutehelplbl.grid(column = 0, row = 2, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        tracerouteoutput = tk.Entry(tracerouteoutputlblfrm, width=60, text="Test text.", state = DISABLED)
        tracerouteoutput.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        nslookuptablblfrm = tk.LabelFrame(nslookuptab, text="NS Lookup")
        nslookuptablblfrm.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICSTICKY)
        nslookupoutputlblfrm = tk.LabelFrame(nslookuptab, text="Output")
        nslookupoutputlblfrm.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICSTICKY)
        nslookuptabcontfrm = tk.Frame(nslookuptablblfrm)
        nslookuptabcontfrm.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICSTICKY)
        nslookuptabbtnfrm = tk.Frame(nslookuptablblfrm)
        nslookuptabbtnfrm.grid(column = 1, row = 0, padx = 0, pady = (10, 5), sticky='N')
        nslookupbtn = tk.Button(nslookuptabbtnfrm, text ="NS Lookup", width = GlobalVars.BTNSIZE, command=GUIActions.toggleinterface)
        nslookupbtn.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
        nslookupcancelbtn = tk.Button(nslookuptabbtnfrm, text ="Cancel", width = GlobalVars.BTNSIZE, command=GUIActions.toggleinterface)
        nslookupcancelbtn.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
        nslookupclearbtn = tk.Button(nslookuptabbtnfrm, text = "Clear", width = GlobalVars.BTNSIZE, command=GUIActions.toggleinterface)
        nslookupclearbtn.grid(column = 0, row = 2, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
        nslookuplbl = tk.Label(nslookuptabcontfrm, text="Address:")
        nslookuplbl.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        nslookupaddr = tk.Entry(nslookuptabcontfrm, width = 35)
        nslookupaddr.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        nslookuphelplbl = tk.Label(nslookuptabcontfrm, text = "(Ie. 10.1.1.10 10.1.1.10-10.1.1.15 10.1.1.*)")
        nslookuphelplbl.grid(column = 0, row = 2, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
        nslookupoutput = tk.Entry(nslookupoutputlblfrm, width=60, text="Test text.", state = DISABLED)
        nslookupoutput.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)

class BuildGUI():
    root.title(GlobalVars.LSTFULLNAME)
    root.geometry("650x800")
    ico = Image.open(GlobalVars.MAINICO)
    photo = ImageTk.PhotoImage(ico)
    root.wm_iconphoto(False, photo)
    LSTnb = ttk.Notebook(root)
    menubar = tk.Menu(LSTnb)
    menubar = tk.Menu(LSTnb)
    filemenu = tk.Menu(menubar, tearoff=0)                                     
    filemenu.add_command(label="System Reports", command=GUIActions.runreports)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=GUIActions.exitapp)
    menubar.add_cascade(label="File", menu=filemenu)
    toolsmenu = tk.Menu(menubar, tearoff=0)                                    
    toolsmenu.add_command(label="Open Net Toolbox", command=NetToolbox.Open)
    toolsmenu.add_separator()
    toolsmenu.add_command(label="Switch User", command=GUIActions.switchuser)
    toolsmenu.add_command(label="Logout", command=GUIActions.logout)
    toolsmenu.add_command(label="Restart", command=GUIActions.restart)
    toolsmenu.add_command(label="Shutdown", command=GUIActions.shutdown)
    menubar.add_cascade(label="Tools", menu=toolsmenu)
    helpmenu = tk.Menu(menubar, tearoff=0)                                     
    helpmenu.add_command(label="Help", command=GUIActions.openhelp)
    helpmenu.add_separator()
    helpmenu.add_command(label="About", command=GUIActions.openabout)
    menubar.add_cascade(label="Help", menu=helpmenu)
    proctab = tk.Frame(LSTnb)
    servicestab = tk.Frame(LSTnb)
    userstab = tk.Frame(LSTnb)
    nettab = tk.Frame(LSTnb)
    perftab = tk.Frame(LSTnb)
    wrlsstab = tk.Frame(LSTnb)
    LSTnb.add(proctab, text ='Applications')
    LSTnb.add(servicestab, text ='Services')
    LSTnb.add(userstab, text ='Users')
    LSTnb.add(nettab, text ='Networking')
    LSTnb.add(perftab, text ='Performance')
    LSTnb.add(wrlsstab, text = 'Wireless')
    LSTnb.pack(expand = 1, fill ="both")
    root.config(menu=menubar)
    proctabttlfrm = tk.LabelFrame(proctab, text="Running Applications")
    proctabttlfrm.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICFULLFRMSTICKY, columnspan=2)
    procsht = tksheet.Sheet(proctabttlfrm, enable_edit_cell_auto_resize = False, show_row_index = True)
    procsht.grid(padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY)
    procsht.enable_bindings(("row_select"))
    print(GlobalVars.proclist)
    procsht.set_sheet_data(data=GlobalVars.proclist)
    procsht.headers(["User","PID","CPU %","Mem %","TTY","Command"])
    #for each in GlobalVars.proclist:
    #    procsht.insert_row(values=GlobalVars.proclist)
    #procsht.insert_row("test")
    proctabbtnfrm = tk.Frame(proctab)
    proctabbtnfrm.grid(column = 2, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
    killprocbtn = tk.Button(proctabbtnfrm, text="Kill Process", width = GlobalVars.BTNSIZE, state="disabled")
    killprocbtn.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
    spawnprocbtn = tk.Button(proctabbtnfrm, text="Spawn Process", width = GlobalVars.BTNSIZE, command=GUIActions.spawnproc)
    spawnprocbtn.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
    svcstabttlfrm = tk.LabelFrame(servicestab, text="System Services")
    svcstabttlfrm.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICFULLFRMSTICKY, columnspan=2)
    svcssht = tksheet.Sheet(svcstabttlfrm)
    svcssht.grid(padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY)
    svcssht.enable_bindings(("row_select"))
    svcstabbtnfrm = tk.Frame(servicestab)
    svcstabbtnfrm.grid(column = 2, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
    enablesvcbtn = tk.Button(svcstabbtnfrm, text="Enable Service", width = GlobalVars.BTNSIZE, command=GUIActions.enablesvc, state="disabled")
    enablesvcbtn.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
    disablesvcbtn = tk.Button(svcstabbtnfrm, text="Disable Service", width = GlobalVars.BTNSIZE, command=GUIActions.disablesvc, state="disabled")
    disablesvcbtn.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
    startsvcbtn = tk.Button(svcstabbtnfrm, text="Start Service", width = GlobalVars.BTNSIZE, command=GUIActions.startsvc, state="disabled")
    startsvcbtn.grid(column = 0, row = 2, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
    stopsvcbtn = tk.Button(svcstabbtnfrm, text="Stop Service", width = GlobalVars.BTNSIZE, command=GUIActions.stopsvc, state="disabled")
    stopsvcbtn.grid(column = 0, row = 3, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
    usrtabttlfrm = tk.LabelFrame(userstab, text="Logged In Users")
    usrtabttlfrm.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICFULLFRMSTICKY, columnspan=2)
    lclusrtabttlfrm = tk.LabelFrame(userstab, text="Local Users")
    lclusrtabttlfrm.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICFULLFRMSTICKY, columnspan=2)
    currentusrsht = tksheet.Sheet(usrtabttlfrm)
    currentusrsht.grid(padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY)
    print(GlobalVars.loggedusers)
    currentusrsht.enable_bindings(("row_select"))
    currentusrsht.headers(["User"])
    currentusrsht.set_sheet_data(data=GlobalVars.loggedusers)
    lclusrsht = tksheet.Sheet(lclusrtabttlfrm)
    lclusrsht.grid(padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY)
    print(GlobalVars.allusers)
    lclusrsht.enable_bindings(("row_select"))
    lclusrsht.headers(["User"])
    lclusrsht.set_sheet_data(data=GlobalVars.allusers)
    usrtabbtnfrm = tk.Frame(userstab)
    usrtabbtnfrm.grid(column = 2, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
    newuserbtn = tk.Button(usrtabbtnfrm, text="New User", width = GlobalVars.BTNSIZE, command=GUIActions.newuser)
    newuserbtn.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
    disableuserbtn = tk.Button(usrtabbtnfrm, text="Disable User", width = GlobalVars.BTNSIZE, command=GUIActions.disableuser, state="disabled")
    disableuserbtn.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
    deluserbtn = tk.Button(usrtabbtnfrm, text="Remove User", width = GlobalVars.BTNSIZE, command=GUIActions.deluser, state="disabled")
    deluserbtn.grid(column = 0, row = 2, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
    nettabcontfrm = tk.LabelFrame(nettab, text="Connection Status")
    nettabcontfrm.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky='NEW', columnspan=2)
    nettabbtnfrm = tk.Frame(nettab)
    nettabbtnfrm.grid(column = 2, row = 0, padx = 0, pady = (10, 5), sticky='N', rowspan=2)
    intstatsfrm = tk.LabelFrame(nettab, text="Interface Statistics")
    intstatsfrm.grid(column = 0, row = 2, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICFULLFRMSTICKY, columnspan = 3)
    routetblfrm = tk.LabelFrame(nettab, text="Routing Table")
    routetblfrm.grid(column = 0, row = 3, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICFULLFRMSTICKY, columnspan = 3)
    disableintbtn = tk.Button(nettabbtnfrm, text ="Disable", width = GlobalVars.BTNSIZE, command=GUIActions.toggleinterface, state="disabled")
    disableintbtn.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
    dhcpreleasebtn = tk.Button(nettabbtnfrm, text ="DHCP Release", width = GlobalVars.BTNSIZE, command=GUIActions.dhcprelease, state="disabled")
    dhcpreleasebtn.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
    dhcprenewbtn = tk.Button(nettabbtnfrm, text ="DHCP Renew", width = GlobalVars.BTNSIZE, command=GUIActions.dhcprenew, state="disabled")
    dhcprenewbtn.grid(column = 0, row = 2, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
    refreshbtn = tk.Button(nettabbtnfrm, text = "Refresh Stats", width = GlobalVars.BTNSIZE, command=GUIActions.refreshintstats, state="disabled")
    refreshbtn.grid(column = 0, row = 3, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
    nettoolboxbtn = tk.Button(nettabbtnfrm, text ="Net Toolbox", width = GlobalVars.BTNSIZE, command=NetToolbox.Open)
    nettoolboxbtn.grid(column = 0, row = 4, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
    selintname = tk.StringVar()
    intlbl = tk.Label(nettab, text ="Interface Name:")
    intlbl.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICSTICKY)
    intcombo = ttk.Combobox(nettab, values = GlobalVars.INTLIST)
    intcombo.grid(column = 1, row = 0, pady = (10, 5), sticky=GlobalVars.STATICSTICKY)
    intcombo.set("Select Interface")
    intcombo.bind('<<ComboboxSelected>>', lambda event: GUIActions.selectinterface())
    intstatuslbl = tk.Label(nettabcontfrm, text="Interface Status:")
    intstatuslbl.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
    intstatus = tk.Label(nettabcontfrm, text = GlobalVars.CURRENTINTSTAT)
    intstatus.grid(column = 1, row = 1, sticky=GlobalVars.STATICSTICKY)
    macaddrlbl = tk.Label(nettabcontfrm, text="Mac Address:")
    macaddrlbl.grid(column = 0, row = 2, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
    macaddr = tk.Label(nettabcontfrm)
    macaddr.grid(column = 1, row = 2, sticky=GlobalVars.STATICSTICKY)
    mtulbl = tk.Label(nettabcontfrm, text ="MTU:")
    mtulbl.grid(column = 0, row = 3, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
    mtu = tk.Label(nettabcontfrm)
    mtu.grid(column = 1, row = 3, sticky=GlobalVars.STATICSTICKY)
    ipaddrlbl = tk.Label(nettabcontfrm, text="IP Address:")
    ipaddrlbl.grid(column = 0, row = 4, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
    ipaddr = tk.Label(nettabcontfrm)
    ipaddr.grid(column = 1, row = 4, sticky=GlobalVars.STATICSTICKY)
    submasklbl = tk.Label(nettabcontfrm, text="Subnet Mask:")
    submasklbl.grid(column = 0, row = 5, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
    submask = tk.Label(nettabcontfrm)
    submask.grid(column = 1, row = 5, sticky=GlobalVars.STATICSTICKY)
    defgwlbl = tk.Label(nettabcontfrm, text="Default Gateway:")
    defgwlbl.grid(column = 0, row = 6, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
    defgw = tk.Label(nettabcontfrm)
    defgw.grid(column = 1, row = 6, sticky=GlobalVars.STATICSTICKY)
    bcastaddrlbl = tk.Label(nettabcontfrm, text="Broadcast Address:")
    bcastaddrlbl.grid(column = 0, row = 7, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
    bcastaddr = tk.Label(nettabcontfrm)
    bcastaddr.grid(column = 1, row = 7, sticky=GlobalVars.STATICSTICKY)
    dnsserverslbl = tk.Label(nettabcontfrm, text="DNS Servers:")
    dnsserverslbl.grid(column = 0, row = 8, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
    dnsserveraddr = tk.Label(nettabcontfrm)
    dnsserveraddr.grid(column = 1, row = 8, sticky=GlobalVars.STATICSTICKY)
    dnshostnamelbl = tk.Label(nettabcontfrm, text="DNS Hostname:")
    dnshostnamelbl.grid(column = 0, row = 9, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
    dnshostname = tk.Label(nettabcontfrm)
    dnshostname.grid(column = 1, row = 9, sticky=GlobalVars.STATICSTICKY)
    dnsdomainlbl = tk.Label(nettabcontfrm, text="DNS Domain:")
    dnsdomainlbl.grid(column = 0, row = 10, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
    dnsdomain = tk.Label(nettabcontfrm)
    dnsdomain.grid(column = 1, row = 10, sticky=GlobalVars.STATICSTICKY)
    rxpacketlbl = tk.Label(intstatsfrm, text="RX packets")
    rxpacketlbl.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
    rxpacketcntlbl = tk.Label(intstatsfrm)
    rxpacketcntlbl.grid(column = 1, row = 0, sticky = GlobalVars.STATICSTICKY)
    rxpacketbyteslbl = tk.Label(intstatsfrm, text="bytes")
    rxpacketbyteslbl.grid(column = 2, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
    rxpacketbytescntlbl = tk.Label(intstatsfrm)
    rxpacketbytescntlbl.grid(column = 3, row = 0, sticky = GlobalVars.STATICSTICKY)
    rxpacketbyteshumancntlbl = tk.Label(intstatsfrm)
    rxpacketbyteshumancntlbl.grid(column = 4, row = 0, sticky = GlobalVars.STATICSTICKY)
    rxerrorslbl = tk.Label(intstatsfrm, text="RX errors")
    rxerrorslbl.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
    rxerrorscntlbl = tk.Label(intstatsfrm)
    rxerrorscntlbl.grid(column = 1, row = 1,  sticky = GlobalVars.STATICSTICKY)
    rxdroppedlbl = tk.Label(intstatsfrm, text="dropped")
    rxdroppedlbl.grid(column = 2, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
    rxdroppedcntlbl = tk.Label(intstatsfrm)
    rxdroppedcntlbl.grid(column = 3, row = 1, sticky = GlobalVars.STATICSTICKY)
    rxoverrunslbl = tk.Label(intstatsfrm, text="overruns")
    rxoverrunslbl.grid(column = 4, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
    rxoverrunscntlbl = tk.Label(intstatsfrm)
    rxoverrunscntlbl.grid(column = 5, row = 1, sticky = GlobalVars.STATICSTICKY)
    rxframelbl = tk.Label(intstatsfrm, text="frame")
    rxframelbl.grid(column = 6, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
    rxframecntlbl = tk.Label(intstatsfrm)
    rxframecntlbl.grid(column = 7, row = 1, sticky = GlobalVars.STATICSTICKY)
    txpacketlbl = tk.Label(intstatsfrm, text="TX packets")
    txpacketlbl.grid(column = 0, row = 2, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
    txpacketcntlbl = tk.Label(intstatsfrm)
    txpacketcntlbl.grid(column = 1, row = 2, sticky = GlobalVars.STATICSTICKY)
    txpacketbyteslbl = tk.Label(intstatsfrm, text="bytes")
    txpacketbyteslbl.grid(column = 2, row = 2, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
    txpacketbytescntlbl = tk.Label(intstatsfrm)
    txpacketbytescntlbl.grid(column = 3, row = 2, sticky = GlobalVars.STATICSTICKY)
    txpacketbyteshumcntlbl = tk.Label(intstatsfrm)
    txpacketbyteshumcntlbl.grid(column = 4, row = 2, sticky = GlobalVars.STATICSTICKY)
    txerrorslbl = tk.Label(intstatsfrm, text="TX errors")
    txerrorslbl.grid(column = 0, row = 3, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
    txerrorscntlbl = tk.Label(intstatsfrm)
    txerrorscntlbl.grid(column = 1, row = 3, sticky = "S")
    txdroppedlbl = tk.Label(intstatsfrm, text="dropped")
    txdroppedlbl.grid(column = 2, row = 3, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
    txdroppedcntlbl = tk.Label(intstatsfrm)
    txdroppedcntlbl.grid(column = 3, row = 3, sticky = "S")
    txoverrunslbl = tk.Label(intstatsfrm, text="overruns")
    txoverrunslbl.grid(column = 4, row = 3, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
    txoverrunscntlbl = tk.Label(intstatsfrm)
    txoverrunscntlbl.grid(column = 5, row = 3, sticky = "S")
    txfrmlbl = tk.Label(intstatsfrm, text="carrier")
    txfrmlbl.grid(column = 6, row = 3, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
    txfrmcntlbl = tk.Label(intstatsfrm)
    txfrmcntlbl.grid(column = 7, row = 3, sticky = "S")
    txcolslbl = tk.Label(intstatsfrm, text="collisions")
    txcolslbl.grid(column = 8, row = 3, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky = GlobalVars.STATICSTICKY)
    txcolscntlbl = tk.Label(intstatsfrm)
    txcolscntlbl.grid(column = 9, row = 3)
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
    perftabcpufrm = tk.LabelFrame(perftab, text="CPU Usage")
    perftabcpufrm.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICFULLFRMSTICKY)
    perftabttllbl = tk.Label(perftabcpufrm, text="Test Label")
    perftabttllbl.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICSTICKY)
    cpucanvas = Canvas(perftabcpufrm, width=128, height=128, bg='black')
    cpucanvas.grid(column=0, row=0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
    perftabttlhist = tk.LabelFrame(perftab, text="CPU Usage History")
    perftabttlhist.grid(column = 1, row = 0, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky='NEW', columnspan=3)
    cpuhistcanvas = Canvas(perftabttlhist, width=384, height=128, bg='black')
    #cpuhistcanvas.create_image(128, 192)
    cpuhistcanvas.grid(column=0, row=0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
    perftabmemfrm = tk.LabelFrame(perftab, text="Memory")
    perftabmemfrm.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICFULLFRMSTICKY)
    memcanvas = Canvas(perftabmemfrm, width=128, height=128, bg='black')
    memcanvas.create_text(64, 30, text="_______", fill='#800000', font=('Cantarell Regular', 11, 'bold'))
    memcanvas.create_text(64, 35, text="_______", fill='#666600', font=('Cantarell Regular', 11, 'bold'))
    memcanvas.create_text(64, 40, text="_______", fill='#666600', font=('Cantarell Regular', 11, 'bold'))
    memcanvas.create_text(64, 45, text="_______", fill='#1a6600', font=('Cantarell Regular', 11, 'bold'))
    memcanvas.create_text(64, 50, text="_______", fill='#1a6600', font=('Cantarell Regular', 11, 'bold'))
    memcanvas.create_text(64, 55, text="_______", fill='#1a6600', font=('Cantarell Regular', 11, 'bold'))
    memcanvas.create_text(64, 60, text="_______", fill='#1a6600', font=('Cantarell Regular', 11, 'bold'))
    memcanvas.create_text(64, 65, text="_______", fill='#1a6600', font=('Cantarell Regular', 11, 'bold'))
    memcanvas.create_text(64, 70, text="_______", fill='#1a6600', font=('Cantarell Regular', 11, 'bold'))
    memcanvas.create_text(64, 75, text="_______", fill='#66ff33', font=('Cantarell Regular', 11, 'bold'))
    memcanvas.create_text(64, 80, text="_______", fill='#66ff33', font=('Cantarell Regular', 11, 'bold'))
    memcanvas.grid(column=0, row=0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
    perftabmemhist = tk.LabelFrame(perftab, text="Memory Usage History")
    perftabmemhist.grid(column = 1, row = 1, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky='NEW', columnspan=3)
    memhistcanvas = Canvas(perftabmemhist, width=384, height=128, bg='black')
    memhistcanvas.grid(column=0, row=0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
    perftabtotalsfrm = tk.LabelFrame(perftab, text="Totals")
    perftabtotalsfrm.grid(column = 0, row = 2, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky='NEW', columnspan=2)
    perftabhandlelbl = tk.Label(perftabtotalsfrm, text="Handle:")
    perftabhandlelbl.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = (5, 5), sticky=GlobalVars.STATICSTICKY)
    perftabhandle = tk.Label(perftabtotalsfrm)
    perftabhandle.grid(column = 1, row = 0, padx = GlobalVars.DEFPADX, pady = (5, 5), sticky='E')
    perftabthreadslbl = tk.Label(perftabtotalsfrm, text="Threads:")
    perftabthreadslbl.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = (5, 5), sticky=GlobalVars.STATICSTICKY)
    perftabthreads = tk.Label(perftabtotalsfrm)
    perftabthreads.grid(column = 1, row = 1, padx = GlobalVars.DEFPADX, pady = (5, 5), sticky='E')
    perftabprocslbl = tk.Label(perftabtotalsfrm, text="Processes:")
    perftabprocslbl.grid(column = 0, row = 2, padx = GlobalVars.DEFPADX, pady = (5, 5), sticky=GlobalVars.STATICSTICKY)
    perftabprocs = tk.Label(perftabtotalsfrm)
    perftabprocs.grid(column = 1, row = 2, padx = GlobalVars.DEFPADX, pady = (5, 5), sticky='E')
    perftabphysmemfrm = tk.LabelFrame(perftab, text="Physical Memory (MB)")
    perftabphysmemfrm.grid(column = 2, row = 2, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky='NEW', columnspan=2)
    perftabmemtotallbl = tk.Label(perftabphysmemfrm, text="Total:")
    perftabmemtotallbl.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = (5, 5), sticky=GlobalVars.STATICSTICKY)
    perftabmemtotal = tk.Label(perftabphysmemfrm)
    perftabmemtotal.grid(column = 1, row = 0, padx = GlobalVars.DEFPADX, pady = (5, 5), sticky=GlobalVars.STATICSTICKY)
    perftabmemavaillbl = tk.Label(perftabphysmemfrm, text="Available:")
    perftabmemavaillbl.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = (5, 5), sticky=GlobalVars.STATICSTICKY)
    perftabmemavail = tk.Label(perftabphysmemfrm)
    perftabmemavail.grid(column = 1, row = 1, padx = GlobalVars.DEFPADX, pady = (5, 5), sticky=GlobalVars.STATICSTICKY)
    perftabmemcachelbl = tk.Label(perftabphysmemfrm, text="Buff/Cache:")
    perftabmemcachelbl.grid(column = 0, row = 2, padx = GlobalVars.DEFPADX, pady = (5, 5), sticky=GlobalVars.STATICSTICKY)
    perftabmemcache = tk.Label(perftabphysmemfrm)
    perftabmemcache.grid(column = 1, row = 2, padx = GlobalVars.DEFPADX, pady = (5, 5), sticky=GlobalVars.STATICSTICKY)
    perftabtotalsfrm = tk.LabelFrame(perftab, text="Commit Charge (K)")
    perftabtotalsfrm.grid(column = 0, row = 3, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky='NEW', columnspan=2)
    perftabcommittotallbl = tk.Label(perftabtotalsfrm, text="Total:")
    perftabcommittotallbl.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = (5, 5), sticky=GlobalVars.STATICSTICKY)
    perftabcommittotal = tk.Label(perftabtotalsfrm)
    perftabcommittotal.grid(column = 1, row = 0, padx = GlobalVars.DEFPADX, pady = (5, 5), sticky=GlobalVars.STATICSTICKY)
    perftabcommitlimitlbl = tk.Label(perftabtotalsfrm, text="Limit:")
    perftabcommitlimitlbl.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = (5, 5), sticky=GlobalVars.STATICSTICKY)
    perftabcommitlimit = tk.Label(perftabtotalsfrm)
    perftabcommitlimit.grid(column = 1, row = 1, padx = GlobalVars.DEFPADX, pady = (5, 5), sticky=GlobalVars.STATICSTICKY)
    perftabcommitpeaklbl = tk.Label(perftabtotalsfrm, text="Peak:")
    perftabcommitpeaklbl.grid(column = 0, row = 2, padx = GlobalVars.DEFPADX, pady = (5, 5), sticky=GlobalVars.STATICSTICKY)
    perftabcommitpeak = tk.Label(perftabtotalsfrm)
    perftabcommitpeak.grid(column = 1, row = 2, padx = GlobalVars.DEFPADX, pady = (5, 5), sticky=GlobalVars.STATICSTICKY)
    perftabphysmemfrm = tk.LabelFrame(perftab, text="Swap Memory (MB)")
    perftabphysmemfrm.grid(column = 2, row = 3, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky='NEW', columnspan=2)
    perftabswaptotallbl = tk.Label(perftabphysmemfrm, text="Total:")
    perftabswaptotallbl.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = (5, 5), sticky=GlobalVars.STATICSTICKY)
    perftabswaptotal = tk.Label(perftabphysmemfrm)
    perftabswaptotal.grid(column = 1, row = 0, padx = GlobalVars.DEFPADX, pady = (5, 5), sticky=GlobalVars.STATICSTICKY)
    perftabswapusedlbl = tk.Label(perftabphysmemfrm, text="Used:")
    perftabswapusedlbl.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = (5, 5), sticky=GlobalVars.STATICSTICKY)
    perftabswapused = tk.Label(perftabphysmemfrm)
    perftabswapused.grid(column = 1, row = 1, padx = GlobalVars.DEFPADX, pady = (5, 5), sticky=GlobalVars.STATICSTICKY)
    perftabswapfreelbl = tk.Label(perftabphysmemfrm, text="Free:")
    perftabswapfreelbl.grid(column = 0, row = 2, padx = GlobalVars.DEFPADX, pady = (5, 5), sticky=GlobalVars.STATICSTICKY)
    perftabswapfree = tk.Label(perftabphysmemfrm)
    perftabswapfree.grid(column = 1, row = 2, padx = GlobalVars.DEFPADX, pady = (5, 5), sticky=GlobalVars.STATICSTICKY)
    perftabstatslblfrm = tk.Frame(perftab)
    perftabstatslblfrm.grid(column = 0, row = 4, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky='NEW', columnspan=4)
    perftabstatsproclbl = tk.Label(perftabstatslblfrm, text="Processes:")
    perftabstatsproclbl.grid(column=0, row=0, padx=GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICSTICKY)
    perftabstatsproc = tk.Label(perftabstatslblfrm)
    perftabstatsproc.grid(column=1, row=0, padx=GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICSTICKY)
    perftabstatscpulbl = tk.Label(perftabstatslblfrm, text="CPU Usage:")
    perftabstatscpulbl.grid(column=2, row=0, padx=GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICSTICKY)
    perftabstatscpu = tk.Label(perftabstatslblfrm)
    perftabstatscpu.grid(column=3, row=0, padx=GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICSTICKY)
    perftabstatmemuselbl = tk.Label(perftabstatslblfrm, text="Mem Usage:")
    perftabstatmemuselbl.grid(column=4, row=0, padx=GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICSTICKY)
    perftabstatmemuse = tk.Label(perftabstatslblfrm)
    perftabstatmemuse.grid(column=5, row=0, padx=GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICSTICKY)
    perftabstatmemuselbl2 = tk.Label(perftabstatslblfrm, text="/")
    perftabstatmemuselbl2.grid(column=6, row=0, padx=GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICSTICKY)
    perftabstatmemusetotal = tk.Label(perftabstatslblfrm)
    perftabstatmemusetotal.grid(column=7, row=0, padx=GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICSTICKY)
    wrlssintlbl = tk.Label(wrlsstab, text ="WLAN Interface Name:")
    wrlssintlbl.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky='NW')
    wrlssintcombo = ttk.Combobox(wrlsstab, values = GlobalVars.WRLSSINTLIST)
    wrlssintcombo.grid(column = 1, row = 0, pady = (10, 5), sticky='NW')
    wrlssintcombo.set("Select Interface:")
    wrlssintcombo.bind('<<ComboboxSelected>>', lambda event: GUIActions.selwrlssint())
    wrlsstabttlfrm = tk.LabelFrame(wrlsstab, text="Connection Status")
    wrlsstabttlfrm.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICFULLFRMSTICKY, columnspan=2)
    wrlssavailtabttlfrm = tk.LabelFrame(wrlsstab, text="Available Networks")
    wrlssavailtabttlfrm.grid(column = 0, row = 2, padx = GlobalVars.DEFPADX, pady = (10, 5), sticky=GlobalVars.STATICFULLFRMSTICKY, columnspan=2)
    wrlssavail = tksheet.Sheet(wrlssavailtabttlfrm)
    wrlssavail.grid(padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY)
    wrlssavail.enable_bindings(("row_select"))
    wrlsstabbtnfrm = tk.Frame(wrlsstab)
    wrlsstabbtnfrm.grid(column = 3, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N', rowspan=2)
    wrlsstabbtn2frm = tk.Frame(wrlsstab)
    wrlsstabbtn2frm.grid(column = 3, row = 2, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N', rowspan=2)
    rfwrlssbtn = tk.Button(wrlsstabbtn2frm, text="Refresh", width = GlobalVars.BTNSIZE)
    rfwrlssbtn.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
    connectwrlssbtn = tk.Button(wrlsstabbtn2frm, text="Connect", width = GlobalVars.BTNSIZE, state="disabled")
    connectwrlssbtn.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
    disconnectwrlssbtn = tk.Button(wrlsstabbtn2frm, text="Disconnect", width = GlobalVars.BTNSIZE, state="disabled")
    disconnectwrlssbtn.grid(column = 0, row = 2, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
    wrlssdisableintbtn = tk.Button(wrlsstabbtnfrm, text ="Disable", width = GlobalVars.BTNSIZE, command=GUIActions.toggleinterface, state="disabled")
    wrlssdisableintbtn.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
    wrlssrefreshbtn = tk.Button(wrlsstabbtnfrm, text = "Refresh Stats", width = GlobalVars.BTNSIZE, command=GUIActions.refreshintstats, state="disabled")
    wrlssrefreshbtn.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky='N')
    wrlssintstatuslbl = tk.Label(wrlsstabttlfrm, text="Interface Status:")
    wrlssintstatuslbl.grid(column = 0, row = 0, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
    wrlssintstatus = tk.Label(wrlsstabttlfrm, text = GlobalVars.CURRENTWRLSSINTSTAT)
    wrlssintstatus.grid(column = 1, row = 0, sticky=GlobalVars.STATICSTICKY)
    wrlsstype = tk.Label(wrlsstabttlfrm, text="IEEE 802.11")
    wrlsstype.grid(column = 0, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
    wrlssessidlbl = tk.Label(wrlsstabttlfrm, text="ESSID:")
    wrlssessidlbl.grid(column = 1, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
    wrlssessid = tk.Label(wrlsstabttlfrm)
    wrlssessid.grid(column = 2, row = 1, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
    wrlssmodelbl = tk.Label(wrlsstabttlfrm, text="Mode:")
    wrlssmodelbl.grid(column = 0, row = 2, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
    wrlssmode = tk.Label(wrlsstabttlfrm)
    wrlssmode.grid(column = 1, row = 2, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
    wrlssfreqlbl = tk.Label(wrlsstabttlfrm, text="Freq:")
    wrlssfreqlbl.grid(column = 2, row = 2, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
    wrlssfreq = tk.Label(wrlsstabttlfrm)
    wrlssfreq.grid(column = 3, row = 2, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
    wrlssaplbl = tk.Label(wrlsstabttlfrm, text="AP:")
    wrlssaplbl.grid(column = 4, row = 2, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
    wrlssap = tk.Label(wrlsstabttlfrm)
    wrlssap.grid(column = 5, row = 2, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
    wrlssbitratelbl = tk.Label(wrlsstabttlfrm, text="Bit Rate:")
    wrlssbitratelbl.grid(column = 0, row = 3, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
    wrlssbitrate = tk.Label(wrlsstabttlfrm)
    wrlssbitrate.grid(column = 1, row = 3, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
    wrlsstxpwrlbl = tk.Label(wrlsstabttlfrm, text="Tx-Pwr:")
    wrlsstxpwrlbl.grid(column = 2, row = 3, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
    wrlsstxpwr = tk.Label(wrlsstabttlfrm)
    wrlsstxpwr.grid(column = 3, row = 3, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
    wrlssretrylbl = tk.Label(wrlsstabttlfrm, text="Retry:")
    wrlsspmlbl = tk.Label(wrlsstabttlfrm, text="Power Management:")
    wrlsspmlbl.grid(column = 0, row = 4, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY, columnspan=2)
    wrlsspm = tk.Label(wrlsstabttlfrm)
    wrlsspm.grid(column = 2, row = 4, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
    wrlsslnkquallbl = tk.Label(wrlsstabttlfrm, text="Link Qual:")
    wrlsslnkquallbl.grid(column = 0, row = 5, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
    wrlsslnkqual = tk.Label(wrlsstabttlfrm)
    wrlsslnkqual.grid(column = 1, row = 5, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
    wrlsssignallbl = tk.Label(wrlsstabttlfrm, text="Signal:")
    wrlsssignallbl.grid(column = 2, row = 5, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)
    wrlsssignal = tk.Label(wrlsstabttlfrm)
    wrlsssignal.grid(column = 3, row = 5, padx = GlobalVars.DEFPADX, pady = GlobalVars.DEFPADY, sticky=GlobalVars.STATICSTICKY)

GUIActions.getmemoryinfo()
GUIActions.getprocinfo()
app=BuildGUI()
root.mainloop()
