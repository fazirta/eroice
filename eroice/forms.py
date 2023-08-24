from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Story, Comment

# Common base form for user registration
class BaseUserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Form for creating a new user with user registration
class CreateUserForm(BaseUserRegistrationForm):
    pass

# Form for creating a new user during landing page registration
class CreateUserFormLanding(BaseUserRegistrationForm):
    pass

# Form for writing a new story
class WriteForm(ModelForm):
    class Meta:
        model = Story
        exclude = ["user", "likes"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize widget attributes for better user interaction
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})
        # Set minimum length for content field
        self.fields['content'].widget.attrs['minlength'] = '200'

# Form for adding a new comment to a story
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ["user", "story"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize widget attribute for the comment field
        self.fields['comment'].widget.attrs.update({'name': 'comment'})
