from django.shortcuts import render
from .models import Cause
from django.shortcuts import get_object_or_404

def cause_list(request):
    causes = Cause.objects.filter(is_featured=True)
    return render(request, 'causes/causes.html', {'causes': causes})

def cause_detail(request, slug):
    cause = get_object_or_404(Cause, slug=slug)
    return render(request, 'causes/cause_details.html', {'cause': cause})


