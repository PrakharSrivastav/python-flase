from flask import request

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def createUser(token):
    """
    Validate and decode token.
    Returned value will be passed in 'token_info' parameter of your operation function, if there is one.
    'sub' or 'uid' will be set in 'user' parameter of your operation function, if there is one.
    'scope' or 'scopes' will be passed to scope validation function.

    :param token Token provided by Authorization header
    :type token: str
    :return: Decoded token information or None if token is invalid
    :rtype: dict | None
    """
    # get the token
    # validate the token using firebase sdk
    # error : return httpstatus 400
    # ok :
        # validate the request
        # userdb.saveuser(request) : try -catch
        # if err return http 500
    # success : http 200 {body}




    return {'scopes': ['read:pets', 'write:pets'], 'uid': 'user_id'}