<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">
  <!-- ================================================================================= -->
  <!--　編集者用「共通スタイルシート」大相撲・十両星取表 -->
  <!--  4.0版 2015.06.30 プレーンテキスト版のプレーンテキスト表示用として新規公開　-->
  <!-- ================================================================================= -->
  <!-- ============================================== -->
  <!-- 力士名                                         -->
  <!-- ============================================== -->
  <xsl:variable name="OS21_PLAYERNAME_DISPLAY_SET">
    <xsl:call-template name="OS21_PLAYERNAME_DISPLAY_SET"/>
  </xsl:variable>
  <!-- ============================================== -->
  <!-- 出身地　                                       -->
  <!-- ============================================== -->
  <xsl:variable name="OS21_CITY_DISPLAY_SET">
    <xsl:call-template name="OS21_CITY_DISPLAY_SET"/>
  </xsl:variable>
  <!-- ============================================== -->
  <!-- 部屋                                           -->
  <!-- ============================================== -->
  <xsl:variable name="OS21_BELONG_DISPLAY_SET">
    <xsl:call-template name="OS21_BELONG_DISPLAY_SET"/>
  </xsl:variable>
  <!-- ========================================================= -->
  <!-- 変数                                                      -->
  <!-- ========================================================= -->
  <!-- ============================ -->
  <!-- 力士名の最大文字数           -->
  <!-- Writing、Formal3字は３文字なので処理なし、Formalの場合のみ考慮 -->
  <!-- ============================ -->
  <xsl:variable name="PlayerNameMaxLen">
    <xsl:call-template name="GetTagsMaxLength_UTL">
      <xsl:with-param name="TargetPath" select="//PlayerName/Formal[not(@*)]"/>
    </xsl:call-template>
  </xsl:variable>
  <!-- ============================ -->
  <!-- 出身地の最大文字数           -->
  <!-- Writing、Formal2字は２文字なので処理なし、Formalの場合のみ考慮 -->
  <!-- NativeCountry（外国力士）かNaviveArea（日本力士）のいずれかの大きい値を設定  -->
  <!-- ============================ -->
  <!-- 国 -->
  <xsl:variable name="CountryMaxLen">
    <xsl:call-template name="GetTagsMaxLength_UTL">
      <xsl:with-param name="TargetPath" select="//PlayerForSumo/NativeCountry/Formal[not(@*)]"/>
    </xsl:call-template>
  </xsl:variable>
  <!-- 地域 -->
  <xsl:variable name="AreaMaxLen">
    <xsl:call-template name="GetTagsMaxLength_UTL">
      <xsl:with-param name="TargetPath" select="//PlayerForSumo/NativeArea/Formal[not(@*)]"/>
    </xsl:call-template>
  </xsl:variable>
  <xsl:variable name="CityMaxLen">
    <xsl:choose>
      <xsl:when test="$CountryMaxLen > $AreaMaxLen">
        <xsl:value-of select="$CountryMaxLen"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="$AreaMaxLen"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:variable>
  <!-- ============================ -->
  <!-- 出身部屋の最大文字数           -->
  <!-- Writing、Formal2字は２文字なので処理なし、Formalの場合のみ考慮 -->
  <!-- ============================ -->
  <xsl:variable name="BelongMaxLen">
    <xsl:call-template name="GetTagsMaxLength_UTL">
      <xsl:with-param name="TargetPath" select="//Belong/Formal[not(@*)]"/>
    </xsl:call-template>
  </xsl:variable>
  <!-- ============================ -->
  <!-- 出身地＋部屋の最大文字数           -->
  <!-- ============================ -->
  <xsl:variable name="CityBelongMaxLen">
    <xsl:value-of select="($CountryMaxLen) + ($BelongMaxLen)"/>
  </xsl:variable>
  <!-- ============================ -->
  <!-- 引き分けなどの存在有無       -->
  <!-- 存在したら1を設定            -->
  <!-- ============================ -->
  <xsl:variable name="TieFlag">
    <!-- OutcomeTotalのWritingの変換後の文字数をカウントし、4文字だったらはみ出し処理 -->
    <!-- 通常、「勝ー敗」だが、引き分けが○数字で勝敗の後に編集されるケースの対応 -->
    <xsl:variable name="outcomelen">
      <xsl:for-each select="//Result/ResultForSumo">
        <xsl:variable name="outometemp">
          <xsl:call-template name="TranslateToRensuuText_UTL">
            <xsl:with-param name="Data" select="SumoOutcomeTotal/Writing"/>
          </xsl:call-template>
        </xsl:variable>
        <xsl:value-of select="string-length($outometemp)"/>
      </xsl:for-each>
    </xsl:variable>
    <xsl:if test="contains($outcomelen,4)">
      <xsl:value-of select="1"/>
    </xsl:if>
  </xsl:variable>
  <!-- ==================================== -->
  <!-- 引退、廃業、出場停止などの最大文字数 -->
  <!-- ==================================== -->
  <xsl:variable name="RetirementMaxLen">
    <xsl:call-template name="GetTagsMaxLength_UTL">
      <xsl:with-param name="TargetPath" select="//Retirement/Formal"/>
    </xsl:call-template>
  </xsl:variable>
  <!-- ======================================================== -->
  <!-- 確認プレーン（起点）　                                   -->
  <!-- ======================================================== -->
  <xsl:template match="SportsData" mode="KAKUNIN2">
    <!-- Ａ４縦印刷時のフォントサイズ切り替え -->
    <!-- Ａ４縦印刷・力士名と部屋がフル表記の時は９pt -->
    <xsl:choose>
      <xsl:when test="($PRINT_F_SET = 1) and ($OS21_PLAYERNAME_DISPLAY_SET =2) and ($OS21_BELONG_DISPLAY_SET = 2)">
        <xsl:call-template name="KAKUNIN2_DIVS_NORMAL_LAYOUT_UTL">
          <!-- 本文要素 -->
          <xsl:with-param name="HONBUN_DATA">
            <xsl:call-template name="honbun"/>
          </xsl:with-param>
          <!--字解-->
          <xsl:with-param name="JIKAI_DATA">
            <xsl:call-template name="Gaiji_KAKUNIN2"/>
          </xsl:with-param>
          <xsl:with-param name="LINE_MAX_LENGTH" select="$PRINT_MAXYOKOTEXT_FontSizeSmall_2_UTIL"/>
          <xsl:with-param name="PAGE_LINE_MAX" select="$PRINT_MAXYOKOLINES_FontSizeSmall_2_UTIL"/>
          <xsl:with-param name="ADD_LINE_COUNT_FLG" select="$ADD_LINE_COUNT_FLG_SET"/>
          <xsl:with-param name="TATEYOKO_FLG" select="2"/>
        </xsl:call-template>
      </xsl:when>
      <xsl:otherwise>
        <xsl:call-template name="KAKUNIN2_DIVS_NORMAL_LAYOUT_UTL">
          <!-- 本文要素 -->
          <xsl:with-param name="HONBUN_DATA">
            <xsl:call-template name="honbun"/>
          </xsl:with-param>
          <!--字解-->
          <xsl:with-param name="JIKAI_DATA">
            <xsl:call-template name="Gaiji_KAKUNIN2"/>
          </xsl:with-param>
          <xsl:with-param name="LINE_MAX_LENGTH" select="$PRINT_MAXYOKOTEXT_DEFAULT_UTIL"/>
          <xsl:with-param name="PAGE_LINE_MAX" select="$PRINT_MAXYOKOLINES_DEFAULT_UTIL"/>
          <xsl:with-param name="ADD_LINE_COUNT_FLG" select="$ADD_LINE_COUNT_FLG_SET"/>
          <xsl:with-param name="TATEYOKO_FLG" select="2"/>
        </xsl:call-template>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!-- =========================================================================== -->
  <!--  本文　　　　　                           　　　　　　　                    -->
  <!-- =========================================================================== -->
  <xsl:template name="honbun">
    <!-- ================================================== -->
    <!-- 星取表編集                                         -->
    <!-- ================================================== -->
    <xsl:call-template name="hositorihyou_KAKUNIN2"/>
    <xsl:if test="Body/TextNote">
      <xsl:for-each select="Body/TextNote">
        <xsl:value-of select="."/>
        <xsl:if test="position() != last()">
          <!-- 改行 -->
          <xsl:value-of select="$LineFeed_UTL"/>
        </xsl:if>
      </xsl:for-each>
    </xsl:if>
    <xsl:if test="(Body/TextNote) and TextNote">
      <!-- 改行 -->
      <xsl:value-of select="$LineFeed_UTL"/>
    </xsl:if>
    <xsl:if test="TextNote">
      <xsl:for-each select="TextNote">
        <xsl:value-of select="."/>
        <xsl:if test="position() != last()">
          <!-- 改行 -->
          <xsl:value-of select="$LineFeed_UTL"/>
        </xsl:if>
      </xsl:for-each>
    </xsl:if>
  </xsl:template>
  <!--=======================================================================================================-->
  <!--星取表テンプレート-->
  <!--=======================================================================================================-->
  <xsl:template name="hositorihyou_KAKUNIN2">
    <!--Head/Meta/Title-->
    <xsl:text>　　☆☆</xsl:text>
    <xsl:value-of select="Head/Meta/Title"/>
    <xsl:text>☆☆　</xsl:text>
    <!--
    <xsl:if test="Head/Limited/LocalInfo">
      <xsl:text>【</xsl:text>
      <xsl:value-of select="Head/Limited/LocalInfo"/>
      <xsl:text>】</xsl:text>
    </xsl:if>
    -->
    <!-- ========================================================= -->
    <!-- タイトル（☆☆十両☆☆＝９文字）の後のスペース処理        -->
    <!-- ========================================================= -->
    <xsl:choose>
      <!-- 力士：３字、出身：２字、部屋：２字 -->
      <xsl:when test="($OS21_PLAYERNAME_DISPLAY_SET = 1) and ($OS21_CITY_DISPLAY_SET = 1) and ($OS21_BELONG_DISPLAY_SET = 1)">
        <xsl:call-template name="PrintSpaceZenkaku_UTL">
          <xsl:with-param name="count" select="17 - 12"/>
        </xsl:call-template>
      </xsl:when>
      <!-- 力士：３字、出身：フル、部屋：フル -->
      <xsl:when test="($OS21_PLAYERNAME_DISPLAY_SET = 1) and ($OS21_CITY_DISPLAY_SET = 2) and ($OS21_BELONG_DISPLAY_SET = 2)">
        <xsl:call-template name="PrintSpaceZenkaku_UTL">
          <xsl:with-param name="count" select="13 + $CityMaxLen + $BelongMaxLen - 12"/>
        </xsl:call-template>
      </xsl:when>
      <!-- 力士：３字、出身：フル、部屋：２字 -->
      <xsl:when test="($OS21_PLAYERNAME_DISPLAY_SET = 1) and ($OS21_CITY_DISPLAY_SET = 2) and ($OS21_BELONG_DISPLAY_SET = 1)">
        <xsl:call-template name="PrintSpaceZenkaku_UTL">
          <xsl:with-param name="count" select="15 + $CityMaxLen - 12"/>
        </xsl:call-template>
      </xsl:when>
      <!-- 力士：３字、出身：２字、部屋：フル -->
      <xsl:when test="($OS21_PLAYERNAME_DISPLAY_SET = 1) and ($OS21_CITY_DISPLAY_SET = 1) and ($OS21_BELONG_DISPLAY_SET = 2)">
        <xsl:call-template name="PrintSpaceZenkaku_UTL">
          <xsl:with-param name="count" select="15 + $BelongMaxLen - 12"/>
        </xsl:call-template>
      </xsl:when>
      <!-- 力士：フル、出身：２字、部屋：２字 -->
      <xsl:when test="($OS21_PLAYERNAME_DISPLAY_SET = 2) and ($OS21_CITY_DISPLAY_SET = 1) and ($OS21_BELONG_DISPLAY_SET = 1)">
        <xsl:call-template name="PrintSpaceZenkaku_UTL">
          <xsl:with-param name="count" select="14 + $PlayerNameMaxLen - 12"/>
        </xsl:call-template>
      </xsl:when>
      <!-- 力士：フル、出身：フル、部屋：フル -->
      <xsl:when test="($OS21_PLAYERNAME_DISPLAY_SET = 2) and ($OS21_CITY_DISPLAY_SET = 2) and ($OS21_BELONG_DISPLAY_SET = 2)">
        <xsl:call-template name="PrintSpaceZenkaku_UTL">
          <xsl:with-param name="count" select="10 + $PlayerNameMaxLen + $CityMaxLen + $BelongMaxLen - 12"/>
        </xsl:call-template>
      </xsl:when>
      <!-- 力士：フル、出身：フル、部屋：２字 -->
      <xsl:when test="($OS21_PLAYERNAME_DISPLAY_SET = 2) and ($OS21_CITY_DISPLAY_SET = 2) and ($OS21_BELONG_DISPLAY_SET = 1)">
        <xsl:call-template name="PrintSpaceZenkaku_UTL">
          <xsl:with-param name="count" select="12 + $PlayerNameMaxLen + $CityMaxLen - 12"/>
        </xsl:call-template>
      </xsl:when>
      <!-- 力士：フル、出身：２字、部屋：フル -->
      <xsl:when test="($OS21_PLAYERNAME_DISPLAY_SET = 2) and ($OS21_CITY_DISPLAY_SET = 1) and ($OS21_BELONG_DISPLAY_SET = 2)">
        <xsl:call-template name="PrintSpaceZenkaku_UTL">
          <xsl:with-param name="count" select="12 + $PlayerNameMaxLen + $BelongMaxLen - 12"/>
        </xsl:call-template>
      </xsl:when>
    </xsl:choose>
    <!-- 引き分けが存在したら１文字空白を設定　-->
    <xsl:if test="$TieFlag = 1">
      <xsl:text>　</xsl:text>
    </xsl:if>
    <!-- 引退、廃業、出場停止などのケースの空白設定 -->
    <!-- 通常３文字エリアだが、出場停止などで４文字以上になるケースの対応 -->
    <xsl:choose>
      <xsl:when test="$RetirementMaxLen > 3">
        <xsl:call-template name="PrintSpaceZenkaku_UTL">
          <xsl:with-param name="count" select="$RetirementMaxLen"/>
        </xsl:call-template>
      </xsl:when>
      <xsl:otherwise>
        <xsl:text>　　　</xsl:text>
      </xsl:otherwise>
    </xsl:choose>
    <!-- ================================================================ -->
    <xsl:value-of select="Head/Limited/LocalInfo"/>
    <!--今場所成績（詳細）の見出し-->
    <xsl:call-template name="seisekimidasi_KAKUNIN2"/>
    <!-- 改行 -->
    <xsl:value-of select="$LineFeed_UTL"/>
    <!--Bodyタグを編集-->
    <xsl:for-each select="Body">
      <!--Title-->
      <xsl:for-each select="Meta/Title">
        <xsl:value-of select="."/>
      </xsl:for-each>
      <!-- 改行 -->
      <xsl:value-of select="$LineFeed_UTL"/>
      <!--Article-->
      <xsl:if test="Article/Paragraph">
        <xsl:text>　</xsl:text>
        <xsl:value-of select="Article/Paragraph"/>
        <!-- 改行 -->
        <xsl:value-of select="$LineFeed_UTL"/>
      </xsl:if>
      <!--Standing-->
      <xsl:for-each select="Standing">
        <xsl:apply-templates select="Player" mode="hositorihyou_KAKUNIN2"/>
      </xsl:for-each>
    </xsl:for-each>
  </xsl:template>
  <!--=======================================================================================================-->
  <!--成績見出しテンプレート-->
  <!--=======================================================================================================-->
  <xsl:template name="seisekimidasi_KAKUNIN2">
    <xsl:call-template name="seisekimidasi_kobetu_KAKUNIN2">
      <xsl:with-param name="POSITION" select="1"/>
    </xsl:call-template>
    <xsl:call-template name="seisekimidasi_kobetu_KAKUNIN2">
      <xsl:with-param name="POSITION" select="2"/>
    </xsl:call-template>
    <xsl:call-template name="seisekimidasi_kobetu_KAKUNIN2">
      <xsl:with-param name="POSITION" select="3"/>
    </xsl:call-template>
    <xsl:call-template name="seisekimidasi_kobetu_KAKUNIN2">
      <xsl:with-param name="POSITION" select="4"/>
    </xsl:call-template>
    <xsl:call-template name="seisekimidasi_kobetu_KAKUNIN2">
      <xsl:with-param name="POSITION" select="5"/>
    </xsl:call-template>
    <xsl:call-template name="seisekimidasi_kobetu_KAKUNIN2">
      <xsl:with-param name="POSITION" select="6"/>
    </xsl:call-template>
    <xsl:call-template name="seisekimidasi_kobetu_KAKUNIN2">
      <xsl:with-param name="POSITION" select="7"/>
    </xsl:call-template>
    <xsl:call-template name="seisekimidasi_kobetu_KAKUNIN2">
      <xsl:with-param name="POSITION" select="8"/>
    </xsl:call-template>
    <xsl:call-template name="seisekimidasi_kobetu_KAKUNIN2">
      <xsl:with-param name="POSITION" select="9"/>
    </xsl:call-template>
    <xsl:call-template name="seisekimidasi_kobetu_KAKUNIN2">
      <xsl:with-param name="POSITION" select="10"/>
    </xsl:call-template>
    <xsl:call-template name="seisekimidasi_kobetu_KAKUNIN2">
      <xsl:with-param name="POSITION" select="11"/>
    </xsl:call-template>
    <xsl:call-template name="seisekimidasi_kobetu_KAKUNIN2">
      <xsl:with-param name="POSITION" select="12"/>
    </xsl:call-template>
    <xsl:call-template name="seisekimidasi_kobetu_KAKUNIN2">
      <xsl:with-param name="POSITION" select="13"/>
    </xsl:call-template>
    <xsl:call-template name="seisekimidasi_kobetu_KAKUNIN2">
      <xsl:with-param name="POSITION" select="14"/>
    </xsl:call-template>
    <xsl:call-template name="seisekimidasi_kobetu_KAKUNIN2">
      <xsl:with-param name="POSITION" select="15"/>
    </xsl:call-template>
  </xsl:template>
  <!--=======================================================================================================-->
  <!--成績見出しテンプレート-->
  <!--=======================================================================================================-->
  <xsl:template name="seisekimidasi_kobetu_KAKUNIN2">
    <xsl:param name="POSITION"/>
    <xsl:if test="Body/Standing/Player/Result/Result[$POSITION]/@Period">
      <xsl:call-template name="RensuuHenkan">
        <xsl:with-param name="Sts" select="3"/>
        <xsl:with-param name="Pdata" select="Body/Standing/Player/Result/Result[$POSITION]/@Period[1]"/>
      </xsl:call-template>
    </xsl:if>
  </xsl:template>
  <!--=======================================================================================================-->
  <!--星取表選手タグテンプレート-->
  <!--=======================================================================================================-->
  <xsl:template match="Player" mode="hositorihyou_KAKUNIN2">
    <!-- ======================================================= -->
    <!-- 変数                                                    -->
    <!-- ======================================================= -->
    <!-- ======================================== -->
    <!-- 力士名                                   -->
    <!-- ======================================== -->
    <xsl:variable name="PlayerName">
      <xsl:choose>
        <xsl:when test="$OS21_PLAYERNAME_DISPLAY_SET = 1">
          <xsl:value-of select="PlayerName/Formal[@Display='3字']"/>
        </xsl:when>
        <!-- フル表記の場合、最大文字数で揃え、空白を埋める -->
        <xsl:otherwise>
          <xsl:value-of select="PlayerName/Formal[not(@*)]"/>
          <xsl:call-template name="PrintSpaceZenkaku_UTL">
            <xsl:with-param name="count" select="$PlayerNameMaxLen - string-length(PlayerName/Formal[not(@*)])"/>
          </xsl:call-template>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <!-- ======================================== -->
    <!-- 出身地                                   -->
    <!-- ======================================== -->
    <xsl:variable name="CityName">
      <xsl:choose>
        <xsl:when test="$OS21_CITY_DISPLAY_SET = 1">
          <xsl:value-of select="PlayerForSumo/NativeArea/Formal[@Display='2字']"/>
          <xsl:value-of select="PlayerForSumo/NativeCountry/Formal[@Display='2字']"/>
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="PlayerForSumo/NativeArea/Formal[not(@*)]"/>
          <xsl:value-of select="PlayerForSumo/NativeCountry/Formal[not(@*)]"/>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <!-- ======================================== -->
    <!-- 部屋　                                   -->
    <!-- ======================================== -->
    <xsl:variable name="Belong">
      <xsl:choose>
        <xsl:when test="$OS21_BELONG_DISPLAY_SET = 1">
          <xsl:value-of select="Belong/Formal[@Display='2字']"/>
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="Belong/Formal[not(@*)]"/>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <!-- ================================================================= -->
    <!-- 表示処理                                                          -->
    <!-- ================================================================= -->
    <!-- ======================================================= -->
    <!--「勝負越」                                               -->
    <!-- ======================================================= -->
    <xsl:choose>
      <xsl:when test="(Result/ResultForSumo/OutcomeAttribute/Writing) and not(PlayerForSumo/PreviousName)">
        <xsl:value-of select="Result/ResultForSumo/OutcomeAttribute/Writing"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:text>　</xsl:text>
      </xsl:otherwise>
    </xsl:choose>
    <!-- ==================================== -->
    <!--力士名                                -->
    <!-- ==================================== -->
    <xsl:choose>
      <xsl:when test="PlayerName/Formal[not(@*)]">
        <!-- 改名がある場合、「▽旧名改め＋改行」を力士名の上に表示 -->
        <xsl:if test="PlayerForSumo/PreviousName/Formal[not(@*)]">
          <xsl:text>▽</xsl:text>
          <xsl:value-of select="PlayerForSumo/PreviousName/Formal[not(@*)]"/>
          <xsl:text>改め</xsl:text>
          <!-- 改行 -->
          <xsl:value-of select="$LineFeed_UTL"/>
          <!-- 勝敗越 -->
          <xsl:choose>
            <xsl:when test="Result/ResultForSumo/OutcomeAttribute/Writing">
              <xsl:value-of select="Result/ResultForSumo/OutcomeAttribute/Writing"/>
            </xsl:when>
            <xsl:otherwise>
              <xsl:text>　</xsl:text>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:if>
        <xsl:value-of select="$PlayerName"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:text>　　　</xsl:text>
      </xsl:otherwise>
    </xsl:choose>
    <!--空白-->
    <xsl:text>　</xsl:text>
    <!-- ==================================== -->
    <!--地位                                  -->
    <!-- ==================================== -->
    <xsl:if test="string-length(PlayerForSumo/SumoGrade/Writing) = 1">
      <xsl:text>　</xsl:text>
    </xsl:if>
    <xsl:value-of select="PlayerForSumo/SumoGrade/Writing"/>
    <xsl:if test="not(PlayerForSumo/SumoGrade/Writing)">
      <xsl:text>　　</xsl:text>
    </xsl:if>
    <!-- ==================================== -->
    <!--出身地・出身部屋                      -->
    <!-- ==================================== -->
    <xsl:if test="
					PlayerForSumo/NativeArea/Formal[not(@*)] or
					PlayerForSumo/NativeCountry/Formal[not(@*)] or
					Belong/Formal[not(@*)]
				">
      <xsl:text>（</xsl:text>
    </xsl:if>
    <xsl:value-of select="$CityName"/>
    <xsl:if test="
					(PlayerForSumo/NativeArea/Formal[not(@*)] or
					PlayerForSumo/NativeCountry/Formal[not(@*)]) and
					Belong/Formal[not(@*)]
				">
      <xsl:text>・</xsl:text>
    </xsl:if>
    <xsl:value-of select="$Belong"/>
    <xsl:if test="
					PlayerForSumo/NativeArea/Formal[not(@*)] or
					PlayerForSumo/NativeCountry/Formal[not(@*)] or
					Belong/Formal[not(@*)]
				">
      <xsl:text>）</xsl:text>
    </xsl:if>
    <!-- =========================================== -->
    <!-- 桁合わせのための空白処理                    -->
    <!-- =========================================== -->
    <xsl:choose>
      <!-- 出身地：フル・部屋：フル  -->
      <!-- 出身地＋部屋の最大値に合わせて、空白を埋める -->
      <xsl:when test="($OS21_CITY_DISPLAY_SET = 2) and ($OS21_BELONG_DISPLAY_SET = 2)">
        <xsl:call-template name="PrintSpaceZenkaku_UTL">
          <xsl:with-param name="count" select="$CityBelongMaxLen - string-length($CityName)  - string-length($Belong)"/>
        </xsl:call-template>
      </xsl:when>
      <!-- 出身地：２字・部屋：フル  -->
      <!-- 部屋の最大値に合わせて、空白を埋める -->
      <xsl:when test="($OS21_CITY_DISPLAY_SET = 1) and ($OS21_BELONG_DISPLAY_SET = 2)">
        <xsl:call-template name="PrintSpaceZenkaku_UTL">
          <xsl:with-param name="count" select="$BelongMaxLen - string-length($Belong)"/>
        </xsl:call-template>
      </xsl:when>
      <!-- 出身地：フル・部屋：２字  -->
      <!-- 出身地の最大値に合わせて、空白を埋める -->
      <xsl:when test="($OS21_CITY_DISPLAY_SET = 2) and ($OS21_BELONG_DISPLAY_SET = 1)">
        <xsl:call-template name="PrintSpaceZenkaku_UTL">
          <xsl:with-param name="count" select="$CityMaxLen - string-length($CityName)"/>
        </xsl:call-template>
      </xsl:when>
    </xsl:choose>
    <!-- ============================================================= -->
    <!--引退 or 今場所成績-->
    <xsl:choose>
      <xsl:when test="PlayerForSumo/Retirement/Formal[not(@*)]">
        <!-- ========================== -->
        <!--引退や廃業                  -->
        <!-- ========================== -->
        <xsl:value-of select="PlayerForSumo/Retirement/Formal[not(@*)]"/>
        <!-- 引退や廃業時に桁揃えで空白１文字 -->
        <xsl:if test="string-length(PlayerForSumo/Retirement/Formal[not(@*)]) = 2">
          <xsl:text>　</xsl:text>
        </xsl:if>
      </xsl:when>
      <xsl:otherwise>
        <!-- =========================== -->
        <!--今場所成績                   -->
        <!-- =========================== -->
        <xsl:choose>
          <xsl:when test="Result/ResultForSumo/SumoOutcomeTotal/Writing">
            <xsl:call-template name="TranslateToRensuuText_UTL">
              <xsl:with-param name="Data" select="Result/ResultForSumo/SumoOutcomeTotal/Writing"/>
            </xsl:call-template>
          </xsl:when>
          <xsl:otherwise>
            <xsl:text>　</xsl:text>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:otherwise>
    </xsl:choose>
    <!-- 引き分けなどが存在したら１文字空白を設定　-->
    <xsl:if test="$TieFlag = 1">
      <xsl:variable name="outcomeplayer">
        <xsl:call-template name="TranslateToRensuuText_UTL">
          <xsl:with-param name="Data" select="Result/ResultForSumo/SumoOutcomeTotal/Writing"/>
        </xsl:call-template>
      </xsl:variable>
      <xsl:if test="string-length($outcomeplayer) != 4">
        <xsl:text>　</xsl:text>
      </xsl:if>
    </xsl:if>
    <!-- 引退、廃業、出場停止などのケースの空白設定 -->
    <!-- Retirement/Formalの最大値からRetirement/Formalの長さを空白で埋める -->
    <!-- Retirement/Formalがなければ、最大値から３を引く                     -->
    <xsl:if test="$RetirementMaxLen > 3">
      <xsl:choose>
        <xsl:when test="(PlayerForSumo/Retirement) and (string-length(PlayerForSumo/Retirement/Formal) > 3)">

          <xsl:call-template name="PrintSpaceZenkaku_UTL">
            <xsl:with-param name="count" select="$RetirementMaxLen - string-length(PlayerForSumo/Retirement/Formal)"/>
          </xsl:call-template>

        </xsl:when>
        <xsl:otherwise>
          <xsl:call-template name="PrintSpaceZenkaku_UTL">
            <xsl:with-param name="count" select="$RetirementMaxLen - 3"/>
          </xsl:call-template>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:if>
    <!-- =========================== -->
    <!--今場所成績（詳細）           -->
    <!-- =========================== -->
    <xsl:for-each select="Result/Result/Outcome/Writing">
      <xsl:value-of select="."/>
    </xsl:for-each>
    <!-- 改行 -->
    <xsl:value-of select="$LineFeed_UTL"/>
  </xsl:template>
  <!--=======================================================================================================-->
  <!--Gaijiテンプレート-->
  <!--=======================================================================================================-->
  <xsl:template name="Gaiji_KAKUNIN2">
    <!-- 字解編集 -->
    <xsl:variable name="JIKAI_DATA">
      <xsl:for-each select=".//Body/TextNote">
        <xsl:call-template name="Gaiji_EDT"/>
      </xsl:for-each>
      <xsl:for-each select=".//Meta/Title">
        <xsl:call-template name="Gaiji_EDT"/>
      </xsl:for-each>
      <xsl:for-each select=".//Head/Limited/LocalInfo">
        <xsl:call-template name="Gaiji_EDT"/>
      </xsl:for-each>
      <xsl:for-each select=".//Article/Paragraph">
        <xsl:call-template name="Gaiji_EDT"/>
      </xsl:for-each>
      <xsl:for-each select=".//Result/ResultForSumo/OutcomeAttribute/Writing">
        <xsl:call-template name="Gaiji_EDT"/>
      </xsl:for-each>
      <xsl:for-each select=".//PlayerForSumo/PreviousName/Formal[not(@*)]">
        <xsl:call-template name="Gaiji_EDT"/>
      </xsl:for-each>
      <xsl:for-each select=".//PlayerName/Formal[not(@*)]">
        <xsl:call-template name="Gaiji_EDT"/>
      </xsl:for-each>
      <xsl:for-each select=".//PlayerForSumo/SumoGrade/Writing">
        <xsl:call-template name="Gaiji_EDT"/>
      </xsl:for-each>
      <xsl:for-each select=".//PlayerForSumo/NativeArea/Formal[not(@*)]">
        <xsl:call-template name="Gaiji_EDT"/>
      </xsl:for-each>
      <xsl:for-each select=".//PlayerForSumo/NativeCountry/Formal[not(@*)]">
        <xsl:call-template name="Gaiji_EDT"/>
      </xsl:for-each>
      <xsl:for-each select=".//Belong/Formal[not(@*)]">
        <xsl:call-template name="Gaiji_EDT"/>
      </xsl:for-each>
      <xsl:for-each select=".//Result/ResultForSumo/SumoOutcomeTotal/Writing">
        <xsl:call-template name="Gaiji_EDT"/>
      </xsl:for-each>
      <xsl:for-each select=".//Result/Result/Outcome/Writing">
        <xsl:call-template name="Gaiji_EDT"/>
      </xsl:for-each>
      <xsl:for-each select=".//PlayerForSumo/Retirement/Formal[not(@*)]">
        <xsl:call-template name="Gaiji_EDT"/>
      </xsl:for-each>
    </xsl:variable>
    <xsl:if test="($JIKAI_DATA!='')">
      <!--字解見出し-->
      <xsl:text>字解情報</xsl:text>
      <!-- 改行 -->
      <xsl:value-of select="$LineFeed_UTL"/>
      <xsl:value-of disable-output-escaping="yes" select="$JIKAI_DATA"/>
    </xsl:if>
  </xsl:template>
</xsl:stylesheet>
