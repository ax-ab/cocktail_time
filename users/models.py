
#https://testdriven.io/blog/django-custom-user-model/
#https://medium.com/agatha-codes/options-objects-customizing-the-django-user-model-6d42b3e971a4
#https://docs.djangoproject.com/en/2.2/topics/auth/customizing/
#https://wsvincent.com/django-custom-user-model-tutorial/
#TODO: Verify the following: https://www.codingforentrepreneurs.com/blog/how-to-create-a-custom-django-user-model/

from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
from django.utils import timezone
from core.models import Cocktail

# A CustomUserManager is needed to bypass the required input for a username when creating a super user (see seond def in class)
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password):
        user = self.model(email=email, password=password)
        user.set_password(password)
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.model(email=email, password=password)
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    # Medium article insert. Removed print email below as there as no reason to print it in the console when entered
    def get_by_natural_key(self, email_):
        #print(email_)
        return self.get(email=email_)

# PermissionsMixin import to secure the permission settings in the standard groups (see admin interface)
# Testdriven.io adds the date_joined (remember to import timezone). I suspect that this also allows for the last login column that is added automatically
# Required fields is only the username field and the password where neither needs to be mentioned explictely
class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(blank=True, null=True, max_length=30)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    fav_cocktails = models.ManyToManyField(Cocktail)
    #TODO: Optional: Provide any custom fields here

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
   
    objects = CustomUserManager()

    def get_short_name(self):
        return self.email

    # Medium article insert.
    def natural_key(self):
        return self.email

    def __str__(self):
        return self.email