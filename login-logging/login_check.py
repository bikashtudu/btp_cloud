import os 
import re

m1 = {}

'''
output_file = open("/home/prasad/Desktop/btp/test2/login-logging/login_data.pl","r")

for line in output_file:
	if 'user_login' in line:
		name = line.split(',')
		User_name = name[0].split('(')
		vm_name = name[1].split(')')
		if User_name[1] in m1:		
			if not(vm_name[0] in m1[User_name[1]]):
				m1[User_name[1]].append(vm_name[0])							
		else:
			m1[User_name[1]] = [vm_name[0]]
	else: 
		break
	
output_file.close()
'''

output_file = open("login_knowledgebase.txt","r")
knowledge_base = output_file.readlines()
output_file.close()

match1 = "session opened for"

in_file = open("/var/log/auth.log","r")
output_file = open("login_data.pl","w+")

for line in in_file:
	if match1 in line:
		date_time = line[0:16]
		s = line[line.rindex('user'):]
		a = s.split(' ')
		if a[1] in m1:
			if not ('vm2' in m1[a[1]]):
				m1[a[1]].append('vm2')	
				file_out = "user_login("+a[1]+",vm2).\n"
				output_file.write(file_out)
		else:	
			m1[a[1]] = ['vm2']
			file_out = "user_login("+a[1]+",vm2).\n"
			output_file.write(file_out)
		
output_file.write('\n')
output_file.writelines(knowledge_base)	
output_file.close()
in_file.close()
