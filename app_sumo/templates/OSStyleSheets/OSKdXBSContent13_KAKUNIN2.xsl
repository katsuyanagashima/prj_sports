<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">
  <!-- ================================================================================= -->
  <!--　編集者用「共通スタイルシート」大相撲・勝負 -->
  <!--  4.0版 2015.06.30 プレーンテキスト版のプレーンテキスト表示用として新規公開 -->
  <!--  4.01版 2015.●.● pタグのMatchStartクラス（対戦開始情報）を追加 -->
  <!--                    pタグのOikomiStartクラス（追い込み開始情報）を追加 -->
  <!-- ================================================================================= -->
  <!-- =================================== 変数定義 ==================================== -->
  <!-- ================================================================================= -->
  <!--【commonsetting定義】-->
  <!-- ================================================================================= -->
  <!-- 縦書き/横書き設定 -->
  <xsl:variable name="PTEXT_TATEYOKO_OS13_OS14_SET">
    <xsl:call-template name="PTEXT_TATEYOKO_OS13_OS14_SET"/>
  </xsl:variable>
  <!-- 選手名表示切替 -->
  <xsl:variable name="OS13_OS14_PLAYERNAME_DISPLAY_SET">
    <xsl:call-template name="OS13_OS14_PLAYERNAME_DISPLAY_SET"/>
  </xsl:variable>
  <!-- 対戦型　最大折り返し文字数定義-->
  <xsl:variable name="PRINT_MAXTEXT_FLG_OS13_OS14_SET">
    <!--可変要素がないので個別定義しない-->
    <xsl:value-of select="0"/>
  </xsl:variable>
  <xsl:variable name="PRINT_MAXTEXT_OS13_OS14_SET">
    <!--可変要素がないので個別定義しない-->
    <xsl:value-of select="99999"/>
  </xsl:variable>
  <!--対戦成績の表示、非表示-->
  <xsl:variable name="FLG_OUTCOME_TSUSAN">
    <xsl:call-template name="OS13_OS14_OUTCOME_TSUSAN_DISPLAY_SET"/>
  </xsl:variable>
  <!--今場所成績の表示、非表示-->
  <xsl:variable name="FLG_OUTCOME_KONBASHO">
    <xsl:call-template name="OS13_OS14_OUTCOME_KONBASHO_DISPLAY_SET"/>
  </xsl:variable>
  <!--時間の表示、非表示-->
  <xsl:variable name="FLG_CLOSINGTIME">
    <xsl:call-template name="OS13_OS14_CLOSINGTIME_DISPLAY_SET"/>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- 縦書き/横書き設定 -->
  <!-- ================================================================================= -->
  <xsl:variable name="OS13_OS14_PTEXT_TATEYOKO">
    <xsl:choose>
      <xsl:when test="$PTEXT_TATEYOKO_OS13_OS14_SET=0">
        <!-- 共通設定を適用 -->
        <xsl:value-of select="$PTEXT_TATEYOKO_SET"/>
      </xsl:when>
      <xsl:otherwise>
        <!-- 個別設定を適用 -->
        <xsl:value-of select="$PTEXT_TATEYOKO_OS13_OS14_SET"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- １ページ最大行数を取得 -->
  <!-- 判断条件は「印刷方向定義」「縦書き/横書き設定」 -->
  <!-- ================================================================================= -->
  <xsl:variable name="OS13_OS14_PRINT_MAXLINE">
    <xsl:choose>
      <!--Ａ４タテ印刷-->
      <xsl:when test="$PRINT_F_SET=1">
        <xsl:choose>
          <xsl:when test="$OS13_OS14_PTEXT_TATEYOKO=1">
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
          <xsl:when test="$OS13_OS14_PTEXT_TATEYOKO=1">
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
  <xsl:variable name="OS13_OS14_MAXLENGTH">
    <xsl:variable name="NUM_CHECK">
      <xsl:choose>
        <xsl:when test="$PRINT_MAXTEXT_FLG_OS13_OS14_SET=1">
          <!-- 個別定義が有効な場合 -->
          <xsl:value-of select="$PRINT_MAXTEXT_OS13_OS14_SET"/>
        </xsl:when>
        <xsl:otherwise>
          <!-- 個別定義が無効な場合、共通定義を取得 -->
          <xsl:choose>
            <!--Ａ４タテ印刷-->
            <xsl:when test="$PRINT_F_SET=1">
              <xsl:choose>
                <xsl:when test="$OS13_OS14_PTEXT_TATEYOKO=1">
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
                <xsl:when test="$OS13_OS14_PTEXT_TATEYOKO=1">
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
  <xsl:variable name="OS13_OS14_PRINT_MAXLENGTH">
    <xsl:choose>
      <xsl:when test="$OS13_OS14_PTEXT_TATEYOKO=1">
        <!-- 縦書き -->
        <xsl:value-of select="$OS13_OS14_MAXLENGTH"/>
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
      <xsl:when test="$OS13_OS14_PLAYERNAME_DISPLAY_SET = 1">
        <xsl:value-of select="5"/>
      </xsl:when>
      <xsl:when test="$OS13_OS14_PLAYERNAME_DISPLAY_SET = 2">
        <xsl:value-of select="6"/>
      </xsl:when>
      <xsl:otherwise/>
    </xsl:choose>
  </xsl:variable>
  <!--下段（右）の力士名の折り返し文字数-->
  <xsl:variable name="LowerPlayerAreaLength">
    <xsl:choose>
      <xsl:when test="$OS13_OS14_PLAYERNAME_DISPLAY_SET = 1">
        <xsl:value-of select="4"/>
      </xsl:when>
      <xsl:when test="$OS13_OS14_PLAYERNAME_DISPLAY_SET = 2">
        <xsl:value-of select="6"/>
      </xsl:when>
      <xsl:otherwise/>
    </xsl:choose>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- 記録エリア編集文字数。半角１文字以上 -->
  <!-- ================================================================================= -->
  <xsl:variable name="ResultAreaLength">
    <!-- 決まり手 -->
    <xsl:value-of select="6"/>
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
      <xsl:with-param name="LINE_MAX_LENGTH" select="$OS13_OS14_PRINT_MAXLENGTH"/>
      <xsl:with-param name="PAGE_LINE_MAX" select="$OS13_OS14_PRINT_MAXLINE"/>
      <xsl:with-param name="ADD_LINE_COUNT_FLG" select="$ADD_LINE_COUNT_FLG_SET"/>
      <xsl:with-param name="TATEYOKO_FLG" select="$OS13_OS14_PTEXT_TATEYOKO"/>
      <xsl:with-param name="ADD_OIKOMI_CLASS_FLG" select="1"/>
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
    <!--Bodyタグを編集-->
    <xsl:for-each select="Body">
      <!--Title-->
      <xsl:call-template name="TitleAndClass_KAKUNIN2">
        <xsl:with-param name="BodyMeta" select="Meta"/>
      </xsl:call-template>
      <!--Article-->
      <xsl:if test="Article/Paragraph">
        <xsl:value-of select="$WhiteSpaceZenkaku_UTL"/>
        <xsl:value-of select="Article/Paragraph"/>
        <xsl:value-of select="$LineFeed_UTL"/>
      </xsl:if>
      <!--Match-->
      <xsl:variable name="MatchData">
        <xsl:apply-templates select="Match" mode="MakushitaikaTorikumi_KAKUNIN2"/>
      </xsl:variable>
      <!-- pタグに設定するclass付加制御（OikomiStartを自動付加しない）のため排除処理を行う -->
      <xsl:call-template name="Taisen_SetNoClass_UTL">
        <xsl:with-param name="Data" select="$MatchData"/>
      </xsl:call-template>
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
    <!--対戦成績-->
    <xsl:variable name="UpperPlayersOutcomeMakuuchiTsusan">
      <xsl:if test="$FLG_OUTCOME_TSUSAN = 1">
        <xsl:value-of select="Player[1]/Result/Result[@Period='幕内通算']/ResultForSumo/SumoOutcomeTotal/Writing"/>
      </xsl:if>
    </xsl:variable>
    <xsl:variable name="UpperPlayerName">
      <xsl:choose>
        <!--パターン「1」-->
        <xsl:when test="$OS13_OS14_PLAYERNAME_DISPLAY_SET = 1">
          <!--対戦成績-->
          <xsl:value-of select="$UpperPlayersOutcomeMakuuchiTsusan"/>
          <xsl:call-template name="PrintSpaceZenkaku_UTL">
            <xsl:with-param name="count" select="1 - string-length($UpperPlayersOutcomeMakuuchiTsusan)"/>
          </xsl:call-template>
          <!--力士名-->
          <xsl:value-of select="Player[1]/PlayerName/Formal[@Display='3字']"/>
          <xsl:variable name="tmpArea">
            <xsl:value-of select="Player[1]/PlayerForSumo/NativeCountry/Writing"/>
            <xsl:value-of select="Player[1]/PlayerForSumo/NativeArea/Writing"/>
            <xsl:value-of select="Player[1]/PlayerForSumo/NativeCity/Writing"/>
          </xsl:variable>
          <xsl:value-of select="$WhiteSpaceZenkaku_UTL"/>
          <xsl:value-of select="$LineFeed_UTL"/>
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
                  <xsl:with-param name="Outcome" select="$UpperPlayersOutcomeMakuuchiTsusan"/>
                  <xsl:with-param name="Data" select="Player[1]/PlayerName/Formal[@Display='3字']"/>
                  <xsl:with-param name="Length" select="$UpperPlayerAreaLength"/>
                </xsl:call-template>
              </xsl:when>
              <xsl:otherwise>
                <xsl:call-template name="AddSpaceForTaisen_KAKUNIN_OSCOM2">
                  <xsl:with-param name="Outcome" select="$UpperPlayersOutcomeMakuuchiTsusan"/>
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
      <!--今場所成績-->
      <xsl:if test="$FLG_OUTCOME_KONBASHO = 1">
        <xsl:call-template name="AddBR_KAKUNIN_OSCOM2">
          <xsl:with-param name="Data" select="concat($WhiteSpaceZenkaku_UTL, Player[1]/Result/Result[@Period='今場所']/ResultForSumo/SumoOutcomeTotal/Writing)"/>
          <xsl:with-param name="Length" select="$UpperPlayerAreaLength"/>
          <xsl:with-param name="LeftOrRight" select="1"/>
          <xsl:with-param name="KakkoHamidashiFlg" select="0"/>
        </xsl:call-template>
      </xsl:if>
    </xsl:variable>
    <!--=====決まり手=====-->
    <xsl:variable name="tmpWinningTrick" select="MatchDetail/WinningTrick/Formal[not(@*)]"/>
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
      <!--決まり手の７字取り処理-->
      <xsl:call-template name="AddBRandSpaceToWinningTrick_OSCOM2">
        <xsl:with-param name="PLAYER_INFO_1" select="$UpperPlayerName"/>
        <xsl:with-param name="WINNING_TRICK" select="$tmpWinningTrick"/>
        <xsl:with-param name="PLAYER1_AREA_LENGTH" select="$UpperPlayerAreaLength"/>
        <xsl:with-param name="WINNING_TRICK_LENGTH" select="$lengthWinningTrick"/>
        <xsl:with-param name="RESULT_AREA_LENGTH" select="$ResultAreaLength"/>
        <xsl:with-param name="RESULT_AREA_OVERFLOWED" select="$ResultAreaOverflowed"/>
      </xsl:call-template>
      <!--時間-->
      <xsl:if test="MatchDetail/ClosingInfo/ClosingTime/Writing and $FLG_CLOSINGTIME = 1">
        <xsl:text>（</xsl:text>
        <xsl:value-of select="MatchDetail/ClosingInfo/ClosingTime/Writing"/>
        <xsl:text>）</xsl:text>
        <xsl:value-of select="$LineFeed_UTL"/>
      </xsl:if>
    </xsl:variable>
    <!--=====下段（右）力士=====-->
    <!--対戦成績-->
    <xsl:variable name="LowerPlayersOutcomeMakuuchiTsusan">
      <xsl:if test="$FLG_OUTCOME_TSUSAN = 1">
        <xsl:value-of select="Player[2]/Result/Result[@Period='幕内通算']/ResultForSumo/SumoOutcomeTotal/Writing"/>
      </xsl:if>
    </xsl:variable>
    <xsl:variable name="LowerPlayerName">
      <xsl:choose>
        <!--パターン「1」-->
        <xsl:when test="$OS13_OS14_PLAYERNAME_DISPLAY_SET = 1">
          <!--力士名-->
          <xsl:value-of select="Player[2]/PlayerName/Formal[@Display='3字']"/>
          <!--対戦成績-->
          <xsl:value-of select="$LowerPlayersOutcomeMakuuchiTsusan"/>
          <xsl:value-of select="$LineFeed_UTL"/>
        </xsl:when>
        <!--パターン「2」-->
        <xsl:otherwise>
          <!--力士名、対戦成績-->
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
            <!--対戦成績-->
            <xsl:value-of select="$LowerPlayersOutcomeMakuuchiTsusan"/>
          </xsl:variable>
          <xsl:call-template name="AddBR_KAKUNIN_OSCOM2">
            <xsl:with-param name="Data" select="$tmpPlayerNameAndGrade"/>
            <xsl:with-param name="Length" select="$LowerPlayerAreaLength"/>
            <xsl:with-param name="LeftOrRight" select="2"/>
            <xsl:with-param name="KakkoHamidashiFlg" select="0"/>
          </xsl:call-template>
        </xsl:otherwise>
      </xsl:choose>
      <!--今場所成績-->
      <xsl:if test="$FLG_OUTCOME_KONBASHO = 1">
        <xsl:call-template name="AddBR_KAKUNIN_OSCOM2">
          <xsl:with-param name="Data" select="Player[2]/Result/Result[@Period='今場所']/ResultForSumo/SumoOutcomeTotal/Writing"/>
          <xsl:with-param name="Length" select="$UpperPlayerAreaLength"/>
          <xsl:with-param name="LeftOrRight" select="1"/>
          <xsl:with-param name="KakkoHamidashiFlg" select="0"/>
        </xsl:call-template>
      </xsl:if>
    </xsl:variable>
    <!--=====表示=====-->
    <xsl:value-of select="$MatchClass_UTL"/>
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
    <xsl:call-template name="PrintSpaceZenkaku_UTL">
      <xsl:with-param name="count" select="$UpperPlayerAreaLength"/>
    </xsl:call-template>
    <xsl:value-of select="$BodyMeta/Title"/>
    <xsl:value-of select="$LineFeed_UTL"/>
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
        <xsl:when test="$OS13_OS14_PLAYERNAME_DISPLAY_SET = 1">
          <xsl:for-each select="//Match/Player[1]/PlayerName/Formal[@Display='3字']">
            <xsl:call-template name="Gaiji_EDT"/>
          </xsl:for-each>
        </xsl:when>
        <xsl:when test="$OS13_OS14_PLAYERNAME_DISPLAY_SET = 2">
          <xsl:for-each select="//Match/Player[1]/PlayerName/Formal[not(@*)]">
            <xsl:call-template name="Gaiji_EDT"/>
          </xsl:for-each>
        </xsl:when>
        <xsl:otherwise/>
      </xsl:choose>
      <!--=====下段=====-->
      <!--力士名-->
      <xsl:choose>
        <xsl:when test="$OS13_OS14_PLAYERNAME_DISPLAY_SET = 1">
          <xsl:for-each select="//Match/Player[2]/PlayerName/Formal[@Display='3字']">
            <xsl:call-template name="Gaiji_EDT"/>
          </xsl:for-each>
        </xsl:when>
        <xsl:when test="$OS13_OS14_PLAYERNAME_DISPLAY_SET = 2">
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
