import os
import glob
import shutil

# 指定图片所在的文件夹路径
folder_path = "data/Norway_double/images"

# 获取文件夹中所有的图片文件
image_files = glob.glob(os.path.join(folder_path, "*.jpeg"))  # 修改文件扩展名以适应你的实际情况

# 遍历图片文件
for i in range(len(image_files)):
    if i % 5 != 0:
        # 删除后两个图片文件
        os.remove(image_files[i])

# 下面的代码好像没用到，反正就能处理了。，。，。

# # 移动图片到新文件夹中
# new_folder_path = "data/google_norway/images"  # 指定保存第一个图片的新文件夹路径
# os.makedirs(new_folder_path, exist_ok=True)

# # 遍历图片文件并将其写入新文件夹中
# for image_file in image_files:
#     shutil.copy(image_file, new_folder_path)