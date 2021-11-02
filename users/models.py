import string
import random
import uuid
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.core.mail import send_mail

def generate_password():
    """Generate random password."""
    all = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.sample(all, 8))
    return password
class UserManager(BaseUserManager):
    """Creates a custom user"""

    def create_superuser(self, email, first_name, last_name, password):
        """
        Creates and saves a superuser with the given email, first name,
        last name and password.
        """

        if not email:
            raise ValueError('Must include Email')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True 
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Create User"""

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=100, editable=False)
    email = models.CharField(max_length=100, unique=True, null=False)
    isPassChanged = models.BooleanField(default=False, null=False)
    is_active = models.BooleanField(
        _('active'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'
        ),
    )
    """
        - is_superuser field provided by PermissionsMixin
        - groups field provided by PermissionsMixin
        - user_permissions field provided by PermissionsMixin
    """
    date_joined = models.DateTimeField(
        _('date joined'), default=timezone.now
    )
    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name']

    def is_active_user(self):
        """Check if user is active"""
        return self.is_active

    def get_email(self):
        """Return the email of a user"""
        return str(self.email)

    def get_full_name(self):
        """Return the full name of a user"""
        full_name = '%s %s' % (self.first_name, self.last_name)
        return str(full_name.strip())

    def get_email_full_name(self):
        """Return the Email and full name of a user"""
        return "%s %s %s" % (self.email, self.first_name, self.last_name)

    def get_short_name(self):
        """Return the first name of a user"""
        return self.first_name

    def __str__(self):
        """Return user first name."""

        return self.first_name


def create_password(sender, instance, created, **kwargs):
        """Auto generate a password for a user, save it and send it to the email \
            of the user"""
        print(created, "Created")
        if created:
            created_password = generate_password()
            print(created_password, "printed password")
            instance.set_password(created_password)
            instance.save()

post_save.connect(create_password, sender=User)



