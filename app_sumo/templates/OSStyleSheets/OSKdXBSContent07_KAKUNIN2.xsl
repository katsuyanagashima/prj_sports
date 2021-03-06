<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">
  <!-- ================================================================================= -->
  <!--　編集者用「共通スタイルシート」大相撲・幕下以下取組 -->
  <!--  4.0版 2015.06.30 プレーンテキスト版のプレーンテキスト表示用として新規公開 -->
  <!--  4.01版 2015.●.● pタグのMatchStartクラス（対戦開始情報）を追加 -->
  <!--                    pタグのOikomiStartクラス（追い込み開始情報）を追加 -->
  <!-- ================================================================================= -->
  <!-- =================================== 変数定義 ==================================== -->
  <!-- ================================================================================= -->
  <!--【commonsetting定義】-->
  <!-- ================================================================================= -->
  <!-- 縦書き/横書き設定 -->
  <xsl:variable name="PTEXT_TATEYOKO_OS07_SET">
    <xsl:call-template name="PTEXT_TATEYOKO_OS07_SET"/>
  </xsl:variable>
  <!-- 選手名表示切替 -->
  <xsl:variable name="OS07_PLAYERNAME_DISPLAY_SET">
    <xsl:call-template name="OS07_PLAYERNAME_DISPLAY_SET"/>
  </xsl:variable>
  <!-- 対戦型　最大折り返し文字数定義-->
  <xsl:variable name="PRINT_MAXTEXT_FLG_OS07_SET">
    <xsl:call-template name="PRINT_MAXTEXT_FLG_OS07_SET"/>
  </xsl:variable>
  <xsl:variable name="PRINT_MAXTEXT_OS07_SET">
    <xsl:call-template name="PRINT_MAXTEXT_OS07_SET"/>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- 縦書き/横書き設定 -->
  <!-- ================================================================================= -->
  <xsl:variable name="OS07_PTEXT_TATEYOKO">
    <xsl:choose>
      <xsl:when test="$PTEXT_TATEYOKO_OS07_SET=0">
        <!-- 共通設定を適用 -->
        <xsl:value-of select="$PTEXT_TATEYOKO_SET"/>
      </xsl:when>
      <xsl:otherwise>
        <!-- 個別設定を適用 -->
        <xsl:value-of select="$PTEXT_TATEYOKO_OS07_SET"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- １ページ最大行数を取得 -->
  <!-- 判断条件は「印刷方向定義」「縦書き/横書き設定」 -->
  <!-- ================================================================================= -->
  <xsl:variable name="OS07_PRINT_MAXLINE">
    <xsl:choose>
      <!--Ａ４タテ印刷-->
      <xsl:when test="$PRINT_F_SET=1">
        <xsl:choose>
          <xsl:when test="$OS07_PTEXT_TATEYOKO=1">
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
          <xsl:when test="$OS07_PTEXT_TATEYOKO=1">
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
  <xsl:variable name="OS07_MAXLENGTH">
    <xsl:variable name="NUM_CHECK">
      <xsl:choose>
        <xsl:when test="$PRINT_MAXTEXT_FLG_OS07_SET=1">
          <!-- 個別定義が有効な場合 -->
          <xsl:value-of select="$PRINT_MAXTEXT_OS07_SET"/>
        </xsl:when>
        <xsl:otherwise>
          <!-- 個別定義が無効な場合、共通定義を取得 -->
          <xsl:choose>
            <!--Ａ４タテ印刷-->
            <xsl:when test="$PRINT_F_SET=1">
              <xsl:choose>
                <xsl:when test="$OS07_PTEXT_TATEYOKO=1">
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
                <xsl:when test="$OS07_PTEXT_TATEYOKO=1">
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
  <xsl:variable name="OS07_PRINT_MAXLENGTH">
    <xsl:choose>
      <xsl:when test="$OS07_PTEXT_TATEYOKO=1">
        <!-- 縦書き -->
        <xsl:value-of select="$OS07_MAXLENGTH"/>
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
  <!-- 名前エリア編集文字数（編集パターン「2」でのみ使用）-->
  <!-- ================================================================================= -->
  <!--上段（左）の力士名と出身地の折り返し文字数-->
  <xsl:variable name="UpperPlayerAreaLength">
    <xsl:choose>
      <xsl:when test="$OS07_PLAYERNAME_DISPLAY_SET = 2">
        <xsl:value-of select="floor(($OS07_MAXLENGTH - $ResultAreaLength) div 2)"/>
      </xsl:when>
      <xsl:otherwise/>
    </xsl:choose>
  </xsl:variable>
  <!--下段（右）の力士名と出身地の折り返し文字数-->
  <xsl:variable name="LowerPlayerAreaLength">
    <xsl:choose>
      <xsl:when test="$OS07_PLAYERNAME_DISPLAY_SET = 2">
        <xsl:value-of select="floor(($OS07_MAXLENGTH - $ResultAreaLength) div 2)"/>
      </xsl:when>
      <xsl:otherwise/>
    </xsl:choose>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- 記録エリア編集文字数。半角１文字以上 -->
  <!-- ================================================================================= -->
  <xsl:variable name="ResultAreaLength">
    <!--「―　」で固定-->
    <xsl:value-of select="2"/>
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
      <xsl:with-param name="LINE_MAX_LENGTH" select="$OS07_PRINT_MAXLENGTH"/>
      <xsl:with-param name="PAGE_LINE_MAX" select="$OS07_PRINT_MAXLINE"/>
      <xsl:with-param name="ADD_LINE_COUNT_FLG" select="$ADD_LINE_COUNT_FLG_SET"/>
      <xsl:with-param name="TATEYOKO_FLG" select="$OS07_PTEXT_TATEYOKO"/>
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
    <!--「1」力士名は３字＋出身地は２字-->
    <!--「2」力士名は正式名＋出身地は正式名-->
    <!--=====上段（左）力士=====-->
    <xsl:variable name="UpperPlayerName">
      <!--勝ち越し／負け越し-->
      <xsl:value-of select="Player[1]/Result/ResultForSumo/OutcomeAttribute/Writing"/>
      <xsl:choose>
        <!--パターン「1」-->
        <xsl:when test="$OS07_PLAYERNAME_DISPLAY_SET = 1">
          <!--力士名-->
          <xsl:value-of select="Player[1]/PlayerName/Formal[@Display='3字']"/>
          <xsl:variable name="tmpArea">
            <xsl:value-of select="Player[1]/PlayerForSumo/NativeCountry/Writing"/>
            <xsl:value-of select="Player[1]/PlayerForSumo/NativeArea/Writing"/>
            <xsl:value-of select="Player[1]/PlayerForSumo/NativeCity/Writing"/>
          </xsl:variable>
          <!--出身地-->
          <xsl:if test="string-length($tmpArea)!=0">
            <xsl:value-of select="concat('（',$tmpArea,'）')"/>
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
                <xsl:value-of select="Player[1]/PlayerName/Formal[@Display='3字']"/>
              </xsl:when>
              <xsl:otherwise>
                <xsl:value-of select="Player[1]/PlayerName/Formal[not(@*)]"/>
              </xsl:otherwise>
            </xsl:choose>
          </xsl:variable>
          <!--出身地-->
          <xsl:variable name="tmpKakkoAndArea">
            <xsl:variable name="tmpArea">
              <xsl:value-of select="Player[1]/PlayerForSumo/NativeCountry/Formal[not(@*)]"/>
              <xsl:value-of select="Player[1]/PlayerForSumo/NativeArea/Formal[not(@*)]"/>
              <xsl:if test="
                        (Player[1]/PlayerForSumo/NativeCountry/Formal[not(@*)]
                        or Player[1]/PlayerForSumo/NativeArea/Formal[not(@*)])
                        and Player[1]/PlayerForSumo/NativeCity/Formal[not(@*)]">
                <xsl:text>・</xsl:text>
              </xsl:if>
              <xsl:value-of select="Player[1]/PlayerForSumo/NativeCity/Formal[not(@*)]"/>
            </xsl:variable>
            <xsl:if test="string-length($tmpArea)!=0">
              <xsl:value-of select="concat('（',$tmpArea,'）')"/>
            </xsl:if>
          </xsl:variable>
          <!--力士名＋出身地が１行に収まらない場合、力士名の後をスペースで埋めてから改行-->
          <xsl:variable name="SpaceAfterPlayerName">
            <xsl:if test="string-length($tmpPlayerName) + string-length($tmpKakkoAndArea) &gt; $UpperPlayerAreaLength">
              <xsl:call-template name="PrintSpaceZenkaku_UTL">
                <xsl:with-param name="count" select="$UpperPlayerAreaLength - string-length($tmpPlayerName)"/>
              </xsl:call-template>
              <xsl:call-template name="PrintSpaceZenkaku_UTL">
                <xsl:with-param name="count" select="$UpperPlayerAreaLength - string-length($tmpKakkoAndArea) -1"/>
              </xsl:call-template>
            </xsl:if>
          </xsl:variable>
          <xsl:call-template name="AddBR_KAKUNIN_OSCOM2">
            <xsl:with-param name="Data" select="concat($tmpPlayerName, $SpaceAfterPlayerName, $tmpKakkoAndArea)"/>
            <xsl:with-param name="Length" select="$UpperPlayerAreaLength"/>
            <xsl:with-param name="LeftOrRight" select="1"/>
            <xsl:with-param name="KakkoHamidashiFlg" select="0"/>
          </xsl:call-template>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <!--=====決まり手=====-->
    <xsl:variable name="ResultAreaInfo">
      <xsl:text>―</xsl:text>
    </xsl:variable>
    <!--=====下段（右）力士=====-->
    <!--勝ち越し／負け越し-->
    <xsl:variable name="OutcomeAttribute">
      <xsl:value-of select="Player[2]/Result/ResultForSumo/OutcomeAttribute/Writing"/>
    </xsl:variable>    
    <xsl:variable name="LowerPlayerName">
      <xsl:choose>
        <!--パターン「1」-->
        <xsl:when test="$OS07_PLAYERNAME_DISPLAY_SET = 1">
          <!--力士名-->
          <xsl:value-of select="Player[2]/PlayerName/Formal[@Display='3字']"/>
          <!--勝ち越し／負け越し-->
          <xsl:value-of select="$OutcomeAttribute"/>
          <!--出身地-->
          <xsl:variable name="tmpArea">
            <xsl:value-of select="Player[2]/PlayerForSumo/NativeCountry/Writing"/>
            <xsl:value-of select="Player[2]/PlayerForSumo/NativeArea/Writing"/>
            <xsl:value-of select="Player[2]/PlayerForSumo/NativeCity/Writing"/>
          </xsl:variable>
          <xsl:if test="string-length($tmpArea)!=0">
            <xsl:value-of select="concat('（',$tmpArea,'）')"/>
          </xsl:if>
        </xsl:when>
        <!--パターン「2」-->
        <xsl:otherwise>
          <!--力士名-->
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
          </xsl:variable>
          <!--出身地-->
          <xsl:variable name="tmpKakkoAndArea">
            <xsl:variable name="tmpArea">
              <xsl:value-of select="Player[2]/PlayerForSumo/NativeCountry/Formal[not(@*)]"/>
              <xsl:value-of select="Player[2]/PlayerForSumo/NativeArea/Formal[not(@*)]"/>
              <xsl:if test="
                  (Player[2]/PlayerForSumo/NativeCountry/Formal[not(@*)]
                  or Player[2]/PlayerForSumo/NativeArea/Formal[not(@*)])
                  and Player[2]/PlayerForSumo/NativeCity/Formal[not(@*)]">
                <xsl:text>・</xsl:text>
              </xsl:if>
              <xsl:value-of select="Player[2]/PlayerForSumo/NativeCity/Formal[not(@*)]"/>
            </xsl:variable>
            <xsl:if test="string-length($tmpArea)!=0">
              <xsl:value-of select="concat('（',$tmpArea,'）')"/>
            </xsl:if>
          </xsl:variable>
          <!--力士名＋出身地が１行に収まらない場合、力士名の後をスペースで埋めてから改行-->
          <xsl:variable name="SpaceAfterPlayerName">
            <xsl:if test="string-length($tmpPlayerNameAndGrade) + string-length($tmpKakkoAndArea) &gt; $LowerPlayerAreaLength">
              <xsl:call-template name="PrintSpaceZenkaku_UTL">
                <xsl:with-param name="count" select="$LowerPlayerAreaLength - string-length($tmpPlayerNameAndGrade)"/>
              </xsl:call-template>
              <xsl:call-template name="PrintSpaceZenkaku_UTL">
                <xsl:with-param name="count" select="$LowerPlayerAreaLength - string-length($tmpKakkoAndArea) -1"/>
              </xsl:call-template>
            </xsl:if>
          </xsl:variable>
          <xsl:call-template name="AddBR_KAKUNIN_OSCOM2">
            <xsl:with-param name="Data" select="concat($tmpPlayerNameAndGrade, $SpaceAfterPlayerName, $tmpKakkoAndArea)"/>
            <xsl:with-param name="Length" select="$LowerPlayerAreaLength"/>
            <xsl:with-param name="LeftOrRight" select="2"/>
            <xsl:with-param name="KakkoHamidashiFlg" select="0"/>
          </xsl:call-template>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <!--=====表示=====-->
    <xsl:value-of select="$MatchClass_UTL"/>
    <xsl:choose>
      <!--パターン「1」-->
      <xsl:when test="$OS07_PLAYERNAME_DISPLAY_SET = 1">
        <xsl:value-of select="$UpperPlayerName"/>
        <xsl:value-of select="$ResultAreaInfo"/>
        <xsl:value-of select="$LowerPlayerName"/>
        <xsl:value-of select="$LineFeed_UTL"/>
      </xsl:when>
      <!--パターン「2」-->
      <xsl:otherwise>
        <xsl:call-template name="TaisenLayout_TORIKUMI_OSCOM">
          <xsl:with-param name="PLAYER_INFO_1" select="$UpperPlayerName"/>
          <xsl:with-param name="PLAYER_INFO_2" select="$LowerPlayerName"/>
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
        <xsl:when test="$OS07_PLAYERNAME_DISPLAY_SET = 1">
          <xsl:for-each select="//Match/Player[1]/PlayerName/Formal[@Display='3字']">
            <xsl:call-template name="Gaiji_EDT"/>
          </xsl:for-each>
        </xsl:when>
        <xsl:when test="$OS07_PLAYERNAME_DISPLAY_SET = 2">
          <xsl:for-each select="//Match/Player[1]/PlayerName/Formal[not(@*)]">
            <xsl:call-template name="Gaiji_EDT"/>
          </xsl:for-each>
        </xsl:when>
        <xsl:otherwise/>
      </xsl:choose>
      <!--=====下段=====-->
      <!--力士名-->
      <xsl:choose>
        <xsl:when test="$OS07_PLAYERNAME_DISPLAY_SET = 1">
          <xsl:for-each select="//Match/Player[2]/PlayerName/Formal[@Display='3字']">
            <xsl:call-template name="Gaiji_EDT"/>
          </xsl:for-each>
        </xsl:when>
        <xsl:when test="$OS07_PLAYERNAME_DISPLAY_SET = 2">
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
