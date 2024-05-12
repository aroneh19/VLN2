from user.models import Profile
from company.models import Company

def user_type(request):
    if request.user.is_authenticated:
        is_company = Company.objects.filter(user=request.user).exists()
        if is_company:
            photo = Company.objects.get(user=request.user).logo
        else:
            photo = Profile.objects.get(user=request.user).picture
        return {
            'is_company': is_company,
            'photo': photo,
        }
    return {}