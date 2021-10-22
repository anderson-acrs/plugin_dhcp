from extras.plugins import PluginConfig

class DhcpConfig(PluginConfig):
    name = 'dhcp'
    verbose_name = 'dhcp'
    description = 'An example plugin for development purposes'
    version = '1.0.2'
    author = 'anderson claudio'
    author_email = 'anderson.acrs@gmail.com'
    base_url = 'dhcp'
    required_settings = []
    default_settings = {
        'loud': False
    }

config = DhcpConfig
