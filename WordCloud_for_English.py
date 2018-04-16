
# coding: utf-8

# In[1]:


from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS,  ImageColorGenerator
# 获取当前文件路径
dir = path.dirname('.')
text = open(path.join(dir, 'English.txt')).read()#英文直接读取
# 设置背景图片
mask_coloring = imread(path.join(dir, "th.png"))
wc = WordCloud(background_color="white", #背景颜色
                            max_words=1000,# 词云显示的最大词�?                            mask=mask_coloring,#设置背景图片                          
                            max_font_size=80, #字体最大�?                            random_state=80)
wc.generate(text) #分词
image_colors = ImageColorGenerator(mask_coloring) # 从背景图片生成颜色�?# 显示图片
plt.figure()
plt.imshow(wc)
plt.axis("off")
# 绘制词云
plt.figure()
plt.imshow(wc.recolor(color_func=image_colors))  # recolor wordcloud and show
plt.axis("off")
# 绘制背景图片为颜色的图片
plt.figure()
plt.imshow(mask_coloring, cmap=plt.cm.gray)
plt.axis("off")
plt.show()
# 保存图片
wc.to_file(path.join(dir, "wordcloud.png"))