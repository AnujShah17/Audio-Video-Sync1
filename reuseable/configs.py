import subprocess

global udid


class MobileConfig:
    port = 4723
    IP = "0.0.0.0"
    flash = []
    audio_det = []

    @staticmethod
    def get_device_udid():
        cmd = "adb devices -l"
        output = subprocess.check_output(cmd.split())
        devices = output.decode().strip().split("\n")[1:]
        if len(devices) == 1:
            return devices[0].split()[0]
        else:
            for device in devices:
                if "device" in device:
                    return device.split()[0]
        return None

    @staticmethod
    def get_android_version():
        cmd = "adb shell getprop ro.build.version.release"
        output = subprocess.check_output(cmd.split())
        version = output.decode().strip()
        return version

    desired_caps = {
        'deviceName': 'Pixel 2',
        'platformName': 'Android',
        'platformVersion': get_android_version(object),
        'udid': get_device_udid(object)
    }

