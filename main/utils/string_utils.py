def build_api_log_message(method, endpoint_url, payload=None, response=None):
    """ Build the LOG message for the API calls to the service.
    :param method:        str  Request method name such as GET, POST, PUT, DELETE, PATCH
    :param endpoint_url:  str  Full endpoint URL of service to which the request will be sent.
    :param payload:       str  Data or payload send along with the REST request.
    :param response:      str  Response that comes from the API service.
    :return: Formatted string message that can be used as log message.
    """
    message_type = "[Request]" if response is None else f"[Rsp:{response.status_code}]"
    if response is not None:
        message = {"content": response.json() if response.ok else response.text}
    else:
        message = {"url": f'{endpoint_url}'}
        if payload:
            message["payload"] = payload

    return f"{method:<6} {message_type}\t{message}"
