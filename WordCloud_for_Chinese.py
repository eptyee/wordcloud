
# coding: utf-8

# In[2]:


from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
# 获取当前文件路径
dir = path.dirname('.')
text1=open(path.join(dir,'chinese.txt')).read()
text2 = jieba.cut_for_search(text1)
text_ch=" ".join(text2)
# 设置背景图片
mask_coloring = imread(path.join(dir, "mask.png"))
wc = WordCloud(font_path='simsun.ttf',mask=mask_coloring,
                    background_color="white", max_words=2000,
                    max_font_size=80, random_state=80)
# 生成词云
wc.generate(text_ch)
image_colors = ImageColorGenerator(mask_coloring) # 从背景图片生成颜色�?# 显示图片
plt.figure()
plt.imshow(wc)
plt.axis("off")
# 绘制词云
plt.figure()
plt.imshow(wc.recolor(color_func=image_colors)) # recolor wordcloud and show
plt.axis("off")
# 绘制背景图片为颜色的图片
plt.figure()
plt.imshow(mask_coloring, cmap=plt.cm.gray)
plt.axis("off")
plt.show()
# 保存图片
wc.to_file(path.join(dir, "词云.png"))