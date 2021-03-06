<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">
  <!-- ================================================================================= -->
  <!--　編集者用「共通スタイルシート」大相撲・優勝三賞受賞力士 -->
	<!--  4.0版 2015.06.30 プレーンテキスト版のプレーンテキスト表示用として新規公開　-->
  <!-- ================================================================================= -->
  <!-- ================================================================================= -->
  <!--【commonsetting定義】-->
  <!-- ================================================================================= -->
  <!-- 縦書き/横書き設定 -->
  <xsl:variable name="PTEXT_TATEYOKO_OS17_SET">
    <xsl:call-template name="PTEXT_TATEYOKO_OS17_SET"/>
  </xsl:variable>
  <!-- 力士名表示切替 -->
  <xsl:variable name="OS17_PLAYERNAME_DISPLAY_SET">
    <!-- Writing固定(Formalと一致するため) -->
    <xsl:value-of select="1"/>
  </xsl:variable>
  <!-- 部屋・出身地表示切替 -->
  <xsl:variable name="OS17_BELONG_DISPLAY_SET">
    <xsl:call-template name="OS17_BELONG_DISPLAY_SET"/>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- 縦書き/横書き設定 -->
  <!-- ================================================================================= -->
  <xsl:variable name="OS17_PTEXT_TATEYOKO">
    <xsl:choose>
      <xsl:when test="$PTEXT_TATEYOKO_OS17_SET = 0">
        <!-- 共通設定を適用 -->
        <xsl:value-of select="$PTEXT_TATEYOKO_SET"/>
      </xsl:when>
      <xsl:otherwise>
        <!-- 個別設定を適用 -->
        <xsl:value-of select="$PTEXT_TATEYOKO_OS17_SET"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- １ページ最大行数を取得 -->
  <!-- 判断条件は「印刷方向定義」「縦書き/横書き設定」 -->
  <!-- ================================================================================= -->
  <xsl:variable name="OS17_PRINT_MAXLINE">
    <xsl:choose>
      <!--Ａ４タテ印刷-->
      <xsl:when test="$PRINT_F_SET=1">
        <xsl:choose>
          <!-- 縦書き -->
          <xsl:when test="$OS17_PTEXT_TATEYOKO=1">
            <xsl:value-of select="$PRINT_MAXLINES_TATE_TATE_SET"/>
          </xsl:when>
          <!-- 横書き -->
          <xsl:otherwise>
            <xsl:value-of select="$PRINT_MAXLINES_TATE_YOKO_SET"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:when>
      <!--Ａ４ヨコ印刷-->
      <xsl:otherwise>
        <xsl:choose>
          <!-- 縦書き -->
          <xsl:when test="$OS17_PTEXT_TATEYOKO=1">
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
  <!-- １行最大折り返し文字数を取得 -->
  <!-- ================================================================================= -->
  <xsl:variable name="OS17_MAXLENGTH">
    <xsl:choose>
      <!--Ａ４タテ印刷-->
      <xsl:when test="$PRINT_F_SET=1">
        <xsl:choose>
          <!-- 縦書き -->
          <xsl:when test="$OS17_PTEXT_TATEYOKO=1">
            <xsl:choose>
              <!-- 部屋・出身地が紙面表記の場合は15固定 -->
              <xsl:when test="$OS17_BELONG_DISPLAY_SET = 1">
                <xsl:value-of select="15"/>
              </xsl:when>
              <!-- フル表記の場合は15固定 -->
              <xsl:otherwise>
                <xsl:value-of select="25"/>
              </xsl:otherwise>
            </xsl:choose>
          </xsl:when>
          <!-- 横書き -->
          <xsl:otherwise>
            <xsl:value-of select="$PRINT_MAXTEXT_TATE_YOKO_SET"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:when>
      <!--Ａ４ヨコ印刷-->
      <xsl:otherwise>
        <xsl:choose>
          <xsl:when test="$OS17_PTEXT_TATEYOKO=1">
            <!-- 縦書き -->
            <xsl:choose>
              <!-- 部屋・出身地が紙面表記の場合は15固定 -->
              <xsl:when test="$OS17_BELONG_DISPLAY_SET = 1">
                <xsl:value-of select="15"/>
              </xsl:when>
              <!-- フル表記の場合は15固定 -->
              <xsl:otherwise>
                <xsl:value-of select="25"/>
              </xsl:otherwise>
            </xsl:choose>
          </xsl:when>
          <xsl:otherwise>
            <!-- 横書き -->
            <xsl:value-of select="$PRINT_MAXTEXT_YOKO_YOKO_SET"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:variable>
	<!--=======================================================================================================-->
	<!--【プレーンテキスト版】スポーツデータタグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="SportsData" mode="KAKUNIN2">
    <!-- 縦書き／横書きで処理振り分け -->
    <xsl:choose>
      <!-- 縦書き -->
      <xsl:when test="$OS17_PTEXT_TATEYOKO = 1">
        <xsl:call-template name="EditTate"/>
      </xsl:when>
      <!-- 横書き -->
      <xsl:when test="$OS17_PTEXT_TATEYOKO = 2">
        <xsl:call-template name="EditYoko"/>
      </xsl:when>
    </xsl:choose>
	</xsl:template>
	<!--=======================================================================================================-->
	<!-- 縦書きテンプレート（起点） -->
	<!--=======================================================================================================-->
  <xsl:template name="EditTate">
    <!-- ==========================-->
    <!-- 優勝力士を編集 -->
    <!-- ==========================-->
    <xsl:variable name="WinnerText">
      <!-- 編集開始 -->
      <xsl:text>▽優勝力士</xsl:text>
      <xsl:value-of select="$LineFeed_UTL"/>
      <!-- 各ボディを編集 -->
      <xsl:apply-templates select="Body[Meta/DataType='優勝力士']" mode="KAKUNIN2_TATE"/>
    </xsl:variable>
    <!-- ==========================-->
    <!-- 三賞受賞力士を編集 -->
    <!-- ==========================-->
    <xsl:variable name="AwardText">
      <!-- 賞名の最大長を取得 -->
      <xsl:variable name="AwardNameMaxLength">
        <xsl:call-template name="GetTagsMaxLength_UTL">
          <xsl:with-param name="TargetPath" select="Body[Meta/DataType='三賞受賞力士']/Meta/Title"/>
        </xsl:call-template>
      </xsl:variable>
      <!-- 編集開始 -->
      <xsl:text>▽三賞受賞力士</xsl:text>
      <xsl:value-of select="$LineFeed_UTL"/>
      <!-- 各ボディを編集 -->
      <xsl:apply-templates select="Body[Meta/DataType='三賞受賞力士']" mode="KAKUNIN2_TATE">
        <xsl:with-param name="AwardNameMaxLength" select="$AwardNameMaxLength"/>
      </xsl:apply-templates>
    </xsl:variable>
    <!-- ==========================-->
    <!-- レイアウト開始 -->
    <!-- ==========================-->
    <xsl:choose>
      <!-- 部屋・出身が紙面表記の場合は通常DIVレイアウト -->
      <xsl:when test="$OS17_BELONG_DISPLAY_SET = 1">
        <xsl:call-template name="KAKUNIN2_DIVS_NORMAL_LAYOUT_UTL">
          <!-- 本文要素 -->
          <xsl:with-param name="HONBUN_DATA">
            <!-- 優勝力士 -->
            <xsl:value-of select="$WinnerText"/>
            <!-- 改行 -->
            <xsl:if test="$AwardText != ''">
              <xsl:value-of select="$LineFeed_UTL"/>
            </xsl:if>
            <!-- 三賞受賞力士 -->
            <xsl:value-of select="$AwardText"/>
          </xsl:with-param>
          <!-- 字解 -->
          <xsl:with-param name="JIKAI_DATA">
            <xsl:call-template name="Gaiji_KAKUNIN2"/>
          </xsl:with-param>
          <xsl:with-param name="LINE_MAX_LENGTH" select="$OS17_MAXLENGTH"/>
          <xsl:with-param name="PAGE_LINE_MAX" select="$OS17_PRINT_MAXLINE"/>
          <xsl:with-param name="ADD_LINE_COUNT_FLG" select="$ADD_LINE_COUNT_FLG_SET"/>
          <xsl:with-param name="TATEYOKO_FLG" select="$OS17_PTEXT_TATEYOKO"/>
        </xsl:call-template>
      </xsl:when>
      <!-- フル表記の場合は縦ロングレイアウト -->
      <xsl:when test="$OS17_BELONG_DISPLAY_SET = 2">
        <xsl:call-template name="KAKUNIN2_DIVS_TATELONG_LAYOUT_UTL">
          <!-- 本文要素 -->
          <xsl:with-param name="HONBUN_DATA">
            <!-- 優勝力士 -->
            <xsl:value-of select="$WinnerText"/>
            <!-- 改行 -->
            <xsl:if test="$AwardText != ''">
              <xsl:value-of select="$LineFeed_UTL"/>
            </xsl:if>
            <!-- 三賞受賞力士 -->
            <xsl:value-of select="$AwardText"/>
          </xsl:with-param>
          <!-- 字解 -->
          <xsl:with-param name="JIKAI_DATA">
            <xsl:call-template name="Gaiji_KAKUNIN2"/>
          </xsl:with-param>
          <xsl:with-param name="LINE_MAX_LENGTH" select="$OS17_MAXLENGTH"/>
          <xsl:with-param name="PAGE_LINE_MAX" select="$OS17_PRINT_MAXLINE"/>
          <xsl:with-param name="ADD_LINE_COUNT_FLG" select="$ADD_LINE_COUNT_FLG_SET"/>
          <xsl:with-param name="TATEYOKO_FLG" select="$OS17_PTEXT_TATEYOKO"/>
        </xsl:call-template>
      </xsl:when>
    </xsl:choose>
  </xsl:template>
  <!--=======================================================================================================-->
	<!-- 優勝力士の縦書き編集 -->
	<!--=======================================================================================================-->
	<xsl:template match="Body[Meta/DataType='優勝力士']" mode="KAKUNIN2_TATE">
    <!-- 階級名 -->
    <xsl:variable name="ClassName">
      <xsl:value-of select="Meta/Title"/>
    </xsl:variable>
    <!-- 力士情報展開 -->
    <xsl:for-each select="Standing/Player">
      <!--=============-->
      <!-- １行目 -->
      <!--=============-->
      <!-- 階級名 -->
      <xsl:value-of select="$ClassName"/>
      <!-- 力士名 -->
      <xsl:apply-templates select="PlayerName" mode="KAKUNIN2"/>
      <xsl:if test="Result/Award/Count/Writing">
        <!-- 空白 -->
        <xsl:value-of select="$WhiteSpaceZenkaku_UTL"/>
        <!-- 優勝回数 -->
        <xsl:value-of select="Result/Award/Count/Writing"/>
      </xsl:if>
      <!-- 改行 -->
      <xsl:value-of select="$LineFeed_UTL"/>
      <!--=============-->
      <!-- ２行目 -->
      <!--=============-->
      <!-- 勝敗内容 -->
      <xsl:variable name="OutcomeTotal">
        <!-- インデント -->
        <xsl:value-of select="$WhiteSpaceZenkaku_UTL"/>
        <!-- 勝敗内容 -->
        <xsl:value-of select="Result/ResultForSumo/SumoOutcomeTotal/Writing"/>
      </xsl:variable>
      <!-- 部屋・出身地 -->
      <xsl:variable name="BelongAndNativeCountry">
        <!-- 部屋名 -->
        <xsl:variable name="Belong">
          <xsl:apply-templates select="Belong" mode="KAKUNIN2"/>
        </xsl:variable>
        <!-- 出身地・国 -->
        <xsl:variable name="Native">
          <!-- 出身地（日本人力士） -->
          <xsl:apply-templates select="PlayerForSumo/NativeArea" mode="KAKUNIN2"/>
          <!-- 出身国（外国人力士） -->
          <xsl:apply-templates select="PlayerForSumo/NativeCountry" mode="KAKUNIN2"/>
        </xsl:variable>
        <!-- 部屋・出身地の表示設定に応じてレイアウト -->
        <xsl:choose>
          <!-- 紙面表記 -->
          <xsl:when test="$OS17_BELONG_DISPLAY_SET = 1">
            <!-- 部屋名 -->
            <xsl:value-of select="$Belong"/>
            <!-- 空白 -->
            <xsl:value-of select="$WhiteSpaceZenkaku_UTL"/>
            <!-- 出身地・国 -->
            <xsl:value-of select="$Native"/>
          </xsl:when>
          <!-- フル表記 -->
          <xsl:when test="$OS17_BELONG_DISPLAY_SET = 2">
            <!-- 部屋名 -->
            <xsl:value-of select="$Belong"/>
            <!-- 中点 -->
            <xsl:value-of select="'・'"/>
            <!-- 出身地・国 -->
            <xsl:value-of select="$Native"/>
          </xsl:when>
        </xsl:choose>
      </xsl:variable>
      <!-- 出力開始 -->
      <!-- 勝敗内容 -->
      <xsl:value-of select="$OutcomeTotal"/>
      <!-- 空白 -->
      <xsl:call-template name="PrintSpaceZenkaku_UTL">
        <xsl:with-param name="count" select="9 - string-length($OutcomeTotal)"/>
      </xsl:call-template>
      <!-- 部屋・出身地 -->
      <xsl:value-of select="$BelongAndNativeCountry"/>
      <!-- 改行 -->
      <xsl:value-of select="$LineFeed_UTL"/>
    </xsl:for-each>
  </xsl:template> 
  <!--=======================================================================================================-->
	<!-- 三賞受賞力士の縦書き編集 -->
	<!--=======================================================================================================-->
	<xsl:template match="Body[Meta/DataType='三賞受賞力士']" mode="KAKUNIN2_TATE">
    <!-- 賞名の最大長 -->
    <xsl:param name="AwardNameMaxLength"/>
    <!-- 賞名 -->
    <xsl:variable name="AwardName">
      <xsl:value-of select="Meta/Title"/>
    </xsl:variable>
    <!-- 受賞者の有無で処理振り分け -->
    <xsl:choose>
      <!-- 受賞者なし（記事型） -->
      <xsl:when test="Article/Paragraph">
        <!-- 賞名 -->
        <xsl:value-of select="$AwardName"/>
        <!-- 記事 -->
        <xsl:value-of select="Article/Paragraph"/>
        <!-- 改行 -->
        <xsl:value-of select="$LineFeed_UTL"/>
      </xsl:when>
      <!-- 受賞者あり -->
      <xsl:when test="Standing/Player">
        <xsl:for-each select="Standing/Player">
          <!-- 賞名、空白 -->
          <xsl:choose>
            <!-- 先頭は賞名 -->
            <xsl:when test="position() = 1">
              <xsl:value-of select="$AwardName"/>
              <xsl:call-template name="PrintSpaceZenkaku_UTL">
                <xsl:with-param name="count" select="$AwardNameMaxLength - string-length($AwardName)"/>
              </xsl:call-template>
            </xsl:when>
            <!-- ２人目以降は空白 -->
            <xsl:otherwise>
              <xsl:call-template name="PrintSpaceZenkaku_UTL">
                <xsl:with-param name="count" select="$AwardNameMaxLength"/>
              </xsl:call-template>
            </xsl:otherwise>
          </xsl:choose>
          <!-- 力士名 -->
          <xsl:apply-templates select="PlayerName" mode="KAKUNIN2"/>
          <!-- 優勝回数 -->
          <xsl:if test="Result/Award/Count/Writing">
            <xsl:text>（</xsl:text>
            <xsl:value-of select="Result/Award/Count/Writing"/>
            <xsl:text>）</xsl:text>
          </xsl:if>
          <!-- 改行 -->
          <xsl:value-of select="$LineFeed_UTL"/>
        </xsl:for-each>
      </xsl:when>
    </xsl:choose>
	</xsl:template> 
	<!--=======================================================================================================-->
	<!-- 横書きテンプレート（起点） -->
	<!--=======================================================================================================-->
  <xsl:template name="EditYoko">
    <!-- ==========================-->
    <!-- 優勝力士を編集 -->
    <!-- ==========================-->
    <xsl:variable name="WinnerText">
      <!-- 力士名最大長を取得 -->
      <xsl:variable name="PlayerNameMaxLength">
        <xsl:call-template name="GetPlayerNameMaxLength">
          <xsl:with-param name="TargetPath" select="Body[Meta/DataType='優勝力士']"/>
        </xsl:call-template>
      </xsl:variable>
      <!-- 優勝回数最大長を取得 -->
      <xsl:variable name="AwardCountMaxLength">
        <xsl:variable name="TempMaxLength">
          <xsl:call-template name="GetTagsMaxLength_UTL">
            <xsl:with-param name="TargetPath" select="Body[Meta/DataType='優勝力士']/Standing/Player/Result/Award/Count/Writing"/>
          </xsl:call-template>
        </xsl:variable>
        <xsl:choose>
          <!-- 要素が存在する場合は括弧分を加算 -->
          <xsl:when test="$TempMaxLength > 0">
            <xsl:value-of select="$TempMaxLength + 2"/>
          </xsl:when>
          <!-- 要素が存在ない場合はゼロ -->
          <xsl:otherwise>
            <xsl:value-of select="0"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:variable>
      <!-- 勝敗内容最大長を取得 -->
      <xsl:variable name="OutcomTotalMaxLength">
        <xsl:call-template name="GetTagsMaxLength_UTL">
          <xsl:with-param name="TargetPath" select="Body[Meta/DataType='優勝力士']/Standing/Player/Result/ResultForSumo/SumoOutcomeTotal/Writing"/>
        </xsl:call-template>
      </xsl:variable>
      <!-- 編集開始 -->
      <xsl:text>▽優勝力士</xsl:text>
      <xsl:value-of select="$LineFeed_UTL"/>
      <!-- 各ボディを編集 -->
      <xsl:apply-templates select="Body[Meta/DataType='優勝力士']" mode="KAKUNIN2_YOKO">
        <xsl:with-param name="PlayerNameMaxLength" select="$PlayerNameMaxLength"/>
        <xsl:with-param name="AwardCountMaxLength" select="$AwardCountMaxLength"/>
        <xsl:with-param name="OutcomTotalMaxLength" select="$OutcomTotalMaxLength"/>
      </xsl:apply-templates>
    </xsl:variable>
    <!-- ==========================-->
    <!-- 三賞受賞力士を編集 -->
    <!-- ==========================-->
    <xsl:variable name="AwardText">
      <!-- 賞名の最大長を取得 -->
      <xsl:variable name="AwardNameMaxLength">
        <xsl:call-template name="GetTagsMaxLength_UTL">
          <xsl:with-param name="TargetPath" select="Body[Meta/DataType='三賞受賞力士']/Meta/Title"/>
        </xsl:call-template>
      </xsl:variable>
      <!-- 力士名最大長を取得 -->
      <xsl:variable name="PlayerNameMaxLength">
        <xsl:call-template name="GetPlayerNameMaxLength">
          <xsl:with-param name="TargetPath" select="Body[Meta/DataType='三賞受賞力士']"/>
        </xsl:call-template>
      </xsl:variable>
      <!-- 編集開始 -->
      <xsl:text>▽三賞受賞力士</xsl:text>
      <xsl:value-of select="$LineFeed_UTL"/>
      <!-- 各ボディを編集 -->
      <xsl:apply-templates select="Body[Meta/DataType='三賞受賞力士']" mode="KAKUNIN2_YOKO">
        <xsl:with-param name="AwardNameMaxLength" select="$AwardNameMaxLength"/>
        <xsl:with-param name="PlayerNameMaxLength" select="$PlayerNameMaxLength"/>
      </xsl:apply-templates>
    </xsl:variable>
    <!-- ==========================-->
    <!-- レイアウト開始 -->
    <!-- ==========================-->
    <xsl:call-template name="KAKUNIN2_DIVS_NORMAL_LAYOUT_UTL">
      <!-- 本文要素 -->
      <xsl:with-param name="HONBUN_DATA">
        <!-- 優勝力士 -->
        <xsl:value-of select="$WinnerText"/>
        <!-- 改行 -->
        <xsl:if test="$AwardText != ''">
          <xsl:value-of select="$LineFeed_UTL"/>
        </xsl:if>
        <!-- 三賞受賞力士 -->
        <xsl:value-of select="$AwardText"/>
      </xsl:with-param>
      <!-- 字解 -->
      <xsl:with-param name="JIKAI_DATA">
        <xsl:call-template name="Gaiji_KAKUNIN2"/>
      </xsl:with-param>
      <xsl:with-param name="LINE_MAX_LENGTH" select="$OS17_MAXLENGTH"/>
      <xsl:with-param name="PAGE_LINE_MAX" select="$OS17_PRINT_MAXLINE"/>
      <xsl:with-param name="ADD_LINE_COUNT_FLG" select="$ADD_LINE_COUNT_FLG_SET"/>
      <xsl:with-param name="TATEYOKO_FLG" select="$OS17_PTEXT_TATEYOKO"/>
    </xsl:call-template>
  </xsl:template>
  <!--=======================================================================================================-->
	<!-- 優勝力士の横書き編集 -->
	<!--=======================================================================================================-->
	<xsl:template match="Body[Meta/DataType='優勝力士']" mode="KAKUNIN2_YOKO">
    <xsl:param name="PlayerNameMaxLength"/>
    <xsl:param name="AwardCountMaxLength"/>
    <xsl:param name="OutcomTotalMaxLength"/>
    <!-- 階級名 -->
    <xsl:variable name="ClassName">
      <xsl:value-of select="Meta/Title"/>
    </xsl:variable>
    <!-- 力士情報展開 -->
    <xsl:for-each select="Standing/Player">
      <!-- 階級名 -->
      <xsl:value-of select="$ClassName"/>
      <!-- 力士名 -->
      <xsl:variable name="PlayerName">
        <xsl:apply-templates select="PlayerName" mode="KAKUNIN2"/>
      </xsl:variable>
      <xsl:value-of select="$PlayerName"/>
      <!-- 優勝回数 -->
      <xsl:variable name="AwardCount">
        <xsl:if test="Result/Award/Count/Writing">
          <xsl:text>（</xsl:text>
          <xsl:value-of select="Result/Award/Count/Writing"/>
          <xsl:text>）</xsl:text>
        </xsl:if>
      </xsl:variable>
      <xsl:value-of select="$AwardCount"/>
      <!-- 空白調整 -->
      <xsl:call-template name="PrintSpaceZenkaku_UTL">
        <xsl:with-param name="count" select="$PlayerNameMaxLength - string-length($PlayerName)"/>
      </xsl:call-template>
      <xsl:call-template name="PrintSpaceZenkaku_UTL">
        <xsl:with-param name="count" select="$AwardCountMaxLength - string-length($AwardCount)"/>
      </xsl:call-template>
      <!-- 勝敗内容 -->
      <xsl:variable name="OutcomeTotal">
        <xsl:value-of select="Result/ResultForSumo/SumoOutcomeTotal/Writing"/>
      </xsl:variable>
      <xsl:value-of select="$OutcomeTotal"/>
      <xsl:call-template name="PrintSpaceZenkaku_UTL">
        <xsl:with-param name="count" select="$OutcomTotalMaxLength - string-length($OutcomeTotal)"/>
      </xsl:call-template>
      <!-- 部屋・出身地 -->
      <xsl:text>（</xsl:text>
      <!-- 部屋名 -->
      <xsl:apply-templates select="Belong" mode="KAKUNIN2"/>
      <xsl:text>・</xsl:text>
      <!-- 出身地（日本人力士のみ） -->
      <xsl:apply-templates select="PlayerForSumo/NativeArea" mode="KAKUNIN2"/>
      <!-- 出身国（外国人力士のみ） -->
      <xsl:apply-templates select="PlayerForSumo/NativeCountry" mode="KAKUNIN2"/>
      <xsl:text>）</xsl:text>
      <!-- 改行 -->
      <xsl:value-of select="$LineFeed_UTL"/>
    </xsl:for-each>
  </xsl:template> 
  <!--=======================================================================================================-->
	<!-- 三賞受賞力士の横書き編集 -->
	<!--=======================================================================================================-->
	<xsl:template match="Body[Meta/DataType='三賞受賞力士']" mode="KAKUNIN2_YOKO">
    <!-- 賞名の最大長 -->
    <xsl:param name="AwardNameMaxLength"/>
    <!-- 力士名の最大長 -->
    <xsl:param name="PlayerNameMaxLength"/>
    <!-- 賞名 -->
    <xsl:variable name="AwardName">
      <xsl:value-of select="Meta/Title"/>
    </xsl:variable>
    <!-- 受賞者の有無で処理振り分け -->
    <xsl:choose>
      <!-- 受賞者なし（記事型） -->
      <xsl:when test="Article/Paragraph">
        <!-- 賞名 -->
        <xsl:value-of select="$AwardName"/>
        <!-- 記事 -->
        <xsl:value-of select="Article/Paragraph"/>
        <!-- 改行 -->
        <xsl:value-of select="$LineFeed_UTL"/>
      </xsl:when>
      <!-- 受賞者あり -->
      <xsl:when test="Standing/Player">
        <xsl:for-each select="Standing/Player">
          <!-- 賞名、空白 -->
          <xsl:choose>
            <!-- 先頭は賞名 -->
            <xsl:when test="position() = 1">
              <xsl:value-of select="$AwardName"/>
              <xsl:call-template name="PrintSpaceZenkaku_UTL">
                <xsl:with-param name="count" select="$AwardNameMaxLength - string-length($AwardName)"/>
              </xsl:call-template>
            </xsl:when>
            <!-- ２人目以降は空白 -->
            <xsl:otherwise>
              <xsl:call-template name="PrintSpaceZenkaku_UTL">
                <xsl:with-param name="count" select="$AwardNameMaxLength"/>
              </xsl:call-template>
            </xsl:otherwise>
          </xsl:choose>
          <!-- 力士名 -->
          <xsl:variable name="PlayerName">
            <xsl:apply-templates select="PlayerName" mode="KAKUNIN2"/>
          </xsl:variable>
          <xsl:value-of select="$PlayerName"/>
          <!-- 優勝回数 -->
          <xsl:if test="Result/Award/Count/Writing">
            <xsl:text>（</xsl:text>
            <xsl:value-of select="Result/Award/Count/Writing"/>
            <xsl:text>）</xsl:text>
          </xsl:if>
          <!-- 改行 -->
          <xsl:value-of select="$LineFeed_UTL"/>
        </xsl:for-each>
      </xsl:when>
    </xsl:choose>
	</xsl:template> 
  <!--=======================================================================================================-->
  <!-- 力士名の最大長を取得 -->
  <!--=======================================================================================================-->
  <xsl:template name="GetPlayerNameMaxLength">
    <!-- 検索対象のパス -->
    <xsl:param name="TargetPath"/>
    <!-- 力士名の表示対象 -->
    <xsl:variable name="PLAYERNAME_DISPLAY_NODE">
      <xsl:choose>
        <!-- Writing -->
        <xsl:when test="$OS17_PLAYERNAME_DISPLAY_SET = 1">
          <xsl:value-of select="'Writing'"/>
        </xsl:when>
        <!-- Formal -->
        <xsl:when test="$OS17_PLAYERNAME_DISPLAY_SET = 2">
          <xsl:value-of select="'Formal'"/>
        </xsl:when>
      </xsl:choose>
    </xsl:variable>
    <!-- 表示対象の最大長を取得 -->
    <xsl:choose>
      <xsl:when test="count($TargetPath//Player) &gt; 0">
        <xsl:for-each select="$TargetPath//Player">
          <xsl:sort select="string-length(PlayerName/*[name()=$PLAYERNAME_DISPLAY_NODE and not(@*)])" data-type="number" order="descending"/>
          <xsl:if test="position() = 1">
            <xsl:value-of select="string-length(PlayerName/*[name()=$PLAYERNAME_DISPLAY_NODE and not(@*)])"/>
          </xsl:if>
        </xsl:for-each>
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="0"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 力士名の編集 -->
  <!--=======================================================================================================-->  
  <xsl:template match="Player/PlayerName" mode="KAKUNIN2">
    <xsl:param name="PlayerNameMaxLength" select="0"/>
    <xsl:choose>
      <!-- Writing -->
      <xsl:when test="$OS17_PLAYERNAME_DISPLAY_SET = 1 and Writing">
        <xsl:value-of select="Writing"/>
      </xsl:when>
      <!-- Formal -->
      <xsl:when test="$OS17_PLAYERNAME_DISPLAY_SET = 2 and Formal[not(@*)]">
        <xsl:value-of select="Formal[not(@*)]"/>
      </xsl:when>
      <!-- 想定外の表示設定、タグ無し -->
      <xsl:otherwise>
        <xsl:text>　　　</xsl:text>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 部屋、出身地・国の編集 -->
  <!--=======================================================================================================-->  
  <xsl:template match="Player/Belong|PlayerForSumo/NativeArea|PlayerForSumo/NativeCountry" mode="KAKUNIN2">
    <xsl:choose>
      <!-- Writing -->
      <xsl:when test="$OS17_BELONG_DISPLAY_SET = 1 and Writing">
        <xsl:value-of select="Writing"/>
      </xsl:when>
      <!-- Formal（フル） -->
      <xsl:when test="$OS17_BELONG_DISPLAY_SET = 2 and Formal[not(@*)]">
        <xsl:value-of select="Formal[not(@*)]"/>
      </xsl:when>
    </xsl:choose>
  </xsl:template>
	<!--=======================================================================================================-->
	<!-- 字解編集 -->
	<!--=======================================================================================================-->
	<xsl:template name="Gaiji_KAKUNIN2">
		<!-- 字解情報を編集 -->
		<xsl:variable name="JIKAI_DATA">
      <!-- 字解タグの親要素を展開 -->
      <xsl:for-each select="//*[KdGaiji]">
        <!-- 親要素のノード名取得 -->
        <xsl:variable name="ParentName" select="name(.)"/>
        <!-- 表示開始 -->
        <xsl:choose>
          <!-- 親要素がWriting、Formal -->
          <xsl:when test="$ParentName='Writing' or $ParentName='Formal'">
            <!-- 先祖要素に応じて処理 -->
            <xsl:choose>
              <!-- 力士名（表示切替有り） -->
              <xsl:when test="ancestor::PlayerName">
                <xsl:choose>
                  <!-- Writing表示時 -->
                  <xsl:when test="$OS17_PLAYERNAME_DISPLAY_SET = 1 and $ParentName='Writing'">
                    <xsl:call-template name="Gaiji_EDT"/>
                  </xsl:when>
                  <!-- Formal表示時（フル表記の字解を編集） -->
                  <xsl:when test="$OS17_PLAYERNAME_DISPLAY_SET = 2 and $ParentName='Formal' and not(@*)">
                    <xsl:call-template name="Gaiji_EDT"/>
                  </xsl:when>
                </xsl:choose>
              </xsl:when>
              <!-- 部屋、出身地、出身国（表示切替有り） -->
              <xsl:when test="ancestor::Belong|ancestor::NativeArea|ancestor::NativeCountry">
                <xsl:choose>
                  <!-- Writing表示時 -->
                  <xsl:when test="$OS17_BELONG_DISPLAY_SET = 1 and $ParentName='Writing'">
                    <xsl:call-template name="Gaiji_EDT"/>
                  </xsl:when>
                  <!-- Formal表示時（フル表記の字解を編集） -->
                  <xsl:when test="$OS17_BELONG_DISPLAY_SET = 2 and $ParentName='Formal' and not(@*)">
                    <xsl:call-template name="Gaiji_EDT"/>
                  </xsl:when>
                </xsl:choose>
              </xsl:when>
              <!-- その他（表示切替が無い要素）はWritingのみ字解編集 -->
              <xsl:otherwise>
                <xsl:if test="$ParentName = 'Writing'">
                  <xsl:call-template name="Gaiji_EDT"/>
                </xsl:if>
              </xsl:otherwise>
            </xsl:choose>
          </xsl:when>
          <!-- その他はそのまま字解編集 -->
          <xsl:otherwise>
            <xsl:call-template name="Gaiji_EDT"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:for-each>
		</xsl:variable>
    <!--字解情報が存在した場合-->
    <xsl:if test="($JIKAI_DATA!='')">
      <!--字解見出し-->
      <xsl:text>字解情報</xsl:text>
      <xsl:value-of select="$LineFeed_UTL"/>
      <!--字解情報-->
      <xsl:value-of select="$JIKAI_DATA"/>
    </xsl:if>
	</xsl:template>
</xsl:stylesheet>
