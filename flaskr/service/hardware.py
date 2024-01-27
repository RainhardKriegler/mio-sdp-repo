import subprocess


class Hardware:

    def get_cpu_temp(self):
        temp = subprocess.run("vcgencmd measure_temp",
                              shell=True, stdout=subprocess.PIPE, text=True)
        return temp.stdout[5:(len(temp.stdout)-2)]
