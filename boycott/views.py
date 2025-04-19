from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import BoycottCategory, BoycottTarget, UserReport
from .forms import ReportForm


class BoycottListView(ListView):
    model = BoycottTarget
    template_name = 'boycott/list.html'
    context_object_name = 'targets'

    def get_queryset(self):
        queryset = super().get_queryset().filter(verified=True)
        category_pk = self.kwargs.get('pk')
        if category_pk:
            queryset = queryset.filter(category__pk=category_pk)
        return queryset.prefetch_related('alternatives')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = BoycottCategory.objects.all()
        return context


class BoycottDetailView(DetailView):
    model = BoycottTarget
    template_name = 'boycott/detail.html'
    context_object_name = 'target'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        target = self.object
        context.update({
            'reports': target.userreport_set.filter(approved=True)[:5]
        })
        return context


# views.py
def submit_report(request, pk):
    target = get_object_or_404(BoycottTarget, pk=pk)

    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.target = target

            # Handle the additional notes field
            notes = request.POST.get('notes', '')
            if notes:
                report.description = notes  # Assuming you want to store notes in description

            if request.user.is_authenticated:
                report.submitted_by = request.user

            report.save()
            return render(request, 'boycott/report_success.html', {'target': target})
    else:
        form = ReportForm()

    return render(request, 'boycott/report_form.html', {
        'form': form,
        'target': target,
        'checklist_items': [
            "I confirm this evidence directly relates to the company",
            "The source is independent and verifiable",
            "I understand false reports may result in account suspension"
        ]
    })