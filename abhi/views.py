from django.shortcuts import render
from .models import BlogContent
from django.http import HttpResponse
from .test import testForm
from .test import ModelsDemoForm
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    return render(request ,'index.html',)



def blogs(request):
    obj=BlogContent.objects.all()
    context={"all_blogs" : obj}
    return render(request, 'pages/blogs.html',context)



def add_blog(request):
    return render (request, 'pages/add_blogs.html')




def add_blogs_handler(request):
    if request.GET.get('Name'):
        title_r=request.GET.get('Name')
        author_r=request.GET.get('Author')
        description_r=request.GET.get('description')
        no_of_lines_r = request.GET.get('no_of_lines')

        a=BlogContent(title= title_r , author = author_r , description =description_r , no_of_lines = no_of_lines_r)

        a.save() 
        return render (request,'pages/add_blogs.html',{'response_1':'blog saved successfully .....!'})
    else :
        return render (request,'pages/add_blogs.html',{'response_1':'some thing went wrong.....!'})
    



def delete_blogs_handler(request):
    if request.GET.get('id_1'):
        ID_r=request.GET.get('id_1')
        a=BlogContent.objects.get(id =ID_r)
        a.delete()

        return render (request,'pages/add_blogs.html',{'response':'blog deleted  successfully .....!'})
    else:
        return render (request,'pages/add_blogs.html',{'response':'something went wrong .....!'})



def test(request):
    form =testForm()
    return render (request ,'pages/testform.html',{'test':form})


def submit(request):
    return HttpResponse("submitted....!")


def modelsForm(request):
    success=''
    form=ModelsDemoForm(request.POST or None)
    if form.is_valid():
        form.save()
        success='form saved successfully....!'
    context={'form1':form , 'success1':success}
    return render (request,'pages/model_form.html',context)


def delete_by_id(request,id):
    BlogContent.objects.get(pk=id).delete()
    success='Deleted Successfully...!'
    return render(request,'pages/blogs.html',{'success1':success})


def update_blog(request ,id):
    obj=BlogContent.objects.get(id=id)
    return render (request,'pages/updateBlog.html',{'data':obj})

def update_data(request,id):
    success=''
    c_id=id
    c_title=request.POST.get('Name')
    c_author=request.POST.get('author')
    c_description=request.POST.get('description')
    c_no_of_line=request.POST.get('no_of_lines')
  
    obj=get_object_or_404(BlogContent,id=c_id)
    obj.title=c_title
    obj.author=c_author
    obj.description=c_description
    obj.no_of_lines=c_no_of_line

    obj.save()
    success=f"{c_id}data updated successfully"
    return render(request,'pages/blogs.html',{'success':success})




     