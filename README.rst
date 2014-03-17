=====================
 Django Auth Actions
=====================

Django Auth Actions provides support for checking whether a user is
authorized to take a particular action. For example, users may simply
need to be logged in to add an item to the cart, but must have
presented credentials within the last five minutes to checkout.

Django Auth Action works with Django's auth system, and requires the
Django session framework.

This implementation is a prototype, and is currently under development.

Configuration
=============

#. Add ``authactions`` to the list of ``INSTALLED_APPS``::

   INSTALLED_APPS = (
       'django.contrib.auth',
       'django.contrib.sessions',
       'authaction',
   )

#. Add the middleware to the list of ``MIDDLEWARE_CLASSES``::

   MIDDLEWARE_CLASSES = (
       'django.middleware.common.CommonMiddleware',
       'django.contrib.sessions.middleware.SessionMiddleware',
       'django.middleware.csrf.CsrfViewMiddleware',
       'django.contrib.auth.middleware.AuthenticationMiddleware',
       'authaction.middleware.AuthActionMiddleware',
   )

#. Map actions to conditions in the ``AUTH_ACTION_CONDITIONS``
   setting::

   AUTH_ACTION_CONDITIONS = {
       'add_to_cart': authaction.conditions.logged_in,
       'checkout': authaction.conditions.logged_in_within(
           datetime.timedelta(minutes=5)),
   }

Checking Authorization
======================

You can check authorization with a view decorator, or using a context
manager.

For example, to use a decorator::

  from authaction.guard import auth_action_required

  @auth_action_required('add_to_cart')
  def add_to_cart(request):

      #  ...

If the condition is not met, a redirect will be returned.
