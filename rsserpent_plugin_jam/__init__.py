from rsserpent.models import Persona, Plugin

from . import route


plugin = Plugin(
    name="rsserpent-plugin-jam",
    author=Persona(
        name="wuzhongyi1105",
        link="https://github.com/wuzhongyi1105",
        email="dw@watelier.cn",
    ),
    prefix="/jam",
    repository="https://github.com/wuzhongyi1105/rsserpent-plugin-jam",
    routers={route.path: route.provider},
)
