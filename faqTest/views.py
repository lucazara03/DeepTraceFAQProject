from django.shortcuts import render

from django.shortcuts import render
from .models import FAQForm

def home_test(request):
    punteggio_ottenuto = None
    
    if request.method == "POST":
        form = FAQForm(request.POST)
        if form.is_valid():
            istanza_test = form.save()
            
            return render(request, 'faqTest/faqTest.html', {
                'punteggio': istanza_test.punteggio_totale,
                'email': istanza_test.paziente_email
            })
    else:
        form = FAQForm()
    
    return render(request, 'faqTest/faqTest.html', {'form': form})