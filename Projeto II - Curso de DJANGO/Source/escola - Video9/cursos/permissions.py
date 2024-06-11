
# Definir uma permission para que somente um user possa remover dados de cursos

from rest_framework import permissions

# Se for superuser ele aceita o delete
class EhSuperUsuario(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            if request.user.is_superuser:
                return True
            return False
        return True