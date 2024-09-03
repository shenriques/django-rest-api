from rest_framework import permissions
from .permissions import IsStaffEditorPermission

class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

# ensure only objects associated with current authenticated user are returned
class UserQuerySetMixin():

    user_field = 'user'
    # method to customise queryset (qs) returned by view (overrides method from parent generics.ListCreateAPIView)
    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        # create dictionary to filter the queryset
        lookup_data = {}
            # only objects associated with user
        lookup_data[self.user_field] = user
        # get original qs according to filtering/restrictions applied in base class
        query_set = super().get_queryset(*args, **kwargs)
        # apply the user filter by unpacking dict into keyword args

        if user.is_staff: # if user has staff permissions, they can edit/delete anything
            return query_set
        return query_set.filter(**lookup_data)