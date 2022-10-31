import datetime
import os
import subprocess
import time
import sys

# Открытие файла лога
f = open('/var/log/backup.log','a+')
f.write("Скрипт начал выполнение: " + datetime.datetime.now().strftime("%d-%m-%Y")+ "\n")

#Бэкап разделов и запись логов
portision1 = "/media/premiumq/Backup/Portision1_" + datetime.datetime.now().strftime("%d-%m-%Y") + ".img"
subprocess.run(["dd", "if=/dev/nvme0n1p1", "of=" + portision1])

f.write(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S") + " - Резервная копия раздела 1 создана!" + "\n")

portision2 = "/media/premiumq/Backup/Portision2_" + datetime.datetime.now().strftime("%d-%m-%Y") + ".img"
subprocess.run(["dd", "if=/dev/nvme0n1p2", "of=" + portision2])

f.write(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S") + " - Резервная копия раздела 2 создана!" + "\n")

portision3 = "/media/premiumq/Backup/Portision3_" + datetime.datetime.now().strftime("%d-%m-%Y") + ".img"
subprocess.run(["dd", "if=/dev/nvme0n1p3", "of=" + portision3])

f.write(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S") + " - Резервная копия раздела 3 создана!" + "\n")

portision4 = "/media/premiumq/Backup/Portision4_" + datetime.datetime.now().strftime("%d-%m-%Y") + ".img"
subprocess.run(["dd", "if=/dev/nvme0n1p4", "of=" + portision4])

f.write(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S") + " - Резервная копия раздела подкачки создана!" + "\n")
f.write(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S") + " - Скрипт успешно завершил свою работу." + "\n" + "\n")
f.close()

#Чистим файл, оставляем 100 строк
N = 100
with open("/var/log/backup.log","r+") as f:
   data = f.readlines()
   if len(data) > N: data = data[N:len(data)]
   f.seek(0)
   f.writelines(data)
   f.truncate()
f.close()
#Удаление файлов старше 15 дней

if len(sys.argv) != 2:
    sys.argv[0], "/media/premiumq/Backup"
    sys.exit(1)

workdir = sys.argv[1]

now = time.time()
old = now - 15 * 24 * 60 * 60

for f in os.listdir(workdir):
    path = os.path.join(workdir, f)
    if os.path.isfile(path):
        stat = os.stat(path)
        if stat.st_ctime < old:
            os.remove(path)

f = open('/var/log/backup.log','a+')
f.write(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S") + " - Файлы старше 15 дней, удалены." + "\n")
f.close()


