import subprocess


class Hardware:

    def get_cpu_temp(self):
        temperatur = subprocess.run("vcgencmd measure_temp",
                     shell=True, stdout=subprocess.PIPE, text=True)
        return temperatur[5:(len(temperatur)-2)]
