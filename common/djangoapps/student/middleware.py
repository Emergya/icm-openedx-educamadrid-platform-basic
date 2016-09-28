"""
Middleware that checks user standing for the purpose of keeping users with
disabled accounts from accessing the site.
"""
from edxmako.shortcuts import marketing_link
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.utils.translation import ugettext as _

from student.models import UserStanding, UserProfile


class UserStandingMiddleware(object):
    """
    Checks a user's standing on request. Returns a 403 if the user's
    status is 'disabled'.
    """
    def process_request(self, request):
        user = request.user
        try:
            user_account = UserStanding.objects.get(user=user.id)
            # because user is a unique field in UserStanding, there will either be
            # one or zero user_accounts associated with a UserStanding
        except UserStanding.DoesNotExist:
            pass
        else:
            if user_account.account_status == UserStanding.ACCOUNT_DISABLED:
                msg = _(
                    'Your account has been disabled. If you believe '
                    'this was done in error, please contact us at '
                    '{support_email}'
                ).format(
                    support_email=u'<a href="mailto:{address}?subject={subject_line}">{address}</a>'.format(
                        address=settings.DEFAULT_FEEDBACK_EMAIL,
                        subject_line=_('Disabled Account'),
                    ),
                )
                return HttpResponseForbidden(msg)


class MandatoryFieldsMiddleware(object):
    """
    Middleware: If a user hasn't got the mandatory fields (in this case: gender), it will be redirected to the user form.
    """

    def process_view(self, request, view_func, view_args, view_kwargs):  # pylint: disable=unused-argument
        user = request.user
        # Only obey to the user if it exists
        try:
            profile = UserProfile.objects.get(user_id=user.id)
            form_to_update_profile = reverse('student.views.register_user')
            not_redirect = (form_to_update_profile, reverse('student.views.logout_user'),
                            reverse('student.views.signin_user'),
                            reverse('student.views.fill_fields_new_ldap_login'),
                            marketing_link('HONOR'),
                            marketing_link('HONOR') + '#honor',
                            marketing_link('TOS'))

            # It's not the form (avoid inifinite redirect) and hasn't got gender or age
            if not any([(request.path == url) for url in not_redirect]) and (profile.educational_centre_code is None or profile.year_of_birth is None /
                                                                             profile.educational_centre_name is None or profile.teaching_profession is None /
                                                                             profile.specialty is None):
                return redirect(form_to_update_profile)
        except UserProfile.DoesNotExist:
            pass

        return None
