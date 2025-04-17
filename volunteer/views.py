from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import VolunteerForm


def volunteer_view(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            volunteer = form.save()

            # For AJAX requests
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'message': 'Thank you for volunteering! We will contact you soon.',
                    'name': volunteer.name  # Optional: include submitted name in response
                })

            # For regular form submission
            messages.success(request, 'Thank you for volunteering!')
            return redirect('volunteer:volunteer')

        # Handle form errors for AJAX
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': False,
                'errors': form.errors.get_json_data()
            }, status=400)

    else:
        form = VolunteerForm()

    return render(request, 'volunteer/volunteer.html', {'form': form})