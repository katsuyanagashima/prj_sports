<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">
  <!-- ================================================================================= -->
  <!--　編集者用「共通スタイルシート」大相撲・幕内星取表 -->
  <!--  4.0版 2015.06.30 プレーンテキスト版のプレーンテキスト表示用として新規公開　-->
  <!-- ================================================================================= -->
  <!-- ============================================== -->
  <!-- 力士名                                         -->
  <!-- ============================================== -->
  <xsl:variable name="OS22_PLAYERNAME_DISPLAY_SET">
    <!--    <xsl:call-template name="OS22_PLAYERNAME_DISPLAY_SET"/>   -->
    <!-- フルネーム固定 -->
    <xsl:value-of select="1"/>
  </xsl:variable>
  <!-- ========================================================= -->
  <!-- 変数                                                      -->
  <!-- ========================================================= -->
  <!-- ============================ -->
  <!-- 力士名の最大文字数           -->
  <!-- Writing、Formal3字は２文字なので処理なし、Formalの場合のみ考慮 -->
  <!-- ============================ -->
  <xsl:variable name="PlayerNameMaxLen">
    <!-- 東 -->
    <xsl:variable name="playertemp1">
      <xsl:call-template name="GetTagsMaxLength_UTL">
        <xsl:with-param name="TargetPath" select="//SportsData/Body[1]/Standing/Player/PlayerName/Formal[not(@*)]"/>
      </xsl:call-template>
    </xsl:variable>
    <!-- 西 -->
    <xsl:variable name="playertemp2">
      <xsl:call-template name="GetTagsMaxLength_UTL">
        <xsl:with-param name="TargetPath" select="//SportsData/Body[2]/Standing/Player/PlayerName/Formal[not(@*)]"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:choose>
      <xsl:when test="$playertemp1 > $playertemp2">
        <xsl:value-of select="$playertemp1"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="$playertemp2"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:variable>
  <!-- ============================ -->
  <!-- 力士名の最長文字列           -->
  <!-- ============================ -->
  <xsl:variable name="allplayerMaxLen">
    <xsl:call-template name="GetTagsMaxLength_UTL">
      <xsl:with-param name="TargetPath" select="//Player/PlayerName/Formal[not(@*)]"/>
    </xsl:call-template>
  </xsl:variable>
  <!-- ============================ -->
  <!-- 出身地の最大文字数           -->
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
  <!-- 休場力士の有無           -->
  <!-- ============================ -->
  <xsl:variable name="rest_temp">
    <xsl:for-each select="//Result/ResultForSumo/SumoOutcomeTotal">
      <xsl:value-of select="Writing"/>
    </xsl:for-each>
  </xsl:variable>
  <!-- ============================ -->
  <!-- タイトルの長さ               -->
  <!-- ============================ -->
  <xsl:variable name="titleLen">
    <xsl:value-of select="string-length(//Title)"/>
  </xsl:variable>
  <!-- ============================ -->
  <!-- Class（十両など）の最大文字数 -->
  <!-- ============================ -->
  <xsl:variable name="ClassMaxLen">
    <xsl:call-template name="GetTagsMaxLength_UTL">
      <xsl:with-param name="TargetPath" select="//Class"/>
    </xsl:call-template>
  </xsl:variable>
  <!-- ============================ -->
  <!-- Grade（横綱など）の最大文字数 -->
  <!-- ============================ -->
  <xsl:variable name="GradeMaxLen">
    <xsl:call-template name="GetTagsMaxLength_UTL">
      <xsl:with-param name="TargetPath" select="//SumoGrade/Writing"/>
    </xsl:call-template>
  </xsl:variable>
  <!-- ============================ -->
  <!-- ○勝○敗などの最大文字数 -->
  <!-- ============================ -->
  <xsl:variable name="OutcomeTotalMaxLen">
    <xsl:call-template name="GetTagsMaxLength_UTL">
      <xsl:with-param name="TargetPath" select="//SumoOutcomeTotal/Writing"/>
    </xsl:call-template>
  </xsl:variable>
  <!-- ============================= -->
  <!-- 三賞などの力士名の最大文字数  -->
  <!-- ============================= -->
  <xsl:variable name="PlaynameOtherMaxLen">
    <xsl:variable name="playernameAllMaxLen">
      <xsl:call-template name="GetTagsMaxLength_UTL">
        <xsl:with-param name="TargetPath" select="//SumoOutcomeTotal/Writing"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="$playernameAllMaxLen"/>
  </xsl:variable>
  <!-- ============================= -->
  <!-- 三賞などの賞の最大文字列  -->
  <!-- ============================= -->
  <xsl:variable name="AwardMaxText">
    <xsl:call-template name="GetTagsMaxLengthStirng_UTL">
      <xsl:with-param name="TargetPath" select="//Award/Count/Writing"/>
    </xsl:call-template>
  </xsl:variable>
  <!-- ============================= -->
  <!-- 三賞などの賞の最大文字数  -->
  <!-- ============================= -->
  <xsl:variable name="AwardMaxLen">
    <xsl:variable name="awardmaxlentemp">
      <xsl:call-template name="TranslateToRensuuText_UTL">
        <xsl:with-param name="Data" select="$AwardMaxText"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:value-of select="string-length($awardmaxlentemp)"/>
  </xsl:variable>
  <!-- ======================================================== -->
  <!-- 確認プレーン（起点）　                                   -->
  <!-- ======================================================== -->
  <xsl:template match="SportsData" mode="KAKUNIN2">
    <xsl:choose>
      <xsl:when test="$PRINT_F_SET = 1">
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
    <!-- タイトル（☆☆十両☆☆＝15文字）の後のスペース処理        -->
    <!-- ========================================================= -->
    <!-- 力士名のフル表記(2)／２字(otherwize)で処理を分ける -->
    <xsl:choose>
      <!-- =================================== -->
      <!-- 力士名が２文字の場合                -->
      <!-- =================================== -->
      <xsl:when test="$OS22_PLAYERNAME_DISPLAY_SET = 2">
        <xsl:choose>
          <!-- OutcomeTotalの最大文字数で処理を分けているのは、連数字変換しているため、５文字以上は余計に１マイナス -->
          <xsl:when test="$OutcomeTotalMaxLen > 4">
            <xsl:call-template name="PrintSpaceZenkaku_UTL">
              <xsl:with-param name="count" select="$CountryMaxLen + $BelongMaxLen + $GradeMaxLen + $OutcomeTotalMaxLen -1 - $titleLen -1"/>
            </xsl:call-template>
          </xsl:when>
          <xsl:otherwise>
            <xsl:call-template name="PrintSpaceZenkaku_UTL">
              <xsl:with-param name="count" select="$CountryMaxLen + $BelongMaxLen + $GradeMaxLen + $OutcomeTotalMaxLen - $titleLen - 1"/>
            </xsl:call-template>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:when>
      <!-- =================================== -->
      <!-- 力士名がフル表記の場合              -->
      <!-- =================================== -->
      <xsl:otherwise>
        <xsl:choose>
          <!-- OutcomeTotalの最大文字数で処理を分けているのは、連数字変換しているため、５文字以上は余計に１マイナス -->
          <xsl:when test="$OutcomeTotalMaxLen > 4">
            <xsl:call-template name="PrintSpaceZenkaku_UTL">
              <xsl:with-param name="count" select="$PlayerNameMaxLen + $CountryMaxLen + $BelongMaxLen + $GradeMaxLen + $OutcomeTotalMaxLen -1 - $titleLen -3"/>
            </xsl:call-template>
          </xsl:when>
          <xsl:otherwise>
            <xsl:call-template name="PrintSpaceZenkaku_UTL">
              <xsl:with-param name="count" select="$PlayerNameMaxLen + $CountryMaxLen + $BelongMaxLen + $GradeMaxLen + $OutcomeTotalMaxLen - $titleLen - 3"/>
            </xsl:call-template>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:otherwise>
    </xsl:choose>
    <!-- ========================================================= -->
    <xsl:value-of select="Head/Limited/LocalInfo"/>
    <!--今場所成績（詳細）の見出し-->
    <xsl:call-template name="seisekimidasi_KAKUNIN2"/>
    <!-- 改行 -->
    <xsl:value-of select="$LineFeed_UTL"/>
    <!--Bodyタグを編集-->
    <xsl:for-each select="Body">
      <xsl:if test="Meta/DataType='幕内力士'">
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
      </xsl:if>
    </xsl:for-each>
    <!--空白行-->
    <xsl:if test="Body[Meta/DataType='幕内力士'] and (Body[Meta/DataType='優勝力士'] or Body[Meta/DataType='三賞受賞力士'])">
      <!-- 改行 -->
      <xsl:value-of select="$LineFeed_UTL"/>
    </xsl:if>
    <!-- ================================================= -->
    <!--優勝力士                                           -->
    <!-- ================================================= -->
    <xsl:if test="Body[Meta/DataType='優勝力士']">
      <xsl:text>▽優勝力士</xsl:text>
      <!-- 改行 -->
      <xsl:value-of select="$LineFeed_UTL"/>
      <xsl:for-each select="Body[Meta/DataType='優勝力士']">
        <!--Class-->
        <xsl:text>【</xsl:text>
        <xsl:value-of select="Meta/Class"/>
        <xsl:text>】</xsl:text>
        <!-- 桁揃えの処理 -->
        <xsl:if test="string-length(Meta/Class) &lt; $ClassMaxLen">
          <xsl:call-template name="PrintSpaceZenkaku_UTL">
            <xsl:with-param name="count" select="$ClassMaxLen - string-length(Meta/Class)"/>
          </xsl:call-template>
        </xsl:if>
        <!--Paragraphタグ-->
        <xsl:for-each select="Article/Paragraph">
          <xsl:text>　</xsl:text>
          <xsl:value-of select="."/>
        </xsl:for-each>
        <!--選手情報-->
        <xsl:apply-templates select="Standing/Player" mode="yuusyousannsyoujusyou_KAKUNIN2"/>
        <!-- 改行 -->
        <xsl:value-of select="$LineFeed_UTL"/>
      </xsl:for-each>
    </xsl:if>
    <!--空白行-->
    <xsl:if test="Body[Meta/DataType='優勝力士'] and Body[Meta/DataType='三賞受賞力士']">
      <!-- 改行 -->
      <xsl:value-of select="$LineFeed_UTL"/>
    </xsl:if>
    <!-- ================================================= -->
    <!--三賞受賞力士                                       -->
    <!-- ================================================= -->
    <xsl:if test="Body[Meta/DataType='三賞受賞力士']">
      <xsl:text>▽三賞受賞力士</xsl:text>
      <!-- 改行 -->
      <xsl:value-of select="$LineFeed_UTL"/>
      <xsl:for-each select="Body[Meta/DataType='三賞受賞力士']">
        <!--Scope-->
        <xsl:text>【</xsl:text>
        <xsl:value-of select="Meta/Scope"/>
        <xsl:text>】</xsl:text>
        <!--Paragraphタグ-->
        <xsl:for-each select="Article/Paragraph">
          <xsl:value-of select="."/>
        </xsl:for-each>
        <!--選手情報-->
        <xsl:for-each select="Standing/Player">
          <xsl:apply-templates select="." mode="yuusyousannsyoujusyou_KAKUNIN2"/>
          <xsl:if test="position() != last()">
            <!-- 改行 -->
            <xsl:value-of select="$LineFeed_UTL"/>
            <!-- 複数選手発生、改行後の空白調整 -->
            <xsl:call-template name="PrintSpaceZenkaku_UTL">
              <xsl:with-param name="count" select="string-length(Result/Award/@Kind) + 2"/>
            </xsl:call-template>
          </xsl:if>
        </xsl:for-each>
        <!-- 改行 -->
        <xsl:value-of select="$LineFeed_UTL"/>
      </xsl:for-each>
    </xsl:if>
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
        <xsl:when test="$OS22_PLAYERNAME_DISPLAY_SET = 2">
          <xsl:value-of select="PlayerName/Formal[@Display='対戦表記']"/>
          <xsl:if test="string-length(PlayerName/Formal[@Display='対戦表記']) = 1">
            <xsl:text>　</xsl:text>
          </xsl:if>
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
      <xsl:value-of select="PlayerForSumo/NativeArea/Writing"/>
      <xsl:value-of select="PlayerForSumo/NativeCountry/Writing"/>
    </xsl:variable>
    <!-- ======================================== -->
    <!-- 部屋　                                   -->
    <!-- ======================================== -->
    <xsl:variable name="Belong">
      <xsl:value-of select="Belong/Writing"/>
    </xsl:variable>
    <!-- ================================================================= -->
    <!-- ======================================== -->
    <!--「勝負越」                                -->
    <!-- ======================================== -->
    <xsl:choose>
      <xsl:when test="(Result/ResultForSumo/OutcomeAttribute/Writing) and not(PlayerForSumo/PreviousName)">
        <xsl:value-of select="Result/ResultForSumo/OutcomeAttribute/Writing"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:text>　</xsl:text>
      </xsl:otherwise>
    </xsl:choose>
    <!-- ======================================== -->
    <!--力士名                                    -->
    <!-- ======================================== -->
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
    <!-- ======================================== -->
    <!--地位                                      -->
    <!-- ======================================== -->
    <xsl:call-template name="PrintSpaceZenkaku_UTL">
      <xsl:with-param name="count" select="$GradeMaxLen - string-length(PlayerForSumo/SumoGrade/Writing)"/>
    </xsl:call-template>
    <xsl:value-of select="PlayerForSumo/SumoGrade/Writing"/>
    <!-- ======================================== -->
    <!--出身地・出身部屋                          -->
    <!-- ======================================== -->
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
    <!-- 出身地：フル・部屋：フル  -->
    <xsl:call-template name="PrintSpaceZenkaku_UTL">
      <xsl:with-param name="count" select="$CityBelongMaxLen - string-length($CityName)  - string-length($Belong) -1"/>
    </xsl:call-template>
    <!-- ======================================== -->
    <!--引退 or 今場所成績                        -->
    <!-- ======================================== -->
    <!-- 変数 -->
    <!-- ○勝○敗などを連数字変換 -->
    <xsl:variable name="outcometotaltemp">
      <xsl:call-template name="TranslateToRensuuText_UTL">
        <xsl:with-param name="Data" select="Result/ResultForSumo/SumoOutcomeTotal/Writing"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:choose>
      <!-- ============================================================== -->
      <!-- 引退など                                                       -->
      <!-- ============================================================== -->
      <!-- 引退などの情報があった場合、○勝○敗は表示せず、引退などを表示 -->
      <xsl:when test="PlayerForSumo/Retirement/Formal[not(@*)]">
        <xsl:choose>
          <!-- ○勝○敗を連数字変換しているため、Writingの最大が５文字以上の場合、最大値から1マイナスで空白埋め -->
          <xsl:when test="$OutcomeTotalMaxLen > 4">
            <xsl:value-of select="PlayerForSumo/Retirement/Formal[not(@*)]"/>
            <xsl:call-template name="PrintSpaceZenkaku_UTL">
              <xsl:with-param name="count" select="$OutcomeTotalMaxLen - string-length(PlayerForSumo/Retirement/Formal[not(@*)]) -1"/>
            </xsl:call-template>
          </xsl:when>
          <!-- ○勝○敗が４文字以下の場合、最大値から勝敗数の文字数を引いた値で空白埋め -->
          <xsl:otherwise>
            <xsl:value-of select="PlayerForSumo/Retirement/Formal[not(@*)]"/>
            <xsl:call-template name="PrintSpaceZenkaku_UTL">
              <xsl:with-param name="count" select="$OutcomeTotalMaxLen - string-length(PlayerForSumo/Retirement/Formal[not(@*)])"/>
            </xsl:call-template>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:when>
      <!-- ============================================================== -->
      <!-- 今場所の成績                                                   -->
      <!-- ============================================================== -->
      <!-- 引退などの情報がない場合、○勝○敗などの今場所の成績を表示 -->
      <xsl:otherwise>
        <xsl:choose>
          <!-- ○勝○敗を連数字変換しているため、Writingの最大が５文字以上の場合、最大値から1マイナスで空白埋め -->
          <xsl:when test="$OutcomeTotalMaxLen > 4">
            <xsl:value-of select="$outcometotaltemp"/>
            <xsl:call-template name="PrintSpaceZenkaku_UTL">
              <xsl:with-param name="count" select="$OutcomeTotalMaxLen - string-length($outcometotaltemp) -1"/>
            </xsl:call-template>
          </xsl:when>
          <!-- ○勝○敗が４文字以下の場合、最大値から勝敗数の文字数を引いた値で空白埋め -->
          <xsl:otherwise>
            <xsl:value-of select="$outcometotaltemp"/>
            <xsl:call-template name="PrintSpaceZenkaku_UTL">
              <xsl:with-param name="count" select="$OutcomeTotalMaxLen - string-length($outcometotaltemp)"/>
            </xsl:call-template>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:otherwise>
    </xsl:choose>
    <!-- ======================================== -->
    <!--今場所成績（詳細）-->
    <!-- ======================================== -->
    <xsl:for-each select="Result/Result/Outcome/Writing">
      <xsl:value-of select="."/>
    </xsl:for-each>
    <!-- 改行 -->
    <xsl:value-of select="$LineFeed_UTL"/>
  </xsl:template>
  <!--=======================================================================================================-->
  <!--優勝三賞受賞力士選手タグテンプレート-->
  <!--=======================================================================================================-->
  <xsl:template match="Player" mode="yuusyousannsyoujusyou_KAKUNIN2">
    <!-- =================================== -->
    <!--力士名                               -->
    <!-- =================================== -->
    <xsl:if test="//Standing/Player/PlayerName/Formal[not(@*)]">
      <xsl:if test="PlayerForSumo/PreviousName/Formal[not(@*)]">
        <xsl:text>　</xsl:text>
        <xsl:value-of select="PlayerForSumo/PreviousName/Formal[not(@*)]"/>
        <xsl:text>改め</xsl:text>
        <!-- 改行 -->
        <xsl:value-of select="$LineFeed_UTL"/>
      </xsl:if>
      <!-- =================================== -->
      <!--力士名                               -->
      <!-- =================================== -->
      <xsl:value-of select="PlayerName/Formal[not(@*)]"/>
      <!-- =================================== -->
      <!--優勝の場合の「○度目」「初優勝」など-->
      <!--殊勲賞、敢闘賞、技能賞の「初」など-->
      <!-- =================================== -->
      <!-- 変数 -->
      <!-- 賞 -->
      <xsl:variable name="awardtemp">
        <xsl:call-template name="TranslateToRensuuText_UTL">
          <xsl:with-param name="Data" select="Result/Award/Count/Writing"/>
        </xsl:call-template>
      </xsl:variable>
      <!-- 力士名と賞の最大値 -->
      <xsl:variable name="PawardMaxLen">
        <!-- <xsl:value-of select="$PlaynameOtherMaxLen"/> -->
        <xsl:value-of select="10"/>
      </xsl:variable>
      <!-- ========================================== -->
      <!-- 表示処理                                   -->
      <!-- ========================================== -->
      <xsl:if test="Result/Award/Count/Writing">
        <xsl:text>（</xsl:text>
        <xsl:value-of select="$awardtemp"/>
        <xsl:text>）</xsl:text>
      </xsl:if>
    </xsl:if>
    <!-- 力士名の桁合わせ　-->
    <xsl:call-template name="PrintSpaceZenkaku_UTL">
      <xsl:with-param name="count" select="$allplayerMaxLen - string-length(PlayerName/Formal[not(@*)])"/>
    </xsl:call-template>
    <!-- 賞の桁合わせ -->
    <xsl:choose>
      <xsl:when test="Result/Award/Count/Writing">
        <xsl:call-template name="PrintSpaceZenkaku_UTL">
          <xsl:with-param name="count" select="$AwardMaxLen -  string-length(Result/Award/Count/Writing)"/>
        </xsl:call-template>
      </xsl:when>
      <xsl:otherwise>
        <xsl:call-template name="PrintSpaceZenkaku_UTL">
          <xsl:with-param name="count" select="$AwardMaxLen +2"/>
        </xsl:call-template>
      </xsl:otherwise>
    </xsl:choose>
    <!-- =================================== -->
    <!--場所成績                             -->
    <!-- =================================== -->
    <xsl:if test="//Standing/Player/Result[not(@*)]/ResultForSumo/SumoOutcomeTotal/Writing">
      <xsl:call-template name="TranslateToRensuuText_UTL">
        <xsl:with-param name="Data" select="Result[not(@*)]/ResultForSumo/SumoOutcomeTotal/Writing"/>
      </xsl:call-template>
    </xsl:if>
    <!-- =================================== -->
    <!--部屋・出身地                         -->
    <!-- =================================== -->
    <xsl:if test="Belong/Formal[not(@*)]">
      <xsl:text>（</xsl:text>
      <!--部屋-->
      <xsl:value-of select="PlayerForSumo/NativeCountry/Formal[not(@*)]"/>
      <xsl:value-of select="PlayerForSumo/NativeArea/Formal[not(@*)]"/>
      <xsl:text>・</xsl:text>
      <!--出身地-->
      <xsl:value-of select="Belong/Formal[not(@*)]"/>
      <xsl:text>）</xsl:text>
    </xsl:if>
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
      <xsl:for-each select=".//PlayerForSumo/NativeCity/Formal[not(@*)]">
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
