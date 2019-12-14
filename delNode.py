	

def del_list(num):
			employee_file = open("config/shadowsocks.json", "r") 
			employee_vmess = open("config/config.json", "r") 
			spilted = ''
			for employee in employee_file.readlines():
				spilted = employee.split('//') 
			sp_vm =''
			for em_vm in employee_vmess.readlines():
				sp_vm = em_vm.split('//')   
			i=0
			for ipaddresschoose in range(0,len(spilted)):
				i = i+1
			employee_file.close()
			k=i
			for ip_list in range(0,len(sp_vm)):
				k = k+1

			employee_vmess.close()
			
			if (int(num) <= int(i) and int(num) > 0):
				print("ssr")
				resultc=''
				if(int(num)==1):
					
					spilted[0]=''
					
					w=2
					if int(i)==1:
						w=1
					else :
						resultc=resultc+spilted[int(w)-1]
					for b in range(int(w),int(i)):
						if w is not 1:
							resultc=resultc+"//"+spilted[b]
				elif(int(num) > 1):
					
					spilted[(int(num)-1)]=''
					resultc=resultc+spilted[0]
					for b in range(1,(int(num)-1)):
						
						resultc=resultc+"//"+spilted[b]
					for r in range(int(num),(int(i))):
						
						resultc=resultc+"//"+spilted[r]
				configessrfile = open("config/shadowsocks.json","w")
				configessrfile.write(resultc)
				configessrfile.close()	
 
			
			if (int(num) > int(i) and int(num) <= int(k)):
				employee_file = open("config/shadowsocks.json", "r") 
				solvethesign = len(employee_file.read())
				employee_file.close()
				if (solvethesign is not 0):
					print("v2ray")
					resultc=''
					if(int(num)==int(i)+1 ):
					
						sp_vm[0]=''
					
						w=2
						if (int(k)-int(i))==1:
							w=0
						else :
							resultc=resultc+sp_vm[int(w)-1]
						for b in range(int(w),int(k)-int(i)):
							if w is not 1:
								resultc=resultc+"//"+sp_vm[b]
					elif(int(num) > int(i)+1):
					
						sp_vm[(int(num)-1-int(i))]=''
						resultc=resultc+sp_vm[0]
						for b in range(1,(int(num)-int(i)-1)):
							resultc=resultc+"//"+sp_vm[b]
						for r in range(int(num)-int(i),(int(k)-int(i))):
							resultc=resultc+"//"+sp_vm[r]
					employeevmessfile = open("config/config.json","w")
					employeevmessfile.write(resultc)
					employeevmessfile.close()	
				else:
					print("v2ray")
					resultc=''
					if(int(num)==1):
					
						sp_vm[0]=''
					
						w=2
						if int(k)==1:
							w=1
						else :
							resultc=resultc+sp_vm[int(w)-1]
						for b in range(int(w),int(k)):
							if w is not 1:
								resultc=resultc+"//"+sp_vm[b]
					elif(int(num) > 1):
						
						sp_vm[(int(num)-1)]=''
						resultc=resultc+sp_vm[0]
						for b in range(1,(int(num)-1)):
							
							resultc=resultc+"//"+sp_vm[b]
						for r in range(int(num),(int(k))):
							
							resultc=resultc+"//"+sp_vm[r]
					configevmessfile = open("config/config.json","w")
					configevmessfile.write(resultc)
					configevmessfile.close()	
 
 
				



