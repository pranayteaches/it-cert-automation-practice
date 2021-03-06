import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")

    # If the first is alphabet
    if username[0].isalpha():

        # Usernames can't be shorter than minlen
        if len(username) < minlen: return False
            
        # Usernames can only use letters, numbers, dots and underscores
        if not re.match('^[a-z0-9._]*$', username): return False
        
        # else return true
        return True

    # if the first letter is not an alphabet
    else:
        return False

    
