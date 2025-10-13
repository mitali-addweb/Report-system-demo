from django.shortcuts import redirect
from functools import wraps

def allowed_roles_or_permissions(roles=[], permissions=[]):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            user = request.user
            if not user.is_authenticated:
                return redirect('login')

            # Check roles
            if roles:
                user_groups = user.groups.values_list('name', flat=True)
                if any(role in user_groups for role in roles):
                    return view_func(request, *args, **kwargs)

            # Check permissions
            if permissions:
                if any(user.has_perm(perm) for perm in permissions):
                    return view_func(request, *args, **kwargs)

            # If neither roles nor permissions match
            return redirect('access_denied')
        
        return wrapper
    return decorator
