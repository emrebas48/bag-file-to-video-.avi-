@Author Emre Bas

# first we install the packages
# Zuerst installieren wir die Pakete
import cv2
import numpy as np

# Create a VideoCapture object
# Erstellen Sie ein VideoCapture-Objekt

cap = cv2.VideoCapture(1)

# Check if camera opened successfully
# Überprüfen Sie, ob die Kamera erfolgreich geöffnet wurde
if (cap.isOpened() == False):
    print("Unable to read camera feed")

# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# Standardauflösungen des Frames werden abgerufen. Die Standardauflösungen sind systemabhängig.
# We convert the resolutions from float to integer.
# Wir wandeln die Auflösungen von Float in Integer um.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
# Definieren Sie den Codec und erstellen Sie ein VideoWriter-Objekt. Die Ausgabe wird in der Datei 'outpy.avi' gespeichert.
out = cv2.VideoWriter('output/test.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

while(True):
    ret, frame = cap.read()

    if ret == True:

        # Write the frame into the file 'output.avi'
        # Frame in die Datei 'output.avi' schreiben
        out.write(frame)

        # Display the resulting frame
        # Den resultierenden Rahmen anzeigen
        cv2.imshow('frame',frame)

        # Press Q on keyboard to stop recording
        # Drücken Sie Q auf der Tastatur, um die Aufnahme zu stoppen
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Break the loop
    # Unterbrechen Sie die Schleife
    else:
        break

# When everything done, release the video capture and video write objects
# Wenn alles erledigt ist, geben Sie die Objekte Video Capture und Video Write frei
cap.release()
out.release()

# Closes all the frames
# Schließt alle Frames
cv2.destroyAllWindows()



