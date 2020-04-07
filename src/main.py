import src.GetPCA as PCA
from PIL import Image

path = "D:/code/python/asignments/datashet/4/1.png"
image = Image.open(path)
image.show()
out = PCA.PCA(path)
print(out)
# show 5 image ket qua
for i in range(len(out)):
    im = Image.open(out[i])
    im.show()
