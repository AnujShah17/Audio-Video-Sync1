import pandas as pd

df = pd.read_excel('analysis_31.xlsx', sheet_name='Flash')
da = pd.read_excel('analysis_31.xlsx', sheet_name='Audio')
# print(type(da['Audio value']))
# print(da['Audio_time'])
value_flash=[]
time_flash=[]
for i in range(len(df['flash_time'])):
    if float(df['flash_time'][i])<float(df['flash_time'][0]+15):
        if float(df['flash value'][i])>0.4:
            time_flash.append(df['flash_time'][i])
            value_flash.append(df['flash value'][i])
print(len(value_flash))

value_audio=[]
time_audio=[]
for i in range(len(da['Audio_time'])):
    if float(da['Audio_time'][i])<float(da['Audio_time'][0]+15):
        if float(da['Audio value'][i])>0.4:
            time_audio.append(da['Audio_time'][i])
            value_audio.append(da['Audio value'][i])
print(len(value_audio))

flash_data = {'flash value': value_flash, 'flash_time': time_flash}
audio_data = {'Audio value': value_audio, 'Audio_time': time_audio}
fdata = pd.DataFrame(flash_data)
adata = pd.DataFrame(audio_data)
writer = pd.ExcelWriter('Audio_video_data.xlsx', engine='xlsxwriter')
fdata.to_excel(writer, sheet_name='Flash', index=False)
adata.to_excel(writer, sheet_name='Audio', index=False)
writer.close()