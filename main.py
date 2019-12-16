import os
import sys
import dealNode
import list_node
import delNode
import bookurl
import ping
def picture():
		print ("(  ____ \( \      \__   __/( (    /|  ")
		print ("| (    \/| (         ) (   |  \  ( |  ")
		print ("| (_____ | |         | |   |   \ | |  ")
		print ("(_____  )| |         | |   | (\ \) |  ")
		print ("      ) || |         | |   | | \   |  ")
		print ("/\____) || (____/\___) (___| )  \  |  ")
		print ("\_______)(_______/\_______/|/    )_)  ")
		print()
		print()
def help():
		picture()
		print ("sliny version 1.1  ( author:dawn)")
		print("usage: python3 main.py -h  [help] /i [init] /-s [stop] /-p <ping default all>")
		print("usage: python3 main.py -N  [Node] <Node> /-d [del Node number] /-b [book url]")
		print("usage: python3 main.py -l  [list of Node] |-r [run] <list> /-s [stop] /-p <ping num>")

		
def main():
	if len(sys.argv)==1:	
		help()
	elif len(sys.argv)==2:
		if sys.argv[1] == "-h":
			help()
		if sys.argv[1] == "-p":
			picture()
			ping.pingall()
		elif sys.argv[1] == "-l":
			picture()
			list_node.node_list()
		elif sys.argv[1] == "-i":
			picture()
			os.system("bash init.sh 1")
		elif sys.argv[1] == "-s":
			picture()
			activev2ray = int(os.system("bash runandstop.sh tv"))
			if activev2ray == 0:
				os.system("bash runandstop.sh dv")
			os.system("bash runandstop.sh ds")	
	elif len(sys.argv)==3:
		if sys.argv[1] == "-N":
			picture()
			s = sys.argv[2]
			is_ssr = s.find('ssr://')
			is_vmess = s.find('vmess://')
			if is_vmess != -1:
				vmess = s[is_vmess:].strip()
				dealNode.decode_v2ray(vmess)
			elif is_ssr != -1:
				ssr = s[is_ssr:].strip()
				
				dealNode.decode_ssr(ssr)
			else:
				print("Node is worse !!!")
		elif sys.argv[1] == "-b":
			z = sys.argv[2]
			bk_hp = z.find('https://')
			bk_hps = z.find('https://')
			if bk_hp != -1:
				bookurl.bookur(z)
				
			elif bk_hps != -1:
				bookurl.bookur(z)
			
		elif sys.argv[2] == "-s":
				picture()
				activev2ray = int(os.system("bash runandstop.sh tv"))
				if activev2ray == 0:
					os.system("bash runandstop.sh dv")
				os.system("bash runandstop.sh ds")
		elif sys.argv[1] == "-d":
			picture()
			num = sys.argv[2]
			delNode.del_list(num)

	elif len(sys.argv)==4:
		if sys.argv[1] == "-l":
			if sys.argv[2] == "-r":
				picture()
				activev2ray = int(os.system("bash runandstop.sh tv"))
				if activev2ray == 0:
					os.system("bash runandstop.sh dv")
				flag = list_node.choic_node(sys.argv[3])
				if flag == "ssr":
					os.system("bash runandstop.sh rs")
				if flag == "v2ray":
					os.system("bash runandstop.sh rv")
			elif sys.argv[2] == "-p":
				picture()
				ping.pinchoice(sys.argv[3])
			

main()

