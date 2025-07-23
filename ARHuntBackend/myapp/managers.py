from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('An email must be provided.'))
        if not extra_fields.get('username'):
            raise ValueError(_('A username must be provided.'))
        if not extra_fields.get('grade'):
            raise ValueError(_('A grade level must be provided.'))
        if not extra_fields.get('grade'):
            raise ValueError(_('A grade level must be provided.'))
        if not (9 <= extra_fields.get('grade') <= 12):
            raise ValueError(_('Grade must be between 9 and 12.'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, password, **extra_fields):
        if not extra_fields.get('username'):
            raise ValueError(_('A username must be provided.'))
        extra_fields.setdefault('grade', 13)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, password, **extra_fields)