from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import ContactMessage


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            # For AJAX requests
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'message': 'Your message has been sent successfully!'
                })

            # For regular form submission
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact:contact')

        # Handle form errors for AJAX
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': False,
                'errors': form.errors.get_json_data()
            }, status=400)

    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})