from django.views import View


class BaseView(View):
  def current_user(self):
    return self.request.user
  
  def is_anonymous_user(self):
    return self.request.user.is_anonymous

  def is_authenticated_user(self):
    return self.request.user.is_authenticated
