from django import forms

class FormUserNeededMixin(object):
    def form_valid(self, form):
        if self.request.user.is_authenticated():
            form.instance.user = self.request.user
            return super(FormUserNeededMixin, self).form_valid(form)
        else:
            form.add_error("text", "User must be logged in to continue")
            return self.form_invalid(form)


class UserOwnerMixin(FormUserNeededMixin, object):
    def form_valid(self, form):
        if form.instance.user.id == self.request.user.id:
            return super(FormUserNeededMixin, self).form_valid(form)
        else:
            form.add_error("text", "Must be this user to change data")
            return self.form_invalid(form)
