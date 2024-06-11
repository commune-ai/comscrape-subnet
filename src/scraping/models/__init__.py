from .google import Google
from .bing import Bing
from .duckduckgo import Duckduckgo

services = {
    'google': Google,
    'bing': Bing,
    'duckduckgo': Duckduckgo,
}

def get_service_class(service_name):
    return services.get(service_name)