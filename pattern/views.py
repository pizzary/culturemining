from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

import cv2
import numpy as np
from django.http import JsonResponse, HttpResponse
from .image_retrieval import algorithm2
from .models import Patternbank, Category_Article, Dynasty_Article
from django.db.models import Q
# Create your views here.
def pattern(request):
    if request.method == 'GET':
        search_query = request.GET.get('search_query', '')  # 获取搜索关键字
        dynasty = request.GET.get('dynasty', '')  # 获取选择的年代
        category = request.GET.get('category', '')  # 获取选择的类别
        species = request.GET.get('species', '')  # 获取选择的类别

        patterns = Patternbank.objects.all()  # 获取所有Patternbank对象

        if search_query:
            # 使用Q对象进行多列搜索
            patterns = patterns.filter(
                Q(name__icontains=search_query) |
                Q(category__icontains=search_query) |
                Q(species__icontains=search_query) |
                Q(dynasty__icontains=search_query) |
                Q(content__icontains=search_query) |
                Q(patterns__icontains=search_query)
                # 添加其他需要搜索的列
            )
        if dynasty:
            patterns = patterns.filter(dynasty=dynasty)  # 根据年代进行过滤
            print(1)
        if category:
            patterns = patterns.filter(category=category)  # 根据类别进行过滤
            print(2)
        if species:
            patterns = patterns.filter(species=species)  # 根据寓意进行过滤

        context = {'patterns': patterns}
        return render(request, 'pattern.html', context)
    else:
        return render(request, "pattern.html")

def passage(request, title, type):
    articles1 = Category_Article.objects.all()
    articles2 = Dynasty_Article.objects.all()
    if type == 1:
        link = Category_Article.objects.filter(category__icontains=title)  # 根据搜索字符串进行查找，使用 icontains 进行不区分大小写的模糊匹配
    elif type == 2:
        link = Dynasty_Article.objects.filter(dynasty__icontains=title)  # 根据搜索字符串进行查找，使用 icontains 进行不区分大小写的模糊匹配
        print(len(link))
    else:
        link = None
    return render(request, "passage.html", {'articles1': articles1, 'articles2': articles2, 'link': link, 'type': type})
"""
def passage_index_link(request, title):

    context = {
        'dynasty': title,
        # 其他需要传递给模板的数据...
    }
    return render(request, 'pattern.html', context)
"""
def single(request):
    return render(request, "blog.html")

def blog(request):
    return render(request, "blog.html")

def retrieval(request):
    if request.method == 'POST':
        # 获取上传的图像文件
        uploaded_image = request.FILES['image']

        # 读取上传的图像文件
        image_data = uploaded_image.read()

        # 传递数据库中的图像路径列表
        database_image_bytes = Patternbank.objects.values_list('img_bytes', flat=True)
        database_image_urls = Patternbank.objects.values_list('img', flat=True)

        # 执行图像检索算法，根据选择的算法处理图像
        algorithm = request.POST.get('algorithm')  # 获取选择的算法

        if algorithm == 'algorithm2':
            # 使用算法2进行处理
            results = algorithm2(image_data, database_image_bytes, database_image_urls)

            # Create a list to hold the content of each image
            image_contents = []
            i = 0
            for result in results:

                i = i + 1
                image_url, similarity = result
                if similarity != 1.0:
                    break
                # Append the content of the image to the list
                image_contents.append(image_url)
            data = {
                'similar_image_bytes': image_data,
                'image_urls': image_contents
            }
            return render(request, "retrieval.html", data)
    else:
        data = {
            # 'similar_image_bytes': image_data,
            # 'image_urls': image_contents
            'url': Patternbank.objects.first().img
        }
        return render(request, "retrieval.html", data)
