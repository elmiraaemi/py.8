import os
import imageio
file_list=sorted(os.listdir("python/T8/image"))
images=[]
for file in file_list:
    file_path="python/T8/imag/"+file
    IMage=imageio.imread(file_path)
    images.append(IMage)
imageio.mimsave("python/T8/image/mygif.gif",images)
