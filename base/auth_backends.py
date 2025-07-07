from mozilla_django_oidc.auth import OIDCAuthenticationBackend
from .models import Role

class MyOIDCAuthBackend(OIDCAuthenticationBackend):
    def create_user(self, claims):
        user = super().create_user(claims)
        self._set_roles(user, claims)
        return user

    def update_user(self, user, claims):
        user = super().update_user(user, claims)
        self._set_roles(user, claims)
        return user

    def _set_roles(self, user, claims):
        roles = claims.get('roles', [])
        # Clear old roles
        Role.objects.filter(user=user).delete()
        # Add new roles
        for role_name in roles:
            Role.objects.create(user=user, role=role_name)
