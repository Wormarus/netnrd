from tkinter import *
from tkinter import ttk
import tkinter.simpledialog
import tkinter.messagebox
from tkinter import messagebox
import subprocess
import os

class App(Tk):

    def __init__(self):
        super(App, self).__init__()

        self.title("NETnrd")
        self.minsize(200, 100)
        self.resizable(width=False, height=False)
        self.configure(bg="white")

        tabControl = ttk.Notebook(self)
        self.tab1 = ttk.Frame(tabControl)
        tabControl.add(self.tab1, text="UNTU")

        self.tab2 = ttk.Frame(tabControl)
        tabControl.add(self.tab2, text="QoS")
        self.tab3 = ttk.Frame(tabControl)

        tabControl.add(self.tab3, text="Setup")
        tabControl.pack(expand=1, fill="both")

        self.widgets()

        '''NAT change'''

    def widgets(self):

        def routero():
            stat["text"] = "Open"
            stat['fg'] = "green"
            messagebox.showinfo("Important Note",
                                "There`s no consistent Open NAT Script at the moment.\nCurrent script may or may not work for you, depending on your firewall rules.")
            subprocess.call("./opn.sh")

        def routerm():
            stat["text"] = "Moderate"
            stat['fg'] = "orange"
            subprocess.call("./mod.sh")

        def routers():
            stat["text"] = "Strict"
            stat['fg'] = "red"
            subprocess.call("./str.sh")

        def routerf():
            stat["text"] = "Inactive"
            stat['fg'] = "black"
            subprocess.call("./rstop.sh")

        def spd1():
            messagebox.showinfo("Important Note",
                                "The consumption is shown in a terminal through which app was lauched. To stop the monitoring tool use <Ctrl+C> combination.")
            subprocess.call("./spd.sh")

        def pccust():
            valueu = tkinter.simpledialog.askstring("Packet Corruption upstream",
                                                    "Please insert your desired upstream corruption (in %): ")
            valued = tkinter.simpledialog.askstring("Packet Corruption downstream",
                                                    "Please insert your desired downstream corruption (in %): ")
            with open("pc.sh") as f:
                lines = f.readlines()
                lines = [l for l in lines]
                with open("pc1.sh", "w+") as f1:
                    f1.writelines(lines)

            g1 = open('pc.sh', 'r')
            g2 = open('pc1.sh', 'w')

            checkWords = ("customu", "customd")
            repWords = (valueu, valued)

            for line in g1:
                for check, rep in zip(checkWords, repWords):
                    line = line.replace(check, rep)
                g2.write(line)
            g1.close()
            g2.close()

            subprocess.call("./pc1.sh")

        def prcust():
            messagebox.showinfo("Important Note",
                                "Every other packet will be reordered.")
            subprocess.call("./pr.sh")

        def pdcust():
            valueu = tkinter.simpledialog.askstring("Packet Duplication upstream",
                                                    "Please insert your desired upstream duplication (in %): ")
            valued = tkinter.simpledialog.askstring("Packet Duplication downstream",
                                                    "Please insert your desired downstream duplication (in %): ")
            with open("pd.sh") as f:
                lines = f.readlines()
                lines = [l for l in lines]
                with open("pd1.sh", "w+") as f1:
                    f1.writelines(lines)

            g1 = open('pd.sh', 'r')
            g2 = open('pd1.sh', 'w')

            checkWords = ("customu", "customd")
            repWords = (valueu, valued)

            for line in g1:
                for check, rep in zip(checkWords, repWords):
                    line = line.replace(check, rep)
                g2.write(line)
            g1.close()
            g2.close()

            subprocess.call("./pd1.sh")

        label_0 = Label(self.tab1, text="Current status: ", font="Helvetica 11 bold")
        stat = Label(self.tab1, width="10", height="1", text="Inactive", font="Helvetica 11 bold", bd="20")

        spacer1 = Label(self.tab1, width="5", pady="20")
        spacer2 = Label(self.tab1, width="5", padx="15")

        rlabel = Label(self.tab1, width="10", height="1", text="Linux Router", padx="20", font="Helvetica 9 bold")
        rlabel1 = Label(self.tab1, width="10", height="1", text="Additional features", padx="20", font="Helvetica 9 bold")
        button_1 = Button(self.tab1, text="Open", width="10", command=routero)
        button_2 = Button(self.tab1, text="Moderate", width="10", command=routerm)
        button_3 = Button(self.tab1, text="Strict", width="10", command=routers)
        button_4 = Button(self.tab1, text="Turn off", width="13", command=routerf)
        button_5 = Button(self.tab1, text="Monitoring Tool", width="13", command=spd1)
        button_6 = Button(self.tab1, text="Packet corruption", width="14", command=pccust)
        button_7 = Button(self.tab1, text="Packet duplication", width="14", command=pdcust)
        button_8 = Button(self.tab1, text="Packet re-ordering", width="14", command=prcust)

        label_0.grid(row=1, column=3)
        stat.grid(row=1, column=4)

        spacer1.grid(row=3, column=2,)
        spacer2.grid(row=0, column=2)

        rlabel.grid(row=0, column=0)
        button_1.grid(row=1, column=0)
        button_2.grid(row=2, column=0)
        button_3.grid(row=3, column=0)

        rlabel1.grid(row=0, column=1)
        button_4.grid(row=2, column=4)
        button_5.grid(row=3, column=4)
        button_6.grid(row=1, column=1)
        button_7.grid(row=2, column=1)
        button_8.grid(row=3, column=1)

        '''NETEM'''

        def bnorm():
            label_1["text"] = "Bandwidth Normal"
            label_1['fg'] = "green"
            subprocess.call("./bnorm.sh")

        def bbad():
            label_1["text"] = "Bandwidth Bad"
            label_1['fg'] = "orange"
            subprocess.call("./bbad.sh")

        def bxtr():
            label_1["text"] = "Bandwidth Extreme"
            label_1['fg'] = "red"
            subprocess.call("./bxtr.sh")

        def bcust():
            label_1["text"] = "Bandwidth Custom"
            label_1['fg'] = "blue"
            valueu = tkinter.simpledialog.askstring("Bandwidth restriction upstream", "Please insert your desired downstream limitation (in kbit): ")
            valued = tkinter.simpledialog.askstring("Bandwidth restriction downstream", "Please insert your desired upstream limitation (in kbit): ")

            with open("bcust.sh") as f:
                lines = f.readlines()
                lines = [l for l in lines]
                with open("bcust1.sh", "w+") as f1:
                    f1.writelines(lines)

            g1 = open('bcust.sh', 'r')
            g2 = open('bcust1.sh', 'w')

            checkWords = ("customu", "customd")
            repWords = (valueu, valued)

            for line in g1:
                for check, rep in zip(checkWords, repWords):
                    line = line.replace(check, rep)
                g2.write(line)
            g1.close()
            g2.close()

            subprocess.call("./bcust1.sh")

        def lnorm():
            label_1["text"] = "Latency Normal"
            label_1['fg'] = "green"
            subprocess.call("./lnorm.sh")

        def lbad():
            label_1["text"] = "Latency Bad"
            label_1['fg'] = "orange"
            subprocess.call("./lbad.sh")

        def lxtr():
            label_1["text"] = "Latency Extreme"
            label_1['fg'] = "red"
            subprocess.call("./lxtr.sh")

        def lcust():
            label_1["text"] = "Latency Custom"
            label_1['fg'] = "blue"

            valueu = tkinter.simpledialog.askstring("Latency restriction upstream", "Please insert your desired upstream limitation (in ms): ")
            valued = tkinter.simpledialog.askstring("Latency restriction downstream", "Please insert your desired downstream limitation (in ms): ")
            with open("lcust.sh") as f:
                lines = f.readlines()
                lines = [l for l in lines]
                with open("lcust1.sh", "w+") as f1:
                    f1.writelines(lines)

            g1 = open('lcust.sh', 'r')
            g2 = open('lcust1.sh', 'w')

            checkWords = ("customu", "customd")
            repWords = (valueu, valued)

            for line in g1:
                for check, rep in zip(checkWords, repWords):
                    line = line.replace(check, rep)
                g2.write(line)
            g1.close()
            g2.close()

            subprocess.call("./lcust1.sh")

        def pnorm():
            label_1["text"] = "Packet Loss Normal"
            label_1['fg'] = "green"
            subprocess.call("./plnorm.sh")

        def pbad():
            label_1["text"] = "Packet Loss Bad"
            label_1['fg'] = "orange"
            subprocess.call("./plbad.sh")

        def pxtr():
            label_1["text"] = "Packet Loss Extreme"
            label_1['fg'] = "red"
            subprocess.call("./plxtr.sh")

        def pcust():
            label_1["text"] = "Packet Loss Custom"
            label_1['fg'] = "blue"
            valueu = tkinter.simpledialog.askstring("Packet Loss restriction upstream",
                                                    "Please insert your desired upstream limitation (in %): ")
            valued = tkinter.simpledialog.askstring("Packet Loss restriction downstream",
                                                    "Please insert your desired downstream limitation (in %): ")
            with open("plcust.sh") as f:
                lines = f.readlines()
                lines = [l for l in lines]
                with open("plcust1.sh", "w+") as f1:
                    f1.writelines(lines)

            g1 = open('plcust.sh', 'r')
            g2 = open('plcust1.sh', 'w')

            checkWords = ("customu", "customd")
            repWords = (valueu, valued)

            for line in g1:
                for check, rep in zip(checkWords, repWords):
                    line = line.replace(check, rep)
                g2.write(line)
            g1.close()
            g2.close()

            subprocess.call("./plcust1.sh")

        def cnorm():
            label_1["text"] = "Combined Normal"
            label_1['fg'] = "green"
            subprocess.call("./cnorm.sh")

        def cbad():
            label_1["text"] = "Combined Bad"
            label_1['fg'] = "orange"
            subprocess.call("./cbad.sh")

        def cxtr():
            label_1["text"] = "Combined Extreme"
            label_1['fg'] = "red"
            subprocess.call("./cxtr.sh")

        def ccust():
            label_1["text"] = "Combined Custom"
            label_1['fg'] = "blue"
            cbup = tkinter.simpledialog.askstring("Bandwidth restriction upstream", "Please insert your desired upstream limitation(in kbit): ")
            cbdown = tkinter.simpledialog.askstring("Bandwidth restriction downstream", "Please insert your desired downstream limitation(in kbit): ")
            clup = tkinter.simpledialog.askstring("Latency restriction upstream", "Please insert your desired upstream limitation (in ms): ")
            cldown = tkinter.simpledialog.askstring("Latency restriction downstream", "Please insert your desired downstream limitation (in ms): ")
            cpup = tkinter.simpledialog.askstring("Packet loss restriction upstream", "Please insert your desired upstream limitation (in %): ")
            cpdown = tkinter.simpledialog.askstring("Packet loss restriction downstream", "Please insert your desired downstream limitation (in %): ")

            with open("ccust.sh") as f:
                lines = f.readlines()
                lines = [l for l in lines]
                with open("ccust1.sh", "w+") as f1:
                    f1.writelines(lines)

            g1 = open('ccust.sh', 'r')
            g2 = open('ccust1.sh', 'w')

            checkWords = ("customu1", "customd1", "customu2", "customd2", "customu3", "customd3")
            repWords = (cbup, cbdown, clup, cldown, cpup, cpdown)

            for line in g1:
                for check, rep in zip(checkWords, repWords):
                    line = line.replace(check, rep)
                g2.write(line)
            g1.close()
            g2.close()

            subprocess.call("./ccust1.sh")

        def x1():
            label_1["text"] = "None"
            label_1['fg'] = "black"
            subprocess.call("./stop.sh")

        def x2():
            subprocess.call("./exp.sh")
            messagebox.showinfo("Export Info", "Information is exported to 'log.txt' file in 'Home' folder")

        bl1 = Label(self.tab2, width="22", height="1", text="Bandwidth", font="Helvetica 9 bold")
        b1 = Button(self.tab2, text="Normal", width="10", command=bnorm)
        b2 = Button(self.tab2, text="Bad", width="10", command=bbad)
        b3 = Button(self.tab2, text="Extreme", width="10", command=bxtr)
        b4 = Button(self.tab2, text="Custom", width="10", command=bcust)

        ll1 = Label(self.tab2, width="22", height="1", text="Latency", font="Helvetica 9 bold")
        l1 = Button(self.tab2, text="Normal", width="10", command=lnorm)
        l2 = Button(self.tab2, text="Bad", width="10", command=lbad)
        l3 = Button(self.tab2, text="Extreme", width="10", command=lxtr)
        l4 = Button(self.tab2, text="Custom", width="10", command=lcust)

        pl1 = Label(self.tab2, width="25", height="1", text="Packet Loss", font="Helvetica 9 bold")
        p1 = Button(self.tab2, text="Normal", width="10", command=pnorm)
        p2 = Button(self.tab2, text="Bad", width="10", command=pbad)
        p3 = Button(self.tab2, text="Extreme", width="10", command=pxtr)
        p4 = Button(self.tab2, text="Custom", width="10", command=pcust)

        cl1 = Label(self.tab2, width="22", height="1", text="Combined", font="Helvetica 9 bold")
        c1 = Button(self.tab2, text="Normal", width="10", command=cnorm)
        c2 = Button(self.tab2, text="Bad", width="10", command=cbad)
        c3 = Button(self.tab2, text="Extreme", width="10", command=cxtr)
        c4 = Button(self.tab2, text="Custom", width="10", command=ccust)

        label_0 = Label(self.tab2, width="17", pady="8", text="Current restriction: ", font="Helvetica 10 bold")
        label_1 = Label(self.tab2, width="20", text="None", font="Helvetica 10 bold")
        x1 = Button(self.tab2, text="STOP", width="10", font="Helvetica 10 bold", command=x1)
        x2 = Button(self.tab2, text="Export Info", font="Helvetica 10 bold", width="10", command=x2)

        bl1.grid(row=0, column=0)
        b1.grid(row=1, column=0)
        b2.grid(row=2, column=0)
        b3.grid(row=3, column=0)
        b4.grid(row=4, column=0)

        ll1.grid(row=0, column=1)
        l1.grid(row=1, column=1)
        l2.grid(row=2, column=1)
        l3.grid(row=3, column=1)
        l4.grid(row=4, column=1)

        pl1.grid(row=0, column=2)
        p1.grid(row=1, column=2)
        p2.grid(row=2, column=2)
        p3.grid(row=3, column=2)
        p4.grid(row=4, column=2)

        cl1.grid(row=0, column=3)
        c1.grid(row=1, column=3)
        c2.grid(row=2, column=3)
        c3.grid(row=3, column=3)
        c4.grid(row=4, column=3)

        label_0.grid(row=6, column=0)
        label_1.grid(row=6, column=1)
        x1.grid(row=6, column=2)
        x2.grid(row=6, column=3)

        '''OS Config'''

        def notif():
            messagebox.showinfo("Important Notes","DO NOT use 'Setup pt.1 & pt.2' buttons more than once per OS intallation. If you need to change anything, please refer to 'Change Setup Info' section.")

        def devs():
            messagebox.showinfo("Developers","Created by Wormarus\n Contact me:\n<wormarus.git@gmail.com>")

        def update():

            upd6 = "#!/bin/bash\nyes | apt-get install net-tools\nyes | apt-get install speedometer\nyes | apt-get install bind9 dnsutils\nyes | apt-get install isc-dhcp-server"
            uupd6 = open("update6.sh", "w+")
            uupd6.write(upd6)
            os.chmod("update6.sh", 700)

            getinf = "#!/bin/bash\necho 'Below you may find your DHCP assigned WAN IP & NIC names.' >> NETINFO.txt\nifconfig -a >> NETINFO.txt\necho 'Below you may fing your WAN defaullt gateway.' >> NETINFO.txt\nip route | grep default >> NETINFO.txt"
            ggetinf = open("getinf.sh", "w+")
            ggetinf.write(getinf)
            os.chmod("getinf.sh", 700)

        def update6():
            subprocess.call("./update6.sh")

        def getinf():
            subprocess.call("./getinf.sh")

        def bash():

            req1 = tkinter.simpledialog.askstring("LAN Interface",
                                                    "Please insert your LAN Interface (e.g. 'enp3s0'): ")
            req2 = tkinter.simpledialog.askstring("WAN Interface",
                                                    "Please insert your WAN Interface (e.g. 'enp6s1'): ")
            req3 = tkinter.simpledialog.askstring("DHCP assigned WAN IP",
                                                    "Please insert your DHCP assigned WAN IP on Ubuntu (e.g. '195.88.83.164'): ")
            req5 = tkinter.simpledialog.askstring("LAN Gateway on destination device",
                                                    "Please insert your LAN Gateway on destination device(e.g. '192.168.1.1'): ")

            bn = "#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem rate 1000kbit\ntc qdisc add dev {} root netem rate 1000kbit".format(req1, req2, req1, req2)
            bb = "#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem rate 500kbit\ntc qdisc add dev {} root netem rate 500kbit".format(req1, req2, req1, req2)
            bx = "#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem rate 250kbit\ntc qdisc add dev {} root netem rate 250kbit".format(req1, req2, req1, req2)
            bc = "#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem rate customukbit\ntc qdisc add dev {} root netem rate customdkbit".format(req1, req2, req1, req2)

            ln = "#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem delay 100ms\ntc qdisc add dev {} root netem delay 100ms".format(req1, req2, req1, req2)
            lb = "#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem delay 300ms\ntc qdisc add dev {} root netem delay 300ms".format(req1, req2, req1, req2)
            lx = "#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem delay 500ms\ntc qdisc add dev {} root netem delay 500ms".format(req1, req2, req1, req2)
            lc = "#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem delay customums\ntc qdisc add dev {} root netem delay customdms".format(req1, req2, req1, req2)

            pln = "#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem loss 1%\ntc qdisc add dev {} root netem loss 1%".format(req1, req2, req1, req2)
            plb = "#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem loss 5%\ntc qdisc add dev {} root netem loss 5%".format(req1, req2, req1, req2)
            plx = "#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem loss 13%\ntc qdisc add dev {} root netem loss 12%".format(req1, req2, req1, req2)
            plc = "#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem loss customu%\ntc qdisc add dev {} root netem loss customd%".format(req1, req2, req1, req2)

            cn = "#!/bin/bash\n#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem rate 1000kbit delay 100ms loss 1%\ntc qdisc add dev {} root netem rate 1000kbit delay 100ms loss 1%".format(
                req1, req2, req1, req2)
            cb = "#!/bin/bash\n#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem rate 500kbit delay 300ms loss 5%\ntc qdisc add dev {} root netem rate 500kbit delay 300ms loss 5%".format(
                req1, req2, req1, req2)
            cx = "#!/bin/bash\n#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem rate 250kbit delay 500ms loss 13%\ntc qdisc add dev {} root netem rate 250kbit delay 500ms loss 12%".format(
                req1, req2, req1, req2)
            cc = "#!/bin/bash\n#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem rate customu1kbit delay customu2ms loss customu3%\ntc qdisc add dev {} root netem rate customd1kbit delay customd2ms loss customd3%".format(
                req1, req2, req1, req2)

            pd = "#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem duplicate customu%\ntc qdisc add dev {} root netem duplicate customd%".format(req1, req2, req1, req2)
            pc = "#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem corrupt customu%\ntc qdisc add dev {} root netem corrupt customd%".format(req1, req2, req1, req2)
            pr = "#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem gap 5 delay 10ms".format(req1, req2, req1)

            stp = "#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root".format(req1, req2)
            vwv = "#!/bin/bash\ndate >> log.txt\ntc -s qdisc ls dev {} >> log.txt\ntc -s qdisc ls dev {} >> log.txt".format(req1, req2)
            spd = "#!/bin/bash\nspeedometer -s -l -t {} -s -l -t {} -m $((2048*2048*3/2))".format(req1, req2)

            opn = "#!/bin/bash\niptables -F\niptables -X\niptables -t nat -F\niptables -t nat -X\niptables -t mangle -F\niptables -t mangle -X\niptables -P INPUT ACCEPT\niptables -P FORWARD ACCEPT\niptables -P OUTPUT ACCEPT\niptables -t nat -A POSTROUTING -o {} -j SNAT --to-source {}\niptables -t nat -A PREROUTING -i {} -j DNAT --to-destination {}\niptables -A FORWARD -i {} -o {} -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT\niptables -A FORWARD -i {} -o {} -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT\niptables -A INPUT -i {} -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT\niptables -A INPUT -i {} -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT\nifdown {}\nifup {}\nifdown {}\nifup {}\n/etc/init.d/networking restart\n/etc/init.d/networking reload".format(
                req2, req3, req2, req5, req1, req2, req2, req1, req1, req2, req1, req1, req2, req2)
            mod = "#!/bin/bash\niptables -F\niptables -X\niptables -t nat -F\niptables -t nat -X\niptables -t mangle -F\niptables -t mangle -X\niptables -P INPUT ACCEPT\niptables -P FORWARD ACCEPT\niptables -P OUTPUT ACCEPT\niptables -t nat -A POSTROUTING -o {} -j SNAT --to-source {}\niptables -t nat -A PREROUTING -i {} -j DNAT --to-destination {}\niptables -A INPUT -i {} -p tcp -m state --state ESTABLISHED,RELATED -j ACCEPT\niptables -A INPUT -i {} -p udp -m state --state ESTABLISHED,RELATED -j ACCEPT\niptables -A INPUT -i {} -p tcp -m state --state NEW -j DROP\niptables -A INPUT -i {} -p udp -m state --state NEW -j DROP\nifdown {}\nifup {}\nifdown {}\nifup {}\n/etc/init.d/isc-dhcp-server restart\n/etc/init.d/networking restart\n/etc/init.d/networking reload".format(
                req2, req3, req2, req5, req2, req2, req2, req2, req1, req1, req2, req2)
            str = "#!/bin/bash\niptables -F\niptables -X\niptables -t nat -F\niptables -t nat -X\niptables -t mangle -F\niptables -t mangle -X\niptables -P INPUT ACCEPT\niptables -P FORWARD ACCEPT\niptables -P OUTPUT ACCEPT\niptables -t nat -A POSTROUTING -o {} -j MASQUERADE --random\niptables -A FORWARD -i {} -o {} -m state --state RELATED, ESTABLISHED -j ACCEPT\niptables -A FORWARD -i {} -o {}  -j ACCEPT\nifdown {}\nifup {}\nifdown {}\nifup {}\n/etc/init.d/networking restart\n/etc/init.d/networking reload".format(
                req2, req2, req1, req1, req2, req1, req1, req2, req2)
            rstp = "#!/bin/bash\niptables -F\niptables -X\niptables -t nat -F\niptables -t nat -X\niptables -t mangle -F\niptables -t mangle -X\niptables -P INPUT ACCEPT\niptables -P FORWARD ACCEPT\niptables -P OUTPUT ACCEPT\nifdown {}\nifup {}\nifdown {}\nifup {}\n/etc/init.d/networking restart\n/etc/init.d/networking reload".format(
                req1, req1, req2, req2)

            bnn = open("bnorm.sh", "w+")
            bbb = open("bbad.sh", "w+")
            bxx = open("bxtr.sh", "w+")
            bcc = open("bcust.sh", "w+")
            bcc1 = open("bcust1.sh", "w+")

            lnn = open("lnorm.sh", "w+")
            lbb = open("lbad.sh", "w+")
            lxx = open("lxtr.sh", "w+")
            lcc= open("lcust.sh", "w+")
            lcc1= open("lcust1.sh", "w+")

            plnn = open("plnorm.sh", "w+")
            plbb = open("plbad.sh", "w+")
            plxx = open("plxtr.sh", "w+")
            plcc = open("plcust.sh", "w+")
            plcc1 = open("plcust1.sh", "w+")

            cnn = open("cnorm.sh", "w+")
            cbb = open("cbad.sh", "w+")
            cxx = open("cxtr.sh", "w+")
            ccc = open("ccust.sh", "w+")
            ccc1 = open("ccust1.sh", "w+")

            prw = open("pr.sh", "w+")
            pdw = open("pd.sh", "w+")
            pcw = open("pc.sh", "w+")
            pdw1 = open("pd1.sh", "w+")
            pcw1 = open("pc1.sh", "w+")

            stpp = open("stop.sh", "w+")
            vwvw = open("exp.sh", "w+")
            spd2 = open("spd.sh", "w+")

            ropn = open ("opn.sh", "w+")
            rmod = open ("mod.sh", "w+")
            rstr = open ("str.sh", "w+")
            rrstp = open ("rstop.sh", "w+")

            bnn.write(bn)
            bbb.write(bb)
            bxx.write(bx)
            bcc.write(bc)
            bcc1.write(bc)

            lnn.write(ln)
            lbb.write(lb)
            lxx.write(lx)
            lcc.write(lc)
            lcc1.write(lc)

            plnn.write(pln)
            plbb.write(plb)
            plxx.write(plx)
            plcc.write(plc)
            plcc1.write(plc)

            cnn.write(cn)
            cbb.write(cb)
            cxx.write(cx)
            ccc.write(cc)
            ccc1.write(cc)

            stpp.write(stp)
            vwvw.write(vwv)
            spd2.write(spd)

            pcw.write(pc)
            prw.write(pr)
            pdw.write(pd)
            pcw1.write(pc)
            pdw1.write(pd)

            ropn.write(opn)
            rmod.write(mod)
            rstr.write(str)
            rrstp.write(rstp)

            os.chmod("bnorm.sh", 700)
            os.chmod("bbad.sh", 700)
            os.chmod("bxtr.sh", 700)
            os.chmod("bcust.sh", 700)
            os.chmod("bcust1.sh", 700)

            os.chmod("lnorm.sh", 700)
            os.chmod("lbad.sh", 700)
            os.chmod("lxtr.sh", 700)
            os.chmod("lcust.sh", 700)
            os.chmod("lcust1.sh", 700)

            os.chmod("plnorm.sh", 700)
            os.chmod("plbad.sh", 700)
            os.chmod("plxtr.sh", 700)
            os.chmod("plcust.sh", 700)
            os.chmod("plcust1.sh", 700)

            os.chmod("cnorm.sh", 700)
            os.chmod("cbad.sh", 700)
            os.chmod("cxtr.sh", 700)
            os.chmod("ccust.sh", 700)
            os.chmod("ccust1.sh", 700)

            os.chmod("stop.sh", 700)
            os.chmod("exp.sh", 700)
            os.chmod("spd.sh", 700)

            os.chmod("pc.sh", 700)
            os.chmod("pd.sh", 700)
            os.chmod("pr.sh", 700)
            os.chmod("pc1.sh", 700)
            os.chmod("pd1.sh", 700)

            os.chmod("opn.sh", 700)
            os.chmod("mod.sh", 700)
            os.chmod("str.sh", 700)
            os.chmod("rstop.sh", 700)

        def consys():
            req1 = tkinter.simpledialog.askstring("LAN Interface",
                                                    "Please insert your LAN Interface (e.g. 'enp3s0'): ")
            req2 = tkinter.simpledialog.askstring("WAN Interface",
                                                    "Please insert your WAN Interface (e.g. 'enp6s0'): ")
            req3 = tkinter.simpledialog.askstring("LAN Gateway",
                                                  "Please insert your LAN Gateway (e.g. '192.168.1.1'): ")
            req4 = tkinter.simpledialog.askstring("WAN Gateway",
                                                  "Please insert your WAN Gateway (e.g. '195.88.145.142'): ")
            sqg = "{"
            sqg1 = "}"
            sqg2 = '"'

            ipf = "\nnet.ipv4.ip_forward=1"
            ipf1 = open("/etc/sysctl.conf", "w+")
            ipf1.write(ipf)

            dhcpser = "INTERFACESv4 = {}{}{}".format(sqg2, req1, sqg2)
            dhcpser1 = open("/etc/default/isc-dhcp-server", "w+")
            dhcpser1.write(dhcpser)

            dhcpc = "subnet 192.168.1.0 netmask 255.255.255.0 {}\nrange  192.168.1.2 192.168.1.250;\nddns-update-style none;\nauthoritative;\noption subnet-mask 255.255.255.0;\noption domain-name-servers 1.1.1.1;\noption routers 192.168.1.1;\noption broadcast-address 192.168.1.255;\ndefault-lease-time 600;\nmax-lease-time 7200;\n{}".format(sqg,sqg1)
            dhcpc1 = open("/etc/dhcp/dhcpd.conf", "w+")
            dhcpc1.write(dhcpc)

            nic = "#Loopback\nauto lo\niface lo inet loopback\n\n#WAN\nauto {}\niface {} inet dhcp\n\n#LAN\nauto {}\niface {} inet static\naddress 192.168.1.1\nnetmask 255.255.255.0".format(req2, req2, req1, req1)
            nicu = open("/etc/network/interfaces", "w+")
            nicu.write(nic)


            dnsc = "options {}\ndirectory {}/var/cache/bind{};\nforwarders {}\n{} port 53;\n{} port 53;\n{};\ndnssec-validation auto;\nlisten-on-v6 {} any; {};\n{};".format(sqg, sqg2, sqg2, sqg, req4, req3, sqg1, sqg, sqg1, sqg1)
            dnsc1 = open("/etc/bind/named.conf.options", "w+")
            dnsc1.write(dnsc)

        def nset():
            req1 = tkinter.simpledialog.askstring("LAN Interface",
                                                  "Please insert your LAN Interface (e.g. 'enp3s0'): ")
            req2 = tkinter.simpledialog.askstring("WAN Interface",
                                                  "Please insert your WAN Interface (e.g. 'enp6s0'): ")
            nic = "#Loopback\nauto lo\niface lo inet loopback\n\n#WAN\nauto {}\niface {} inet dhcp\n\n#LAN\nauto {}\niface {} inet static\naddress 192.168.1.1\nnetmask 255.255.255.0".format(
                req2, req2, req1, req1)
            nicu = open("/etc/network/interfaces", "w+")
            nicu.write(nic)

        def dnset():
            req3 = tkinter.simpledialog.askstring("LAN Gateway",
                                                  "Please insert your LAN Gateway (e.g. '192.168.1.1'): ")
            req4 = tkinter.simpledialog.askstring("WAN Gateway",
                                                  "Please insert your WAN Gateway (e.g. '195.88.145.142'): ")

            sqg = "{"
            sqg1 = "}"
            sqg2 = '"'
            dnsc = "options {}\ndirectory {}/var/cache/bind{};\nforwarders {}\n{} port 53;\n{} port 53;\n{};\ndnssec-validation auto;\nlisten-on-v6 {} any; {};\n{};".format(sqg, sqg2, sqg2, sqg, req4, req3, sqg1, sqg, sqg1, sqg1)
            dnsc1 = open("/etc/bind/named.conf.options", "w+")
            dnsc1.write(dnsc)

        def dhset():
            req1 = tkinter.simpledialog.askstring("LAN Interface",
                                                  "Please insert your LAN Interface (e.g. 'enp3s0'): ")
            sqg2 = '"'
            sqg = "{"
            sqg1 = "}"

            dhcpser = "INTERFACESv4 = {}{}{}".format(sqg2, req1, sqg2)
            dhcpser1 = open("/etc/default/isc-dhcp-server", "w+")
            dhcpser1.write(dhcpser)

            dhcpc = "subnet 192.168.1.0 netmask 255.255.255.0 {}\nrange  192.168.1.2 192.168.1.250;\nddns-update-style none;\nauthoritative;\noption subnet-mask 255.255.255.0;\noption domain-name-servers 1.1.1.1;\noption routers 192.168.1.1;\noption broadcast-address 192.168.1.255;\ndefault-lease-time 600;\nmax-lease-time 7200;\n{}".format(sqg,sqg1)
            dhcpc1 = open("/etc/dhcp/dhcpd.conf", "w+")
            dhcpc1.write(dhcpc)

        def router():
            req1 = tkinter.simpledialog.askstring("LAN Interface",
                                                  "Please insert your LAN Interface (e.g. 'enp3s0'): ")
            req2 = tkinter.simpledialog.askstring("WAN Interface",
                                                  "Please insert your WAN Interface (e.g. 'enp6s1'): ")
            req3 = tkinter.simpledialog.askstring("DHCP assigned WAN IP",
                                                  "Please insert your DHCP assigned WAN IP on Ubuntu (e.g. '195.88.83.164'): ")
            req5 = tkinter.simpledialog.askstring("LAN Gateway on destination device",
                                                  "Please insert your LAN Gateway on destination device(e.g. '192.168.1.1'): ")

            opn = "#!/bin/bash\niptables -F\niptables -X\niptables -t nat -F\niptables -t nat -X\niptables -t mangle -F\niptables -t mangle -X\niptables -P INPUT ACCEPT\niptables -P FORWARD ACCEPT\niptables -P OUTPUT ACCEPT\niptables -t nat -A POSTROUTING -o {} -j SNAT --to-source {}\niptables -t nat -A PREROUTING -i {} -j DNAT --to-destination {}\niptables -A FORWARD -i {} -o {} -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT\niptables -A FORWARD -i {} -o {} -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT\niptables -A INPUT -i {} -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT\niptables -A INPUT -i {} -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT\nifdown {}\nifup {}\nifdown {}\nifup {}\n/etc/init.d/networking restart\n/etc/init.d/networking reload".format(
                req2, req3, req2, req5, req1, req2, req2, req1, req1, req2, req1, req1, req2, req2)
            mod = "#!/bin/bash\niptables -F\niptables -X\niptables -t nat -F\niptables -t nat -X\niptables -t mangle -F\niptables -t mangle -X\niptables -P INPUT ACCEPT\niptables -P FORWARD ACCEPT\niptables -P OUTPUT ACCEPT\niptables -t nat -A POSTROUTING -o {} -j SNAT --to-source {}\niptables -t nat -A PREROUTING -i {} -j DNAT --to-destination {}\niptables -A INPUT -i {} -p tcp -m state --state ESTABLISHED,RELATED -j ACCEPT\niptables -A INPUT -i {} -p udp -m state --state ESTABLISHED,RELATED -j ACCEPT\niptables -A INPUT -i {} -p tcp -m state --state NEW -j DROP\niptables -A INPUT -i {} -p udp -m state --state NEW -j DROP\nifdown {}\nifup {}\nifdown {}\nifup {}\n/etc/init.d/isc-dhcp-server restart\n/etc/init.d/networking restart\n/etc/init.d/networking reload".format(
                req2, req3, req2, req5, req2, req2, req2, req2, req1, req1, req2, req2)
            str = "#!/bin/bash\niptables -F\niptables -X\niptables -t nat -F\niptables -t nat -X\niptables -t mangle -F\niptables -t mangle -X\niptables -P INPUT ACCEPT\niptables -P FORWARD ACCEPT\niptables -P OUTPUT ACCEPT\niptables -t nat -A POSTROUTING -o {} -j MASQUERADE --random\niptables -A FORWARD -i {} -o {} -m state --state RELATED, ESTABLISHED -j ACCEPT\niptables -A FORWARD -i {} -o {}  -j ACCEPT\nifdown {}\nifup {}\nifdown {}\nifup {}\n/etc/init.d/networking restart\n/etc/init.d/networking reload".format(
                req2, req2, req1, req1, req2, req1, req1, req2, req2)
            rstp = "#!/bin/bash\niptables -F\niptables -X\niptables -t nat -F\niptables -t nat -X\niptables -t mangle -F\niptables -t mangle -X\niptables -P INPUT ACCEPT\niptables -P FORWARD ACCEPT\niptables -P OUTPUT ACCEPT\nifdown {}\nifup {}\nifdown {}\nifup {}\n/etc/init.d/networking restart\n/etc/init.d/networking reload".format(req1, req1, req2, req2)

            ropn = open("opn.sh", "w+")
            rmod = open("mod.sh", "w+")
            rstr = open("str.sh", "w+")
            rrstp = open("rstop.sh", "w+")

            ropn.write(opn)
            rmod.write(mod)
            rstr.write(str)
            rrstp.write(rstp)

        def netconf():
            req1 = tkinter.simpledialog.askstring("LAN Interface",
                                                    "Please insert your LAN Interface (e.g. 'enp3s0'): ")
            req2 = tkinter.simpledialog.askstring("WAN Interface",
                                                    "Please insert your WAN Interface (e.g. 'enp6s1'): ")

            bn = "#!/bin/bash\n#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem rate 384kbit\ntc qdisc add dev {} root netem rate 384kbit".format(req1, req2, req1, req2)
            bb = "#!/bin/bash\n#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem rate 192kbit\ntc qdisc add dev {} root netem rate 192kbit".format(req1, req2, req1, req2)
            bx = "#!/bin/bash\n#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem rate 64kbit\ntc qdisc add dev {} root netem rate 64kbit".format(req1, req2, req1, req2)
            bc = "#!/bin/bash\n#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem rate customukbit\ntc qdisc add dev {} root netem rate customdkbit".format(req1, req2, req1, req2)

            ln = "#!/bin/bash\n#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem delay 100ms\ntc qdisc add dev {} root netem delay 100ms".format(req1, req2, req1, req2)
            lb = "#!/bin/bash\n#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem delay 300ms\ntc qdisc add dev {} root netem delay 300ms".format(req1, req2, req1, req2)
            lx = "#!/bin/bash\n#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem delay 550ms\ntc qdisc add dev {} root netem delay 550ms".format(req1, req2, req1, req2)
            lc = "#!/bin/bash\n#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem delay customums\ntc qdisc add dev {} root netem delay customdms".format(req1, req2, req1, req2)

            pln = "#!/bin/bash\n#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem loss 1%\ntc qdisc add dev {} root netem loss 1%".format(req1, req2, req1, req2)
            plb = "#!/bin/bash\n#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem loss 5%\ntc qdisc add dev {} root netem loss 5%".format(req1, req2, req1, req2)
            plx = "#!/bin/bash\n#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem loss 10%\ntc qdisc add dev {} root netem loss 10%".format(req1, req2, req1, req2)
            plc = "#!/bin/bash\n#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem loss customu%\ntc qdisc add dev {} root netem loss customd%".format(req1, req2, req1, req2)

            cn = "#!/bin/bash\n#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem rate 384kbit delay 100ms loss 1%\ntc qdisc add dev {} root netem rate 384kbit delay 100ms loss 1%".format(req1, req2, req1, req2)
            cb = "#!/bin/bash\n#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem rate 192kbit delay 300ms loss 5%\ntc qdisc add dev {} root netem rate 192kbit delay 300ms loss 5%".format(req1, req2, req1, req2)
            cx = "#!/bin/bash\n#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem rate 64kbit delay 550ms loss 10%\ntc qdisc add dev {} root netem rate 64kbit delay 550ms loss 10%".format(req1, req2, req1, req2)
            cc = "#!/bin/bash\n#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem rate customu1kbit delay customu2ms loss customu3%\ntc qdisc add dev {} root netem rate customd1kbit delay customd2ms loss customd3%".format(req1, req2, req1, req2)

            pd = "#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem duplicate customu%\ntc qdisc add dev {} root netem duplicate customd%".format(
                req1, req2, req1, req2)
            pc = "#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem corrupt customu%\ntc qdisc add dev {} root netem corrupt customd%".format(
                req1, req2, req1, req2)
            pr = "#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root\nmodprobe sch_netem\ntc qdisc add dev {} root netem gap 5 delay 10ms".format(
                req1, req2, req1)

            stp = "#!/bin/bash\ntc qdisc de dev {} root\ntc qdisc de dev {} root".format(req1, req2)
            vwv = "#!/bin/bash\ndate >> log.txt\ntc -s qdisc ls dev {} >> log.txt\ntc -s qdisc ls dev {} >> log.txt".format(req1, req2)

            bnn = open("bnorm.sh", "w+")
            bbb = open("bbad.sh", "w+")
            bxx = open("bxtr.sh", "w+")
            bcc = open("bcust.sh", "w+")
            bcc1 = open("bcust1.sh", "w+")

            lnn = open("lnorm.sh", "w+")
            lbb = open("lbad.sh", "w+")
            lxx = open("lxtr.sh", "w+")
            lcc = open("lcust.sh", "w+")
            lcc1 = open("lcust1.sh", "w+")

            plnn = open("plnorm.sh", "w+")
            plbb = open("plbad.sh", "w+")
            plxx = open("plxtr.sh", "w+")
            plcc = open("plcust.sh", "w+")
            plcc1 = open("plcust1.sh", "w+")

            cnn = open("cnorm.sh", "w+")
            cbb = open("cbad.sh", "w+")
            cxx = open("cxtr.sh", "w+")
            ccc = open("ccust.sh", "w+")
            ccc1 = open("ccust1.sh", "w+")

            stpp = open("stop.sh", "w+")
            vwvw = open("exp.sh", "w+")

            prw = open("pr.sh", "w+")
            pdw = open("pd.sh", "w+")
            pcw = open("pc.sh", "w+")

            pcw.write(pc)
            prw.write(pr)
            pdw.write(pd)

            bnn.write(bn)
            bbb.write(bb)
            bxx.write(bx)
            bcc.write(bc)
            bcc1.write(bc)

            lnn.write(ln)
            lbb.write(lb)
            lxx.write(lx)
            lcc.write(lc)
            lcc1.write(lc)

            plnn.write(pln)
            plbb.write(plb)
            plxx.write(plx)
            plcc.write(plc)
            plcc1.write(plc)

            cnn.write(cn)
            cbb.write(cb)
            cxx.write(cx)
            ccc.write(cc)
            ccc1.write(cc)

            stpp.write(stp)
            vwvw.write(vwv)

        fsl1 = Label(self.tab3, width="10", height="1", text="System Setup", padx="20", font="Helvetica 9 bold")
        fs0 = Button(self.tab3, text="Create base bash", width="18", command=update)
        fsl2 = Label(self.tab3, width="18", height="1", text="App Setup",padx="20", font="Helvetica 9 bold")
        fs5 = Button(self.tab3, text="Export network info", width="18", command=getinf)
        fs6 = Button(self.tab3, text="Configure system files", width="18", command=consys)
        fs7 = Button(self.tab3, text="Create app files", width="18", command=bash)
        fs8 = Button(self.tab3, text="Credits", width="14", command=devs)

        scl1 = Label(self.tab3, width="18", text="Change Setup Info", padx="20", font="Helvetica 9 bold")
        sc1 = Button(self.tab3, text="Router", width="14", command=router)
        sc2 = Button(self.tab3, text="NETEM", width="14", command=netconf)
        sc3 = Button(self.tab3, text="Network Interfaces", width="14", command=nset)
        sc4 = Button(self.tab3, text="DNS", width="14", command=dnset)
        sc5 = Button(self.tab3, text="DHCP", width="14", command=dhset)
        sc6 = Button(self.tab3, text="Tools Install", width="18", command=update6)

        notesl = Label(self.tab3, text="Additional Notes", width="14", font="Helvetica 9 bold")
        notes = Button(self.tab3, text="README", width="14", command=notif)

        fsl1.grid(row=0, column=0)
        fs0.grid(row=1, column=0)
        fsl2.grid(row=0, column=1)
        fs5.grid(row=1, column=1)
        fs6.grid(row=2, column=1)
        fs7.grid(row=3, column=1)
        fs8.grid(row=1, column=3)

        scl1.grid(row=0, column=2)
        sc1.grid(row=1, column=2)
        sc2.grid(row=2, column=2)
        sc3.grid(row=3, column=2)
        sc4.grid(row=4, column=2)
        sc5.grid(row=5, column=2)
        sc6.grid(row=2, column=0)

        notesl.grid(row=0, column=3)
        notes.grid(row=2, column=3)

app = App()
app.mainloop()