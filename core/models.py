from django.db import models
import uuid
from stdimage.models import StdImageField

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    
    return filename

class BaseModel(models.Model):
    criacao = models.DateField('Criação', auto_now_add=True)
    edicao = models.DateField('Edição', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta():
        abstract = True

class Cargo(BaseModel):
    cargo = models.CharField('Cargo', max_length=50)

    class Meta():
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
    
    def __str__(self):
        return self.cargo


class Membro(BaseModel):
    nome = models.CharField('Nome', max_length=50)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    foto = StdImageField('Foto',upload_to= get_file_path, variations= {'thumb':{'width': 400, 'height': 400, 'crop':True}} )
    bio = models.TextField('bio', max_length=200)
    facebook = models.CharField('Facebook', max_length=200, default='#')
    github = models.CharField("Github", max_length=200, default='#')
    linkedn = models.CharField('Linkedn', max_length=200, default='#')

    class Meta:
        verbose_name = 'Membro'
        verbose_name_plural = 'Membros'
    
    def __str__(self):
        return self.nome
    

class Registro(BaseModel):
    titulo = models.CharField('Título', max_length=50)
    etapa = models.CharField('Etapa', max_length=50)
    objetivo = models.CharField('Objetivo', max_length=50)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations= {'thumb':{'width':640, 'height':400, 'crop':True}} )
    descricao = models.TextField('descricao', max_length=150, null=True)

    class Meta:
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'
    
    def __str__(self):
        return self.titulo
