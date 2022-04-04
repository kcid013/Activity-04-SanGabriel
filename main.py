import cv2

print ("""[1] - fixed image of a cat
[2] - select your own image and flag
""")

opt = int(input("select: "))

if opt == 1:
    filePath = 'cat.jpg'
    windowTitle = 'picture of cat'
    readCVimg = cv2.imread(filePath, -1)
    cv2.imshow(windowTitle, readCVimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

elif opt == 2:
    windowTitle = 'chosen picture'
    filePath = input("type the name and extension of the image: ")
    print("""type of flags:
    [1] - colored
    [2] - grayscale
    [3] - unchanged
    """)
    opt = int(input("select: "))

    if opt == 1:
        flagType = 1
    elif opt == 2:
        flagType = 0
    elif opt == 3:
        flagType = -1

    readCVimg = cv2.imread(filePath, flagType)
    cv2.imshow(windowTitle, readCVimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()