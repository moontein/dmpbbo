import subprocess
import os,sys

def executeBinary(executable_name,arguments,print_command=False):
    
    if (not os.path.isfile(executable_name)):
        print("")
        print("ERROR: Executable '"+executable+"' does not exist.")
        print("Please call 'make install' in the build directory first.")
        print("")
        sys.exit(-1);
        
    command = executable_name+" "+arguments
    if print_command:
        print(command)
    
    subprocess.call(command, shell=True)
    
    return command

def executeBinaryWithDirectory(directory,executable_name,arguments,print_command=False):

    for try_directory in ['./',directory]:
        executable = try_directory+executable_name
        print(executable)
        
        if (os.path.isfile(executable)):
            command = executable+" "+arguments
            if print_command:
                print(command)
            
            subprocess.call(command, shell=True)
            return command
    
    print("")
    print("ERROR: Executable '"+executable_name+"' does not exist in '"+directory+" or './'.")
    print("Please call 'make install' in the build directory first.")
    print("")
    sys.exit(-1);
    return None
