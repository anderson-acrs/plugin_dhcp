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
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
                permissions=['dhcp.add_dhcp']
            ),
            PluginMenuButton(
                link='plugins:dhcp:dhcp_import',
                title='Import a New .CSV date',
                icon_class='mdi mdi-upload',
                color=ButtonColorChoices.BLUE,
                permissions=['dhcp.import_dhcp']
            ),
        )
    ),

    PluginMenuItem(
        link='plugins:dhcp:ipfixo_list',
        link_text='Fixed Address List',
        permissions=['dhcpd.ipfixo_view'],
        buttons=(
            PluginMenuButton(
                link='plugins:dhcp:ipfixo_add',
                title='Add a new Address',
                icon_class='mdi mdi-plus-thick',
                color=ButtonColorChoices.GREEN,
                permissions=['dhcp.add_ipfixo']
            ),
            PluginMenuButton(
                link='plugins:dhcp:ipfixo_import',
                title='Import a New .CSV date',
                icon_class='mdi mdi-upload',
                color=ButtonColorChoices.BLUE,
                permissions=['ipfixo.import_ipfixo']
            ),
        )
    ),
)
