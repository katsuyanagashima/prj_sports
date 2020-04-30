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
JOU_NAME     = '●●●競馬場'
JOU_SEISEKIA = '●'
JOU_3CHAR    = '●'
JOU_BANEI    = False

NIGHT_RACE_NAME = '●●●●●'

#####################
# watchdoc 関連　End
#####################