from .models import Savat


def baskets(request):
    user = request.user
    return {'baskets': Savat.objects.filter(user=user) if user.is_authenticated else []}