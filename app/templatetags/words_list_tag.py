from app.models import Word
from .library import register


@register.simple_tag(name='list')
def get_word_list():
    return Word.objects.all()