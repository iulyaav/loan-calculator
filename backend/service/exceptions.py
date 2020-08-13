from rest_framework.exceptions import APIException


class ValidationError(APIException):
    status_code = 400
    default_detail = "One or several parameters are either missing or ill configured."
    default_code = "bad_request"
