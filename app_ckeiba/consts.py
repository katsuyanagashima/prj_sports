########################
# watchdoc 関連　Start
########################
GO_RECURSIVELY = False # 再帰的
CSV_LOCK_FILE = '.csv_lockfile'

CSVDATA         = "CSVフォルダ"

NORMAL   = True
ABNORMAL = False

# 監視対象ファイルのパターンマッチを指定する
TARGET_FILE_DAT_RECORD = ['*BA7*','*SEI*']

EVENTDATEDATA            = 'BA7' # 開催日割データ
SIMPLERACERESULTSDATA    = 'SEI' # 簡易競走成績データ

RACECARD            = 'SUA' # 出馬表Aデータ（番組情報）
ARRIVALTIME         = 'SU6' # 着タイムデータ
BETTINGHANDLE       = 'WI2' # 単勝複勝払戻データ
BRACKETQUINELLA     = 'BL2' # 枠複枠単払戻データ
QUINELLA            = 'QU2' # 馬連馬単ワイド払戻データ
TIERCES             = 'TB3' # 三連複払戻データ
TIERCE              = 'TB4' # 三連単払戻データ
ADDITIONALDOCUMENT  = 'BU1' # 付加文書データ

# エラーメッセージ

# 競馬場マスタ 必須項目
JOU_NAME     = '●●●●●●●●●●●●●●●●●●●●'
JOU_SEISEKIA = '●'
JOU_3CHAR    = '●●●'
JOU_BANEI    = False

# 競走種類マスタ
RACE_TYPE_NAME = '●●●●●●●●●●'
RACE_TYPE_DELIVERYTYPE = 3

# 品種年齢区分マスタ
NAME_FOR_RACE_TYPE = '●●●●●●●●●●'

# 負担重量区分マスタ
HANDICAP_NAME= '●●●●●'

# 中央交流区分マスタ
JRA_EXCHANGES = '●●●●●●●●●●'

# グレードマスタ
GRADE_NAME = '●●●●'

# 芝・ダート区分マスタ
TURF_DIRT_NAME = '●●●●●'

# コース区分マスタ
COURSE_CLASS_NAME= '●●●●●'

# 回り区分マスタ
CW_OR_CCW = '●●●●●'

# 天候マスタ
WEATHER_NAME = '●●●●●'

# 馬場状態マスタ
TRACK_CONDITION_NAME = '●●●●●'

# ナイター区分マスタ
NIGHT_RACE_NAME = '●●●●●'

# 性別マスタ
HORSE_GENDER = '●●'

# 所属場マスタ
BELONGING = '●●●●●●●●●●'

# 騎手変更理由マスタ
JOCKEY_CHANGED_REASON_NAME = '●●●●●●●●●●'

# 着差マスタ
MARGIN_NAME = '●●●●●●●●●●'

# 事故種類マスタ
ACCIDENT_TYPE_NAME = '●●●●●●●●●●●●●●●'

# 事故理由マスタ
ACCIDENT_REASON_NAME = '●●●●●●●●●●●●●●●'

# 事象マスタ
MATTER_NAME = '●●●●●●●●●●'

# 対象者マスタ
TARGET_PERSON_NAME = '●●●●●●●●●●'

#####################
# watchdoc 関連　End
#####################