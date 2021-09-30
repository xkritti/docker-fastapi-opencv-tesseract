# import cv2
# import numpy as np
# import pytesseract



# """ img import """
# img = cv2.imread("images/img-001.jpg")
# """ resize to 50 %"""
# width = int(img.shape[1] * 50 / 100)
# height = int(img.shape[0] * 50 / 100)
# dsize = (width, height)
# resize = cv2.resize(img, dsize)
# cv2.imshow("input image", resize)
# """ convert bgr to hsv """
# hsv = cv2.cvtColor(resize, cv2.COLOR_BGR2HSV)

# # find bule green red square
# """ find blue square """
# lower_blue = np.array([75, 125, 125])
# upper_blue = np.array([130, 255, 255])
# mask = cv2.inRange(hsv, lower_blue, upper_blue)

# """find contours of blue square"""
# (cnts, _) = cv2.findContours(mask.copy(),
#                              cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# """ crop img bule square"""
# for c in cnts:
#     x, y, w, h = cv2.boundingRect(c)
#     if w > 50 and h > 50:
#         img1 = resize[y:y+h, x:x+w]
#         #  img1 => crop bulesquare img
#         cv2.imshow("Crop 1 IMG", img1)
#         """ find red,green squaer in bulesquare img """
#         # find green ( Text in green is code room )
#         hsv2 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
#         lower_green = np.array([38, 125, 125])
#         upper_green = np.array([75, 255, 255])
#         mask2 = cv2.inRange(hsv2, lower_green, upper_green)
#         # findcontours of green square
#         (cnts1, _) = cv2.findContours(mask2.copy(),
#                                       cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#         for c in cnts1:
#             x, y, w, h = cv2.boundingRect(c)
#             if w > 50 and h > 50:
#                 img2 = img1[y:y+h, x:x+w]
#                 # img2 => crop greenquare img
#                 ocr_result1 = pytesseract.image_to_string(img2, lang="eng")
#                 print('ocr_result1 :', ocr_result1)
#                 cv2.imshow("Crop 2 IMG", img2)

#         # find red ( Text in red is electicity unit )
#         hsv3 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
#         lower_red = np.array([0, 125, 125])
#         upper_red = np.array([35, 255, 255])
#         mask3 = cv2.inRange(hsv3, lower_red, upper_red)
#         # findcontours of red square
#         (cnts2, _) = cv2.findContours(mask3.copy(),
#                                       cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#         for c in cnts2:
#             x, y, w, h = cv2.boundingRect(c)
#             if w > 50 and h > 50:
#                 img3 = img1[y:y+h, x:x+w]
#                 hImg, wImg, _ = img3.shape
#                 # img3 => crop rednquare img
#                 res = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
#                 im_bw = cv2.threshold(res, 115, 255, cv2.THRESH_BINARY)[1]
#                 test = cv2.bitwise_not(im_bw)
#                 blurred = cv2.GaussianBlur(test, (3, 3), 3)
#                 ocr_result2 = pytesseract.image_to_string(
#                     blurred, config="--oem 3 -c tessedit_char_whitelist=0123456789")
#                 temp = pytesseract.image_to_boxes(
#                     blurred, config="--oem 3 -c tessedit_char_whitelist=0123456789")
#                 for b in temp.splitlines():
#                     b = b.split(' ')
#                     x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
#                     cv2.rectangle(img3, (x, hImg-y),
#                                   (w, hImg-h), (0, 255, 0), 1)
#                     cv2.putText(img3, b[0], (x, hImg-y),
#                                 cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 1)

#                 print('ocr_result2 :', ocr_result2)
#                 cv2.imshow("Crop 3 IMG", img3)

# # cv2.imwrite(str(idx) + '.png', new_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
