from django.db import models
from django.urls import reverse

class Language(models.Model):
    name = models.CharField(null=False, blank=False, max_length=30)
    compiled = models.BooleanField(default=False, help_text='Compiled or interpreted')
    learned_at = models.DateField(null=True, blank=True, help_text='When you learned the language')
    observations = models.TextField(max_length=500, blank=True)

    PROCEDURAL_PARADIGM = 'procedural'
    DECLARATIVE_PARADIGM = 'declarative'
    FUNCTIONAL_PARADIGM = 'functional'
    OBJECT_ORIENTED_PARADIGM = 'OOP'
    PARADIGM_CHOICES = (
        (PROCEDURAL_PARADIGM, 'Procedural'),
        (DECLARATIVE_PARADIGM, 'Declarative'),
        (FUNCTIONAL_PARADIGM, 'Functional'),
        (OBJECT_ORIENTED_PARADIGM, 'Object Oriented'),
    )
    main_paradigm = models.CharField(
        choices=PARADIGM_CHOICES, 
        default=PROCEDURAL_PARADIGM, 
        blank=False, 
        max_length=20
    )

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('languages:language_detail', kwargs={"pk": self.pk})

