import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'APP1.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

for user in User.objects.all():
    user.set_password(user.password)
    user.save()