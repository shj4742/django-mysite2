from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from .models import FoodCalorie


def index(request):
    food_list =  FoodCalorie.objects.all()
    # 每页显示10条数据
    paginator = Paginator(food_list, 5, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page 不是整数 显示第一页
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果page 溢出了则显示最后一条
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'calorie_counter.html', {'contacts': contacts})