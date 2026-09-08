from django.core.management.base import BaseCommand
from laudos.models import (
    Paciente,
    Medico,
    StatusMedicao,
    Exame,
    Medicao,
    TemplateLaudo,
    Laudo,
)
from datetime import date, datetime


class Command(BaseCommand):
    help = "Popula o banco com dados de teste para desenvolvimento"

    def handle(self, *args, **kwargs):
        # Status de medição
        status_valida, _ = StatusMedicao.objects.get_or_create(descricao="válida")
        status_invalida, _ = StatusMedicao.objects.get_or_create(descricao="inválida")
        StatusMedicao.objects.get_or_create(descricao="pendente")

        # Paciente
        paciente, _ = Paciente.objects.get_or_create(
            cpf="12345678900",
            defaults={
                "nome": "Maria Silva",
                "idade": 34,
                "sexo": "feminino",
            },
        )

        # Médico
        medico, _ = Medico.objects.get_or_create(
            crm="CRM12345",
            defaults={"nome": "Dr. João Souza"},
        )

        # Template de laudo padrão
        template, _ = TemplateLaudo.objects.get_or_create(
            nome="Template Padrão",
            defaults={
                "conteudo": "Laudo de MRPA - {paciente} - {data_exame}",
                "padrao": True,
            },
        )

        # Exame (repare: campos chamam-se paciente_id e medico_id no seu model)
        exame, _ = Exame.objects.get_or_create(
            paciente_id=paciente,
            medico_id=medico,
            data_exame=date.today(),
            defaults={"observacoes": "Exame de teste gerado pela seed"},
        )

        # Medições
        Medicao.objects.get_or_create(
            exame=exame,
            pressao_sistolica=128,
            pressao_diastolica=81,
            defaults={
                "frequencia_cardiaca": 67,
                "classificacao_pa": "normal",
                "status_medicao": status_valida,
            },
        )
        Medicao.objects.get_or_create(
            exame=exame,
            pressao_sistolica=190,
            pressao_diastolica=110,
            defaults={
                "frequencia_cardiaca": 95,
                "classificacao_pa": "hipertensão estágio 2",
                "status_medicao": status_invalida,
            },
        )

        # Laudo
        Laudo.objects.get_or_create(
            exame=exame,
            template_laudo=template,
            defaults={"data_geracao": datetime.now()},
        )

        self.stdout.write(self.style.SUCCESS("Seed executada com sucesso."))
