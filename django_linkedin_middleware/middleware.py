import logging

from django.conf import settings
from django.shortcuts import redirect
from linkedin import linkedin

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object

logger = logging.getLogger("LinkledinMiddleware")


class LinkedinMiddleware(MiddlewareMixin):

    def __init__(self, get_response=None):
        """
        Init the middleware with the response and the linkedin authentication object
        :param get_response: the middleware response
        """
        super().__init__()
        self.get_response = get_response
        self.authentication = linkedin.LinkedInAuthentication(settings.LINKEDIN_APPLICATION_KEY,
                                                              settings.LINKEDIN_APPLICATION_SECRET,
                                                              settings.LINKEDIN_APPLICATION_RETURN_CALLBACK,
                                                              settings.LINKEDIN_APPLICATION_PROFILE)

    def __call__(self, request):
        """
        Process the middleware request
        :param request: the request
        :return: response: the response
        """
        response = self.get_response(request)
        if request.resolver_match is not None and self.is_authorized_page(request.resolver_match.url_name):
            return self.process_linkedin_authentication(request)
        return response

    def process_linkedin_authentication(self, request):
        """
        Process a LinkedIn Authentication
        :param request: the request
        :return: if we have the authorization_code, we process the response.
        If we don't have this code, we have to parse the URL to retrieve the authorization code
        """
        logger.debug("AUTH CODE :" + str(self.authentication.authorization_code))
        if 'auth_code' not in request.session:
            url_data = request.build_absolute_uri().split('?code=', 1)
            if len(url_data) != 2:
                logger.debug("Not authentified yet, redirect to the authorization URL : " + str(
                    self.authentication.authorization_url))
                return redirect(self.authentication.authorization_url)
            else:
                auth_code = url_data[1].split('&state=')[0]
                self.authentication.authorization_code = auth_code
                request.session['auth_code'] = auth_code
                linked_authentication = self.authentication.get_access_token()
                logger.debug("We have the TOKEN : " + str(linked_authentication.access_token))
                application = linkedin.LinkedInApplication(token=linked_authentication.access_token)
                data = application.get_profile()
                self.get_resume_info(request, data)
                return redirect(request.resolver_match.url_name)  # To change to access other pages
        return self.get_response(request)

    @staticmethod
    def get_resume_info(request, data):
        """
        Get full information from a resume and add theses information to the session cache
        :param data: the authentication code needed to request the linkedinAPI
        :param request: the request
        """
        logger.debug("resume Data : " + str(data))
        request.session['linkedin_firstName'] = data.get('firstName')
        request.session['linkedin_lastName'] = data.get('lastName')
        request.session['linkedin_headline'] = data.get('headline')

    @staticmethod
    def is_authorized_page(url_name):
        """
        Validate if the request page need an authentication

        Check if the page match the correct path to force a ask for a linkedin authentication
        The pattern '*' can be use to force every request to redirect to linkedin for an authentication.
        This behavior can be disable for specific pages by adding the pages to
        the global variable PAGES_WITHOUT_LINKEDIN_AUTH_REQUIRED in the settings config file.
        Return ``True`` for a authorized page, ``False`` otherwise.
        """
        return url_name not in settings.PAGES_WITHOUT_LINKEDIN_AUTH_REQUIRED and (any(
            pattern == '*' for pattern in settings.PAGES_WITH_LINKEDIN_AUTH_REQUIRED) or
            url_name in settings.PAGES_WITH_LINKEDIN_AUTH_REQUIRED)
