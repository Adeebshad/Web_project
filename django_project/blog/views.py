from django.shortcuts import render
posts = [
    {
        'author': "Adeeb",
        'title':'Logistic Regression',
        'content':'Logistic regression is the appropriate regression analysis to conduct when the dependent variable is dichotomous (binary).  Like all regression analyses, the logistic regression is a predictive analysis.',
        'date_posted': 'August 5, 2020',
        'new' : 5
        # 'image':"./Capture.JPG"

    },
    {
        'author': "Rakib",
        'title':'Convolutional Neural Network',
        'content':'In deep learning, a convolutional neural network is a class of deep neural networks, most commonly applied to analyzing visual imagery. They are also known as shift invariant or space invariant artificial neural networks,based on their shared-weights architecture and translation invariance characteristics.',
        'date_posted': 'August 15, 2020',
        'new': 12
        # 'image':"./Capture.JPG"

    }
]
# Create your views here.

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title': 'About' })