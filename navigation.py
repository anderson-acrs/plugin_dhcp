from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

menu_items = (
    PluginMenuItem(
        link='plugins:dhcp:dhcp_list',
        link_text='DHCPs Listing',
        permissions=['dhcpd.dhcp_view'],
        buttons=(
            PluginMenuButton(
                link='plugins:dhcp:dhcp_add',
                title='Add a new dhcp',
                icon_class='fa fa-plus',
                color=ButtonColorChoices.GREEN,
                permissions=['dhcp.add_dhcp']
            ),
        )
    ),
    PluginMenuItem(
        link='plugins:dhcp:dhcp_list',
        link_text='Edita um dhcp',
        permissions=['dhcp.change_dhcp'],
    ),
    PluginMenuItem(
        link='plugins:dhcp:ipfixo_list',
        link_text='Ipfixeds Listing',
        permissions=['dhcpd.ipfixo_view'],
        buttons=(
            PluginMenuButton(
                link='plugins:dhcp:ipfixo_add',
                title='Add a new Ip Fixo',
                icon_class='fa fa-plus',
                color=ButtonColorChoices.GREEN,
                permissions=['dhcp.add_ipfixo']
            ),
        )
    ),
)
