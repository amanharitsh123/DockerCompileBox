import subprocess, os, time, signal

def subprocess_cmd(command,inputfile,outputfile):
	process = subprocess.Popen(command,stdout=outputfile,stdin=inputfile,shell=True, preexec_fn=os.setsid)
	is_timeout=wait_timeout(process,1)
	if is_timeout:
		print("TLE!!")

def wait_timeout(proc, seconds):
	start = time.time()
	end = start + seconds
	interval = min(seconds / 1000.0, .25)

	while True:
		result = proc.poll()
		if result is not None:
			return result
		if time.time() >= end:
			os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
			print("killing")
			return True
		time.sleep(interval)



command_to_compile="python3 test.py"
inputfile=open("inp.txt")
sanitized_input=open("sanitized_input","w+")
outputfile=open("output.txt","a+")
# Fetch Parameters
parameters=inputfile.readline()

# Stripfile for the first line
subprocess.Popen("sed '1d'  inp.txt",stdout=sanitized_input,stdin=inputfile,shell=True, preexec_fn=os.setsid)
print("paramerters are ",parameters)

sanitized_input=open("sanitized_input","r")
subprocess_cmd(command_to_compile,sanitized_input,outputfile)

# os.system("python3 test.py")
