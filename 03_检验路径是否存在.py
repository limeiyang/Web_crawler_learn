
import os
path = "C:\/Users\/Administrator\/Desktop\/武汉工程大学2019年3月2日"
if not os.path.exists(path):
    print("路径不存在，进行创建")
    os.makedirs(path);
    print("创建成功。")
    pass
else:
    print("文件路径存在")
    pass
