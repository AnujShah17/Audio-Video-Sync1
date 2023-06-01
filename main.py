import threading
import time
import simple_colors
from arduino import flash_detect
from reuseable import serverAppium
from testScripts import testgoogleFile
from reuseable.configs import MobileConfig
from testScripts import testVideo
from audio import listen
import excel_data

# from preRequisites import preSettings

x = True
if __name__ == '__main__':

    try:
        print("----pre setting is being executed----")
        # ser,led = preSettings.pre_req()
        serverAppium.start_server()
        ser, led = flash_detect.arduino()
        time.sleep(2)
        print(simple_colors.green("----pre setting has been finished sucessfully----"))
    except:
        x = False
        print(simple_colors.red("----pre settings has failed!----"))
    if x == True:
        try:
            print(simple_colors.blue("----Relauching the application----"))
            # testVideo.launch_appium_driver()
            testgoogleFile.launch_appium_driver()
        except:
            pass

        # pin,port=flash_detect.arduino()
        data1 = []
        # wb, ws, header_format=excel_data.starting_workbook()

        # print("Starting the thread",i)
        # thread1 = threading.Thread(target=testVideo.play_video)
        thread1 = threading.Thread(target=testgoogleFile.play_video)
        thread1.start()
        # thread6 = threading.Thread(target=listen.audio_return)
        # thread6.start()
        thread2 = threading.Thread(target=flash_detect.getArduino, args=(ser, led))
        thread2.start()
        # testVideo.timeSleep()
        # thread5 = threading.Thread(target=testVideo.pauseVideo)
        # thread5.start()
        # thread5.join()
        thread1.join()
        # thread6.join()
        thread2.join()
        # thread3.join()
        time.sleep(5)
        c = excel_data.appending(testVideo.dict)
        data1.append(c)
        print("--Flash--", MobileConfig.flash)
        print("--Audio--", MobileConfig.audio_det)
        # excel_data.creating_table(ws, data1, header_format)
        # testVideo.close_app()
        # excel_data.close_workbook(wb)


    else:
        print("There is an error in code!!")

    # serverAppium.stop_server()
