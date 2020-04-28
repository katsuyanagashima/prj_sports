from django import template
from django.template.defaultfilters import stringfilter

register = template.Library() # Djangoのテンプレートタグライブラリ

# カスタムフィルタとして登録する
@register.filter
@stringfilter # 文字列に自動変換できるデコレータ
def text_get4char(str):
    return str[0:4]