#!/usr/bin/env python3

import subprocess,os
from termcolor import colored

def banner():
	x="""
		_  _ _ _    _    ____ ____   ____ ____ ___ 
		|_/  | |    |    |___ |__/   |  | |  |   /
		| \\_ | |___ |___ |___ |  \\   |__| |__|  /  
      """


 
	y = "		+-----------------------------------------+"     
	z = "							~~Twitter: Killeroo7p\n"
	print(colored(x,'blue'))
	print(colored(y,'red'))
	print(colored(z,'green'))


def aws_brute(wordlistFile,service):

	print(colored("\nX------------------------------X\n\tTesting For "+service+"\nX------------------------------X\n","yellow"))
	worked_cmds = []

	with open("aws_brute_results/"+service,"a") as aws_result:

		with open(wordlistFile,"r") as wordlist:
			for word in wordlist:
				word = word.strip()
				cmd = f"aws {service} {word}"
				print(colored("[-]"+cmd,"cyan"))

				try:
					with open(os.devnull,"w") as DEVNULL:
						output = (subprocess.check_output(cmd,shell=True,stderr=DEVNULL)).decode()
					

					print("------------------------------------\n"+output+"------------------------------------\n")
					worked_cmds.append(cmd)
					aws_result.write(cmd+"\n---------------------------------------------------\n"+output+"---------------------------------------------------\n")

				except KeyboardInterrupt:
					exit()
				except:
					print(colored("-->Error","red"))

		print(colored("\nWORKED COMMANDS","yellow"))
		aws_result.write("\tWORKED COMMANDS\n")
		for cmds in worked_cmds:
			print(colored(cmds,"blue"))
			aws_result.write(cmds+"\n")

def main():
	
	banner()
	
	services={
		"sts":"wordlists/sts_wordlist",
		"dynamoDB":"wordlists/dynamoDB_wordlist",
		"iam":"wordlists/iam_wordlist",
		"sti":"wordlists/sti_wordlist",
		"s3":"wordlists/s3_wordlist"
	}

	os.mkdir("aws_brute_results")

	for serv in services:	
		aws_brute(services[serv],serv)


main()