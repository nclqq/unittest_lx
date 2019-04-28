def check_password(password):
    """
        1. 必须包含大写字母、小写字母、数字
        2. 长度必须在 6 位或以上
    """
    if len(password) < 6:
        return False

    upper, lower, digital = False, False, False

    for c in password:
        if '0' <= c and c <= '9':
            digital = True
        elif c >= 'a' and c <= 'z':
            lower = True
        elif c >= 'A' and c <= 'Z':
            upper = True

    return upper and lower and digital #如果都为true，则正确
