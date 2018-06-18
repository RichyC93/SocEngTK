
import cv2, ftplib, paramiko, sys, time

camera = cv2.VideoCapture(1); time.sleep(0.1)
timestamp = time.ctime(); return_value, image = camera.read()
cv2.imwrite("snapshots/%s.png" % timestamp, image)
del(camera)

if raw_input("Upload? Default [N]: "):
    host = "45.55.210.48"; port = 22
    transport = paramiko.Transport((host, port))
    username = "root"; password = "herewasi13"
    transport.connect(username = username, password = password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    path = "/var/www/RC/RC/static/webcam.png"
    sftp.put("%s.png" % timestamp, path); sftp.close()
    transport.close()
    print "Upload Done!"
