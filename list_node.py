	

def node_list():
			
			
			print ("-----------------------------")
			print ("|           Node            |")
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
					print ("* "+str(i)+ ". "+ipaddress[0] + "        ")
			
			
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
					print ("* "+str(i)+ ". "+ip_address[0] + "        ")
	
			print ("-----------------------------")    
		
		
			employee_vmess.close()

	




def choic_node(num):
				employee_file = open("config/shadowsocks.json", "r") 
				spilted=''
				for employee in employee_file.readlines():
					spilted = employee.split('//') 
				employee_file.close()
				
				choosenodenum = int (num)
				testvalue = 0
				flag=""
				if choosenodenum <= (len(spilted)):
					employee_filebychoice = open("/etc/shadowsocks.json", "w")
					for ipaddresschoose in range(0,len(spilted)):
						ipaddresschoose = ipaddresschoose + 1
						if choosenodenum == ipaddresschoose:    
							employee_filebychoice.write(spilted[choosenodenum-1])
							testvalue = 1;
							flag="ssr" 
					employee_filebychoice.close()
				else:

					em_vm = open("config/config.json", "r") 
					sp_vm=''
					for vm_node in em_vm.readlines():
						sp_vm = vm_node.split('//') 
					em_vm.close()	
					vm_ch=(len(sp_vm))+(len(spilted))
					if choosenodenum <= vm_ch:
						vm_list=(len(spilted))+1	
						employee_filebychoice = open("/etc/v2ray/config.json", "w")
						for ipaddresschoose in range(0,len(sp_vm)):
							ipaddresschoose = ipaddresschoose +vm_list	
							if choosenodenum == ipaddresschoose:    
								employee_filebychoice.write(sp_vm[choosenodenum-vm_list])
								testvalue = 1;
								flag="v2ray"
						employee_filebychoice.close()

				if testvalue == 1 :
					print("	choice success ")
			
				else :
					print("	Invail value")
				return flag




