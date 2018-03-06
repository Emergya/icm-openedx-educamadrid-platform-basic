from lms.lib.comment_client import CommentClientRequestError
from django_comment_client.utils import JsonError
from courseware.courses import get_course_with_access
from django.http import Http404
from opaque_keys.edx.keys import CourseKey
import json
import logging

log = logging.getLogger(__name__)


class AjaxExceptionMiddleware(object):
    """
    Middleware that captures CommentClientRequestErrors during ajax requests
    and tranforms them into json responses
    """
    def process_exception(self, request, exception):
        """
        Processes CommentClientRequestErrors in ajax requests. If the request is an ajax request,
        returns a http response that encodes the error as json
        """
        if isinstance(exception, CommentClientRequestError) and request.is_ajax():
            try:
                return JsonError(json.loads(exception.message), exception.status_code)
            except ValueError:
                return JsonError(exception.message, exception.status_code)
        return None


class HaveCourseDiscussionTab(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        request_path = request.path_info
        if '/courses/' in request_path and '/discussion/' in request_path or '/discussion' in request_path:
            if not request.user.is_anonymous():
                course_key = CourseKey.from_string(view_kwargs.get('course_id'))
                course = get_course_with_access(request.user, 'load', course_key, check_if_enrolled=True)
                discussion_in_course = False
                if course.tabs:
                    for tab in course.tabs:
                        if tab.type == 'discussion':
                            if tab.is_hidden:
                                raise Http404
                            discussion_in_course = True
                            break
                if not discussion_in_course:
                    raise Http404
