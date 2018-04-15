from django.forms import ModelForm
from .models import Egg

class EggForm(ModelForm):
    class Meta:
        model = Egg
        fields = ['egg_code', 'egg_name', 'base_color', 'ornament', 'picture', 'cooked', 'best_before', 'price']
