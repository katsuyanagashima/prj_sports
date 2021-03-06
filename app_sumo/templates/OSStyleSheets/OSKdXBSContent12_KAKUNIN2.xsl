<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">
  <!-- ================================================================================= -->
  <!--　編集者用「共通スタイルシート」大相撲・幕下以下勝負 -->
  <!--  4.0版 2015.06.30 プレーンテキスト版のプレーンテキスト表示用として新規公開 -->
  <!--  4.01版 2015.●.● pタグのMatchStartクラス（対戦開始情報）を追加 -->
  <!--                    pタグのOikomiStartクラス（追い込み開始情報）を追加（１段で編集する場合のみ） -->
  <!-- ================================================================================= -->
  <!-- =================================== 変数定義 ==================================== -->
  <!-- ================================================================================= -->
  <!--【commonsetting定義】-->
  <!-- ================================================================================= -->
  <!-- 縦書き/横書き設定 -->
  <xsl:variable name="PTEXT_TATEYOKO_OS12_SET">
    <xsl:call-template name="PTEXT_TATEYOKO_OS12_SET"/>
  </xsl:variable>
  <!-- 選手名表示切替 -->
  <xsl:variable name="OS12_PLAYERNAME_DISPLAY_SET">
    <xsl:call-template name="OS12_PLAYERNAME_DISPLAY_SET"/>
  </xsl:variable>
  <!-- 対戦型　最大折り返し文字数定義-->
  <xsl:variable name="PRINT_MAXTEXT_FLG_OS12_SET">
    <!--可変要素がないので個別定義しない-->
    <xsl:value-of select="0"/>
  </xsl:variable>
  <xsl:variable name="PRINT_MAXTEXT_OS12_SET">
    <!--可変要素がないので個別定義しない-->
    <xsl:value-of select="99999"/>
  </xsl:variable>
  <!--決まり手の表示、非表示-->
  <xsl:variable name="FLG_WINNINGTRICK">
    <xsl:call-template name="OS12_WINNINGTRICK_DISPLAY_SET"/>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- 縦書き/横書き設定 -->
  <!-- ================================================================================= -->
  <xsl:variable name="OS12_PTEXT_TATEYOKO">
    <xsl:choose>
      <xsl:when test="$PTEXT_TATEYOKO_OS12_SET=0">
        <!-- 共通設定を適用 -->
        <xsl:value-of select="$PTEXT_TATEYOKO_SET"/>
      </xsl:when>
      <xsl:otherwise>
        <!-- 個別設定を適用 -->
        <xsl:value-of select="$PTEXT_TATEYOKO_OS12_SET"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- １ページ最大行数を取得 -->
  <!-- 判断条件は「印刷方向定義」「縦書き/横書き設定」 -->
  <!-- ================================================================================= -->
  <xsl:variable name="OS12_PRINT_MAXLINE">
    <xsl:choose>
      <!--Ａ４タテ印刷-->
      <xsl:when test="$PRINT_F_SET=1">
        <xsl:choose>
          <xsl:when test="$OS12_PTEXT_TATEYOKO=1">
            <!-- 縦書き -->
            <xsl:value-of select="$PRINT_MAXLINES_TATE_TATE_SET"/>
          </xsl:when>
          <xsl:otherwise>
            <!-- 横書き -->
            <xsl:value-of select="$PRINT_MAXLINES_TATE_YOKO_SET"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:when>
      <!--Ａ４ヨコ印刷-->
      <xsl:otherwise>
        <xsl:choose>
          <xsl:when test="$OS12_PTEXT_TATEYOKO=1">
            <!-- 縦書き -->
            <xsl:value-of select="$PRINT_MAXLINES_YOKO_TATE_SET"/>
          </xsl:when>
          <xsl:otherwise>
            <!-- 横書き -->
            <xsl:value-of select="$PRINT_MAXLINES_YOKO_YOKO_SET"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- １行最大折り返し文字数を取得（対戦表示部） -->
  <!-- ================================================================================= -->
  <xsl:variable name="OS12_MAXLENGTH">
    <xsl:variable name="NUM_CHECK">
      <xsl:choose>
        <xsl:when test="$PRINT_MAXTEXT_FLG_OS12_SET=1">
          <!-- 個別定義が有効な場合 -->
          <xsl:value-of select="$PRINT_MAXTEXT_OS12_SET"/>
        </xsl:when>
        <xsl:otherwise>
          <!-- 個別定義が無効な場合、共通定義を取得 -->
          <xsl:choose>
            <!--Ａ４タテ印刷-->
            <xsl:when test="$PRINT_F_SET=1">
              <xsl:choose>
                <xsl:when test="$OS12_PTEXT_TATEYOKO=1">
                  <!-- 縦書き -->
                  <xsl:value-of select="$PRINT_MAXTEXT_TATE_TATE_SET"/>
                </xsl:when>
                <xsl:otherwise>
                  <!-- 横書き -->
                  <xsl:value-of select="$PRINT_MAXTEXT_TATE_YOKO_SET"/>
                </xsl:otherwise>
              </xsl:choose>
            </xsl:when>
            <!--Ａ４ヨコ印刷-->
            <xsl:otherwise>
              <xsl:choose>
                <xsl:when test="$OS12_PTEXT_TATEYOKO=1">
                  <!-- 縦書き -->
                  <xsl:value-of select="$PRINT_MAXTEXT_YOKO_TATE_SET"/>
                </xsl:when>
                <xsl:otherwise>
                  <!-- 横書き -->
                  <xsl:value-of select="$PRINT_MAXTEXT_YOKO_YOKO_SET"/>
                </xsl:otherwise>
              </xsl:choose>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <xsl:choose>
      <!--最小値（18字未満ではフォーマットが崩れる）-->
      <xsl:when test="$NUM_CHECK &lt; 18">
        <xsl:value-of select="18"/>
      </xsl:when>
      <!--最大値-->
      <xsl:when test="$NUM_CHECK &gt; 24">
        <xsl:value-of select="24"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="$NUM_CHECK"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- １行最大折り返し文字数を取得（対戦表示以外） -->
  <!-- ================================================================================= -->
  <xsl:variable name="OS12_PRINT_MAXLENGTH">
    <xsl:choose>
      <xsl:when test="$OS12_PTEXT_TATEYOKO=1">
        <!-- 縦書き -->
        <xsl:value-of select="$OS12_MAXLENGTH"/>
      </xsl:when>
      <xsl:otherwise>
        <!-- 横書き -->
        <xsl:choose>
          <!--Ａ４タテ印刷-->
          <xsl:when test="$PRINT_F_SET=1">
            <xsl:value-of select="$PRINT_MAXTEXT_TATE_YOKO_SET"/>
          </xsl:when>
          <!--Ａ４ヨコ印刷-->
          <xsl:otherwise>
            <xsl:value-of select="$PRINT_MAXTEXT_YOKO_YOKO_SET"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- 名前エリア編集文字数 -->
  <!-- ================================================================================= -->
  <!--上段（左）の力士名の折り返し文字数-->
  <xsl:variable name="UpperPlayerAreaLength">
    <xsl:choose>
      <xsl:when test="$OS12_PLAYERNAME_DISPLAY_SET = 1 and $FLG_WINNINGTRICK = 0">
        <xsl:value-of select="3"/>
      </xsl:when>
      <xsl:when test="$OS12_PLAYERNAME_DISPLAY_SET = 1 and $FLG_WINNINGTRICK = 1">
        <xsl:value-of select="5"/>
      </xsl:when>
      <xsl:when test="$OS12_PLAYERNAME_DISPLAY_SET = 2">
        <xsl:value-of select="6"/>
      </xsl:when>
      <xsl:otherwise/>
    </xsl:choose>
  </xsl:variable>
  <!--下段（右）の力士名の折り返し文字数-->
  <xsl:variable name="LowerPlayerAreaLength">
    <xsl:choose>
      <xsl:when test="$OS12_PLAYERNAME_DISPLAY_SET = 1">
        <xsl:value-of select="4"/>
      </xsl:when>
      <xsl:when test="$OS12_PLAYERNAME_DISPLAY_SET = 2">
        <xsl:value-of select="6"/>
      </xsl:when>
      <xsl:otherwise/>
    </xsl:choose>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- 記録エリア編集文字数。半角１文字以上 -->
  <!-- ================================================================================= -->
  <xsl:variable name="ResultAreaLength">
    <!--「1」「2」は決まり手がセットされていても表示しない-->
    <xsl:choose>
      <xsl:when test="$OS12_PLAYERNAME_DISPLAY_SET = 1 and $FLG_WINNINGTRICK = 0">
        <!-- 力士名３字で決まり手なしは「―」で固定 -->
        <xsl:value-of select="1"/>
      </xsl:when>
      <xsl:when test="$FLG_WINNINGTRICK = 0">
        <!-- その他の決まり手なしは「―　」で固定 -->
        <xsl:value-of select="2"/>
      </xsl:when>
      <xsl:otherwise>
        <!-- 決まり手 -->
        <xsl:value-of select="6"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- 確認テンプレート（起点） -->
  <!-- ================================================================================= -->
  <xsl:template match="SportsData" mode="KAKUNIN2">
    <xsl:call-template name="KAKUNIN2_DIVS_TATELONG_LAYOUT_UTL">
      <!-- 本文要素 -->
      <xsl:with-param name="HONBUN_DATA">
        <xsl:call-template name="KAKUNIN_TEXT"/>
      </xsl:with-param>
      <!--字解-->
      <xsl:with-param name="JIKAI_DATA">
        <xsl:call-template name="Gaiji_KAKUNIN2"/>
      </xsl:with-param>
      <xsl:with-param name="LINE_MAX_LENGTH" select="$OS12_PRINT_MAXLENGTH"/>
      <xsl:with-param name="PAGE_LINE_MAX" select="$OS12_PRINT_MAXLINE"/>
      <xsl:with-param name="ADD_LINE_COUNT_FLG" select="$ADD_LINE_COUNT_FLG_SET"/>
      <xsl:with-param name="TATEYOKO_FLG" select="$OS12_PTEXT_TATEYOKO"/>
      <xsl:with-param name="ADD_OIKOMI_CLASS_FLG">
        <xsl:choose>
          <!-- ２段表示の場合はOikomiStartクラス表示なし（縦書き、力士名が３字で決まり手なしの場合） -->
          <xsl:when test="$OS12_PTEXT_TATEYOKO = 1
                      and $OS12_PLAYERNAME_DISPLAY_SET = 1 and $FLG_WINNINGTRICK = 0">
            <xsl:value-of select="0"/>
          </xsl:when>
          <!-- １段表示の場合はOikomiStartクラス表示あり -->
          <xsl:otherwise>
            <xsl:value-of select="1"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:with-param>
    </xsl:call-template>
  </xsl:template>
  <!-- ================================================================================= -->
  <!-- 本文要素（SportsData）-->
  <!-- ================================================================================= -->
  <xsl:template name="KAKUNIN_TEXT">
    <!--幕下以下取組編集-->
    <xsl:call-template name="MakushitaikaTorikumi_KAKUNIN2"/>
    <!--本文内注釈編集（SportsDataと同階層）-->
    <xsl:apply-templates select="../TextNote" mode="KAKUNIN2_EDT"/>
  </xsl:template>
  <!-- ================================================================================= -->
  <!-- ボディ（Body）-->
  <!-- ================================================================================= -->
  <xsl:template name="MakushitaikaTorikumi_KAKUNIN2">
    <xsl:for-each select="Body">
      <xsl:choose>
        <!-- 縦書き、力士名が３字で決まり手なしの場合は２段で表示 -->
        <xsl:when test="$OS12_PTEXT_TATEYOKO = 1
                    and $OS12_PLAYERNAME_DISPLAY_SET = 1 and $FLG_WINNINGTRICK = 0">
          <!-- １段目取組一覧の表示終了位置 -->
          <xsl:variable name="UpperMatchesLastNum">
            <xsl:value-of select="ceiling(count(Match) div 2)"/>
          </xsl:variable>
          <!-- ２段目取組一覧の表示開始位置 -->
          <xsl:variable name="LowerMatchesFirstNum">
            <xsl:value-of select="$UpperMatchesLastNum + 1"/>
          </xsl:variable>
          <!-- １段目編集 -->
          <xsl:variable name="UpperMatches">
            <!--Title-->
            <xsl:call-template name="TitleAndClass_KAKUNIN2">
              <xsl:with-param name="BodyMeta" select="Meta"/>
            </xsl:call-template>
            <!--Match-->
            <xsl:apply-templates select="Match[position() &lt;= $UpperMatchesLastNum]" mode="MakushitaikaTorikumi_KAKUNIN2">
              <xsl:with-param name="UpperPlayerAreaLength" select="$UpperPlayerAreaLength"/>
              <xsl:with-param name="LowerPlayerAreaLength" select="$LowerPlayerAreaLength"/>
              <xsl:with-param name="ResultAreaLength" select="$ResultAreaLength"/>
            </xsl:apply-templates>
          </xsl:variable>
          <!-- ２段目編集 -->
          <xsl:variable name="LowerMatches">
            <!--Title（２段目に対戦がある場合のみ表示）-->
            <xsl:if test="Match[position()=$LowerMatchesFirstNum]">
              <xsl:call-template name="TitleAndClass_KAKUNIN2">
                <!--２段目には階級を表示しないのでダミーのパスを指定-->
                <xsl:with-param name="BodyMeta" select="ThisPathDoesNotExist"/>
              </xsl:call-template>
              <xsl:value-of select="$LineFeed_UTL"/>
            </xsl:if>
            <!--Match-->
            <xsl:apply-templates select="Match[position() &gt;= $LowerMatchesFirstNum]" mode="MakushitaikaTorikumi_KAKUNIN2">
              <xsl:with-param name="UpperPlayerAreaLength" select="$UpperPlayerAreaLength"/>
              <xsl:with-param name="LowerPlayerAreaLength" select="$LowerPlayerAreaLength"/>
              <xsl:with-param name="ResultAreaLength" select="$ResultAreaLength"/>
            </xsl:apply-templates>
          </xsl:variable>
          <!-- １段目、２段目を割り付け -->
          <xsl:call-template name="TABLE_LAYOUT_LeftRight_UTIL">
            <xsl:with-param name="DATA1_AREA" select="7"/>
            <xsl:with-param name="DATA2_AREA" select="7"/>
            <xsl:with-param name="DATA1" select="$UpperMatches"/>
            <xsl:with-param name="DATA2" select="$LowerMatches"/>
            <xsl:with-param name="SPACE" select="1"/>
          </xsl:call-template>
        </xsl:when>
        <!-- その他は１段で表示 -->
        <xsl:otherwise>
          <!--Title-->
          <xsl:call-template name="TitleAndClass_KAKUNIN2">
            <xsl:with-param name="BodyMeta" select="Meta"/>
          </xsl:call-template>
          <!--Match-->
          <xsl:variable name="MatchData">
            <xsl:apply-templates select="Match" mode="MakushitaikaTorikumi_KAKUNIN2"/>
          </xsl:variable>
          <!-- pタグに設定するclass付加制御（OikomiStartを自動付加しない）のため排除処理を行う -->
          <xsl:call-template name="Taisen_SetNoClass_UTL">
            <xsl:with-param name="Data" select="$MatchData"/>
          </xsl:call-template>
        </xsl:otherwise>
      </xsl:choose>
      <!--本文内注釈編集（Matchと同階層）-->
      <xsl:apply-templates select="TextNote" mode="KAKUNIN2_EDT"/>
    </xsl:for-each>
    <!--本文内注釈編集（Bodyと同階層）-->
    <xsl:apply-templates select="TextNote" mode="KAKUNIN2_EDT"/>
  </xsl:template>
  <!-- ================================================================================= -->
  <!-- 対戦（Match）-->
  <!-- ================================================================================= -->
  <xsl:template match="Match" mode="MakushitaikaTorikumi_KAKUNIN2">
    <!--「1」力士名は３字-->
    <!--「2」力士名は正式名-->
    <!--=====上段（左）力士=====-->
    <!--勝ち越し／負け越し-->
    <xsl:variable name="UpperPlayersOutcomeAttribute">
      <!--勝ち越し／負け越し（決まり手ありの場合のみ表示）-->
      <xsl:if test="$FLG_WINNINGTRICK = 1">
        <xsl:value-of select="Player[1]/Result/ResultForSumo/OutcomeAttribute/Writing"/>
      </xsl:if>
    </xsl:variable>
    <xsl:variable name="UpperPlayerName">
      <xsl:choose>
        <!--パターン「1」-->
        <xsl:when test="$OS12_PLAYERNAME_DISPLAY_SET = 1">
          <!--勝ち越し／負け越し（決まり手ありの場合のみ表示）-->
          <xsl:if test="$FLG_WINNINGTRICK = 1">
            <xsl:value-of select="$UpperPlayersOutcomeAttribute"/>
            <xsl:call-template name="PrintSpaceZenkaku_UTL">
              <xsl:with-param name="count" select="1 - string-length($UpperPlayersOutcomeAttribute)"/>
            </xsl:call-template>
          </xsl:if>
          <!--力士名-->
          <xsl:value-of select="Player[1]/PlayerName/Formal[@Display='3字']"/>
          <xsl:if test="$FLG_WINNINGTRICK = 1">
            <xsl:value-of select="$WhiteSpaceZenkaku_UTL"/>
          </xsl:if>
        </xsl:when>
        <!--パターン「2」-->
        <xsl:otherwise>
          <!--力士名-->
          <xsl:variable name="tmpPlayerName">
            <xsl:choose>
              <!--３字以下の場合には字取りするため、３字を使用-->
              <xsl:when test="string-length(Player[1]/PlayerName/Formal[not(@*)]) &lt;= 3
                              and Player[1]/PlayerName/Formal[@Display='3字']">
                <xsl:call-template name="AddSpaceForTaisen_KAKUNIN_OSCOM2">
                  <xsl:with-param name="Outcome" select="$UpperPlayersOutcomeAttribute"/>
                  <xsl:with-param name="Data" select="Player[1]/PlayerName/Formal[@Display='3字']"/>
                  <xsl:with-param name="Length" select="$UpperPlayerAreaLength"/>
                </xsl:call-template>
              </xsl:when>
              <xsl:otherwise>
                <xsl:call-template name="AddSpaceForTaisen_KAKUNIN_OSCOM2">
                  <xsl:with-param name="Outcome" select="$UpperPlayersOutcomeAttribute"/>
                  <xsl:with-param name="Data" select="Player[1]/PlayerName/Formal[not(@*)]"/>
                  <xsl:with-param name="Length" select="$UpperPlayerAreaLength"/>
                </xsl:call-template>
              </xsl:otherwise>
            </xsl:choose>
          </xsl:variable>
          <xsl:call-template name="AddBR_KAKUNIN_OSCOM2">
            <xsl:with-param name="Data" select="$tmpPlayerName"/>
            <xsl:with-param name="Length" select="$UpperPlayerAreaLength"/>
            <xsl:with-param name="LeftOrRight" select="1"/>
            <xsl:with-param name="KakkoHamidashiFlg" select="0"/>
          </xsl:call-template>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <!--=====決まり手=====-->
    <xsl:variable name="tmpWinningTrick">
      <xsl:choose>
        <xsl:when test="$FLG_WINNINGTRICK = 0">
          <xsl:choose>
            <xsl:when test="MatchDetail/MatchResult/Outcome/Writing">
              <xsl:value-of select="MatchDetail/MatchResult/Outcome/Writing"/>
            </xsl:when>
            <xsl:otherwise>
              <xsl:text>―</xsl:text>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="MatchDetail/WinningTrick/Formal[not(@*)]"/>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <xsl:variable name="lengthWinningTrick" select="string-length($tmpWinningTrick)"/>
    <!-- 上段力士名エリアへのはみ出し部分-->
    <xsl:variable name="ResultAreaOverflowed">
      <!--決まり手が７字で、上段力士の１行目の最後の文字が空白の場合は、１字はみ出し処理する-->
      <xsl:if test="$lengthWinningTrick = $ResultAreaLength +1
                  and (substring($UpperPlayerName, $UpperPlayerAreaLength, 1) = '　'
                    or substring($UpperPlayerName, $UpperPlayerAreaLength, 1) = $WhiteSpaceZenkaku_UTL)">
        <xsl:value-of select="substring($tmpWinningTrick, 1, 1)"/>
      </xsl:if>
    </xsl:variable>
    <!--====決まり手エリア=====-->
    <xsl:variable name="ResultAreaInfo">
      <xsl:choose>
        <!--決まり手を非表示-->
        <xsl:when test="$FLG_WINNINGTRICK = 0">
          <xsl:value-of select="$tmpWinningTrick"/>
        </xsl:when>
        <!--決まり手を表示-->
        <xsl:otherwise>
          <!--決まり手の７字取り処理-->
          <xsl:call-template name="AddBRandSpaceToWinningTrick_OSCOM2">
            <xsl:with-param name="PLAYER_INFO_1" select="$UpperPlayerName"/>
            <xsl:with-param name="WINNING_TRICK" select="$tmpWinningTrick"/>
            <xsl:with-param name="PLAYER1_AREA_LENGTH" select="$UpperPlayerAreaLength"/>
            <xsl:with-param name="WINNING_TRICK_LENGTH" select="$lengthWinningTrick"/>
            <xsl:with-param name="RESULT_AREA_LENGTH" select="$ResultAreaLength"/>
            <xsl:with-param name="RESULT_AREA_OVERFLOWED" select="$ResultAreaOverflowed"/>
          </xsl:call-template>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <!--=====下段（右）力士=====-->
    <!--勝ち越し／負け越し-->
    <xsl:variable name="LowerPlayersOutcomeAttribute">
      <!--勝ち越し／負け越し（決まり手ありの場合のみ表示）-->
      <xsl:if test="$FLG_WINNINGTRICK = 1">
        <xsl:value-of select="Player[2]/Result/ResultForSumo/OutcomeAttribute/Writing"/>
      </xsl:if>
    </xsl:variable>
    <xsl:variable name="LowerPlayerName">
      <xsl:choose>
        <!--パターン「1」-->
        <xsl:when test="$OS12_PLAYERNAME_DISPLAY_SET = 1">
          <!--力士名-->
          <xsl:value-of select="Player[2]/PlayerName/Formal[@Display='3字']"/>
          <!--勝ち越し／負け越し（決まり手ありの場合のみ表示）-->
          <xsl:if test="$FLG_WINNINGTRICK = 1">
            <xsl:value-of select="$LowerPlayersOutcomeAttribute"/>
          </xsl:if>
        </xsl:when>
        <!--パターン「2」-->
        <xsl:otherwise>
          <!--力士名、勝ち越し／負け越し-->
          <xsl:variable name="tmpPlayerNameAndGrade">
            <xsl:variable name="tmpPlayerName">
              <xsl:choose>
                <!--３字以下の場合には字取りするため、３字を使用-->
                <xsl:when test="string-length(Player[2]/PlayerName/Formal[not(@*)]) &lt;= 3
                                and Player[2]/PlayerName/Formal[@Display='3字']">
                  <xsl:value-of select="Player[2]/PlayerName/Formal[@Display='3字']"/>
                </xsl:when>
                <xsl:otherwise>
                  <xsl:value-of select="Player[2]/PlayerName/Formal[not(@*)]"/>
                </xsl:otherwise>
              </xsl:choose>
            </xsl:variable>
            <xsl:value-of select="$tmpPlayerName"/>
            <!--勝ち越し／負け越し（決まり手ありの場合のみ表示）-->
            <xsl:value-of select="$LowerPlayersOutcomeAttribute"/>
          </xsl:variable>
          <xsl:call-template name="AddBR_KAKUNIN_OSCOM2">
            <xsl:with-param name="Data" select="$tmpPlayerNameAndGrade"/>
            <xsl:with-param name="Length" select="$LowerPlayerAreaLength"/>
            <xsl:with-param name="LeftOrRight" select="2"/>
            <xsl:with-param name="KakkoHamidashiFlg" select="0"/>
          </xsl:call-template>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <!--=====表示=====-->
    <!-- １段表示の場合のみMatchStartを付加（縦書き・力士名３字・決まり手なしの組み合わせは２段表示のため付加しない）-->
    <xsl:if test="not($OS12_PTEXT_TATEYOKO = 1
                and $OS12_PLAYERNAME_DISPLAY_SET = 1 and $FLG_WINNINGTRICK = 0)">
      <xsl:value-of select="$MatchClass_UTL"/>
    </xsl:if>
    <xsl:call-template name="TaisenLayout_TORIKUMI_OSCOM">
      <xsl:with-param name="PLAYER_INFO_1" select="$UpperPlayerName"/>
      <xsl:with-param name="PLAYER_INFO_2" select="$LowerPlayerName"/>
      <xsl:with-param name="RESULT_AREA_OVERFLOWED" select="$ResultAreaOverflowed"/>
      <xsl:with-param name="RESULT_AREA_INFO" select="$ResultAreaInfo"/>
      <xsl:with-param name="PLAYER1_AREA_LENGTH" select="$UpperPlayerAreaLength"/>
      <xsl:with-param name="PLAYER2_AREA_LENGTH" select="$LowerPlayerAreaLength"/>
      <xsl:with-param name="RESULT_AREA_LENGTH" select="$ResultAreaLength"/>
    </xsl:call-template>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- ヘッダー編集 -->
  <!--=======================================================================================================-->
  <xsl:template name="TitleAndClass_KAKUNIN2">
    <xsl:param name="BodyMeta"/>
    <xsl:choose>
      <!--決まり手を非表示-->
      <xsl:when test="$FLG_WINNINGTRICK = 0">
        <xsl:if test="not(contains($BodyMeta/Title, '十両対戦'))">
          <xsl:value-of select="$WhiteSpaceZenkaku_UTL"/>
          <xsl:text>勝</xsl:text>
          <xsl:call-template name="PrintSpaceZenkaku_UTL">
            <xsl:with-param name="count" select="$UpperPlayerAreaLength + $ResultAreaLength -1"/>
          </xsl:call-template>
          <xsl:text>負</xsl:text>
          <xsl:value-of select="$LineFeed_UTL"/>
        </xsl:if>
        <xsl:for-each select="$BodyMeta/Title">
          <xsl:value-of select="."/>
          <xsl:value-of select="$LineFeed_UTL"/>
        </xsl:for-each>
      </xsl:when>
      <!--決まり手を表示-->
      <xsl:otherwise>
        <xsl:choose>
          <!--【十両対戦】のみTitleを使用する-->
          <xsl:when test="contains($BodyMeta, '十両対戦')">
            <xsl:for-each select="$BodyMeta/Title">
              <xsl:value-of select="."/>
              <xsl:value-of select="$LineFeed_UTL"/>
            </xsl:for-each>
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="$WhiteSpaceZenkaku_UTL"/>
            <xsl:value-of select="$WhiteSpaceZenkaku_UTL"/>
            <xsl:text>勝</xsl:text>
            <xsl:call-template name="PrintSpaceZenkaku_UTL">
              <xsl:with-param name="count" select="$UpperPlayerAreaLength -3"/>
            </xsl:call-template>
            <xsl:text>＝</xsl:text>
            <xsl:call-template name="FillSpace_UTL">
              <xsl:with-param name="Data" select="$BodyMeta/Class"/>
              <xsl:with-param name="AreaLength" select="3"/>
            </xsl:call-template>
            <xsl:text>＝</xsl:text>
            <xsl:call-template name="PrintSpaceZenkaku_UTL">
              <xsl:with-param name="count" select="$ResultAreaLength -4"/>
            </xsl:call-template>
            <xsl:text>負</xsl:text>
            <xsl:value-of select="$LineFeed_UTL"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!-- ================================================================================= -->
  <!-- 字解表示 -->
  <!-- ================================================================================= -->
  <xsl:template name="Gaiji_KAKUNIN2">
    <!-- 字解編集 -->
    <xsl:variable name="JIKAI_DATA">
      <!--=====上段=====-->
      <!--力士名-->
      <xsl:choose>
        <xsl:when test="$OS12_PLAYERNAME_DISPLAY_SET = 1">
          <xsl:for-each select="//Match/Player[1]/PlayerName/Formal[@Display='3字']">
            <xsl:call-template name="Gaiji_EDT"/>
          </xsl:for-each>
        </xsl:when>
        <xsl:when test="$OS12_PLAYERNAME_DISPLAY_SET = 2">
          <xsl:for-each select="//Match/Player[1]/PlayerName/Formal[not(@*)]">
            <xsl:call-template name="Gaiji_EDT"/>
          </xsl:for-each>
        </xsl:when>
        <xsl:otherwise/>
      </xsl:choose>
      <!--=====下段=====-->
      <!--力士名-->
      <xsl:choose>
        <xsl:when test="$OS12_PLAYERNAME_DISPLAY_SET = 1">
          <xsl:for-each select="//Match/Player[2]/PlayerName/Formal[@Display='3字']">
            <xsl:call-template name="Gaiji_EDT"/>
          </xsl:for-each>
        </xsl:when>
        <xsl:when test="$OS12_PLAYERNAME_DISPLAY_SET = 2">
          <xsl:for-each select="//Match/Player[2]/PlayerName/Formal[not(@*)]">
            <xsl:call-template name="Gaiji_EDT"/>
          </xsl:for-each>
        </xsl:when>
        <xsl:otherwise/>
      </xsl:choose>
      <!--記事-->
      <xsl:for-each select=".//Article/Paragraph">
        <xsl:call-template name="Gaiji_EDT"/>
      </xsl:for-each>
      <!--本文内注釈-->
      <xsl:for-each select="..//TextNote">
        <xsl:call-template name="Gaiji_EDT"/>
      </xsl:for-each>
    </xsl:variable>
    <!--字解が存在した場合-->
    <xsl:if test="($JIKAI_DATA!='')">
      <!--字解見出し-->
      <xsl:text>字解情報</xsl:text>
      <xsl:value-of select="$LineFeed_UTL"/>
      <!--字解-->
      <xsl:value-of select="$JIKAI_DATA"/>
    </xsl:if>
  </xsl:template>
</xsl:stylesheet>
