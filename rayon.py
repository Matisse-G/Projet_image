import numpy as np
import matplotlib.pyplot as plt
import skimage.color, skimage.measure

dossier = '/home/matisse/Projet_image/Code_bar/'

img = plt.imread(dossier + 'code1.webp')[:, :, :3] 
h,w,c = img.shape


fig, ax = plt.subplots()
ax.imshow(img)
ax.set_title('piece')
ax.axis('off')

pts = plt.ginput(n=2)   # attend 2 clics, renvoie [(x1, y1), (x2, y2)]
print(pts)

longueur = np.sqrt((pts[1][0]-pts[0][0])**2 + (pts[1][1]-pts[1][0])**2)

print(longueur)

L = max(95, longueur)
