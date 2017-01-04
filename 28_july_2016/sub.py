import subprocess

def create_output_dir():
    output_dir = '/home/webwerks1/vineet/28_july_2016/hello/'
    subprocess.Popen(['mkdir', output_dir])
    return output_dir
    

out_dir = create_output_dir()
filename = out_dir+'hello1.txt'
with open(filename,'w') as script:
	scrpit.write("hello world")
    
