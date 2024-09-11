import os
from PIL import Image
import numpy as np


def modify_image_pixels(directory):
    # 遍历目录下的所有文件
    for filename in os.listdir(directory):
        # 构建完整的文件路径
        file_path = os.path.join(directory, filename)
        # 检查文件是否为图片
        if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            # 加载图片
            img = Image.open(file_path)
            # 将图片转换为数组
            img_array = np.array(img)
            # 修改像素值：将1改为255
            img_array[img_array == 1] = 255
            # 将修改后的数组转换回图片
            new_img = Image.fromarray(img_array)
            # 构建新的文件路径以保存修改后的图片
            new_file_path = os.path.join(directory, 'modified_' + filename)
            # 保存修改后的图片
            new_img.save(new_file_path)
            print(f"图片已修改并保存为: {new_file_path}")


# 指定你的目录路径
directory_path = 'your_directory_path_here'
modify_image_pixels(directory_path)
