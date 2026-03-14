from django.db import models
from django import forms
from django.db import models

class TestFAQ(models.Model):
    FONTE_CHOICES = [
        ('caregiver', 'Caregiver'),
        ('paziente', 'Paziente'),
        ('altro', 'Altro'),
    ]

    paziente_email = models.EmailField(verbose_name="Email del Paziente")
    identificazione_compilatore = models.CharField(
        max_length=20, 
        choices=FONTE_CHOICES, 
        default='caregiver',
        verbose_name="Fonte delle informazioni"
    )
    data_creazione = models.DateTimeField(auto_now_add=True)

    domanda_1 = models.IntegerField(default=0) # Assegni, bollette, contabilità
    domanda_2 = models.IntegerField(default=0) # Moduli e bollettini
    domanda_3 = models.IntegerField(default=0) # Acquisti vestiti/alimentari
    domanda_4 = models.IntegerField(default=0) # Giochi abilità/hobbies
    domanda_5 = models.IntegerField(default=0) # Bollire acqua/caffè
    domanda_6 = models.IntegerField(default=0) # Pasto completo
    domanda_7 = models.IntegerField(default=0) # Eventi correnti
    domanda_8 = models.IntegerField(default=0) # TV, libri, articoli
    domanda_9 = models.IntegerField(default=0) # Appuntamenti, farmaci
    domanda_10 = models.IntegerField(default=0) # Spostarsi/viaggiare

    punteggio_totale = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        """
        Calcola automaticamente la somma dei punteggi prima di salvare su AWS.
        """
        risposte = [
            self.domanda_1, self.domanda_2, self.domanda_3, self.domanda_4, self.domanda_5,
            self.domanda_6, self.domanda_7, self.domanda_8, self.domanda_9, self.domanda_10
        ]
        self.punteggio_totale = sum(risposte)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Test {self.paziente_email} - Score: {self.punteggio_totale}"

class FAQForm(forms.ModelForm):
    SCELTE = [
        (0, "Normale (0)"),
        (1, "Non svolta abitualmente, ma in grado di eseguirla (1)"),
        (2, "Non svolta abitualmente, richiederebbe assistenza (2)"),
        (3, "Svolta autonomamente ma con difficoltà (3)"),
        (4, "Svolta solo con assistenza (4)"),
        (5, "Dipendenza completa (5)"),
    ]

    domanda_1 = forms.ChoiceField(choices=SCELTE, widget=forms.RadioSelect, label="Compilare assegni, pagare bollette, conti e fatture, tenere la contabilità")
    domanda_2 = forms.ChoiceField(choices=SCELTE, widget=forms.RadioSelect, label="Compilare moduli e bollettini")
    domanda_3 = forms.ChoiceField(choices=SCELTE, widget=forms.RadioSelect, label="Acquistare vestiti, prodotti per la casa, alimentari")
    domanda_4 = forms.ChoiceField(choices=SCELTE, widget=forms.RadioSelect, label="Eseguire o partecipare ad un gioco di abilità, svolgere attività ricreative, hobbies")
    domanda_5 = forms.ChoiceField(choices=SCELTE, widget=forms.RadioSelect, label="Far bollire l'acqua, preparare il caffè, spegnere la caldaia")
    domanda_6 = forms.ChoiceField(choices=SCELTE, widget=forms.RadioSelect, label="Preparare un pasto completo ed equilibrato")
    domanda_7 = forms.ChoiceField(choices=SCELTE, widget=forms.RadioSelect, label="Rimanere informato degli eventi correnti")
    domanda_8 = forms.ChoiceField(choices=SCELTE, widget=forms.RadioSelect, label="Prestare attenzione, comprendere e discutere di programmi televisivi, libri, articoli")
    domanda_9 = forms.ChoiceField(choices=SCELTE, widget=forms.RadioSelect, label="Ricordare appuntamenti, ricorrenze familiari, festività imminenti, farmaci da prendere")
    domanda_10 = forms.ChoiceField(choices=SCELTE, widget=forms.RadioSelect, label="Spostarsi e viaggiare all'esterno del quartiere, guidare, prendere un mezzo pubblico")

    FONTE_CHOICES = [('caregiver', 'Caregiver'), ('paziente', 'Paziente'), ('altro', 'Altro')]
    identificazione_compilatore = forms.ChoiceField(choices=FONTE_CHOICES, widget=forms.Select, label="Fonte delle informazioni")

    class Meta:
        model = TestFAQ
        fields = ['paziente_email', 'identificazione_compilatore'] + [f'domanda_{i}' for i in range(1, 11)]