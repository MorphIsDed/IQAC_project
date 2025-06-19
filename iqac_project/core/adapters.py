# core/adapters.py

from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.core.exceptions        import ValidationError

ALLOWED_DOMAIN = 'christuniversity.in'

class SchoolSocialAccountAdapter(DefaultSocialAccountAdapter):
    def clean_email(self, email):
        """
        Allow any subdomain of christuniversity.in,
        e.g. 'dept.christuniversity.in' or just 'christuniversity.in'.
        """
        domain = email.split('@')[-1].lower()
        if not domain.endswith(ALLOWED_DOMAIN):
            raise ValidationError(
                f"Only @{ALLOWED_DOMAIN} email addresses (and its subdomains) may sign in."
            )
        return email
