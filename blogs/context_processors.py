from .models import Category
from assignments.models import SocialMedia

def get_categories(request):
    categories = Category.objects.all()
    return {'categories': categories}


def get_social_links(request):
    social_links = SocialMedia.objects.all()
    return {'social_links': social_links}