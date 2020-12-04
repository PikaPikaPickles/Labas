import numpy as np
from PIL import Image
img = Image.open('lunar02_raw.jpg')
ImgData = np.array(img)
ImgData =ImgData - np.full(ImgData.shape,ImgData.min())
Kof = 255/ImgData.max()
ImgData_ex = ImgData * Kof
print(ImgData_ex)
#print(ImgData)
updated_data = ImgData_ex
res_img = Image.fromarray(updated_data.astype(np.uint8))
res_img.save('NovoeGoto.jpg')
