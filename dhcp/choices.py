from utilities.choices import ChoiceSet

class DhcpChoices(ChoiceSet):
    """ lista tipos do protocolo dhcp"""
    TIPO_IPV4 = 'IPV4'
    TIPO_IPV6 = 'IPV6'
    #TIPO_BOTH = 'IPV4/IPV6'

    CHOICES = (
        (TIPO_IPV4,'IPV4'),
        (TIPO_IPV6, 'IPV6'),
       # (TIPO_BOTH, 'IPV4/IPV6'),
    )
class DhcpOpcaoChoices(ChoiceSet):
    """lista as opcoes de texto do dhcp 43, 60, 66, 68,"""
    TIPO_43 = '43'
    TIPO_60 = '60'
    TIPO_66 = '66'
    TIPO_68 = '68'

    CHOICES = (
        (TIPO_43,'43'),
        (TIPO_60,'60'),
        (TIPO_66,'66'),
        (TIPO_68,'68'),

    )
class DhcpDnsChoices(ChoiceSet):
    """ Lista de opcoes de texto para o DNS """
    TIPO_DNS1 = '10.3.156.40'
    TIPO_DNS2 = '10.3.156.41'
    TIPO_DNS3 = '45.55.153.57'
    TIPO_DNS4 = '8.8.8.8'

    CHOICES = (
        (TIPO_DNS1,'10.3.156.40'),
        (TIPO_DNS2,'10.3.156.41'),
        (TIPO_DNS3,'45.55.153.57'),
        (TIPO_DNS4,'8.8.8.8.8'),

    )