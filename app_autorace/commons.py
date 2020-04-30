import re
class Common():
    # 正規表現で半角ブランク削除
    def chkBlank(self, chkline):

        if (not re.sub('\\s+', '', chkline)):
            return False
        return True