from django.shortcuts import render
from .models import FAQForm, TestFAQ
from django.core.mail import EmailMessage
from .utils import render_to_pdf
from django.contrib import messages
from django.utils import timezone

def home_test(request):
    if request.method == "POST":
        form = FAQForm(request.POST)
        if form.is_valid():
            test_obj = form.save()
            
            pdf_content = render_to_pdf('faqTest/reportPdf.html', {'test': test_obj})
            
            data_locale = timezone.localtime(test_obj.data_creazione)
            data_formattata = data_locale.strftime("%d/%m/%Y alle %H:%M")
            
            if pdf_content:
                email = EmailMessage(
                    subject=f"Report DeepTrace FAQ - {test_obj.paziente_email}",
                    body=f"In allegato il report del test FAQ effettuato il {data_formattata}.",
                    from_email='noreply@deeptrace.it',
                    to=[test_obj.paziente_email],
                )
                email.attach(f'Report_FAQ_{test_obj.id}.pdf', pdf_content, 'application/pdf')
                try:
                    email.send()
                    messages.success(request, f"Il report è stato spedito a {test_obj.paziente_email}.")
                except Exception as e:
                    messages.error(request, f"Errore invio email a {test_obj.paziente_email}.")

            return render(request, 'faqTest/success.html', {'test': test_obj})
        else:
            messages.error(request, "C'è un errore nel modulo. Controlla i campi inseriti.")
    else:
        form = FAQForm()
    return render(request, 'faqTest/faqTest.html', {'form': form})

def storico(request):
    test_salvati = TestFAQ.objects.all().order_by('-data_creazione')
    return render(request, 'faqTest/storico.html', {'test_list': test_salvati})