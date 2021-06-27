# Generated by Django 3.2.4 on 2021-06-27 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OficioInterno',
            fields=[
                ('n_oficio', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Nº Ofício')),
                ('setor', models.CharField(choices=[('CAPS', 'CAPS'), ('CAPS-AD', 'CAPS-AD'), ('Controle Interno', 'Controle Interno'), ('CRAS', 'CRAS'), ('CREAS', 'CREAS'), ('Gabinete do Prefeito', 'Gabinete do Prefeito'), ('Licitação e Contratos', 'Licitação e Contratos'), ('Patrimônio', 'Patrimônio'), ('Procuradoria', 'Procuradoria'), ('Pronto Atendimento', 'Pronto Atendimento'), ('Secretaria de Agricultura', 'Secretaria de Agricultura'), ('Secretaria de Apoio Administrativo', 'Secretaria de Apoio Administrativo'), ('Secretaria de Assistência Social', 'Secretaria de Assistência Social'), ('Secretaria de Comércio, Industria e Turismo', 'Secretaria de Comércio, Industria e Turismo'), ('Secretaria de Cultura', 'Secretaria de Cultura'), ('Secretaria de Educação', 'Secretaria de Educação'), ('Secretaria de Esporte e Lazer', 'Secretaria de Esporte e Lazer'), ('Secretaria de Finanças', 'Secretaria de Finanças'), ('Secretaria de Governo', 'Secretaria de Governo'), ('Secretaria de Habitação e Urbanismo', 'Secretaria de Habitação e Urbanismo'), ('Secretaria de Meio Ambiente', 'Secretaria de Meio Ambiente'), ('Secretaria de Obras', 'Secretaria de Obras'), ('Secretaria de Planejamento e Orçamento', 'Secretaria de Planejamento e Orçamento'), ('Secretaria de Recursos Humanos', 'Secretaria de Recursos Humanos'), ('Tributação', 'Tributação'), ('Vigilância Sanitária', 'Vigilância Sanitária')], default='Controle Interno', max_length=255, verbose_name='Setor')),
                ('destinatario', models.CharField(max_length=255, verbose_name='Destinatário')),
                ('assunto', models.CharField(max_length=255, verbose_name='Assunto')),
                ('data', models.DateField(verbose_name='Data')),
            ],
            options={
                'verbose_name': 'Ofício Interno',
                'verbose_name_plural': 'Ofícios Internos',
            },
        ),
    ]
