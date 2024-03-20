# Generated by Django 5.0.3 on 2024-03-20 18:10

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemSolicitacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('preco_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='SolicitacaoServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pendente', 'Pendente'), ('Em Andamento', 'Em Andamento'), ('Concluído', 'Concluído'), ('Cancelado', 'Cancelado')], default='Pendente', max_length=20)),
                ('data_solicitacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modules.servico')),
            ],
        ),
        migrations.DeleteModel(
            name='Fornecedor',
        ),
        migrations.DeleteModel(
            name='Funcionario',
        ),
        migrations.AddField(
            model_name='itemsolicitacao',
            name='solicitacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modules.solicitacaoservico'),
        ),
    ]
