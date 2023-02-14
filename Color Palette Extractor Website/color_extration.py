import numpy as np
from PIL import Image, ImageDraw
from sklearn.cluster import KMeans

def path_to_img_array(path):
    '''
    Load image into numpy array
    '''
    img = Image.open(path)
    vec = np.array(img)
    return vec


def pick_colors(vec, numColors):
    '''
    Do k-means clustering over ``vec`` to return ``numColors``
    '''
    vec = vec.reshape(-1, 3)
    model = KMeans(n_clusters=numColors).fit(vec)
    return model.cluster_centers_


def show_key_colors(colorList):
    '''
    Make a long rectangle, composed of the colors
    detailed in colorList, a list of (R, G, B) tuples
    '''
    n = len(colorList)

    im = Image.new('RGBA', (100 * n, 100))
    draw = ImageDraw.Draw(im)

    save_colors = []
    for idx, color in enumerate(colorList):
        color = tuple([int(x) for x in color])
        save_colors.append(color)
        draw.rectangle([(100 * idx, 0), (100 * (idx + 1), 100 * (idx + 1))], fill=tuple(color))

    im.save("static/images/savethis.png")
    return save_colors



#  # Load an image up to a vector, from a given path
#  path = 'static/images/tt_white.png'
#  vec = path_to_img_array(path)
#
#  # Unrolls our image and runs K-Means clustering to find "Target Points" all of the pixel values are grouped around
#  colors = pick_colors(vec, 3)
#  show_key_colors(colors)
#  # Finally, one last function to take these Targets and plot out some simple boxes to show the colors it found

#plt.imshow(colors)
#plt.imshow(show_key_colors(pick_colors(vec, 2)))


""" 
    EXPLANATION
# img = Image.open('static/images/dog.jpg')  # open
# print(img)
# print(type(img))

# vec = np.array(img)  # make array
# print(vec.shape)  # rgb layout
# print(img.size)

# K-Means Clustering ex: "Aproximação de medias de numerous de cores, (para classificação)

# eshaped = vec.reshape(-1, 3)  # -1 para np separar em Red Green Blue
# rint(reshaped.shape)  # one long chain of RGB values

"""