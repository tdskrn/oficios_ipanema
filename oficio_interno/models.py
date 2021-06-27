from django.db import models

# Create your models here.

CAPS = 'CAPS'
CAPS_AD = 'CAPS-AD'
CONTROLE_INTERNO = 'Controle Interno'
CRAS = 'CRAS'
CREAS = 'CREAS'
GABINETE_PREFEITO = 'Gabinete do Prefeito'
LICITACAO_CONTRATOS = 'Licitação e Contratos'
PATRIMONIO = 'Patrimônio'
PROCURADORIA = 'Procuradoria'
PRONTO_ATENDIMENTO = 'Pronto Atendimento'
SECRETARIA_AGRICULTURA = 'Secretaria de Agricultura'
SECRETARIA_APOIO_ADMINISTRATIVO = 'Secretaria de Apoio Administrativo'
SECRETARIA_ASSISTENCIA_SOCIAL = 'Secretaria de Assistência Social'
SECRETARIA_COMERCIO_INDUSTRIA_TURISMO = 'Secretaria de Comércio, Industria e Turismo'
SECRETARIA_CULTURA = 'Secretaria de Cultura'
SECRETARIA_EDUCACAO = 'Secretaria de Educação'
SECRETARIA_ESPORTE_LAZER = 'Secretaria de Esporte e Lazer'
SECRETARIA_FINANCAS = 'Secretaria de Finanças'
SECRETARIA_GOVERNO = 'Secretaria de Governo'
SECRETARIA_HABITACAO_URBANISMO = 'Secretaria de Habitação e Urbanismo'
SECRETARIA_MEIO_AMBIENTE = 'Secretaria de Meio Ambiente'
SECRETARIA_OBRAS = 'Secretaria de Obras'
SECRETARIA_PLANEJAMENTO_ORCAMENTO = 'Secretaria de Planejamento e Orçamento'
SECRETARIA_RECURSOS_HUMANOS = 'Secretaria de Recursos Humanos'
TRIBUTACAO = 'Tributação'
VIGILANCIA_SANITARIA = 'Vigilância Sanitária'

SECRETARIAS = [
    (CAPS, 'CAPS'),
    (CAPS_AD, 'CAPS-AD'),
    (CONTROLE_INTERNO, 'Controle Interno'),
    (CRAS, 'CRAS'),
    (CREAS, 'CREAS'),
    (GABINETE_PREFEITO, 'Gabinete do Prefeito'),
    (LICITACAO_CONTRATOS, 'Licitação e Contratos'),
    (PATRIMONIO, 'Patrimônio'),
    (PROCURADORIA, 'Procuradoria'),
    (PRONTO_ATENDIMENTO, 'Pronto Atendimento'),
    (SECRETARIA_AGRICULTURA, 'Secretaria de Agricultura'),
    (SECRETARIA_APOIO_ADMINISTRATIVO, 'Secretaria de Apoio Administrativo'),
    (SECRETARIA_ASSISTENCIA_SOCIAL, 'Secretaria de Assistência Social'),
    (SECRETARIA_COMERCIO_INDUSTRIA_TURISMO, 'Secretaria de Comércio, Industria e Turismo'),
    (SECRETARIA_CULTURA, 'Secretaria de Cultura'),
    (SECRETARIA_EDUCACAO, 'Secretaria de Educação'),
    (SECRETARIA_ESPORTE_LAZER, 'Secretaria de Esporte e Lazer'),
    (SECRETARIA_FINANCAS, 'Secretaria de Finanças'),
    (SECRETARIA_GOVERNO, 'Secretaria de Governo'),
    (SECRETARIA_HABITACAO_URBANISMO, 'Secretaria de Habitação e Urbanismo'),
    (SECRETARIA_MEIO_AMBIENTE, 'Secretaria de Meio Ambiente'),
    (SECRETARIA_OBRAS, 'Secretaria de Obras'),
    (SECRETARIA_PLANEJAMENTO_ORCAMENTO, 'Secretaria de Planejamento e Orçamento'),
    (SECRETARIA_RECURSOS_HUMANOS, 'Secretaria de Recursos Humanos'),
    (TRIBUTACAO, 'Tributação'),
    (VIGILANCIA_SANITARIA, 'Vigilância Sanitária'),

]


class OficioInterno(models.Model):
    n_oficio = models.BigAutoField(primary_key=True, editable=True, verbose_name='Nº Ofício')
    setor = models.CharField(verbose_name='Setor',
                             max_length=255,
                             choices=SECRETARIAS,
                             editable=True,
                             default=CONTROLE_INTERNO,
                             )
    destinatario = models.CharField(verbose_name='Destinatário', editable=True, max_length=255)
    assunto = models.CharField(verbose_name='Assunto', editable=True, max_length=255)
    data = models.DateField(verbose_name='Data', editable=True, auto_now=False, auto_now_add=False)

    def __str__(self):
        return f'Nº{self.n_oficio} | {self.setor} | {self.destinatario} | {self.assunto} | {self.data}'

    class Meta:
        verbose_name = 'Ofício Interno'
        verbose_name_plural = 'Ofícios Internos'
