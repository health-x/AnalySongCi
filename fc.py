import jieba
import matplotlib
import matplotlib.pyplot as plt 

filename = '附件1：《宋词三百首》.txt'
file = open(filename,'r')
content = file.read().replace("，",",").replace("！",",").replace("“",",")\
            .replace("”",",").replace("。",",").replace("？",",").replace("：",",")\
            .replace("...",",").replace("、",",").replace('\u3000',',')\
            .replace(' ',',').replace('\n','').replace('-',',').strip()
file.close()
words =jieba.cut(content,cut_all=True)
counts = {}
for word in words:
    if ',' not in word:
        counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse =True)
print(items[:20])
x_word,y = [],[]
for i in items[:20]:
    x_word.append(i[0])
    y.append(i[1])
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize=(18,8),dpi=75)
x = range(len(x_word))
plt.title('宋词词频分析',fontsize=25)
plt.xlabel('词语',fontsize=25,labelpad=10)
plt.ylabel('词频',fontsize=25,labelpad=10)
plt.bar(x,y,width=0.5,color=['b','r','g','y','c','m','y','k','g','c','g'])
plt.xticks(x,x_word)
plt.show()
