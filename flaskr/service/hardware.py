import os


class Hardware:

    def get_cpu_temp(self):
        temperatur = os.popen("vcgencmd measure_temp").read()
        return temperatur[5:(len(temperatur)-2)]
