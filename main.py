import threading

import time
import simple_colors
from arduino import flash_detect
import pandas as pd

from reuseable.configs import MobileConfig
from testScripts import testVideo
from audio import listen
import excel_data
from preRequisites import preSettings

x=True
if __name__ == '__main__':

    try:
        print("----pre setting has been called----")
        ser = preSettings.pre_req()
        print(simple_colors.green("----pre setting has been finished sucessfully----"))
    except:
        x=False
        print(simple_colors.red("----pre settings has failed!----"))
    if (x==True):
        try:
            print(simple_colors.blue("----Relauching the application----"))
            testVideo.launch_appium_driver()
        except:
            pass

        # pin,port=flash_detect.arduino()
        data1=[]
        # wb, ws, header_format=excel_data.Starting_workbook()


        thread1 = threading.Thread(target=testVideo.play_video)
        thread1.start()
        # thread3 = threading.Thread(target=listen.listen)
        # thread3.start()
        # time.sleep(1)
        thread2 = threading.Thread(target=flash_detect.getArduino(ser))
        thread2.start()
        thread6 = threading.Thread(target=listen.audio_return)
        thread6.start()
        # testVideo.timeSleep()
        thread1.join()
        # thread2.join()
        # thread3.join()
        thread6.join()
        time.sleep(5)
        print(testVideo.dict)
        c=excel_data.appending(testVideo.dict)
        data1.append(c)
        # print("....//iteration completed//....", i+1)
        print("audio_time",MobileConfig.audio_det)
        # excel_data.creating_table(ws, data1, header_format)
        testVideo.close_app()
        # excel_data.close_workbook(wb)



    else:
        print("There is an error in code!!")

    # serverAppium.stop_server()
