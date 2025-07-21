# Permissions and Groups Setup

- Custom permissions defined in Book model: can_view, can_create, can_edit, can_delete.
- Groups created: Editors, Viewers, Admins.
- Permissions assigned accordingly.
- Views are protected with @permission_required decorator using these permissions.
- Users must belong to groups with appropriate permissions to access views.
