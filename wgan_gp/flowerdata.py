import numpy as np
import glob
import imageio
'''
装载 flower 数据集
'''
def load_data(dirname=None):
    if not dirname:
        dirname = 'D:/PythonWorkspace/GanLearning/images/flower'
    origin = 'D:/PythonWorkspace/GanLearning/images/flower'

    data = []
    for image in glob.glob(dirname + "/*"):
        image_data = imageio.imread(image)  # imageio 利用 PIL 来读取图片数据
        data.append(image_data)
    # 将数据标准化成 [-1, 1] 的取值, 这也是 Tanh 激活函数的输出范围
    input_data = np.array(data).astype(np.uint8)
    return input_data
