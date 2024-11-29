import cv2
import numpy as np

class Madeni_Para_Tanimlayici:

    def __init__(self):
        self.total = 0
        self.last_image = None

    def tanimalama_Fonksiyonu(self,image_path):
        image = cv2.imread(image_path)
        image_blur = cv2.medianBlur(image,25)
        image_blur_gray = cv2.cvtColor(image_blur, cv2.COLOR_BGR2GRAY)
        image_res ,image_thresh = cv2.threshold(image_blur_gray,240,400,cv2.THRESH_BINARY_INV)

        madeni_para_deger = []

        contours , _ = cv2.findContours(image_thresh , cv2.RETR_TREE , cv2.CHAIN_APPROX_TC89_KCOS)
        area = {}
        for i in range(len(contours)):
            cnt = contours[i]
            ar = cv2.contourArea(cnt)
            print(ar)
            area[i] = ar
            if ar > 200:  # Filter based on minimum area threshold
                M = cv2.moments(cnt)
                if M["m00"] != 0:
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])

                    # Append area and coordinates as a dictionary
                    madeni_para_deger.append({
                        "area": ar,
                        "center_x": cX,
                        "center_y": cY
                    })


        srt = sorted(area.items() , key = lambda x : x[1] , reverse = True)
        results = np.array(srt).astype("int")
        num = np.argwhere(results[: , 1] > 200).shape[0]

        for i in range(1 , num):
            image_copy = cv2.drawContours(image , contours , results[i , 0] ,(0 , 255 , 0) , 3)
        print("Number of coins is " , num - 1)

        for mp_deger in madeni_para_deger:
            if(int(mp_deger['area'])>12000):
                deger = "  1 TL"
                self.total += 1
            elif (int(mp_deger['area']) > 10000 and int(mp_deger['area']) < 12000):
                deger = "50 Kurus"
                self.total += 0.5
            elif (int(mp_deger['area']) > 7000 and int(mp_deger['area']) < 9000):
                deger = "25 Kurus"
                self.total += 0.25
            elif (int(mp_deger['area']) > 6000 and int(mp_deger['area']) < 7000):
                deger = "10 Kurus"
                self.total += 0.1
            elif (int(mp_deger['area']) > 4500 and int(mp_deger['area']) < 7000):
                deger = "5 Kurus"
                self.total += 0.05
            else:
                deger="0TL"



            cv2.putText(
                image,
                f"{deger}",
                (mp_deger['center_x'] - 33, mp_deger['center_y']),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 0, 0),
                2
            )
        #cv2.imwrite(r"img.jpg", image_copy)
        self.last_image = image_copy
        cv2.waitKey(0)

#mpt_1 = Madeni_Para_Tanimlayici()
#mpt_1.tanimalama_Fonksiyonu("madeni_para_1.jpg")
