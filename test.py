import os

def list_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            print(file_path)

# 指定文件夹路径
folder_path = "c:\\Users\\60331\\Downloads"

# 调用函数列出文件
list_files(folder_path)