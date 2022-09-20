import os
import imageio.v2
myfiles = os.listdir('image')
images = []
for i in range(len(myfiles)):
    image = imageio.imread(myfiles[i])
    images.append(image)
imageio.mimsave('gif.gif', images)