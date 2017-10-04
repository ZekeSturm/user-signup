def checker(username,password,confirm,email):
    error = False
    blankerror = "You must fill out this field."
    overundererror = "Your {} must be between 3 and 20 characters long."
    invaliderror = "Your {} must not contain any spaces"
    unameerror = ""
    passerror = ""
    confirmerror = ""
    emailerror = ""

    if len(username) < 3 or len(username) > 20:
        error = True
        unameerror = overundererror.format("username")
    if not len(username):
        error = True
        unameerror = blankerror
    if unameerror == "":
        for i in range(len(username)):
            if username[i] == " ":
                error = True
                unameerror = invaliderror.format("username")
                break
    if not len(password):
        error = True
        passerror = blankerror
    if len(password) < 3 or len(password) > 20:
        error = True
        passerror = overundererror.format("password")
    if passerror == "":
        for i in range(len(password)):
            if password[i] == " ":
                error = True
                unameerror = invaliderror.format("password")
                break
    if not len(confirm):
        error = True
        confirmerror = blankerror
    if password != confirm:
        error = True
        confirmerror = "Both password fields must match."
    if email and (len(email) < 3 or len(email) > 20):
        error = True
        emailerror = overundererror.format("email")
    if emailerror == "":
        foundat = False
        founddot = False
        for i in range(len(email)):
            if email[i] == " ":
                error = True
                emailerror = "Your email must not contain any spaces, and must be a valid address (containing both @ and .)"
                break
            if email[i] == "@":
                foundat = True
            if foundat and email[i] == ".":
                founddot = True
        else:
            if not foundat or not founddot:
                error = True
                emailerror = "Your email address must be valid (containing both an @ symbol and a .)"

    return {'error':error, 'unameerror':unameerror, 'passerror':passerror, 'confirmerror':confirmerror, 'emailerror':emailerror}