def validate_ip(s):
    if '.' in s:
        parts = s.split('.')
        if len(parts) != 4:
            return "Neither"
        for part in parts:
            if ' ' in part or not part.isdigit() or int(part) < 0 or int(part)>255:
                return "Neither"
        return "IPv4"
    elif ':' in s:
        parts = s.split(':')
        if len(parts) != 8: 
            return "Neither"
        for part in parts:
            try:
                if ' ' in part or int(part, 16) > int('ffff', 16):
                    return "Neither"
            except:
                return "Neither"
        return "IPv6"
    else:
        return "Neither"








t = int(raw_input())
for i in range(t):
    print validate_ip(raw_input())



