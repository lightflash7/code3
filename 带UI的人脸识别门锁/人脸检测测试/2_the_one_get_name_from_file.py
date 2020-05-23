from ast import literal_eval
import cv2
import face_recognition
import numpy as np
from PIL import Image, ImageFont, ImageDraw


class Face_recognition:
    def __init__(self):
        self.face_locations = []
        self.face_encodings = []
        self.face_names = []
        self.process_this_frame = True

    def turn_on_camera(self):
        self.video_capture = cv2.VideoCapture(0)

    def save_people_to_file(self):
        f = open('./photos_of_people/people.txt',"w")
        f.writelines(str(self.known_face_names))
        f.close()
        pass

    def load_peole_from_file(self):
        f = open('./photos_of_people/people.txt',"r")
        self.known_face_names = literal_eval(f.readline())
        f.close()

    def get_known_face_encoding(self):
        self.known_face_encodings=[]
        for person in self.known_face_names:
            filename = './photos_of_people/'+person+'.jpg'
            person_image = face_recognition.load_image_file(filename)
            person_face_encoding = face_recognition.face_encodings(person_image)[0]
            self.known_face_encodings.append(person_face_encoding)

    def face_recognition(self):
        # Grab a single frame of video
        self.ret, self.frame = self.video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(self.frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if self.process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            self.face_locations = face_recognition.face_locations(rgb_small_frame)
            self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)

            self.face_names = []
            for face_encoding in self.face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                name = "未知"

                # # If a match was found in known_self.face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = self.known_face_names[best_match_index]

                self.face_names.append(name)

        self.process_this_frame = not self.process_this_frame

    def show_on_screen(self):
        for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(self.frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(self.frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            # cv2.putText(self.frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            fontpath = "./font/simsun.ttc"  # 宋体字体文件
            font_1 = ImageFont.truetype(fontpath, 30)  # 加载字体, 字体大小
            img_pil = Image.fromarray(self.frame)
            draw = ImageDraw.Draw(img_pil)
            draw.text((left + 10, bottom - 32), name, font=font_1, fill=(255, 255, 255))  # xy坐标, 内容, 字体, 颜色
            self.frame = np.array(img_pil)

        # Display the resulting image
        cv2.imshow('Camera', self.frame)
        cv2.waitKey(1)


if __name__ == '__main__':
    my_face_recognition = Face_recognition()
    my_face_recognition.turn_on_camera()
    # my_face_recognition.load_known_face()
    my_face_recognition.load_peole_from_file()
    my_face_recognition.get_known_face_encoding()
    while True:
        my_face_recognition.face_recognition()
        my_face_recognition.show_on_screen()

