import random
# pc端的user-agent
user_agent_pc = [
    'Mozilla/5.0 (compatible; MSIE 5.0; Windows NT 5.01; Trident/5.1)',
    'Mozilla/5.0 (iPod; U; CPU iPhone OS 4_0 like Mac OS X; gez-ET) AppleWebKit/532.49.5 (KHTML, like Gecko) Version/4.0.5 Mobile/8B113 Safari/6532.49.5',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/534.0 (KHTML, like Gecko) Chrome/39.0.884.0 Safari/534.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_6 rv:2.0; sa-IN) AppleWebKit/534.37.2 (KHTML, like Gecko) Version/5.0.1 Safari/534.37.2',
    'Mozilla/5.0 (Windows NT 5.01) AppleWebKit/534.0 (KHTML, like Gecko) Chrome/31.0.883.0 Safari/534.0',
    'Mozilla/5.0 (Windows; U; Windows 98) AppleWebKit/535.31.4 (KHTML, like Gecko) Version/4.0.1 Safari/535.31.4',
    'Mozilla/5.0 (Windows; U; Windows 98) AppleWebKit/531.4.6 (KHTML, like Gecko) Version/4.1 Safari/531.4.6',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.1 (KHTML, like Gecko) Chrome/27.0.891.0 Safari/536.1'

]


def get_user_agent_pc():
    return random.choice(user_agent_pc)

def get_user_agent_phone():
    return random.choice(user_agent_phone)