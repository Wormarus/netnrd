# netnrd
"NETnrd" is a tool developed to ease the Networking testing/manipulation which runs on Ubuntu 19.04.

For using it you will need 2 NICs (one for LAN & one for WAN). 

It includes the functionality of NETEM (for limitation of Bandwidth, adding Latency and including Packet Loss), Speedometer to view Bandwidth consumption and iptables for changing of NAT types. It also has an option of an easy setup of config files & buttons for further changes withing which may be required.

In order to use netnrd do following: 
1. Copy the executable to your home folder;
2. use <chmod 700 netnrd_git_final> in order to be able to execcute it;
3. run the app through the terminal using sudo <sudo ./netnrd_git_final>;
4. Use <Setup> tab within the app and follow it from top to bottom from left to right;
5. After the setup is done, select NAT type in <UNTU> section of the app to get ip on destination device & apply any limitations that you want.
