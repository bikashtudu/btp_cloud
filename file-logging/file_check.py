import os 
import re
import getpass

username = getpass.getuser()

m1 = {}
m2 = {}

output_file = open("/home/prasad/Desktop/btp/test2/file-logging/file_knowledgebase.txt","r")
knowledge_base = output_file.readlines()
output_file.close()

in_file = open("/home/prasad/Desktop/btp/test2/file-logging/file_mon.txt","r")
output_file = open("/home/prasad/Desktop/btp/test2/file-logging/file_data.pl","w+")

file1 = "ssy"
file2 = "/var/log/syslog"

for line in in_file:
	if ("ftrace_hook" in line) and ((file1 in line) or (file2 in line)):
		a = line.split('ftrace_hook: ')
		cmd = a[len(a)-1].split('(')
				
		if name in m1:	
			if not(cmd[0] in m1[name]):
				m1[name].append(cmd[0])
				file_output = 'file_mon('+name+','+cmd[0]+','+username+',vm2).\n'
				output_file.write(file_output)			
		else:	
			m1[name] = [cmd[0]]	
			file_output = 'file_mon('+name+','+cmd[0]+','+username+',vm2).\n'
			output_file.write(file_output)

	
output_file.write('\n')
output_file.writelines(knowledge_base)	
output_file.close()
in_file.close()	
	    
	    
		






