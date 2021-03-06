<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">
  <!-- ================================================================================= -->
  <!--　編集者用「共通スタイルシート」大相撲・郷土力士勝負（階級別） -->
  <!--  4.0版 2015.06.30 プレーンテキスト版のプレーンテキスト表示用として新規公開 -->
  <!--  4.01版 2015.●.● pタグのMatchStartクラス（対戦開始情報）を追加 -->
  <!--                    pタグのOikomiStartクラス（追い込み開始情報）を追加 -->
  <!-- ================================================================================= -->
  <!-- =================================== 変数定義 ==================================== -->
  <!-- ================================================================================= -->
  <!--【commonsetting定義】-->
  <!-- ================================================================================= -->
  <!-- 縦書き/横書き設定 -->
  <xsl:variable name="PTEXT_TATEYOKO_KYODORIKISHI_TAISEN_SET">
    <xsl:call-template name="PTEXT_TATEYOKO_OS10_OS11_SET"/>
  </xsl:variable>
  <!-- 選手名表示切替 -->
  <xsl:variable name="KYODORIKISHI_TAISEN_PLAYERNAME_DISPLAY_SET">
    <xsl:call-template name="OS10_OS11_PLAYERNAME_DISPLAY_SET"/>
  </xsl:variable>
  <!-- 対戦型　最大折り返し文字数定義-->
  <xsl:variable name="PRINT_MAXTEXT_FLG_KYODORIKISHI_TAISEN_SET">
    <xsl:call-template name="PRINT_MAXTEXT_FLG_OS10_OS11_SET"/>
  </xsl:variable>
  <xsl:variable name="PRINT_MAXTEXT_KYODORIKISHI_TAISEN_SET">
    <xsl:call-template name="PRINT_MAXTEXT_OS10_OS11_SET"/>
  </xsl:variable>
  <!--決まり手の表示、非表示-->
  <xsl:variable name="FLG_WINNINGTRICK">
    <!--郷土力士取組では、この設定値に関わらず固定文字「―」となる-->
    <xsl:call-template name="OS10_OS11_WINNINGTRICK_DISPLAY_SET"/>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- 縦書き/横書き設定 -->
  <!-- ================================================================================= -->
  <xsl:variable name="KYODORIKISHI_TAISEN_PTEXT_TATEYOKO">
    <xsl:choose>
      <xsl:when test="$PTEXT_TATEYOKO_KYODORIKISHI_TAISEN_SET=0">
        <!-- 共通設定を適用 -->
        <xsl:value-of select="$PTEXT_TATEYOKO_SET"/>
      </xsl:when>
      <xsl:otherwise>
        <!-- 個別設定を適用 -->
        <xsl:value-of select="$PTEXT_TATEYOKO_KYODORIKISHI_TAISEN_SET"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- １ページ最大行数を取得 -->
  <!-- 判断条件は「印刷方向定義」「縦書き/横書き設定」 -->
  <!-- ================================================================================= -->
  <xsl:variable name="KYODORIKISHI_TAISEN_PRINT_MAXLINE">
    <xsl:choose>
      <!--Ａ４タテ印刷-->
      <xsl:when test="$PRINT_F_SET=1">
        <xsl:choose>
          <xsl:when test="$KYODORIKISHI_TAISEN_PTEXT_TATEYOKO=1">
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
          <xsl:when test="$KYODORIKISHI_TAISEN_PTEXT_TATEYOKO=1">
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
  <xsl:variable name="KYODORIKISHI_TAISEN_MAXLENGTH">
    <xsl:variable name="NUM_CHECK">
      <xsl:choose>
        <xsl:when test="$PRINT_MAXTEXT_FLG_KYODORIKISHI_TAISEN_SET=1">
          <!-- 個別定義が有効な場合 -->
          <xsl:value-of select="$PRINT_MAXTEXT_KYODORIKISHI_TAISEN_SET"/>
        </xsl:when>
        <xsl:otherwise>
          <!-- 個別定義が無効な場合、共通定義を取得 -->
          <xsl:choose>
            <!--Ａ４タテ印刷-->
            <xsl:when test="$PRINT_F_SET=1">
              <xsl:choose>
                <xsl:when test="$KYODORIKISHI_TAISEN_PTEXT_TATEYOKO=1">
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
                <xsl:when test="$KYODORIKISHI_TAISEN_PTEXT_TATEYOKO=1">
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
      <!--縦書きの最大値（25字以上ではフォーマットが崩れる）-->
      <xsl:when test="$NUM_CHECK &gt; 23 and $KYODORIKISHI_TAISEN_PTEXT_TATEYOKO=1">
        <xsl:value-of select="23"/>
      </xsl:when>
      <!--偶数が設定された場合-->
      <xsl:when test="$NUM_CHECK mod 2 = 0">
        <xsl:value-of select="$NUM_CHECK -1"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="$NUM_CHECK"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- １行最大折り返し文字数を取得（対戦表示以外） -->
  <!-- ================================================================================= -->
  <xsl:variable name="KYODORIKISHI_TAISEN_PRINT_MAXLENGTH">
    <xsl:choose>
      <xsl:when test="$KYODORIKISHI_TAISEN_PTEXT_TATEYOKO=1">
        <!-- 縦書き -->
        <xsl:value-of select="$KYODORIKISHI_TAISEN_MAXLENGTH"/>
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
  <!--上段（左）の力士名と出身地の折り返し文字数-->
  <xsl:variable name="UpperPlayerAreaLength">
    <xsl:choose>
      <xsl:when test="$KYODORIKISHI_TAISEN_PLAYERNAME_DISPLAY_SET = 1">
        <!--力士名３字-->
        <xsl:value-of select="3"/>
      </xsl:when>
      <xsl:when test="$KYODORIKISHI_TAISEN_PLAYERNAME_DISPLAY_SET = 2">
        <!--力士名４字＋勝敗記号１字-->
        <xsl:value-of select="5"/>
      </xsl:when>
      <xsl:when test="$KYODORIKISHI_TAISEN_PLAYERNAME_DISPLAY_SET = 3">
        <!--力士名５字＋勝敗記号１字-->
        <xsl:value-of select="6"/>
      </xsl:when>
      <xsl:otherwise/>
    </xsl:choose>
  </xsl:variable>
  <!--下段（右）の力士名と出身地の折り返し文字数。階級を表示する場合の文字数も含める-->
  <xsl:variable name="LowerPlayerAreaLength">
    <xsl:choose>
      <xsl:when test="$KYODORIKISHI_TAISEN_PLAYERNAME_DISPLAY_SET = 1">
        <!--力士名３字＋括弧２字＋出身地２字＋階級３字-->
        <xsl:value-of select="10"/>
      </xsl:when>
      <xsl:when test="$KYODORIKISHI_TAISEN_PLAYERNAME_DISPLAY_SET = 2">
        <!--力士名３字＋空白１字＋階級３字-->
        <xsl:value-of select="7"/>
      </xsl:when>
      <xsl:when test="$KYODORIKISHI_TAISEN_PLAYERNAME_DISPLAY_SET = 3">
        <xsl:choose>
          <!--力士名５字＋空白１字＋階級３字（最小値）-->
          <xsl:when test="$KYODORIKISHI_TAISEN_MAXLENGTH - $UpperPlayerAreaLength - $ResultAreaLength &lt; 9">
            <xsl:value-of select="9"/>
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="$KYODORIKISHI_TAISEN_MAXLENGTH - $UpperPlayerAreaLength - $ResultAreaLength"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:when>
      <xsl:otherwise/>
    </xsl:choose>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- 記録エリア編集文字数。半角１文字以上 -->
  <!-- ================================================================================= -->
  <xsl:variable name="ResultAreaLength">
    <xsl:choose>
      <xsl:when test="not(//MatchDetail/WinningTrick)">
        <!--郷土力士取組は、決まり手がないので「―　」で固定-->
        <xsl:value-of select="2"/>
      </xsl:when>
      <xsl:when test="$FLG_WINNINGTRICK = 0">
        <!--郷土力士勝負で、決まり手の非表示を選択した場合。「―　」で固定-->
        <xsl:value-of select="2"/>
      </xsl:when>
      <xsl:otherwise>
        <!--郷土力士勝負で、決まり手の表示を選択した場合-->
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
      <xsl:with-param name="LINE_MAX_LENGTH" select="$UpperPlayerAreaLength + $ResultAreaLength + $LowerPlayerAreaLength +1"/>
      <xsl:with-param name="PAGE_LINE_MAX" select="$KYODORIKISHI_TAISEN_PRINT_MAXLINE"/>
      <xsl:with-param name="ADD_LINE_COUNT_FLG" select="$ADD_LINE_COUNT_FLG_SET"/>
      <xsl:with-param name="TATEYOKO_FLG" select="$KYODORIKISHI_TAISEN_PTEXT_TATEYOKO"/>
      <xsl:with-param name="ADD_OIKOMI_CLASS_FLG" select="1"/>
    </xsl:call-template>
  </xsl:template>
  <!-- ================================================================================= -->
  <!-- 本文要素（SportsData）-->
  <!-- ================================================================================= -->
  <xsl:template name="KAKUNIN_TEXT">
    <!--郷土力士対戦（取組または勝負）編集-->
    <xsl:call-template name="KyodorikishiTaisen_KAKUNIN2"/>
    <!--本文内注釈編集（SportsDataと同階層）-->
    <xsl:apply-templates select="../TextNote" mode="KAKUNIN2_EDT"/>
  </xsl:template>
  <!-- ================================================================================= -->
  <!-- ボディ（Body）-->
  <!-- ================================================================================= -->
  <xsl:template name="KyodorikishiTaisen_KAKUNIN2">
    <!--Bodyタグを編集-->
    <xsl:for-each select="Body">
      <!--Title-->
      <xsl:for-each select="Meta/Title">
        <xsl:value-of select="."/>
        <xsl:value-of select="$LineFeed_UTL"/>
      </xsl:for-each>
      <!--Article-->
      <xsl:if test="Article/Paragraph">
        <xsl:value-of select="$WhiteSpaceZenkaku_UTL"/>
        <xsl:value-of select="Article/Paragraph"/>
        <xsl:value-of select="$LineFeed_UTL"/>
      </xsl:if>
      <!--Match-->
      <xsl:variable name="MatchData">
        <xsl:apply-templates select="Match" mode="KyodorikishiTaisen_KAKUNIN2"/>
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
  <xsl:template match="Match" mode="KyodorikishiTaisen_KAKUNIN2">
    <!--「1」上段の力士名は３字＋出身地は表記なし。下段の力士名は３字＋出身地は２字-->
    <!--「2」上段の力士名は４字＋出身地は３字。　　下段の力士名は３字＋出身地は２字-->
    <!--「3」上段の力士名は正式名＋出身地は正式名。下段の力士名は正式名＋出身地は正式名-->
    <!--=====上段（左）力士=====-->
    <xsl:variable name="UpperPlayerName">
      <!--勝敗-->
      <xsl:variable name="Outcome">
        <xsl:value-of select="MatchDetail/MatchResult[1]/Outcome/Writing"/>
      </xsl:variable>
      <!--力士名、勝敗-->
      <xsl:choose>
        <!--パターン「1」-->
        <xsl:when test="$KYODORIKISHI_TAISEN_PLAYERNAME_DISPLAY_SET = 1">
          <!--勝敗-->
          <xsl:value-of select="$Outcome"/>
          <xsl:call-template name="PrintSpaceZenkaku_UTL">
            <xsl:with-param name="count" select="1 - string-length($Outcome)"/>
          </xsl:call-template>
          <!--力士名-->
          <xsl:value-of select="Player[1]/PlayerName/Formal[@Display='3字']"/>
        </xsl:when>
        <!--パターン「2」「3」-->
        <xsl:otherwise>
          <xsl:variable name="tmpPlayerName">
            <xsl:if test="$KYODORIKISHI_TAISEN_PLAYERNAME_DISPLAY_SET = 2">
              <xsl:call-template name="AddSpaceForTaisen_KAKUNIN_OSCOM2">
                <xsl:with-param name="Outcome" select="$Outcome"/>
                <xsl:with-param name="Data" select="Player[1]/PlayerName/Formal[@Display='4字']"/>
                <xsl:with-param name="Length" select="5"/>
              </xsl:call-template>
            </xsl:if>
            <xsl:if test="$KYODORIKISHI_TAISEN_PLAYERNAME_DISPLAY_SET = 3">
              <xsl:choose>
                <!--３字以下の場合には字取りするため、３字を使用-->
                <xsl:when test="string-length(Player[1]/PlayerName/Formal[not(@*)]) &lt;= 3
                              and Player[1]/PlayerName/Formal[@Display='3字']">
                  <xsl:call-template name="AddSpaceForTaisen_KAKUNIN_OSCOM2">
                    <xsl:with-param name="Outcome" select="$Outcome"/>
                    <xsl:with-param name="Data" select="Player[1]/PlayerName/Formal[@Display='3字']"/>
                    <xsl:with-param name="Length" select="$UpperPlayerAreaLength"/>
                  </xsl:call-template>
                </xsl:when>
                <xsl:otherwise>
                  <xsl:call-template name="AddSpaceForTaisen_KAKUNIN_OSCOM2">
                    <xsl:with-param name="Outcome" select="$Outcome"/>
                    <xsl:with-param name="Data" select="Player[1]/PlayerName/Formal[not(@*)]"/>
                    <xsl:with-param name="Length" select="$UpperPlayerAreaLength"/>
                  </xsl:call-template>
                </xsl:otherwise>
              </xsl:choose>
            </xsl:if>
          </xsl:variable>
          <xsl:call-template name="AddBR_KAKUNIN_OSCOM2">
            <xsl:with-param name="Data" select="$tmpPlayerName"/>
            <xsl:with-param name="Length" select="$UpperPlayerAreaLength"/>
            <xsl:with-param name="LeftOrRight" select="1"/>
            <xsl:with-param name="KakkoHamidashiFlg" select="0"/>
          </xsl:call-template>
        </xsl:otherwise>
      </xsl:choose>
      <!--出身地-->
      <xsl:choose>
        <!--パターン「1」-->
        <xsl:when test="$KYODORIKISHI_TAISEN_PLAYERNAME_DISPLAY_SET = 1"/>
        <!--パターン「2」「3」-->
        <xsl:otherwise>
          <xsl:variable name="tmpKakkoAndArea">
            <xsl:variable name="tmpArea">
              <xsl:if test="$KYODORIKISHI_TAISEN_PLAYERNAME_DISPLAY_SET = 2">
                <xsl:value-of select="Player[1]/PlayerForSumo/NativeCity/Formal[@Display='3字']"/>
              </xsl:if>
              <xsl:if test="$KYODORIKISHI_TAISEN_PLAYERNAME_DISPLAY_SET = 3">
                <xsl:choose>
                  <!--３字以下の場合には字取りするため、３字を使用-->
                  <xsl:when test="string-length(Player[1]/PlayerForSumo/NativeCity/Formal[not(@*)]) &lt;=3
                                and Player[1]/PlayerForSumo/NativeCity/Formal[@Display='3字']">
                    <xsl:value-of select="Player[1]/PlayerForSumo/NativeCity/Formal[@Display='3字']"/>
                  </xsl:when>
                  <xsl:otherwise>
                    <xsl:value-of select="Player[1]/PlayerForSumo/NativeCity/Formal[not(@*)]"/>
                  </xsl:otherwise>
                </xsl:choose>
              </xsl:if>
            </xsl:variable>
            <xsl:if test="string-length($tmpArea)!=0">
              <xsl:call-template name="AddSpaceForTaisen_KAKUNIN_OSCOM2">
                <xsl:with-param name="Data" select="concat('（',$tmpArea,'）')"/>
                <xsl:with-param name="Length" select="$UpperPlayerAreaLength"/>
              </xsl:call-template>
            </xsl:if>
          </xsl:variable>
          <xsl:call-template name="AddBR_KAKUNIN_OSCOM2">
            <xsl:with-param name="Data" select="$tmpKakkoAndArea"/>
            <xsl:with-param name="Length" select="$UpperPlayerAreaLength"/>
            <xsl:with-param name="LeftOrRight" select="1"/>
            <xsl:with-param name="KakkoHamidashiFlg" select="1"/>
          </xsl:call-template>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <!--=====決まり手=====-->
    <xsl:variable name="tmpWinningTrick">
      <xsl:choose>
        <xsl:when test="$FLG_WINNINGTRICK = 0 or not(//MatchDetail/WinningTrick)">
          <xsl:text>―</xsl:text>
        </xsl:when>
        <xsl:otherwise>
          <xsl:choose>
            <!--パターン「1」「2」-->
            <xsl:when test="$KYODORIKISHI_TAISEN_PLAYERNAME_DISPLAY_SET = 1 or $KYODORIKISHI_TAISEN_PLAYERNAME_DISPLAY_SET = 2">
              <xsl:value-of select="MatchDetail/WinningTrick/Formal[@Display='5字']"/>
            </xsl:when>
            <!--パターン「3」-->
            <xsl:otherwise>
              <xsl:value-of select="MatchDetail/WinningTrick/Formal[not(@*)]"/>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <xsl:variable name="lengthWinningTrick" select="string-length($tmpWinningTrick)"/>
    <!-- 上段力士名エリアへのはみ出し部分-->
    <xsl:variable name="ResultAreaOverflowed">
      <!--決まり手が７字で、上段力士の１行目の最後の文字が空白の場合は、１字はみ出し処理する-->
      <xsl:if test="$FLG_WINNINGTRICK = 1
                  and $lengthWinningTrick = $ResultAreaLength +1
                  and (substring($UpperPlayerName, $UpperPlayerAreaLength, 1) = '　'
                    or substring($UpperPlayerName, $UpperPlayerAreaLength, 1) = $WhiteSpaceZenkaku_UTL)">
        <xsl:value-of select="substring($tmpWinningTrick, 1, 1)"/>
      </xsl:if>
    </xsl:variable>
    <!--====決まり手エリア=====-->
    <xsl:variable name="ResultAreaInfo">
      <xsl:choose>
        <!--パターン「1」または取組-->
        <xsl:when test="$KYODORIKISHI_TAISEN_PLAYERNAME_DISPLAY_SET = 1 or not(//MatchDetail/WinningTrick) or $FLG_WINNINGTRICK = 0">
          <xsl:value-of select="$tmpWinningTrick"/>
        </xsl:when>
        <!--パターン「2」「3」-->
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
    <!--異なる階級の力士と対戦する場合は相手の階級を表示-->
    <xsl:variable name="LowerPlayersSumoRank">
      <xsl:if test="Player[2]/PlayerForSumo/SumoGrade/Writing">
        <xsl:value-of select="Player[2]/PlayerForSumo/SumoGrade/SumoRank"/>
      </xsl:if>
    </xsl:variable>
    <xsl:variable name="LowerPlayerName">
      <!--力士名-->
      <xsl:choose>
        <!--パターン「1」-->
        <xsl:when test="$KYODORIKISHI_TAISEN_PLAYERNAME_DISPLAY_SET = 1">
          <xsl:value-of select="Player[2]/PlayerName/Formal[@Display='3字']"/>
        </xsl:when>
        <!--パターン「2」「3」-->
        <xsl:otherwise>
          <xsl:variable name="tmpPlayerNameAndGrade">
            <xsl:variable name="tmpPlayerName">
              <xsl:if test="$KYODORIKISHI_TAISEN_PLAYERNAME_DISPLAY_SET = 2">
                <xsl:value-of select="Player[2]/PlayerName/Formal[@Display='3字']"/>
              </xsl:if>
              <xsl:if test="$KYODORIKISHI_TAISEN_PLAYERNAME_DISPLAY_SET = 3">
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
              </xsl:if>
            </xsl:variable>
            <xsl:value-of select="$tmpPlayerName"/>
            <!--階級-->
            <xsl:if test="$LowerPlayersSumoRank != ''">
              <xsl:value-of select="$WhiteSpaceZenkaku_UTL"/>
              <xsl:value-of select="$LowerPlayersSumoRank"/>
            </xsl:if>
          </xsl:variable>
          <xsl:call-template name="AddBR_KAKUNIN_OSCOM2">
            <xsl:with-param name="Data" select="$tmpPlayerNameAndGrade"/>
            <xsl:with-param name="Length" select="$LowerPlayerAreaLength"/>
            <xsl:with-param name="LeftOrRight" select="2"/>
            <xsl:with-param name="KakkoHamidashiFlg" select="0"/>
          </xsl:call-template>
        </xsl:otherwise>
      </xsl:choose>
      <!--出身地-->
      <xsl:choose>
        <!--パターン「1」-->
        <xsl:when test="$KYODORIKISHI_TAISEN_PLAYERNAME_DISPLAY_SET = 1">
          <xsl:variable name="tmpArea">
            <xsl:value-of select="Player[2]/PlayerForSumo/NativeCountry/Writing"/>
            <xsl:value-of select="Player[2]/PlayerForSumo/NativeArea/Writing"/>
            <xsl:value-of select="Player[2]/PlayerForSumo/NativeCity/Writing"/>
          </xsl:variable>
          <xsl:if test="string-length($tmpArea)!=0">
            <xsl:value-of select="concat('（',$tmpArea,'）')"/>
          </xsl:if>
        </xsl:when>
        <!--パターン「2」「3」-->
        <xsl:otherwise>
          <xsl:variable name="tmpKakkoAndArea">
            <xsl:variable name="tmpArea">
              <xsl:if test="$KYODORIKISHI_TAISEN_PLAYERNAME_DISPLAY_SET = 2">
                <xsl:value-of select="concat(
                  Player[2]/PlayerForSumo/NativeCountry/Writing,
                  Player[2]/PlayerForSumo/NativeArea/Writing,
                  Player[2]/PlayerForSumo/NativeCity/Writing
                )"/>
              </xsl:if>
              <xsl:if test="$KYODORIKISHI_TAISEN_PLAYERNAME_DISPLAY_SET = 3">
                <xsl:value-of select="Player[2]/PlayerForSumo/NativeCountry/Formal[not(@*)]"/>
                <xsl:value-of select="Player[2]/PlayerForSumo/NativeArea/Formal[not(@*)]"/>
                <xsl:if test="
                  (Player[2]/PlayerForSumo/NativeCountry/Formal[not(@*)]
                  or Player[2]/PlayerForSumo/NativeArea/Formal[not(@*)])
                  and Player[2]/PlayerForSumo/NativeCity/Formal[not(@*)]">
                  <xsl:text>・</xsl:text>
                </xsl:if>
                <xsl:value-of select="Player[2]/PlayerForSumo/NativeCity/Formal[not(@*)]"/>
              </xsl:if>
            </xsl:variable>
            <xsl:if test="string-length($tmpArea)!=0">
              <xsl:value-of select="concat('（',$tmpArea,'）')"/>
            </xsl:if>
          </xsl:variable>
          <xsl:call-template name="AddBR_KAKUNIN_OSCOM2">
            <xsl:with-param name="Data" select="$tmpKakkoAndArea"/>
            <xsl:with-param name="Length" select="$LowerPlayerAreaLength"/>
            <xsl:with-param name="LeftOrRight" select="2"/>
            <xsl:with-param name="KakkoHamidashiFlg" select="1"/>
          </xsl:call-template>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <!--=====表示=====-->
    <xsl:value-of select="$MatchClass_UTL"/>
    <xsl:choose>
      <!--パターン「1」-->
      <xsl:when test="$KYODORIKISHI_TAISEN_PLAYERNAME_DISPLAY_SET = 1">
        <xsl:value-of select="$UpperPlayerName"/>
        <xsl:value-of select="$ResultAreaInfo"/>
        <xsl:value-of select="$LowerPlayerName"/>
        <!--異なる階級の力士と対戦する場合は相手の階級を表示-->
        <xsl:value-of select="$LowerPlayersSumoRank"/>
        <xsl:value-of select="$LineFeed_UTL"/>
      </xsl:when>
      <!--パターン「2」「3」-->
      <xsl:otherwise>
        <xsl:call-template name="TaisenLayout_TORIKUMI_OSCOM">
          <xsl:with-param name="PLAYER_INFO_1" select="$UpperPlayerName"/>
          <xsl:with-param name="PLAYER_INFO_2" select="$LowerPlayerName"/>
          <xsl:with-param name="RESULT_AREA_OVERFLOWED" select="$ResultAreaOverflowed"/>
          <xsl:with-param name="RESULT_AREA_INFO" select="$ResultAreaInfo"/>
          <xsl:with-param name="PLAYER1_AREA_LENGTH" select="$UpperPlayerAreaLength"/>
          <xsl:with-param name="PLAYER2_AREA_LENGTH" select="$LowerPlayerAreaLength"/>
          <xsl:with-param name="RESULT_AREA_LENGTH" select="$ResultAreaLength"/>
        </xsl:call-template>
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
        <xsl:when test="$KYODORIKISHI_TAISEN_PLAYERNAME_DISPLAY_SET = 1">
          <xsl:for-each select="//Match/Player[1]/PlayerName/Formal[@Display='3字']">
            <xsl:call-template name="Gaiji_EDT"/>
          </xsl:for-each>
        </xsl:when>
        <xsl:when test="$KYODORIKISHI_TAISEN_PLAYERNAME_DISPLAY_SET = 2">
          <xsl:for-each select="//Match/Player[1]/PlayerName/Formal[@Display='4字']">
            <xsl:call-template name="Gaiji_EDT"/>
          </xsl:for-each>
        </xsl:when>
        <xsl:otherwise>
          <xsl:for-each select="//Match/Player[1]/PlayerName/Formal[not(@*)]">
            <xsl:call-template name="Gaiji_EDT"/>
          </xsl:for-each>
        </xsl:otherwise>
      </xsl:choose>
      <!--出身地-->
      <xsl:choose>
        <xsl:when test="$KYODORIKISHI_TAISEN_PLAYERNAME_DISPLAY_SET = 1">
        </xsl:when>
        <xsl:when test="$KYODORIKISHI_TAISEN_PLAYERNAME_DISPLAY_SET = 2">
          <xsl:for-each select="//Match/Player[1]/PlayerForSumo/NativeCity/Formal[@Display='3字']">
            <xsl:call-template name="Gaiji_EDT"/>
          </xsl:for-each>
        </xsl:when>
        <xsl:otherwise>
          <xsl:for-each select="//Match/Player[1]/PlayerForSumo/NativeCity/Formal[not(@*)]">
            <xsl:call-template name="Gaiji_EDT"/>
          </xsl:for-each>
        </xsl:otherwise>
      </xsl:choose>
      <!--=====下段=====-->
      <!--力士名-->
      <xsl:choose>
        <xsl:when test="$KYODORIKISHI_TAISEN_PLAYERNAME_DISPLAY_SET = 1 or $KYODORIKISHI_TAISEN_PLAYERNAME_DISPLAY_SET = 2">
          <xsl:for-each select="//Match/Player[2]/PlayerName/Formal[@Display='3字']">
            <xsl:call-template name="Gaiji_EDT"/>
          </xsl:for-each>
        </xsl:when>
        <xsl:otherwise>
          <xsl:for-each select="//Match/Player[2]/PlayerName/Formal[not(@*)]">
            <xsl:call-template name="Gaiji_EDT"/>
          </xsl:for-each>
        </xsl:otherwise>
      </xsl:choose>
      <!--出身地-->
      <xsl:choose>
        <xsl:when test="$KYODORIKISHI_TAISEN_PLAYERNAME_DISPLAY_SET = 1 or $KYODORIKISHI_TAISEN_PLAYERNAME_DISPLAY_SET = 2">
          <xsl:for-each select="//Match/Player[2]/PlayerForSumo/NativeCity/Writing">
            <xsl:call-template name="Gaiji_EDT"/>
          </xsl:for-each>
        </xsl:when>
        <xsl:otherwise>
          <xsl:for-each select="//Match/Player[2]/PlayerForSumo/NativeCity/Formal[not(@*)]">
            <xsl:call-template name="Gaiji_EDT"/>
          </xsl:for-each>
        </xsl:otherwise>
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
