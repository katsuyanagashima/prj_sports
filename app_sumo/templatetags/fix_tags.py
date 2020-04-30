from django import template
from django.template.defaultfilters import stringfilter
import re

register = template.Library() # Djangoのテンプレートタグライブラリ

# カスタムフィルタとして登録する
@register.filter
@stringfilter # 文字列に自動変換できるデコレータ
def get_first4char(str):
    return str[0:4]

@register.filter
@stringfilter
def get_5_11char(str):
    return str[5:5]

#半角数字を全角に変換
@register.filter
@stringfilter
def intToZen(i):
     HAN2ZEN = str.maketrans({"0":"０", "1":"１", "2":"２", "3":"３", "4":"４", "5":"５", "6":"６", "7":"７", "8":"８", "9":"９", ".":"．"})
     return str(i).translate(HAN2ZEN)

#半角数字を連数字に変換
"""
@register.filter
@stringfilter
def intToZen(i):
     HAN2ZEN = str.maketrans({"0":"０", "1":"１", "2":"２", "3":"３", "4":"４", "5":"５", "6":"６", "7":"７", "8":"８", "9":"９", ".":"．", "43":"◎"})
     return str(i).translate(HAN2ZEN)
"""

#少数の整数部がゼロだったら除外
# 例）0.654 →　.654
@register.filter
@stringfilter
def remmove_integer0(str):
    return str.replace('0.','.')

#２文字に分割
@register.filter
@stringfilter
def split2char(str):
    return re.split('(..)',str)[1::2]

"""    
buf='abcdef'
list = re.split('(..)',buf)[1::2]
print list
"""