<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">
  <!-- ================================================================================= -->
  <!--　編集者用「共通スタイルシート」大相撲・郷土力士星取表 -->
  <!--  4.0版　2015.06.30 プレーンテキスト版のプレーンテキスト表示用として新規公開　-->
  <!-- ================================================================================= -->
  <!--=========================================================================-->
  <!-- プレーンテキストテンプレート -->
  <!--=========================================================================-->
  <!-- ============================================== -->
  <!-- 力士名                                         -->
  <!-- ============================================== -->
  <!-- WritingとFormal4字が同じため、Writing(4字)とフル表記の切り替えとする　-->
  <xsl:variable name="OS15_PLAYERNAME_DISPLAY_SET">
    <xsl:call-template name="OS15_PLAYERNAME_DISPLAY_SET"/>
  </xsl:variable>
  <!-- ============================================== -->
  <!-- 出身地                                         -->
  <!-- ============================================== -->
  <!-- WritingとFormal3字が同じため、Wrinting(3字)、フル表記、市町村付きで切り替える　-->
  <xsl:variable name="OS15_CITY_DISPLAY_SET">
    <xsl:call-template name="OS15_CITY_DISPLAY_SET"/>
  </xsl:variable>
  <!-- ============================================== -->
  <!-- 出身部屋                                       -->
  <!-- ============================================== -->
  <!-- WritingとFormal2字が同じため、Writing(2字)、フル表記、3字で切り替える　-->
  <xsl:variable name="OS15_BELONG_DISPLAY_SET">
    <xsl:call-template name="OS15_BELONG_DISPLAY_SET"/>
  </xsl:variable>
  <!-- ========================================================= -->
  <!-- 変数                                                      -->
  <!-- ========================================================= -->
  <!-- ============================ -->
  <!-- 力士名の最大文字数           -->
  <!-- Writing、Formal4字は４文字なので処理なし、Formalの場合のみ考慮 -->
  <!-- ============================ -->
  <xsl:variable name="PlayerNameMaxLen">
    <xsl:call-template name="GetTagsMaxLength_UTL">
      <xsl:with-param name="TargetPath" select="//PlayerName/Formal[not(@*)]"/>
    </xsl:call-template>
  </xsl:variable>
  <!-- ============================ -->
  <!-- 出身地の最大文字数           -->
  <!-- Writing、Formal3字は３文字なので処理なし、Formalの場合のみ考慮 -->
  <!-- ============================ -->
  <xsl:variable name="CityMaxLen">
    <xsl:call-template name="GetTagsMaxLength_UTL">
      <xsl:with-param name="TargetPath" select="//PlayerForSumo/NativeCity/Formal[not(@*)]"/>
    </xsl:call-template>
  </xsl:variable>
  <!-- ============================ -->
  <!-- 出身地（市町村名付き）の最大文字数           -->
  <!-- ============================ -->
  <xsl:variable name="CityNameMaxLen">
    <xsl:call-template name="GetTagsMaxLength_UTL">
      <xsl:with-param name="TargetPath" select="//PlayerForSumo/NativeCity/Formal[@Display='市町村付']"/>
    </xsl:call-template>
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
  <!-- ======================================================== -->
  <!-- 確認プレーン（起点）　                                   -->
  <!-- ======================================================== -->
  <xsl:template match="SportsData" mode="KAKUNIN2">
    <!-- Ａ４縦印刷時のフォントサイズ切り替え -->
    <!-- Ａ４縦印刷で出身地がフル表記の時のみ、９ｐｔで表示　-->
    <xsl:choose>
      <xsl:when test="($PRINT_F_SET = 1) and ($OS15_CITY_DISPLAY_SET = 2)">
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
    <!-- ================================================== -->
    <!-- 本文内注釈編集                                     -->
    <!-- ================================================== -->
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
  <!-- =========================================================================== -->
  <!--星取表テンプレート                                                           -->
  <!-- =========================================================================== -->
  <xsl:template name="hositorihyou_KAKUNIN2">
    <!-- ========================================================= -->
    <!-- 見出し部分の表示                                          -->
    <!-- ========================================================= -->
    <!-- Head/Meta部分 -->
    <xsl:text>　　☆☆</xsl:text>
    <xsl:value-of select="Head/Meta/Title"/>
    <xsl:text>☆☆　</xsl:text>
    <!-- 【北海道】など　-->
    <xsl:if test="Head/Limited/LocalInfo">
      <xsl:text>【</xsl:text>
      <xsl:value-of select="Head/Limited/LocalInfo"/>
      <xsl:text>】　</xsl:text>
      <!-- ３文字分固定を確保するための処理 -->
      <xsl:if test="string-length(Head/Limited/LocalInfo) = 2">
        <xsl:text>　</xsl:text>
      </xsl:if>
      <!-- ================================================================= -->
      <!-- 力士名が４文字（Writing、Formal4字）でなく、フル表示した際、
　　　　　５文字以上の場合に空白を入れる処理
      ====================================================================== -->
      <xsl:if test="($OS15_PLAYERNAME_DISPLAY_SET = 2) and ($PlayerNameMaxLen > 4)">
        <xsl:call-template name="PrintSpaceZenkaku_UTL">
          <xsl:with-param name="count" select="$PlayerNameMaxLen - 3"/>
        </xsl:call-template>
      </xsl:if>
      <!-- ================================================================= -->
      <!-- 出身地が３文字（Writing、Formal3字）でなく、フル表示した際、
　　　　　４文字以上の場合に空白を入れる処理
      ====================================================================== -->
      <xsl:if test="($OS15_CITY_DISPLAY_SET = 2) and ($CityMaxLen > 3)">
        <xsl:call-template name="PrintSpaceZenkaku_UTL">
          <xsl:with-param name="count" select="$CityMaxLen - 3"/>
        </xsl:call-template>
      </xsl:if>
      <!-- ================================================================= -->
      <!-- 出身地が３文字（市町村付き）が４文字以上の場合に空白を入れる処理
      ====================================================================== -->
      <xsl:if test="($OS15_CITY_DISPLAY_SET = 3) and ($CityNameMaxLen > 3)">
        <xsl:call-template name="PrintSpaceZenkaku_UTL">
          <xsl:with-param name="count" select="$CityNameMaxLen - 3"/>
        </xsl:call-template>
      </xsl:if>
      <!-- ================================================================= -->
      <!-- 部屋が２文字以上の場合に空白を入れる処理
      ====================================================================== -->
      <xsl:if test="($OS15_BELONG_DISPLAY_SET = 2) and ($BelongMaxLen > 2)">
        <xsl:call-template name="PrintSpaceZenkaku_UTL">
          <xsl:with-param name="count" select="$BelongMaxLen - 2"/>
        </xsl:call-template>
      </xsl:if>
      <!-- ================================================================= -->
      <!-- 部屋が３文字の場合に空白を入れる処理
      ====================================================================== -->
      <xsl:if test="$OS15_BELONG_DISPLAY_SET = 3">
        <xsl:text>　</xsl:text>
      </xsl:if>
    </xsl:if>
    <!-- ====================================================== -->
    <!-- 今場所成績（詳細）の見出し                             -->
    <!-- ====================================================== -->
    <xsl:call-template name="seisekimidasi_KAKUNIN2"/>
    <!-- 改行 -->
    <xsl:value-of select="$LineFeed_UTL"/>
    <!-- ====================================================== -->
    <!-- Body/Meta部分                                          -->
    <!-- ====================================================== -->
    <xsl:for-each select="Body">
      <!--Title　【幕　下】など　-->
      <xsl:text>　</xsl:text>
      <xsl:for-each select="Meta/Title">
        <xsl:value-of select="."/>
      </xsl:for-each>
      <!-- 改行 -->
      <xsl:value-of select="$LineFeed_UTL"/>
      <!-- ====================================================== -->
      <!-- Article                                                -->
      <!-- ====================================================== -->
      <xsl:if test="Article/Paragraph">
        <xsl:text>　</xsl:text>
        <xsl:value-of select="Article/Paragraph"/>
        <!-- 改行 -->
        <xsl:value-of select="$LineFeed_UTL"/>
      </xsl:if>
      <!-- ======================================================= -->
      <!-- Standing                                                -->
      <!-- ======================================================= -->
      <xsl:for-each select="Standing">
        <xsl:apply-templates select="Player" mode="hositorihyou_KAKUNIN2"/>
      </xsl:for-each>
    </xsl:for-each>
  </xsl:template>
  <!-- =========================================================================== -->
  <!--成績見出しテンプレート                                                       -->
  <!-- =========================================================================== -->
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
  <!-- =========================================================================== -->
  <!-- 成績見出しテンプレート                                                      -->
  <!-- =========================================================================== -->
  <xsl:template name="seisekimidasi_kobetu_KAKUNIN2">
    <xsl:param name="POSITION"/>
    <xsl:if test="Body/Standing/Player/Result/Result[$POSITION]/@Period">
      <xsl:call-template name="RensuuHenkan">
        <xsl:with-param name="Sts" select="3"/>
        <xsl:with-param name="Pdata" select="Body/Standing/Player/Result/Result[$POSITION]/@Period[1]"/>
      </xsl:call-template>
    </xsl:if>
  </xsl:template>
  <!-- =========================================================================== -->
  <!-- 星取表選手タグテンプレート                                                  -->
  <!-- =========================================================================== -->
  <xsl:template match="Player" mode="hositorihyou_KAKUNIN2">
    <!-- ==================================================== -->
    <!-- 変数                                                 -->
    <!-- ==================================================== -->
    <!-- ============================ -->
    <!-- 力士名の表示                 -->
    <!-- ============================ -->
    <xsl:variable name="PlayerName">
      <xsl:choose>
        <xsl:when test="$OS15_PLAYERNAME_DISPLAY_SET = 1">
          <!-- <xsl:value-of select="PlayerName/Writing"/>  -->
          <xsl:value-of select="PlayerName/Formal[@Display='4字']"/>
        </xsl:when>
        <xsl:when test="$OS15_PLAYERNAME_DISPLAY_SET = 2">
          <xsl:value-of select="PlayerName/Formal[not(@*)]"/>
          <!-- ４字取りを基準に行を揃えるための空白処理 -->
          <!-- ４字以下は４字に揃える、５字以上は力士の最大長に合わせて、空白１字を付ける -->
          <xsl:choose>
            <xsl:when test="$PlayerNameMaxLen &lt; 5">
              <xsl:call-template name="PrintSpaceZenkaku_UTL">
                <xsl:with-param name="count" select="4 - string-length(PlayerName/Formal[not(@*)])"/>
              </xsl:call-template>
            </xsl:when>
            <xsl:otherwise>
              <xsl:call-template name="PrintSpaceZenkaku_UTL">
                <xsl:with-param name="count" select="$PlayerNameMaxLen - string-length(PlayerName/Formal[not(@*)]) + 1"/>
              </xsl:call-template>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="PlayerName/Formal[@Display='4字']"/>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <!-- ============================ -->
    <!-- 出身地の表示                 -->
    <!-- ============================ -->
    <xsl:variable name="CityName">
      <xsl:choose>
        <xsl:when test="$OS15_CITY_DISPLAY_SET = 1">
          <!-- <xsl:value-of select="PlayerForSumo/NativeCity/Writing"/>  -->
          <xsl:value-of select="PlayerForSumo/NativeCity/Formal[@Display='3字']"/>
        </xsl:when>
        <xsl:when test="$OS15_CITY_DISPLAY_SET = 2">
          <xsl:value-of select="PlayerForSumo/NativeCity/Formal[not(@*)]"/>
          <!-- ３字取りを基準に行を揃えるための空白処理 -->
          <!-- ３字以下は３字に揃える、４字以上は最大長に合わせる -->
          <xsl:choose>
            <xsl:when test="$CityMaxLen  &lt; 4">
              <xsl:call-template name="PrintSpaceZenkaku_UTL">
                <xsl:with-param name="count" select="3 - string-length(PlayerForSumo/NativeCity/Formal[not(@*)])"/>
              </xsl:call-template>
            </xsl:when>
            <xsl:otherwise>
              <xsl:call-template name="PrintSpaceZenkaku_UTL">
                <xsl:with-param name="count" select="$CityMaxLen - string-length(PlayerForSumo/NativeCity/Formal[not(@*)])"/>
              </xsl:call-template>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:when>
        <xsl:when test="$OS15_CITY_DISPLAY_SET = 3">
          <xsl:value-of select="PlayerForSumo/NativeCity/Formal[@Display='市町村付']"/>
          <!-- ３字取りを基準に行を揃えるための空白処理 -->
          <!-- ３字以下は３字に揃える、４字以上は最大長に合わせる -->
          <xsl:choose>
            <xsl:when test="$CityNameMaxLen  &lt; 4">
              <xsl:call-template name="PrintSpaceZenkaku_UTL">
                <xsl:with-param name="count" select="3 - string-length(PlayerForSumo/NativeCity/Formal[@Display='市町村付'])"/>
              </xsl:call-template>
            </xsl:when>
            <xsl:otherwise>
              <xsl:call-template name="PrintSpaceZenkaku_UTL">
                <xsl:with-param name="count" select="$CityNameMaxLen - string-length(PlayerForSumo/NativeCity/Formal[@Display='市町村付'])"/>
              </xsl:call-template>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="PlayerForSumo/NativeCity/Writing"/>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <!-- ============================ -->
    <!-- 出身部屋の表示               -->
    <!-- ============================ -->
    <xsl:variable name="Belong">
      <xsl:choose>
        <xsl:when test="$OS15_BELONG_DISPLAY_SET = 1">
          <xsl:value-of select="Belong/Writing"/>
        </xsl:when>
        <xsl:when test="$OS15_BELONG_DISPLAY_SET = 2">
          <xsl:value-of select="Belong/Formal[not(@*)]"/>
        </xsl:when>
        <xsl:when test="$OS15_BELONG_DISPLAY_SET = 3">
          <xsl:value-of select="Belong/Formal[@Display='3字']"/>
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="Belong/Writng"/>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <!-- ==================================================== -->
    <!-- 表示処理                                             -->
    <!-- ==================================================== -->
    <!-- =================================== -->
    <!--「勝負越」☆、★など　               -->
    <!-- =================================== -->
    <xsl:choose>
      <xsl:when test="(Result/ResultForSumo/OutcomeAttribute/Writing) and not(PlayerForSumo/PreviousName)">
        <xsl:value-of select="Result/ResultForSumo/OutcomeAttribute/Writing"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:text>　</xsl:text>
      </xsl:otherwise>
    </xsl:choose>
    <!-- =================================== -->
    <!-- 力士名                              -->
    <!-- =================================== -->
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
    <!-- =================================== -->
    <!--「地位」　東３、西５など　           -->
    <!-- =================================== -->
    <xsl:choose>
      <xsl:when test="PlayerForSumo/SumoGrade/Writing">
        <xsl:value-of select="PlayerForSumo/SumoGrade/Writing"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:text>　</xsl:text>
      </xsl:otherwise>
    </xsl:choose>
    <!--空白-->
    <xsl:text>　</xsl:text>
    <!-- =================================== -->
    <!-- 出身市町村                          -->
    <!-- =================================== -->
    <xsl:choose>
      <xsl:when test="PlayerForSumo/NativeCity/Formal[not(@*)]">
        <xsl:value-of select="$CityName"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:text>　　　</xsl:text>
      </xsl:otherwise>
    </xsl:choose>
    <!-- =================================== -->
    <!-- 出身部屋                            -->
    <!-- =================================== -->
    <xsl:choose>
      <xsl:when test="Belong/Formal[not(@*)]">
        <xsl:text>（</xsl:text>
        <xsl:value-of select="$Belong"/>
        <xsl:text>）</xsl:text>
        <!-- ２字取りが基準（Writing、Formal2字）とし、フル表記の時に
　　　　　　　　　最大文字数に合わせて、空白を埋める処理             -->
        <xsl:if test="$OS15_BELONG_DISPLAY_SET = 2">
          <xsl:if test="$BelongMaxLen > 2">
            <xsl:call-template name="PrintSpaceZenkaku_UTL">
              <xsl:with-param name="count" select="$BelongMaxLen - string-length(Belong/Formal[not(@*)])"/>
            </xsl:call-template>
          </xsl:if>
        </xsl:if>
      </xsl:when>
      <xsl:otherwise>
        <xsl:text>　</xsl:text>
      </xsl:otherwise>
    </xsl:choose>
    <!-- ====================================== -->
    <!--引退 or 今場所成績-->
    <!-- ====================================== -->
    <xsl:choose>
      <xsl:when test="PlayerForSumo/Retirement/Formal[not(@*)]">
        <!-- ==================================== -->
        <!--引退                                  -->
        <!-- ==================================== -->
        <xsl:value-of select="PlayerForSumo/Retirement/Formal[not(@*)]"/>
        <xsl:text>　</xsl:text>
      </xsl:when>
      <xsl:otherwise>
        <!-- ==================================== -->
        <!--今場所成績                            -->
        <!-- ==================================== -->
        <xsl:choose>
          <xsl:when test="Result/ResultForSumo/SumoOutcomeTotal/Writing">
            <xsl:value-of select="Result/ResultForSumo/SumoOutcomeTotal/Writing"/>
          </xsl:when>
          <xsl:otherwise>
            <xsl:text>　　　</xsl:text>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:otherwise>
    </xsl:choose>
    <!--今場所成績（詳細）-->
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
      <xsl:for-each select=".//Head/Meta/Title">
        <xsl:call-template name="Gaiji_EDT"/>
      </xsl:for-each>
      <xsl:for-each select=".//Head/Limited/LocalInfo">
        <xsl:call-template name="Gaiji_EDT"/>
      </xsl:for-each>
      <xsl:for-each select=".//Meta/Title">
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
      <!--字解-->
      <xsl:value-of select="$JIKAI_DATA"/>
    </xsl:if>
  </xsl:template>
</xsl:stylesheet>
