########################
# watchdoc 関連　Start
########################
GO_RECURSIVELY = False # 再帰的
DAD_LOCK_FILE = '.dat_lockfile'

DATDATA         = "固定長フォルダ"
SCHEDULEDATDATA = "スケジュールフォルダ"
PROCESSEDDATDATA= "処理済みフォルダ"
SCHEDULEDATA    = "scheduleData"
PROGRAMDATA     = "programData"
RESULTDATA      = "resultData"
TOP30PRIZEDATA  = "top30prizeData"
OUTSIDETRACKDATA= "outsidetrackData"

NORMAL   = True
ABNORMAL = False

# 監視対象ファイルのパターンマッチを指定する
TARGET_FILE_DAT_RECORD = ['*00000000.dat', '*0000[1-6]001.dat', '*0000[1-6]0[1-9]2.dat','*0000[1-6]1[0-2]2.dat', '*00000003.dat', '*00000004.dat']
TARGET_FILE_SCHEDULE_RECORD = ['*00000000.dat']
TARGET_FILE_PROGRAM_RECORD = ['*0000[1-6]001.dat']
TARGET_FILE_RESULT_RECORD = ['*0000[1-6]0[1-9]2.dat','*0000[1-6]1[0-2]2.dat']
TARGET_FILE_TOP30PRIZE_RECORD = ['*00000003.dat']
TARGET_FILE_OUTSIDETRACK_RECORD = ['*00000004.dat']

SCHEDULE    = 0
PROGRAM     = 1
RESULT      = 2
TOP30PRIZE  = 3
OUTSIDETRACK= 4


# エラーメッセージ


#####################
# watchdoc 関連　End
#####################
