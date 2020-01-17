# Now what is the ARP Spoofing, this is similar to the man in the middle attack here bascially
# All the information of the client like what he is seraching,watching,entering passwords etc
# all these details will pass through our machine then we can drop, modify etc with that
#     information after this info will go to the router and then so on ....
#
# and when the server respond then router will give the response to us then similary
# we can modify,drop etc with the respone and then pass it to the client
#
# basically here we make fool to router that i am the client
# and to client that i am the router


# in the network every clients and the router has the arp table in which they are linking the ip address of the router to router's mac Address and it self's too
# you can check this by this command
# (arp -a)
#
# so whenever the client wants to access the internet it simply send the message to router mac address by its ip address
# normally
# all the clients in the network sends the requests to the router and router send it to the internet and forwards the response to the clients
#
# Here what we can do right ?
#
# lets suppose the ip of router is :
# 10.0.2.1
# client's ip
# 10.0.2.7
#
# Here we will send the two ARP responses one to the router and other to the client
#
# one we will send the ARP response from our machine to the router that
# i am at 10.0.2.7
# now here router will link this ip to my mac address in his ARP table
#
# another response we will send to the client that
# i am at 10.0.2.1
# then here client will update or link our mac address to the ip 10.0.2.1 in his ARP table means whenever it will send the response then it will delievr to the mac address which is our mac address so it means client will pass all the data to my machine because we have change the mac addrees in his arp table

#
# Now here what excatly happened here router will think that i am the client and the client will think that i am the router
# so in this way whenever the client wants to send the message he will send it to me and i will forward it to the router
# and whenever the router wants to send the mesage it will send it to us because router thinks that i am the client and we will forwad the respone to the client because client thinks i am the router
# so it means now all traffic will pass through our interface so we can do the packet sniffer attack to read the data like urls, passwords etc

#
# This is only possible becasue we know ARP protocol is not very secure because as you can
# see here the router and clients in the network updating its ARP table without any confirmation

# now before writtin our code kali linux has the number of tools for the arp spoofing
#     like for this we have to type the command in the terminal for this we have to open 2 terminal
#
# syntax of the command :    arpspoof -i (our interface) -t (target ip) (gateway ip)
# for example
#     arpspoof -i eth0 -t 10.0.2.7 10.0.2.1  command in one terminal
#     This will make the fool to client that i am the router
#
#     arpspoof - i eth0 -t 10.0.2.1 10.0.2.7  command in 2nd terminal
#     this will make the fool to router that i am the client

    # this attack will work for any network where it is a wireless or wired etc here we have the virtual ethernet network so we are using the eth0

# now here when the client sends the responses to us then kali linux stops that response as we know our machine is not the router so in order to accepts all the requests from the client and pass it to the router we have to run this command
# open the new terminal and run the command
# (echo 1 > /proc/sys/net/ipv4/ip_forward)
# after this we can access the internet with out any issue but here what happened that all the response may be it is coming from the client or it's coming by our browsing it will first send to the our machine and then our machine will pass the info to the router
# bascially before this command our response directly go to the router
# after this command even our response first go to our computer than pass it to router