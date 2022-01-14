import speedtest


def speed_tester():
    wifi = speedtest.Speedtest()
    print("Wifi Download Speed is ", (wifi.download()*0.000001))
    print("Wifi Upload Speed is ", wifi.upload())


if __name__=="__main__":
    speed_tester()