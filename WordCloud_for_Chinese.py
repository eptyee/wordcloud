
# coding: utf-8
from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
# 设置文件路径
dir = path.dirname('.')
text1=open(path.join(dir,'chinese.txt')).read()
text2 = jieba.cut_for_search(text1)
text_ch=" ".join(text2)
# 设置词云蒙版
mask_coloring = imread(path.join(dir, "mask.png"))
wc = WordCloud(font_path='simsun.ttf',mask=mask_coloring,
                    background_color="white", max_words=2000,
                    max_font_size=80, random_state=80)
# 生成词云图
wc.generate(text_ch)
image_colors = ImageColorGenerator(mask_coloring) # 原始色彩
plt.figure()
plt.imshow(wc)
plt.axis("off")
# 生成词云图
plt.figure()
plt.imshow(wc.recolor(color_func=image_colors)) # 重置为底图色彩蒙版
plt.axis("off")
# 生成词云图
plt.figure()
plt.imshow(mask_coloring, cmap=plt.cm.gray)
plt.axis("off")
plt.show()
# 保存
wc.to_file(path.join(dir, "词云.png"))
