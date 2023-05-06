import os

# 需要重命名的文件夹路径
folder_path = 'E:\刻晴'

# 获取文件夹中所有的.wav文件
wav_files = [f for f in os.listdir(folder_path) if f.endswith('.wav')]

# 遍历所有的.wav文件，并逐个进行重命名
for i, wav_file in enumerate(wav_files):
    # 构建新文件名
    ss='vocals7-1_'
    new_filename = ss + str(i+1) + '.wav'
    
    # 构建完整的文件路径
    src = os.path.join(folder_path, wav_file)
    dst = os.path.join(folder_path, new_filename)
    
    # 进行文件重命名
    os.rename(src, dst)
