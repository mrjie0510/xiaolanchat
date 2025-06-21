import datetime
from nonebot import on_command
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import Message, MessageEvent, MessageSegment

zhouyisuangua = on_command("卜卦", aliases={"算卦", "SG"})
xiagua = 0
shanggua = 0
binayao = 0

@zhouyisuangua.handle()
async def _(event: MessageEvent, msg: Message = CommandArg()):
    qq = int(event.get_user_id())
    xiagua = int(int(hash(qq))%8)
    dt = datetime.datetime.now()
    shanggua = int(int(dt.strftime("%Y%m%d"))%8)
    content = msg.extract_plain_text()
    if content == "" or content is None:
        await zhouyisuangua.finish(MessageSegment.text("请在指令后输入你想算的东西！"), at_sender=True)
    bianyao = int(int(hash(content))%6)
    jieguo = xiagua+shanggua+bianyao
    await zhouyisuangua.finish(MessageSegment.text("算出来了，结果是"+jieguo+"，但是448行还没写完"),at_sender=True)