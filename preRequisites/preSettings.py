import threading
import time

from arduino import flash_detect
from audio import listen
from reuseable import serverAppium
from testScripts import testVideo

def pre_req():
    # try:
    serverAppium.start_server()
    try:
        testVideo.launch_appium_driver()
    except:
        pass
        pin,port=flash_detect.arduino()
        for i in range(1):
            thread3 = threading.Thread(target=listen.audio_return)
            thread3.start()
            thread1 = threading.Thread(target=testVideo.play_video)
            thread1.start()
            thread2 = threading.Thread(target=flash_detect.getArduino,args=(pin,port))
            thread2.start()
            time.sleep(10)

            thread5 = threading.Thread(target=testVideo.pauseVideo)
            thread5.start()
            thread5.join()

            thread1.join()
            thread2.join()
            thread3.join()
            print("itration complete.......{}".format(i+1))
            time.sleep(1)

    testVideo.close_app()
pre_req()