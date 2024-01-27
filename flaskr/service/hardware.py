import random
import os


class Hardware:

    def get_cpu_temp(self):
        #return random.uniform(30.0, 40.0)
        temperatur=os.popen("vcgencmd measure_temp").read()
        return temperatur[5:(len(temperatur)-2)]
