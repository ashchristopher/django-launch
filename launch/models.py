from django.db import models

class SignupRequest(models.Model):
    active = models.BooleanField(default=True, help_text='Deactivate requests that should be ignored.')
    email = models.EmailField(unique=True)
    invitation_sent = models.BooleanField(default=False, help_text='Has an invitation been sent to this recipient?')
    signed_up = models.BooleanField(default=False, help_text='Has this user signed up?')
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return "SignupRequest for %s" % self.email
    