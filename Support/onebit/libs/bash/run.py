import sys
import os
import commands
import subprocess
import pprint

def main(*args):  
	pp = pprint.PrettyPrinter(indent=4)
	proj_dir = args[2].strip()
	scratch_dir = args[3].strip()
	bundle_dir = args[4].strip()
	
	# maybe catch non existence of file?
	pref_file = os.path.expanduser("~/Library/Processing/preferences.txt")
	
	os.chdir(bundle_dir+'/onebit/libs/processing-cmd')
	
	if args[1].strip()=="NO":
		cmd = "./processing --sketch='%s' --output='%s' --preferences='%s' --run >> log.onebit" % (proj_dir, scratch_dir, pref_file);
	else:
		cmd = "./processing --sketch='%s' --output='%s' --preferences='%s' --present >> log.onebit" % (proj_dir, scratch_dir, pref_file);
	p = subprocess.Popen([cmd], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	p.wait()
	stdout = p.stdout
	stderr = p.stderr
	err = ""
	out = ""
	for line in stdout.readlines():
		if type(line) == list:
			for phrase in line:
				out+=str(phrase)
		else:
			out+=str(line)
	
	for line in stderr.readlines():
		if type(line) == list:
			for phrase in line:
				err+=str(phrase)
		else:
			err+=str(line)
	

	err= pp.pprint(err)
	out=pp.pprint(out)
	if err and out:
		return str(err)+str(out)
	elif err:
		return str(err)
	elif out:
		return str(out)
	else:
		return ""
    
if __name__ == "__main__":
    sys.stdout.write(main(*sys.argv))