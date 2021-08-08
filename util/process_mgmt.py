import subprocess
import shlex
import sys
import signal
import psutil
import time

def kill_child_processes(parent_pid, sig=signal.SIGTERM):
    try:
        parent = psutil.Process(parent_pid)
    except psutil.NoSuchProcess:
        print("parent process not existing")
        return
    children = parent.children(recursive=True)
    for process in children:
        print("try to kill child: " + str(process))
        process.send_signal(sig)

class Subprocess:
    def __init__(self, command):
        self.command = command
        
    def run(self, output=False):
        try:
            if output:
                self.process = subprocess.Popen([self.command], shell=True, stdout=subprocess.PIPE)
            else:
                self.process = subprocess.Popen([self.command], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.pid = self.process.pid  # pid of the roscore process (which has child processes)
            self.process.wait()
            print("STARTED PID:", str(self.pid) + " for: " + self.command)
            text = self.process.stdout.read() 
            return text
        
        except OSError as e:
            sys.stderr.write(self.command, "could not be run")
            raise e

    def get_pid(self):
        return self.pid

    def get_process(self):
        return self.command

    def terminate(self):
        kill_child_processes(self.pid)
#        print("Killing parent node pid:", self.pid)
#        self.process.terminate()
        self.process.wait()
