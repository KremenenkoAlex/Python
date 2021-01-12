from time import sleep

class traffic_light:
    __color = ["red", "yellow", "green"]

    def running(self):
        i = 0
        while i != 3:
            print(traffic_light.__color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(7)
            i += 1

traf = traffic_light()
traf.running()
