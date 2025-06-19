from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from .forms import ResumeForm

def resume_form(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            # Process form data
            data = form.cleaned_data
            data['skills_list'] = data['skills'].split(',')  # Split skills into a list
            
            # Render PDF
            html = render_to_string('builder/pdf_template.html', data)
            response = HttpResponse(content_type='application/pdf')
            pisa_status = pisa.CreatePDF(html, dest=response)
            if pisa_status.err:
                return HttpResponse('We had some errors <pre>' + html + '</pre>')
            return response
    else:
        form = ResumeForm()
    
    return render(request, 'builder/resume_form.html', {'form': form})




