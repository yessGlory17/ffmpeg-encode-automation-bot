# Hedef dosya yolu iste
# Bu dosya içerisindeki .mp4 uzantılı videoları bul.
# x dakika bekleterek bu komutları çalıştır.
import os
import time

print(""" 
##############################################################################
#                                                                            #
#                     Created By yessGlory for                               #
#                                                                            #
#               _ffmpeg encoder automation v1.0 Beta_                        #
#                                                                            #
##############################################################################
""")

path = str(input("Videos file path : "))

print(os.listdir(path))

for i in os.listdir(path):
    if i.endswith('.mp4'):
        print("Mp4 detected : ", i)
        time.sleep(2)
        print("Encode is starting....")
        time.sleep(2)
        encodepath = path + "\\" + i
        splitname = i.split('.')
        outputname = splitname[0] + "OP" + ".mp4"
        print("Outputname : ", outputname)
        print("Encode path: " , encodepath)
        out = path + "\\" + outputname
        print("KAYIT YOLU : " + out)
        command = "ffmpeg -i "+ encodepath + " -vcodec libx265 -crf 28 " + out
        os.system(command)
        time.sleep(1)
        print("\a\a\a")

        