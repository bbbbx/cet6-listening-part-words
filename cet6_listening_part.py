from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud

d = path.dirname(__file__)

# 读文本
text = open(path.join(d, 'cet6_listening_part.txt')).read()

# read the mask / color image taken from
cet6_coloring = np.array(Image.open(path.join(d, "mask_cet6.png")))

wordcloud = WordCloud(width=1200, height=800, max_font_size=120).generate(text)
cet_6_wordcloud = WordCloud(background_color="white", max_words=500, mask=cet6_coloring,
               max_font_size=40, random_state=42, width=2000, height=1200)
# 生成词云
cet_6_wordcloud.generate(text)

# store to file
cet_6_wordcloud.to_file(path.join(d, "word_cloud_cet_6.png"))
wordcloud.to_file(path.join(d, "word_cloud.png"))

# show
plt.imshow(cet_6_wordcloud, interpolation="bilinear")
plt.axis("off")
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()