import numpy as np
import matplotlib.pyplot as plt
import skimage.color, skimage.measure

def w(k, h):
    x = 0
    y = 0
    for i in range (0, k):
        x+=h[i]
    for j in range (0, 256):
        y+=h[j]
    return x/y

def nu(k, h):
    x = 0
    y = 0
    for i in range (0, k):
        x+=i*h[i]
    for j in range (0, 256):
        y+=h[j]
    return x/y

dossier = '/home/matisse/Projet_image/images/'

img = plt.imread(dossier + 'code1.webp')[:, :, :3]
gray = skimage.color.rgb2gray(img)

fig, ax = plt.subplots()
ax.imshow(img)
ax.axis('off')
pts = plt.ginput(n=2)
plt.close(fig)


signature = skimage.measure.profile_line(gray, (pts[0][1], pts[0][0]), (pts[1][1], pts[1][0]), linewidth=5)

plt.figure()
plt.plot(signature)
plt.title('Signature')

h, bords = np.histogram(signature, bins=256, range=(0, 1))

bords = bords*255

plt.figure(2)
plt.bar(bords[:-1], h, width=bords[2]-bords[0])

crit = []
max = 0
seuil = 0

for i in range(0,256):
    index = w(i,h)*((nu(255,h)-nu(i,h))**2) + (1 - w(i,h))*(nu(i,h)**2)
    crit.append(index)
    if crit[i] > max:
        max = crit[i]
        seuil = i


for i in range(0,len(signature)):
    if signature[i] > seuil/255:
        signature[i] = 1
    else:
        signature[i] = 0
        
plt.figure()
plt.plot(signature)
plt.title('Signature')

indices = np.where(signature == 0)[0]
signature = signature[indices[0]:indices[-1] + 1]


plt.figure()
plt.plot(signature)
plt.title('Signature')


# longueur = signature

# print("la longueur de ce rayon utile est:",longueur)

# L = max(95, longueur)






















