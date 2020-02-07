from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
# MyAccountManager says what happens when a user and a super user is created
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must haven email address")
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            email=self.normalize_email(email),
            # normalize just makes the email character to lower case
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class UserAccount(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    # these next fields are required
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date_joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last_login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    
    # this is what the user will use to log in
    USERNAME_FIELD = "email"
    # fields that are required when registering
    REQUIRED_FIELDS = ["username",]

    objects = MyAccountManager()

    # what you would like to return
    def __str__(self):
        return self.email + ", " + self.username
    
    # these functions are required to build custom user
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

# Notes class contains:
class Notes(models.Model):
    # foreign key to the User
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    # link to the note == slug
    slug = models.SlugField(blank=True, unique=True)
    # note title
    title = models.CharField(max_length=200, blank=True)
    # category eg favorites
    category = models.CharField(max_length=200, blank=True)
    # note body
    body = models.TextField(blank=True)
    
    def __str__(self):
        return self.title