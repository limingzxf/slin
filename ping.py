import os

def get_ping_result(ip_address):
	ping="ping"+"  "+ip_address+" -c 1"
	p = os.popen(ping)
	spilted = p.read().split('time=') 
	if(len(spilted)==1):
		spilted="time out"
		return spilted
	else:
		spilted = spilted[1].split('ms') 
		return spilted[0]+"ms"


def pingall():

			print ("-----------------------------")
			print ("|           ping            |")
			employee_file = open("config/shadowsocks.json", "r") 
			solvethesign = len(employee_file.read())
			employee_file.close()
			employee_file = open("config/shadowsocks.json", "r")
			i=0 
			if (solvethesign is not 0):
				spilted=''
				for employee in employee_file.readlines():
					spilted = employee.split('//') 
  			
					
		
				for ipaddresschoose in range(0,len(spilted)):
					i = i+1
					solverange = ipaddresschoose
					ipaddress = spilted[solverange].split('server": \"')
					ipaddress = ipaddress[1].split('",')
					print ("-----------------------------")
					print ("* "+str(i)+ ". "+ipaddress[0] + "     "+get_ping_result(ip_address[0]))
			
			
			employee_file.close()
			employee_vmess = open("config/config.json", "r")
			solvethesig = len(employee_vmess.read()) 
			employee_vmess.close()
			employee_vmess = open("config/config.json", "r")
			if (solvethesig is not 0):
			
				sp_vm=''
				for em_vm in employee_vmess.readlines():
					sp_vm = em_vm.split('//') 
				
				for ip_list in range(0,len(sp_vm)):
					i = i+1
					solve_range = ip_list
					ip_address = sp_vm[solve_range].split('"address":"')
					ip_address = ip_address[1].split('"')
					print ("-----------------------------")
					print ("* "+str(i)+ ". "+ip_address[0] +"       "+str(get_ping_result(ip_address[0])))
	
			print ("-----------------------------")    
		
		
			employee_vmess.close()

	


def pinchoice(num):
				employee_file = open("config/shadowsocks.json", "r") 
				spilted=''
				for employee in employee_file.readlines():
					spilted = employee.split('//') 
				employee_file.close()
				
				choosenodenum = int (num)
				
				
				if choosenodenum <= (len(spilted)):
					print ("-----------------------------")
					print ("|           ping            |")

					for ipaddresschoose in range(0,len(spilted)):
						ipaddresschoose = ipaddresschoose + 1
						if choosenodenum == ipaddresschoose:    
							ipaddress = spilted[choosenodenum-1].split('server": \"')
							ipaddress = ipaddress[1].split('",')
							print ("-----------------------------")
							print ("* "+str(num)+ ". "+ipaddress[0] + "    "+get_ping_result(ip_address[0]))
					print ("-----------------------------")
							
							

				else:
					print ("-----------------------------")
					print ("|           ping            |")

					em_vm = open("config/config.json", "r") 
					sp_vm=''
					for vm_node in em_vm.readlines():
						sp_vm = vm_node.split('//') 
					em_vm.close()	
					vm_ch=(len(sp_vm))+(len(spilted))
					if choosenodenum <= vm_ch:
						vm_list=(len(spilted))+1	
						
						for ipaddresschoose in range(0,len(sp_vm)):
							ipaddresschoose = ipaddresschoose +vm_list	
							if choosenodenum == ipaddresschoose:    
								ip_address=sp_vm[choosenodenum-vm_list].split('"address":"')
								ip_address = ip_address[1].split('"')
								print ("-----------------------------")
								print ("* "+str(num)+ ". "+ip_address[0] +"       "+str(get_ping_result(ip_address[0])))
								
							
						
					print ("-----------------------------")

			
		






