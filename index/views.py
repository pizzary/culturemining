from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, "index.html")

def user(request):
    return render(request, 'personalspace.html')

def news(request):
    return render(request, 'news.html')
#
# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             next_url = request.GET.get('next', '/')
#             return redirect(next_url)
#         else:
#             # 登录失败，返回错误信息给模板
#             error_message = 'Invalid username or password.'
#             return render(request, 'login.html', {'error_message': error_message})
#     else:
#         return render(request, 'login.html')
#
# def register(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         # 创建新用户
#         user = User.objects.create_user(username=username, email=email, password=password)
#         # 登录新用户
#         login(user)
#
#         # 注册成功，重定向到某个页面
#         return redirect('login.html')
#     else:
#         return render(request, 'register.html')

