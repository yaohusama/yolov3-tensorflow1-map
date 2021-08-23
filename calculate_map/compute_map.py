from voc_eval import voc_eval
LABELS=["bus","car","train"]
history= {}
sum=0.
for i in range(len(LABELS)):
    rec,prec,ap = voc_eval(r'..\results\results{}.txt'.format(i), r'..\data\pascal_voc\VOCdevkit\VOC2007\an\{}.xml', r'..\results\index{}.txt'.format(i),
                           LABELS[i], '.',i)
    history[i]=ap
    sum=sum+ap
print(history)
print('map:',sum/len(LABELS))

