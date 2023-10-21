from rest_framework import status
from rest_framework.response import Response


class RestResponse(Response):
    def __init__(self, data=None, message=None, status=True):
        data_content = {
            'status': status,
            'message': message,
            'data': data,
        }
        super().__init__(
            data=data_content,
            content_type='application/json',
            status=self.status_code
        )


class ErrorStatus(RestResponse):
    def __init__(self, data=None, message=None, status=False):
        super().__init__(data=data, status=status, message=message)


class SuccessResponse(RestResponse):
    status_code = status.HTTP_200_OK


class CreateResponse(RestResponse):
    status_code = status.HTTP_201_CREATED


class NoContentResponse(ErrorStatus):
    status_code = status.HTTP_204_NO_CONTENT
