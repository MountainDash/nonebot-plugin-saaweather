from nonebot import require

require("nonebot_plugin_apscheduler")
require("nonebot_plugin_saa")
require("nonebot_plugin_orm")

from nonebot.plugin import PluginMetadata, inherit_supported_adapters

__plugin_meta__ = PluginMetadata(
    name="啥天气",
    description="基于SAA的天气查询插件",
    usage="输入“啥天气”或“天气”加上地名即可查询天气",
    type="application",
    homepage="https://github.com/MountainDash/nonebot-plugin-saaweather",
    supported_adapters=inherit_supported_adapters("nonebot_plugin_saa"),
)
