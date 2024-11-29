import cv2
import numpy as np

class Banknot_Tanimlayici:
    def __init__(self):
        self.total = 0
        self.last_image = None

    def tanimalama_Fonksiyonu_B(self,img_path):
        image = cv2.imread(img_path)

        lower_5 = np.array([100, 0, 180])
        upper_5 = np.array([180, 45, 200])

        lower_10 = np.array([162, 20, 80])
        upper_10 = np.array([174, 255, 255])

        lower_20 = np.array([20, 40, 40])
        upper_20 = np.array([55, 255, 255])

        lower_50 = np.array([10, 50, 200])
        upper_50 = np.array([145, 103, 255])

        lower_100 = np.array([85, 8, 8])
        upper_100 = np.array([110, 205, 255])

        lower_200 = np.array([155, 30, 100])
        upper_200 = np.array([180, 250, 210])


        banknotes = [
            {"lower": lower_5, "upper": upper_5, "deger": "5"},
            {"lower": lower_10, "upper": upper_10, "deger": "10"},
            {"lower": lower_20, "upper": upper_20, "deger": "20"},
            {"lower": lower_50, "upper": upper_50, "deger": "50"},
            {"lower": lower_100, "upper": upper_100, "deger": "100"},
            {"lower": lower_200, "upper": upper_200, "deger": "200"}
        ]

        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        max_weight = 0
        max_name = None
        for filt in banknotes:
            mask_1 = cv2.inRange(hsv, filt["lower"], filt["upper"])
            #result_1 = cv2.bitwise_and(image, image, mask=mask_1)
            weight = cv2.countNonZero(mask_1)
            print(weight)
            if weight>=max_weight:
                max_weight = weight
                max_name = filt["deger"]

        self.total = max_name
        self.last_image = image