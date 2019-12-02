from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def count(request):
    usertext = request.GET['text']
    word_count = {}
    for word in usertext:
        if word not in word_count:
            word_count[word]=1
        else:
            word_count[word]+=1
    sorted_dict=sorted(word_count.items(),key=lambda w:w[1],reverse=True )
    context={
        'total_count':len(request.GET['text']),
        'text':usertext,
        'word_dict':sorted_dict
    }
    return render(request,'count.html',context=context)
