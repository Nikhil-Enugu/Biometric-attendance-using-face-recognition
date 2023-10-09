# Biometric-attendance-using-face-recognition
Introduction: Welcome to the Biomertic attendance using face recognition project repository! 
Firstly the unique QR is generated to each individual which decodes to their unique ID and it is saved as 'ID.png' in the folder 'qr' and their images are saved as 'ID.jpg' in the folder 'faces'.
When the program runs it asks the user to show the qr when the qr is detected in the camera, cv2 decodes the qr and asks the user to show the face.

There are four possible outcomes of the program. They are:
 1) If cv2 doesn't detect the face, it displays the message "Try Again".
 2) If the decoded ID of the QR is not stored in the system, it displays "Invalid QR".
 3) If the face encodings doesn't match with the stored face encodings, it displays "No Match".
 4) If the face encodings match with the stored face encodings, it marks the attendance in the excel sheet and displays the message "Attendance Marked".

Concepts and Libraries utilized:
 1) Tkinter: Tkinter is a standard GUI (Graphical User Interface) library in Python.
 2) NumPy: NumPy enables efficient numerical computations, allowing us to handle arrays and matrices with ease.
 3) cv2: cv2 is used for open-source computer vision, image processing and for decoding the QR.
 4) face_recognition: face_recognition provides API for working with face recognition and facial features detection.
 5) PIL: PIL is used for opening, manipulating, and saving many different image file formats.
 6) OS: OS provides a way to interact with the operating system.It allows us to perform various tasks related to file.
 7) datetime: It allows us to perform various operations related to date and time calculations, formatting, and manipulation.
 8) time: time provides various functions for working with time-related operations like sleep.
 9) openpyxl: openpyxl provides a convenient way to read and write Excel spreadsheets.
