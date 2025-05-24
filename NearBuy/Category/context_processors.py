from .models import Category

def Category_list(request):
    categories = Category.objects.all()
    return {'categories':categories}