'''
实验名称：Si4703 Tuner收音机
版本：v1.0
日期：2022.06.05
作者：01Studio
说明：mp3/wav音频文件播放，使用触摸按键控制。
'''
from si4703Library import si4703Radio

radio = si4703Radio(0x10, 'B13', "B8", "B9")

radio.si4703Init()

radio.si4703SetVolume(10)

radio.si4703SeekUp()

radio.si4703SeekDown()



