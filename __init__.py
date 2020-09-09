from extras.plugins import PluginConfig

class DhcpdConfig(PluginConfig):
    name = 'dhcp'
    verbose_name = 'dhcp'
    description = 'An example plugin for development purposes'
    version = '0.0.1'
    author = 'anderson claudio'
    author_email = 'anderson.acrs@gmail.com'
    base_url = 'dhcp'
    required_settings = []
    default_settings = {
        'loud': False
    }

config = DhcpdConfig