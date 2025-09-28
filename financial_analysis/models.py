from django.db import models
from django.contrib.auth.models import User


class FinancialDocument(models.Model):
    DOCUMENT_TYPES = [
        ('balance', 'Бухгалтерский баланс'),
        ('profit_loss', 'Отчет о прибылях и убытках'),
        ('cash_flow', 'Отчет о движении денежных средств'),  # ДОБАВЛЯЕМ
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPES)
    pdf_file = models.FileField(upload_to='financial_docs/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # def get_ratios(self):
    #     return self.financialratio_set.all()


class FinancialRatio(models.Model):
    document = models.ForeignKey(FinancialDocument, on_delete=models.CASCADE)
    ratio_name = models.CharField(max_length=100)
    ratio_value = models.FloatField()
    calculation_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # значение будет float
        if hasattr(self.ratio_value, 'as_integer_ratio'):
            self.ratio_value = float(self.ratio_value)
        elif isinstance(self.ratio_value, str):
            try:
                self.ratio_value = float(self.ratio_value)
            except (ValueError, TypeError):
                self.ratio_value = 0.0
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.ratio_name}: {self.ratio_value}"


