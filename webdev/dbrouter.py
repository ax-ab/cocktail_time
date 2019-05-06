#https://strongarm.io/blog/multiple-databases-in-django/

class CustomDatabaseRouter:
    """
    Determine how to route database calls for an app's models (in this case, for an app named Example).
    All other models will be routed to the next router in the DATABASE_ROUTERS setting if applicable,
    or otherwise to the default database.
    """

    def db_for_read(self, model, **hints):
        """Send all read operations on Example app models to `example_db`."""
        if model._meta.app_label == 'users':
            return 'users'

        if model._meta.app_label == 'display':
            return 'display'

        return None

    def db_for_write(self, model, **hints):
        """Send all write operations on Example app models to `example_db`."""
        if model._meta.app_label == 'users':
            return 'users'

        if model._meta.app_label == 'display':
            return 'display'

        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Determine if relationship is allowed between two objects."""

        # Allow any relation between two models that are both in the Example app.
        if obj1._meta.app_label == 'users' and obj2._meta.app_label == 'users':
            return True
        # No opinion if neither object is in the Example app (defer to default or other routers).
        elif 'users' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return None

        if obj1._meta.app_label == 'display' and obj2._meta.app_label == 'display':
            return True
        # No opinion if neither object is in the Example app (defer to default or other routers).
        elif 'display' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return None

        # Block relationship if one object is in the Example app and the other isn't.
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure that the Example app's models get created on the right database."""
        if app_label == 'users':
            # The Example app should be migrated only on the example_db database.
            return db == 'users'
        elif db == 'users':
            # Ensure that all other apps don't get migrated on the example_db database.
            return False
        
        if app_label == 'display':
            # The Example app should be migrated only on the example_db database.
            return db == 'display'
        elif db == 'display':
            # Ensure that all other apps don't get migrated on the example_db database.
            return False

        # No opinion for all other scenarios
        return None

#https://docs.djangoproject.com/en/2.1/topics/db/multi-db/
#Disabled documentation router

# class AuthRouter:
#     """
#     A router to control all database operations on models in the
#     auth application.
#     """
#     def db_for_read(self, model, **hints):
#         """
#         Attempts to read auth models go to auth_db.
#         """
#         if model._meta.app_label == 'auth':
#             return 'auth_db'
#         return None

#     def db_for_write(self, model, **hints):
#         """
#         Attempts to write auth models go to auth_db.
#         """
#         if model._meta.app_label == 'auth':
#             return 'auth_db'
#         return None

#     def allow_relation(self, obj1, obj2, **hints):
#         """
#         Allow relations if a model in the auth app is involved.
#         """
#         if obj1._meta.app_label == 'auth' or \
#            obj2._meta.app_label == 'auth':
#            return True
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         """
#         Make sure the auth app only appears in the 'auth_db'
#         database.
#         """
#         if app_label == 'auth':
#             return db == 'auth_db'
#         return None

# import random

# class PrimaryReplicaRouter:
#     def db_for_read(self, model, **hints):
#         """
#         Reads go to a randomly-chosen replica.
#         """
#         return random.choice(['replica1', 'replica2'])

#     def db_for_write(self, model, **hints):
#         """
#         Writes always go to primary.
#         """
#         return 'primary'

#     def allow_relation(self, obj1, obj2, **hints):
#         """
#         Relations between objects are allowed if both objects are
#         in the primary/replica pool.
#         """
#         db_list = ('primary', 'replica1', 'replica2')
#         if obj1._state.db in db_list and obj2._state.db in db_list:
#             return True
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         """
#         All non-auth models end up in this pool.
#         """
#         return True