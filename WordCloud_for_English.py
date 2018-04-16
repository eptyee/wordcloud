
# coding: utf-8
from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS,  ImageColorGenerator

# set the dir path
dir = path.dirname('.')
text = open(path.join(dir, 'English.txt')).read()# the words are saved in the text
# set the color_mask
mask_coloring = imread(path.join(dir, "th.png"))
wc = WordCloud(background_color="white",
                            max_words=1000,                           mask=mask_coloring,                         
                            max_font_size=80,                           random_state=80)
#
wc.generate(text) 
image_colors = ImageColorGenerator(mask_coloring) # 
plt.figure()
plt.imshow(wc)
plt.axis("off")
# 
plt.figure()
plt.imshow(wc.recolor(color_func=image_colors))  # recolor wordcloud and show
plt.axis("off")
#
plt.figure()
plt.imshow(mask_coloring, cmap=plt.cm.gray)
plt.axis("off")
plt.show()
# save the files
wc.to_file(path.join(dir, "wordcloud.png"))
