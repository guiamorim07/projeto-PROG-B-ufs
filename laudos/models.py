from django.db import models

# TABELAS SQL TRANSFORMADAS EM CLASSES PYTHON (DJANGO MODELS)
class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=10)
    cpf = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.nome

class Medico(models.Model):
    nome = models.CharField(max_length=100)
    crm = models.CharField(max_length=20, unique=True)
    

    def __str__(self):
        return self.nome

class StatusMedicao(models.Model):
    descricao = models.CharField(max_length=30)

    def __str__(self):
        return self.descricao


class Exame(models.Model):
    paciente_id = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico_id = models.ForeignKey(Medico, on_delete=models.CASCADE)
    data_exame = models.DateField()
    observacoes = models.TextField()

    def __str__(self):
        return self.paciente_id.nome



class Medicao(models.Model):
    exame = models.ForeignKey(Exame, on_delete=models.CASCADE, related_name="medicoes")
    pressao_sistolica = models.IntegerField()
    pressao_diastolica = models.IntegerField()
    frequencia_cardiaca = models.IntegerField(blank=True, null=True)
    classificacao_pa = models.CharField(max_length=50, blank=True, null=True)
    status_medicao = models.ForeignKey(StatusMedicao, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.pressao_sistolica}x{self.pressao_diastolica}"


class TemplateLaudo(models.Model):
    nome = models.CharField(max_length=100)
    conteudo = models.TextField()
    padrao = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


class Laudo(models.Model):
    exame = models.ForeignKey(Exame, on_delete=models.PROTECT)
    template_laudo = models.ForeignKey(TemplateLaudo, on_delete=models.PROTECT)
    data_geracao = models.DateTimeField()
    caminho_pdf = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
       return f"Laudo do exame {self.exame_id}"