from utilities.choices import ChoiceSet

class DhcpChoices(ChoiceSet):
    """ lista possiveis status do dhcp"""
    TIPO_IPV4 = 'IPV4'
    TIPO_IPV6 = 'IPV6'
    TIPO_BOTH = 'IPV4/IPV6'

    CHOICES = (
        (TIPO_IPV4,'IPV4'),
        (TIPO_IPV6, 'IPV6'),
        (TIPO_BOTH, 'IPV4/IPV6'),
    )
