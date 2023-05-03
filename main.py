import imhancer
import cv2 as cv
import os
import shutil

# define a video capture object and chnage source as needed
vid = cv.VideoCapture(1)
folder_name = "temp_files"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    # get the path of the new folder
temp_path = os.path.abspath(folder_name)
print("New folder created at:", temp_path)


initial_value = 0.5
scaling_factor = 100
def on_change(val):
    value = val / scaling_factor

def validate(value):
    if value < 1:
        cv.setTrackbarPos("thresh_min", "pst", 1)
    elif value > 100:
        cv.setTrackbarPos("thresh_min", "pst", 100)
    else:
        pass

# S = 0.2
# T = 0.01
# b = 0.16
# G = 1.4
# Trackbar for Vevid
cv.namedWindow("Vevid")
cv.createTrackbar("S", "Vevid", 20,1000, on_change)
cv.createTrackbar("T", "Vevid",  1,100, on_change)
cv.createTrackbar("b", "Vevid",  16,100, on_change)
cv.createTrackbar("G", "Vevid",  14,100, on_change)

# Trackbar for PST

# S = 0.3 100
# W = 15
# sigma_LPF = 0.15 100
# thresh_min = 0.05 100
# thresh_max = 0.9 10
# morph_flag = 1 10

cv.namedWindow("pst")
cv.createTrackbar("S", "pst", 30,100, on_change)
cv.createTrackbar("W", "pst",  15,100, on_change)
cv.createTrackbar("sigma_LPF", "pst",  15,100, on_change)
cv.createTrackbar("thresh_min", "pst",  5,100, validate)
cv.createTrackbar("thresh_max", "pst",  9,99, on_change)
cv.createTrackbar("morph_flag", "pst",  1,100, on_change)

# Trackbar for PAGE
# cv.namedWindow("page")
# cv.createTrackbar("mu_1", "page", int(initial_value * scaling_factor), scaling_factor, on_change)
# cv.createTrackbar("mu_2", "page",  int(initial_value * scaling_factor), scaling_factor, on_change)
# cv.createTrackbar("sigma_1", "page",  int(initial_value * scaling_factor), scaling_factor, on_change)
# cv.createTrackbar("sigma_2", "page",  int(initial_value * scaling_factor), 100, on_change)
# cv.createTrackbar("S1", "page",  int(initial_value * scaling_factor), scaling_factor, on_change)
# cv.createTrackbar("S2", "page",  int(initial_value * scaling_factor), 100, on_change)
# cv.createTrackbar("sigma_LPF", "page",  int(initial_value * scaling_factor), scaling_factor, on_change)
# cv.createTrackbar("thresh_min", "page",  int(initial_value * scaling_factor), 100, on_change)
# cv.createTrackbar("thresh_max", "page",  int(initial_value * scaling_factor), scaling_factor, on_change)
# cv.createTrackbar("morph_flag", "page",  int(initial_value * scaling_factor), 100, on_change)




while (True):
    ret, frame = vid.read()
    img_path = temp_path+"/1.png"
    cv.imwrite(img_path, frame)

    # S = 0.2
    # T = 0.01
    # b = 0.16
    # G = 1.4

    S = cv.getTrackbarPos("S", "Vevid") / 100
    T = cv.getTrackbarPos("T", "Vevid") / 100
    b = cv.getTrackbarPos("b", "Vevid") / 100
    G = cv.getTrackbarPos("G", "Vevid") / 10

    # parameters for the pst

    # S = 0.3 100
    # W = 15
    # sigma_LPF = 0.15 100
    # thresh_min = 0.05 100
    # thresh_max = 0.9 10
    # morph_flag = 1 10
    pst_S = cv.getTrackbarPos("S", "pst") / 10
    W = cv.getTrackbarPos("W", "pst")
    sigma_LPF = cv.getTrackbarPos("sigma_LPF", "pst") / 100
    thresh_min = cv.getTrackbarPos("thresh_min", "pst") / 100
    thresh_max = cv.getTrackbarPos("thresh_max", "pst") / 100
    morph_flag = cv.getTrackbarPos("morph_flag", "pst")/ 10


    # mu_1 = 0
    # mu_2 = 0.35
    # sigma_1 = 0.05
    # sigma_2 = 0.7
    # S1 = 0.8
    # S2 = 0.8
    # sigma_LPF = 0.1
    # thresh_min = 0.0
    # thresh_max = 0.9
    # morph_flag = 1

    # mu_1 = cv.getTrackbarPos("mu_1", "page")/100
    # mu_2 = cv.getTrackbarPos("mu_2", "page")/100
    # sigma_1 = cv.getTrackbarPos("sigma_1", "page")/100
    # sigma_2 = cv.getTrackbarPos("sigma_2", "page")/100
    # S1 = cv.getTrackbarPos("S1", "page")/100
    # S2 = cv.getTrackbarPos("S2", "page")/100
    # page_sigma_LPF = cv.getTrackbarPos("sigma_LPF", "page")/100
    # page_thresh_min = cv.getTrackbarPos("thresh_min", "page")/100
    # page_thresh_max = cv.getTrackbarPos("thresh_max", "page")/100
    # page_morph_flag = cv.getTrackbarPos("morph_flag", "page")/100
    font = cv.FONT_HERSHEY_SIMPLEX | cv.FONT_ITALIC

    # S = 0.3
    # W = 15
    # sigma_LPF = 0.15
    # thresh_min = 0.05
    # thresh_max = 0.9
    # morph_flag = 1

    cv.imshow('Input', frame)
    vevid_img = cv.cvtColor(imhancer.enhance(img_file=img_path, vS=S, vT= T, vb=b, vG=G), cv.COLOR_RGB2BGR)
    content = f"S={S}\nT={T}\nb={b}\nG={G}"
    lines = content.split('\n')
    y = 20
    for line in lines:
        cv.putText(vevid_img, line, (7, y), font, 0.5, (0, 0, 255), 2, cv.LINE_AA)
        y += 20  # increase y coordinate for next line
    cv.imshow("Vevid", vevid_img)


    pst_img = imhancer.pst(img_file=img_path, pst_S=pst_S, pst_W=W, pst_sigma_LPF= sigma_LPF, pst_thresh_min=thresh_min, pst_thresh_max=thresh_max, pst_morph_flag=morph_flag )
    pst_img = cv.cvtColor(pst_img, cv.COLOR_GRAY2BGR)
    # content = f"S={pst_S} W={W} sigma_LPF={sigma_LPF} thresh_min={thresh_min} thresh_max={thresh_max} morph_flag={morph_flag}"
    content = f"S={pst_S}\nW={W}\nsigma_LPF={sigma_LPF}\nthresh_min={thresh_min}\nthresh_max={thresh_max}\nmorph_flag={morph_flag}"
    lines = content.split('\n')
    y = 20
    for line in lines:
        cv.putText(pst_img, line, (7, y), font, 0.5, (0, 0, 255), 2, cv.LINE_AA)
        y += 20  # increase y coordinate for next line


    # cv.putText(pst_img, content, (7, 70), font, 1, (100, 255, 0), 3, cv.LINE_AA)
    cv.imshow("pst", pst_img)

    # page_img = imhancer.page(img_file=img_path,mu_1=mu_1, mu_2=mu_2, sigma_1=sigma_1, sigma_2=sigma_2, S1=S1, S2=S2, sigma_LPF=page_sigma_LPF,thresh_min=page_thresh_min,thresh_max=page_thresh_max,morph_flag=page_morph_flag)
    # cv.imshow("page", page_img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        shutil.rmtree(temp_path)
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv.destroyAllWindows()
