<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">
  <!-- ================================================================================= -->
  <!--　編集者用「共通スタイルシート」大相撲・中入り取組 -->
	<!--  4.0版 2015.06.30 プレーンテキスト版のプレーンテキスト表示用として新規公開　-->
	<!--  4.01版 2015.●.● pタグのMatchStartクラス（対戦開始情報）を追加（１段で編集する場合のみ） -->
	<!--                    pタグのOikomiStartクラス（追い込み開始情報）を追加（１段で編集する場合のみ） -->
  <!-- ================================================================================= -->
  <!-- ================================================================================= -->
  <!--【commonsetting定義】-->
  <!-- ================================================================================= -->
  <!-- 縦書き/横書き設定 -->
  <xsl:variable name="PTEXT_TATEYOKO_OS09_SET">
    <xsl:call-template name="PTEXT_TATEYOKO_OS09_SET"/>
  </xsl:variable>
  <!-- 力士名表示切替 -->
  <xsl:variable name="OS09_PLAYERNAME_DISPLAY_SET">
    <xsl:call-template name="OS09_PLAYERNAME_DISPLAY_SET"/>
  </xsl:variable>
  <!-- 過去の取組結果表示切替 -->
  <xsl:variable name="OS09_RESULT_DISPLAY_SET">
    <xsl:call-template name="OS09_RESULT_DISPLAY_SET"/>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- 縦書き/横書き設定 -->
  <!-- ================================================================================= -->
  <xsl:variable name="OS09_PTEXT_TATEYOKO">
    <xsl:choose>
      <xsl:when test="$PTEXT_TATEYOKO_OS09_SET = 0">
        <!-- 共通設定を適用 -->
        <xsl:value-of select="$PTEXT_TATEYOKO_SET"/>
      </xsl:when>
      <xsl:otherwise>
        <!-- 個別設定を適用 -->
        <xsl:value-of select="$PTEXT_TATEYOKO_OS09_SET"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- １ページ最大行数を取得 -->
  <!-- 判断条件は「印刷方向定義」「縦書き/横書き設定」 -->
  <!-- ================================================================================= -->
  <xsl:variable name="OS09_PRINT_MAXLINE">
    <xsl:choose>
      <!--Ａ４タテ印刷-->
      <xsl:when test="$PRINT_F_SET=1">
        <xsl:choose>
          <xsl:when test="$OS09_PTEXT_TATEYOKO=1">
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
          <xsl:when test="$OS09_PTEXT_TATEYOKO=1">
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
  <!-- １行最大折り返し文字数を取得 -->
  <!-- ================================================================================= -->
  <xsl:variable name="OS09_MAXLENGTH">
    <xsl:choose>
      <!--縦書きかつ、力士名が紙面表記の場合（印刷方向共通）-->
      <xsl:when test="$OS09_PTEXT_TATEYOKO=1 and $OS09_PLAYERNAME_DISPLAY_SET=1">
        <xsl:value-of select="15"/>
      </xsl:when>
      <!--Ａ４タテ印刷-->
      <xsl:when test="$PRINT_F_SET=1">
        <xsl:choose>
          <!-- 縦書き -->
          <xsl:when test="$OS09_PTEXT_TATEYOKO=1">
            <xsl:value-of select="$PRINT_MAXTEXT_TATE_TATE_SET"/>
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
          <!-- 縦書き -->
          <xsl:when test="$OS09_PTEXT_TATEYOKO=1">
            <xsl:value-of select="$PRINT_MAXTEXT_YOKO_TATE_SET"/>
          </xsl:when>
          <!-- 横書き -->
          <xsl:otherwise>
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
    <!-- 過去の取組結果表示の有無で処理を振り分け -->
    <xsl:choose>
      <!-- 表示有り -->
      <xsl:when test="$OS09_RESULT_DISPLAY_SET = 1">
        <xsl:apply-templates select="Body" mode="KAKUNIN2_RESULT"/>
      </xsl:when>
      <!-- 表示無し -->
      <xsl:otherwise>
        <xsl:apply-templates select="Body" mode="KAKUNIN2"/>
      </xsl:otherwise>
    </xsl:choose>
	</xsl:template>
	<!--=======================================================================================================-->
	<!-- 中入り取組テンプレート【過去の取組結果：有り】-->
	<!--=======================================================================================================-->
  <xsl:template match="Body" mode="KAKUNIN2_RESULT">
    <!--==================-->
    <!-- 変数定義 -->
    <!--==================-->
    <!-- 上段力士の最大長 -->
    <xsl:variable name="UpperPlayerNameMaxLength">
      <xsl:call-template name="GetPlayerNameMaxLength">
        <xsl:with-param name="PlayerIdx" select="1"/>
      </xsl:call-template>
    </xsl:variable>
    <!-- 下段力士の最大長 -->
    <xsl:variable name="LowerPlayerNameMaxLength">
      <xsl:call-template name="GetPlayerNameMaxLength">
        <xsl:with-param name="PlayerIdx" select="2"/>
      </xsl:call-template>
    </xsl:variable>
    <!-- 過去の取組結果の最大長 -->
    <xsl:variable name="ResultMaxLength">
      <xsl:call-template name="GetResultMaxLength"/>
    </xsl:variable>
    <!--==================-->
    <!-- レイアウト用の変数定義 -->
    <!--==================-->
    <!-- 上段力士エリア編集文字数-->
    <xsl:variable name="UpperPlayerAreaLength">
      <xsl:call-template name="GetPlayerAreaLength">
        <xsl:with-param name="PlayerNameMaxLength" select="$UpperPlayerNameMaxLength"/>
      </xsl:call-template>
    </xsl:variable>
    <!-- 下段力士エリア編集文字数 -->
    <xsl:variable name="LowerPlayerAreaLength">
      <xsl:call-template name="GetPlayerAreaLength">
        <xsl:with-param name="PlayerNameMaxLength" select="$LowerPlayerNameMaxLength"/>
      </xsl:call-template>
    </xsl:variable>
    <!-- 結果エリア編集文字数 -->
    <xsl:variable name="ResultAreaLength">
      <xsl:call-template name="GetResultAreaLength"/>
    </xsl:variable>
    <!--==================-->
    <!-- 本文編集         -->
    <!--==================-->
    <xsl:variable name="HonbunText">
      <!-- 中見出し -->
      <xsl:apply-templates select="Meta/Title" mode="KAKUNIN2">
        <xsl:with-param name="IndentNum" select="$UpperPlayerAreaLength + 2"/> 
      </xsl:apply-templates>
      <!-- Article -->
      <xsl:if test="Article/Paragraph">
        <xsl:value-of select="$WhiteSpaceZenkaku_UTL"/>
        <xsl:value-of select="Article/Paragraph"/>
        <xsl:value-of select="$LineFeed_UTL"/>
      </xsl:if>
      <!-- 見出し編集 -->
      <xsl:call-template name="EditHeader">
        <xsl:with-param name="UpperPlayerAreaLength" select="$UpperPlayerAreaLength"/>
        <xsl:with-param name="LowerPlayerAreaLength" select="$LowerPlayerAreaLength"/>
      </xsl:call-template>
      <!-- 取組編集 -->
      <xsl:variable name="MatchData">
        <xsl:apply-templates select="Match" mode="KAKUNIN2_TA">
          <xsl:with-param name="UpperPlayerAreaLength" select="$UpperPlayerAreaLength"/>
          <xsl:with-param name="LowerPlayerAreaLength" select="$LowerPlayerAreaLength"/>
          <xsl:with-param name="ResultMaxLength" select="$ResultMaxLength"/>
          <xsl:with-param name="ResultAreaLength" select="$ResultAreaLength"/>
        </xsl:apply-templates>
      </xsl:variable>
      <!-- pタグに設定するclass付加制御（OikomiStartを自動付加しない）のため排除処理を行う -->
      <xsl:call-template name="Taisen_SetNoClass_UTL">
        <xsl:with-param name="Data" select="$MatchData"/>
      </xsl:call-template>
      <!-- 本文内注釈編集 -->
      <xsl:apply-templates select="TextNote" mode="KAKUNIN2"/>
    </xsl:variable>
    <!--==================-->
    <!-- レイアウト処理   -->
    <!--==================-->
    <xsl:choose>
      <!-- 縦書き、力士名がフル表記"Formal"の場合は縦ロングでレイアウト -->
      <xsl:when test="$OS09_PTEXT_TATEYOKO = 1 and $OS09_PLAYERNAME_DISPLAY_SET = 2">
        <!-- １行文字数 -->
        <xsl:variable name="MatchMaxLineLength" select="$UpperPlayerAreaLength + $ResultAreaLength + $LowerPlayerAreaLength"/>
        <!-- レイアウト開始 -->
        <xsl:call-template name="KAKUNIN2_DIVS_TATELONG_LAYOUT_UTL">
          <!-- 本文要素 -->
          <xsl:with-param name="HONBUN_DATA" select="$HonbunText"/>
          <!-- 字解 -->
          <xsl:with-param name="JIKAI_DATA">
            <xsl:call-template name="Gaiji_KAKUNIN2"/>
          </xsl:with-param>
          <xsl:with-param name="LINE_MAX_LENGTH" select="$MatchMaxLineLength"/>
          <xsl:with-param name="PAGE_LINE_MAX" select="$OS09_PRINT_MAXLINE"/>
          <xsl:with-param name="ADD_LINE_COUNT_FLG" select="$ADD_LINE_COUNT_FLG_SET"/>
          <xsl:with-param name="TATEYOKO_FLG" select="$OS09_PTEXT_TATEYOKO"/>
          <xsl:with-param name="ADD_OIKOMI_CLASS_FLG" select="1"/>
        </xsl:call-template>
      </xsl:when>
      <!-- その他は共通DIVでレイアウト -->
      <xsl:otherwise>
        <!-- レイアウト開始 -->
        <xsl:call-template name="KAKUNIN2_DIVS_NORMAL_LAYOUT_UTL">
          <!-- 本文要素 -->
          <xsl:with-param name="HONBUN_DATA" select="$HonbunText"/>
          <!-- 字解 -->
          <xsl:with-param name="JIKAI_DATA">
            <xsl:call-template name="Gaiji_KAKUNIN2"/>
          </xsl:with-param>
          <xsl:with-param name="LINE_MAX_LENGTH" select="$OS09_MAXLENGTH"/>
          <xsl:with-param name="PAGE_LINE_MAX" select="$OS09_PRINT_MAXLINE"/>
          <xsl:with-param name="ADD_LINE_COUNT_FLG" select="$ADD_LINE_COUNT_FLG_SET"/>
          <xsl:with-param name="TATEYOKO_FLG" select="$OS09_PTEXT_TATEYOKO"/>
          <xsl:with-param name="ADD_OIKOMI_CLASS_FLG">
            <xsl:choose>
              <!-- １段で編集する場合はOikomiStartクラス表示あり -->
              <xsl:when test="$OS09_PTEXT_TATEYOKO != 1 or $OS09_PLAYERNAME_DISPLAY_SET != 1 or $OS09_RESULT_DISPLAY_SET = 1">
                <xsl:value-of select="1"/>
              </xsl:when>
              <xsl:otherwise>
                <xsl:value-of select="0"/>
              </xsl:otherwise>
            </xsl:choose>
          </xsl:with-param>
        </xsl:call-template>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!--=======================================================================================================-->
	<!-- 中入り取組テンプレート【過去の取組結果：無し】-->
	<!--=======================================================================================================-->
  <xsl:template match="Body" mode="KAKUNIN2">
    <!--==================-->
    <!-- 変数定義 -->
    <!--==================-->
    <!-- 上段力士の最大長 -->
    <xsl:variable name="UpperPlayerNameMaxLength">
      <xsl:call-template name="GetPlayerNameMaxLength">
        <xsl:with-param name="PlayerIdx" select="1"/>
      </xsl:call-template>
    </xsl:variable>
    <!-- 下段力士の最大長 -->
    <xsl:variable name="LowerPlayerNameMaxLength">
      <xsl:call-template name="GetPlayerNameMaxLength">
        <xsl:with-param name="PlayerIdx" select="2"/>
      </xsl:call-template>
    </xsl:variable>
    <!-- 過去の取組結果の最大長 -->
    <xsl:variable name="ResultMaxLength">
      <xsl:call-template name="GetResultMaxLength"/>
    </xsl:variable>
    <!--==================-->
    <!-- レイアウト用の変数定義 -->
    <!--==================-->
    <!-- 上段力士エリア編集文字数-->
    <xsl:variable name="UpperPlayerAreaLength">
      <xsl:call-template name="GetPlayerAreaLength">
        <xsl:with-param name="PlayerNameMaxLength" select="$UpperPlayerNameMaxLength"/>
      </xsl:call-template>
    </xsl:variable>
    <!-- 下段力士エリア編集文字数 -->
    <xsl:variable name="LowerPlayerAreaLength">
      <xsl:call-template name="GetPlayerAreaLength">
        <xsl:with-param name="PlayerNameMaxLength" select="$LowerPlayerNameMaxLength"/>
      </xsl:call-template>
    </xsl:variable>
    <!-- 結果エリア編集文字数 -->
    <xsl:variable name="ResultAreaLength">
      <xsl:call-template name="GetResultAreaLength"/>
    </xsl:variable>
    <!-- 取組の最大文字数 -->
    <xsl:variable name="MatchMaxLineLength" select="$UpperPlayerAreaLength + $ResultAreaLength + $LowerPlayerAreaLength"/>
    <!-- 中見出しのインデント -->
    <xsl:variable name="IndentNum">
      <xsl:choose>
        <!-- ２段で編集（縦書き、力士名が２字"Writing"） -->
        <xsl:when test="$OS09_PTEXT_TATEYOKO = 1 and $OS09_PLAYERNAME_DISPLAY_SET = 1">
          <xsl:value-of select="5"/>
        </xsl:when>
        <!-- １段で編集 -->
        <xsl:otherwise>
          <!-- 中見出しの長さ -->
          <xsl:variable name="TitleLength" select="string-length(Meta/Title)"/>
          <xsl:choose>
            <!-- １行の長さが長い場合は中央に寄せる -->
            <xsl:when test="$MatchMaxLineLength > $TitleLength">
              <xsl:value-of select="ceiling(($MatchMaxLineLength - $TitleLength) div 2)"/>
            </xsl:when>
            <xsl:otherwise>
              <xsl:value-of select="0"/>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <!-- 取組テキスト -->
    <xsl:variable name="MatchText">
      <xsl:choose>
        <!-- ２段で編集（縦書き、力士名が２字表記"Writing"の場合）-->
        <xsl:when test="$OS09_PTEXT_TATEYOKO = 1 and $OS09_PLAYERNAME_DISPLAY_SET = 1">
          <!-- 上段取組一覧の表示終了位置 -->
          <xsl:variable name="UpperMatchesLastNum">
            <xsl:value-of select="floor(count(Match) div 2)"/>
          </xsl:variable>
          <!-- 下段取組一覧の表示開始位置 -->
          <xsl:variable name="LowerMatchesFirstNum">
            <xsl:value-of select="$UpperMatchesLastNum + 1"/>
          </xsl:variable>
          <!-- 取組一覧（上段）を編集 -->
          <xsl:variable name="UpperMatches">
            <!-- 見出し編集 -->
            <xsl:call-template name="EditHeader">
              <xsl:with-param name="UpperPlayerAreaLength" select="$UpperPlayerAreaLength"/>
              <xsl:with-param name="LowerPlayerAreaLength" select="$LowerPlayerAreaLength"/>
            </xsl:call-template>
            <!-- 取組一覧編集 -->
            <xsl:apply-templates select="Match[position() &lt;= $UpperMatchesLastNum]" mode="KAKUNIN2_TA">
              <xsl:with-param name="UpperPlayerAreaLength" select="$UpperPlayerAreaLength"/>
              <xsl:with-param name="LowerPlayerAreaLength" select="$LowerPlayerAreaLength"/>
              <xsl:with-param name="ResultMaxLength" select="$ResultMaxLength"/>
              <xsl:with-param name="ResultAreaLength" select="$ResultAreaLength"/>
            </xsl:apply-templates>
          </xsl:variable>
          <!-- 取組一覧（下段）を編集 -->
          <xsl:variable name="LowerMatches">
            <!-- 取組一覧編集 -->
            <xsl:apply-templates select="Match[position() &gt;= $LowerMatchesFirstNum]" mode="KAKUNIN2_TA">
              <xsl:with-param name="UpperPlayerAreaLength" select="$UpperPlayerAreaLength"/>
              <xsl:with-param name="LowerPlayerAreaLength" select="$LowerPlayerAreaLength"/>
              <xsl:with-param name="ResultMaxLength" select="$ResultMaxLength"/>
              <xsl:with-param name="ResultAreaLength" select="$ResultAreaLength"/>
            </xsl:apply-templates>
          </xsl:variable>
          <!-- 上下の取組一覧を割り付け -->
          <xsl:call-template name="TABLE_LAYOUT_LeftRight_UTIL">
            <xsl:with-param name="DATA1_AREA" select="7"/>
            <xsl:with-param name="DATA2_AREA" select="7"/>
            <xsl:with-param name="DATA1" select="$UpperMatches"/>
            <xsl:with-param name="DATA2" select="$LowerMatches"/>
            <xsl:with-param name="SPACE" select="1"/>
          </xsl:call-template>
        </xsl:when>
        <!-- その他は１段で編集する -->
        <xsl:otherwise>
          <!-- 見出し編集 -->
          <xsl:call-template name="EditHeader">
            <xsl:with-param name="UpperPlayerAreaLength" select="$UpperPlayerAreaLength"/>
            <xsl:with-param name="LowerPlayerAreaLength" select="$LowerPlayerAreaLength"/>
          </xsl:call-template>
          <!-- 取組編集（全て）-->
          <xsl:variable name="MatchData">
            <xsl:apply-templates select="Match" mode="KAKUNIN2_TA">
              <xsl:with-param name="UpperPlayerAreaLength" select="$UpperPlayerAreaLength"/>
              <xsl:with-param name="LowerPlayerAreaLength" select="$LowerPlayerAreaLength"/>
              <xsl:with-param name="ResultMaxLength" select="$ResultMaxLength"/>
              <xsl:with-param name="ResultAreaLength" select="$ResultAreaLength"/>
            </xsl:apply-templates>
          </xsl:variable>
          <!-- pタグに設定するclass付加制御（OikomiStartを自動付加しない）のため排除処理を行う -->
          <xsl:call-template name="Taisen_SetNoClass_UTL">
            <xsl:with-param name="Data" select="$MatchData"/>
          </xsl:call-template>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <!--==================-->
    <!-- レイアウト -->
    <!--==================-->
    <xsl:call-template name="KAKUNIN2_DIVS_NORMAL_LAYOUT_UTL">
      <!-- 本文要素 -->
      <xsl:with-param name="HONBUN_DATA">
        <!-- 中見出し -->
        <xsl:apply-templates select="Meta/Title" mode="KAKUNIN2">
          <xsl:with-param name="IndentNum" select="$IndentNum"/> 
        </xsl:apply-templates>
        <!-- Article -->
        <xsl:if test="Article/Paragraph">
          <xsl:value-of select="$WhiteSpaceZenkaku_UTL"/>
          <xsl:value-of select="Article/Paragraph"/>
          <xsl:value-of select="$LineFeed_UTL"/>
        </xsl:if>
        <!-- 取組本文 -->
        <xsl:value-of select="$MatchText"/>
        <!-- 本文内注釈編集 -->
        <xsl:apply-templates select="TextNote" mode="KAKUNIN2"/>
      </xsl:with-param>
      <!-- 字解 -->
      <xsl:with-param name="JIKAI_DATA">
        <xsl:call-template name="Gaiji_KAKUNIN2"/>
      </xsl:with-param>
      <xsl:with-param name="LINE_MAX_LENGTH" select="$OS09_MAXLENGTH"/>
      <xsl:with-param name="PAGE_LINE_MAX" select="$OS09_PRINT_MAXLINE"/>
      <xsl:with-param name="ADD_LINE_COUNT_FLG" select="$ADD_LINE_COUNT_FLG_SET"/>
      <xsl:with-param name="TATEYOKO_FLG" select="$OS09_PTEXT_TATEYOKO"/>
      <xsl:with-param name="ADD_OIKOMI_CLASS_FLG">
        <xsl:choose>
          <!-- １段で編集する場合はOikomiStartクラス表示あり -->
          <xsl:when test="$OS09_PTEXT_TATEYOKO != 1 or $OS09_PLAYERNAME_DISPLAY_SET != 1 or $OS09_RESULT_DISPLAY_SET = 1">
            <xsl:value-of select="1"/>
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="0"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:with-param>
    </xsl:call-template>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 力士エリア編集文字数 -->
  <!--=======================================================================================================-->
  <xsl:template name="GetPlayerAreaLength">
    <!-- パラメータ：力士名最大長（上段、下段） -->
    <xsl:param name="PlayerNameMaxLength"/>
    <xsl:choose>
      <!-- 力士名がフル表記"Formal"の場合は５固定-->
      <xsl:when test="$OS09_PLAYERNAME_DISPLAY_SET = 2">
        <xsl:value-of select="5"/>
      </xsl:when>
      <!-- 最大力士名が２文字未満 -->
      <xsl:when test="$PlayerNameMaxLength &lt; 2">
        <!-- ２固定 -->
        <xsl:value-of select="2"/>
      </xsl:when>
      <!-- その他は最大長を使用 -->
      <xsl:otherwise>
        <xsl:value-of select="$PlayerNameMaxLength"/>
      </xsl:otherwise> 
    </xsl:choose>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 結果エリア編集文字数 -->
  <!--=======================================================================================================-->
  <xsl:template name="GetResultAreaLength">
    <!-- 過去の取組結果表示の有無で処理を振り分け -->
    <xsl:choose>
      <!-- 表示有り -->
      <xsl:when test="$OS09_RESULT_DISPLAY_SET = 1">
        <xsl:variable name="TempNum">
          <xsl:call-template name="GetResultMaxLength"/>
        </xsl:variable>
        <xsl:value-of select="$TempNum + 4"/>
      </xsl:when>
      <!-- 表示無し -->
      <xsl:otherwise>
        <xsl:choose>
          <!-- 力士名が紙面表記の場合は３固定（幕内通算勝利数＋棒） -->
          <xsl:when test="$OS09_PLAYERNAME_DISPLAY_SET = 1">
            <xsl:value-of select="3"/>
          </xsl:when>
          <!-- フル表記の場合は４固定（幕内通算勝利数＋棒＋空白） -->
          <xsl:otherwise>
            <xsl:value-of select="4"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 力士名の表記取得（対戦型レイアウト） -->
  <!--=======================================================================================================-->
  <xsl:template match="Match/Player" mode="KAKUNIN2_TA">
    <xsl:param name="LeftOrRight"/>
    <xsl:param name="PlayerAreaLength"/>
    <!-- 力士名 -->
    <xsl:call-template name="AddBR_KAKUNIN_OSCOM2">
      <xsl:with-param name="Length" select="$PlayerAreaLength"/>
      <xsl:with-param name="LeftOrRight" select="$LeftOrRight"/>
      <xsl:with-param name="KakkoHamidashiFlg" select="0"/>
      <!-- Writing、Formal切替有り -->
      <xsl:with-param name="Data">
        <xsl:apply-templates select="PlayerName" mode="KAKUNIN2">
          <xsl:with-param name="PlayerAreaLength" select="$PlayerAreaLength"/>
        </xsl:apply-templates>
      </xsl:with-param>
    </xsl:call-template>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 取組編集（対戦型レイアウト）-->
  <!--=======================================================================================================-->
  <xsl:template match="Match" mode="KAKUNIN2_TA">
    <!-- 東西（上下）力士名の最大長 -->
    <xsl:param name="UpperPlayerAreaLength"/>
    <xsl:param name="LowerPlayerAreaLength"/>
    <!-- 過去取組の最大長 -->
    <xsl:param name="ResultMaxLength"/>
    <!-- 結果エリア編集文字数 -->
    <xsl:param name="ResultAreaLength"/>
    <!-- １段で編集する場合 -->
    <xsl:if test="$OS09_PTEXT_TATEYOKO != 1 or $OS09_PLAYERNAME_DISPLAY_SET != 1 or $OS09_RESULT_DISPLAY_SET = 1">
      <!-- pタグにclassを設定 -->
      <xsl:value-of select="$MatchClass_UTL"/>
    </xsl:if>
    <!--======================-->
    <!-- 上段力士名 -->
    <!--======================-->
    <xsl:variable name="UpperPlayerName">
      <xsl:apply-templates select="Player[1]" mode="KAKUNIN2_TA">
        <xsl:with-param name="LeftOrRight" select="2"/><!-- スペース補完のため -->
        <xsl:with-param name="PlayerAreaLength" select="$UpperPlayerAreaLength"/>
      </xsl:apply-templates>
    </xsl:variable>
    <!--======================-->
    <!-- 結果情報 -->
    <!--======================-->
    <xsl:variable name="ResultAreaInfo">
      <!-- 上段力士：通算勝数、十両表記 -->
      <xsl:choose>
        <!-- 幕内通算勝数 -->
        <xsl:when test="Player[1]/Result/Result[@Period='幕内通算']/ResultForSumo/SumoOutcomeTotal/Writing">
          <xsl:value-of select="Player[1]/Result/Result[@Period='幕内通算']/ResultForSumo/SumoOutcomeTotal/Writing"/>
        </xsl:when>
        <!-- 十両力士の表記（過去成績表示有りの場合のみ編集） -->
        <xsl:when test="$OS09_RESULT_DISPLAY_SET = 1 and Player[1]/PlayerForSumo/SumoGrade/Writing">
          <xsl:value-of select="Player[1]/PlayerForSumo/SumoGrade/Writing"/>
        </xsl:when>
        <!-- 相手が十両の場合 -->
        <xsl:otherwise>
          <!-- 過去の取組結果表示の有無で処理振り分け -->
          <xsl:choose>
            <!-- 表示有りは空白 -->
            <xsl:when test="$OS09_RESULT_DISPLAY_SET = 1">
              <xsl:text>　</xsl:text>
            </xsl:when>
            <!-- 表示無しはバツ -->
            <xsl:otherwise>
              <xsl:text>×</xsl:text>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:otherwise>
      </xsl:choose>
      <!-- 過去の取組結果 -->
      <xsl:choose>
        <!-- 表示有り -->
        <xsl:when test="$OS09_RESULT_DISPLAY_SET = 1">
          <xsl:text>（</xsl:text>
          <xsl:choose>
            <!-- 結果有り -->
            <xsl:when test="Player[1]/Result = true()">
              <!-- 上段力士の結果を編集 -->
              <xsl:apply-templates select="Player[1]/Result" mode="KAKUNIN2"/>
            </xsl:when>
            <!-- 結果無し -->
            <xsl:otherwise>
              <!-- 空白 -->
              <xsl:call-template name="PrintSpaceZenkaku_UTL">
                <xsl:with-param name="count" select="$ResultMaxLength"/>
              </xsl:call-template>
            </xsl:otherwise>
          </xsl:choose>
          <xsl:text>）</xsl:text>
        </xsl:when>
        <!-- 表示無し -->
        <xsl:otherwise>
          <xsl:text>―</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <!-- 下段力士：通算勝数、十両表記 -->
      <xsl:choose>
        <!-- 幕内通算勝数 -->
        <xsl:when test="Player[2]/Result/Result[@Period='幕内通算']/ResultForSumo/SumoOutcomeTotal/Writing">
          <xsl:value-of select="Player[2]/Result/Result[@Period='幕内通算']/ResultForSumo/SumoOutcomeTotal/Writing"/>
        </xsl:when>
        <!-- 十両力士の表記（過去成績表示有りの場合のみ編集） -->
        <xsl:when test="$OS09_RESULT_DISPLAY_SET = 1 and Player[2]/PlayerForSumo/SumoGrade/Writing">
          <xsl:value-of select="Player[2]/PlayerForSumo/SumoGrade/Writing"/>
        </xsl:when>
        <!-- 相手が十両の場合 -->
        <xsl:otherwise>
          <!-- 過去の取組結果表示の有無で処理振り分け -->
          <xsl:choose>
            <!-- 表示有りは空白 -->
            <xsl:when test="$OS09_RESULT_DISPLAY_SET = 1">
              <xsl:text>　</xsl:text>
            </xsl:when>
            <!-- 表示無しはバツ -->
            <xsl:otherwise>
              <xsl:text>×</xsl:text>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:otherwise>
      </xsl:choose>
      <!-- 過去対戦結果無し、力士名がフル表記は空白付き -->
      <xsl:if test="$OS09_RESULT_DISPLAY_SET != 1 and $OS09_PLAYERNAME_DISPLAY_SET = 2">
        <xsl:text>　</xsl:text>
      </xsl:if>
      <xsl:value-of select="$LineFeed_UTL"/>
    </xsl:variable>
    <!--======================-->
    <!-- 下段力士名 -->
    <!--======================-->
    <xsl:variable name="LowerPlayerName">
      <xsl:apply-templates select="Player[2]" mode="KAKUNIN2_TA">
        <xsl:with-param name="LeftOrRight" select="2"/>
        <xsl:with-param name="PlayerAreaLength" select="$LowerPlayerAreaLength"/>
      </xsl:apply-templates>
    </xsl:variable>
    <!-- 力士情報、結果情報を整形する -->
    <xsl:call-template name="TaisenLayout_TORIKUMI_OSCOM">
      <xsl:with-param name="PLAYER_INFO_1" select="$UpperPlayerName"/>
      <xsl:with-param name="PLAYER_INFO_2" select="$LowerPlayerName"/>
      <xsl:with-param name="RESULT_AREA_INFO" select="$ResultAreaInfo"/>
      <xsl:with-param name="PLAYER1_AREA_LENGTH" select="$UpperPlayerAreaLength"/>
      <xsl:with-param name="PLAYER2_AREA_LENGTH" select="$LowerPlayerAreaLength"/>
      <xsl:with-param name="RESULT_AREA_LENGTH" select="$ResultAreaLength"/>
    </xsl:call-template>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 中見出し編集 -->
  <!--=======================================================================================================-->
  <xsl:template match="Body/Meta/Title" mode="KAKUNIN2">
    <!-- インデント（空白）数 -->
    <xsl:param name="IndentNum" select="0"/>
    <!-- インデント出力 -->
    <xsl:call-template name="PrintSpaceZenkaku_UTL">
      <xsl:with-param name="count" select="$IndentNum"/>
    </xsl:call-template>
    <!-- 中見出し出力 -->
    <xsl:value-of select="."/>
    <!-- 改行 -->
    <xsl:value-of select="$LineFeed_UTL"/>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- ヘッダー編集 -->
  <!--=======================================================================================================-->
  <xsl:template name="EditHeader">
    <!-- 力士エリアの編集文字数 -->
    <xsl:param name="UpperPlayerAreaLength"/>
    <xsl:param name="LowerPlayerAreaLength"/>
    <!-- 力士カラムの長さ（通算勝数の分を加算） -->
    <xsl:variable name="UpperPlayerColumnLength" select="$UpperPlayerAreaLength + 1"/>
    <xsl:variable name="LowerPlayerColumnLength" select="$LowerPlayerAreaLength + 1"/>    
    <!-- 過去の取組結果を持つ取組を展開 -->
    <xsl:for-each select="Match[Player/Result/Result][1]">
      <!--====================-->
      <!-- １行目（過去の取組場所名） -->
      <!--====================-->
      <xsl:if test="$OS09_RESULT_DISPLAY_SET = 1">
        <!-- 上段力士名（空白） -->
        <xsl:call-template name="PrintSpaceZenkaku_UTL">
          <xsl:with-param name="count" select="$UpperPlayerColumnLength + 1"/>
        </xsl:call-template>
        <!-- 上段力士から過去の取組場所名を編集 -->
        <xsl:for-each select="Player[1]/Result/Result[@Period != '幕内通算']">
          <xsl:value-of select="substring(@Period,3,1)" />
        </xsl:for-each>
        <!-- 下段力士名（空白） -->
        <xsl:call-template name="PrintSpaceZenkaku_UTL">
          <xsl:with-param name="count" select="$LowerPlayerColumnLength + 1"/>
        </xsl:call-template>
        <!-- 改行 -->
        <xsl:value-of select="$LineFeed_UTL"/>
      </xsl:if>
      <!--====================-->
      <!-- ２行目（力士の東西＋過去の取組場所の年度）-->
      <!--====================-->
      <!-- 上段力士の東西 -->
      <xsl:text>（</xsl:text>
      <xsl:choose>
        <xsl:when test="Player[1]/PlayerForSumo/SumoGrade/Direction">
          <xsl:value-of select="Player[1]/PlayerForSumo/SumoGrade/Direction"/>
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>　</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:text>）</xsl:text>
      <!-- 空白調整 -->
      <xsl:call-template name="PrintSpaceZenkaku_UTL">
        <xsl:with-param name="count" select="$UpperPlayerColumnLength - 3"/>
      </xsl:call-template>
      <!-- 過去の取組結果 -->
      <xsl:choose>
        <!-- 表示有り -->
        <xsl:when test="$OS09_RESULT_DISPLAY_SET = 1">
          <!-- 空白 -->
          <xsl:text>　</xsl:text>
          <!-- 上段力士から過去の取組場所の年を編集 -->
          <xsl:for-each select="Player[1]/Result/Result[@Period != '幕内通算']">
            <xsl:choose>
              <!-- １つ前と違う年度なら表示 -->
              <xsl:when test="substring(preceding-sibling::Result[1]/@Period,1,2) != substring(@Period,1,2)">
                <xsl:call-template name="RensuuHenkan">
                  <xsl:with-param name="Sts" select="4"/>
                  <xsl:with-param name="Pdata" select="substring(@Period,1,2)"/>
                </xsl:call-template>
              </xsl:when>
              <!-- 一致は空白 -->
              <xsl:otherwise>
                <xsl:text>　</xsl:text>
              </xsl:otherwise>
            </xsl:choose>
          </xsl:for-each>
          <!-- 空白 -->
          <xsl:text>　</xsl:text>
        </xsl:when>
        <!-- 表示無し -->
        <xsl:otherwise>
          <xsl:text>　</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <!-- 下段力士の東西 -->
      <xsl:text>（</xsl:text>
      <xsl:choose>
        <xsl:when test="Player[2]/PlayerForSumo/SumoGrade/Direction">
          <xsl:value-of select="Player[2]/PlayerForSumo/SumoGrade/Direction"/>
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>　</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:text>）</xsl:text>
      <!-- 空白調整 -->
      <xsl:call-template name="PrintSpaceZenkaku_UTL">
        <xsl:with-param name="count" select="$LowerPlayerColumnLength - 3"/>
      </xsl:call-template>
      <!-- 改行 -->
      <xsl:value-of select="$LineFeed_UTL"/>
    </xsl:for-each>
  </xsl:template>
	<!--=======================================================================================================-->
	<!-- 取組編集（力士名の折り返し無し） -->
	<!--=======================================================================================================-->
  <xsl:template match="Match" mode="KAKUNIN2">
    <!-- 東西（上下）力士名の最大長 -->
    <xsl:param name="UpperPlayerNameMaxLength"/>
    <xsl:param name="LowerPlayerNameMaxLength"/>
    <!-- 過去の取組の最大長 -->
    <xsl:param name="ResultMaxLength" select="0"/>
    <!--======================-->
    <!-- 上段力士 -->
    <!--======================-->
    <!-- 力士名 -->
    <xsl:variable name="UpperPlayerName">
      <xsl:apply-templates select="Player[1]/PlayerName" mode="KAKUNIN2"/>
    </xsl:variable>
    <xsl:value-of select="$UpperPlayerName"/>
    <xsl:call-template name="PrintSpaceZenkaku_UTL">
      <xsl:with-param name="count" select="$UpperPlayerNameMaxLength - string-length($UpperPlayerName)"/>
    </xsl:call-template>
    <!-- 通算勝数、十両表記 -->
    <xsl:choose>
      <!-- 幕内通算勝数 -->
      <xsl:when test="Player[1]/Result/Result[@Period='幕内通算']/ResultForSumo/SumoOutcomeTotal/Writing">
        <xsl:value-of select="Player[1]/Result/Result[@Period='幕内通算']/ResultForSumo/SumoOutcomeTotal/Writing"/>
      </xsl:when>
      <!-- 十両力士表記 -->
      <xsl:when test="Player[1]/PlayerForSumo/SumoGrade/Writing">
        <xsl:value-of select="Player[1]/PlayerForSumo/SumoGrade/Writing"/>
      </xsl:when>
      <!-- 両方無い場合は空白を編集 -->
      <xsl:otherwise>
        <xsl:text>　</xsl:text>
      </xsl:otherwise>
    </xsl:choose>
    <!-- 幕内通算勝数 -->
    <!--======================-->
    <!-- 過去の取組結果 -->
    <!--======================-->
    <xsl:choose>
      <!-- 表示有り -->
      <xsl:when test="$OS09_RESULT_DISPLAY_SET = 1">
        <xsl:choose>
          <!-- 結果有り -->
          <xsl:when test="Player[1]/Result = true()">
            <xsl:text>（</xsl:text>
            <!-- 上段力士の結果を編集 -->
            <xsl:apply-templates select="Player[1]/Result" mode="KAKUNIN2"/>
            <xsl:text>）</xsl:text>
          </xsl:when>
          <!-- 結果無し -->
          <xsl:otherwise>
            <xsl:text>（</xsl:text>
            <!-- 空白 -->
            <xsl:call-template name="PrintSpaceZenkaku_UTL">
              <xsl:with-param name="count" select="$ResultMaxLength"/>
            </xsl:call-template>
            <xsl:text>）</xsl:text>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:when>
      <!-- 表示無し -->
      <xsl:otherwise>
        <xsl:text>―</xsl:text>
      </xsl:otherwise>
    </xsl:choose>
    <!--======================-->
    <!-- 下段力士 -->
    <!--======================-->
    <!-- 通算勝数、十両表記 -->
    <xsl:choose>
      <!-- 幕内通算勝数 -->
      <xsl:when test="Player[2]/Result/Result[@Period='幕内通算']/ResultForSumo/SumoOutcomeTotal/Writing">
        <xsl:value-of select="Player[2]/Result/Result[@Period='幕内通算']/ResultForSumo/SumoOutcomeTotal/Writing"/>
      </xsl:when>
      <!-- 十両力士表記 -->
      <xsl:when test="Player[2]/PlayerForSumo/SumoGrade/Writing">
        <xsl:value-of select="Player[2]/PlayerForSumo/SumoGrade/Writing"/>
      </xsl:when>
      <!-- 両方無い場合は空白を編集 -->
      <xsl:otherwise>
        <xsl:text>　</xsl:text>
      </xsl:otherwise>
    </xsl:choose>
    <!--力士名-->
    <xsl:variable name="LowerPlayerName">
      <xsl:apply-templates select="Player[2]/PlayerName" mode="KAKUNIN2"/>
    </xsl:variable>
    <xsl:value-of select="$LowerPlayerName"/>
    <xsl:call-template name="PrintSpaceZenkaku_UTL">
      <xsl:with-param name="count" select="$LowerPlayerNameMaxLength - string-length($LowerPlayerName)"/>
    </xsl:call-template>
    <!-- 改行 -->
    <xsl:value-of select="$LineFeed_UTL"/>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 過去の取組結果編集 -->
  <!--=======================================================================================================-->  
  <xsl:template match="Player/Result" mode="KAKUNIN2">
    <xsl:for-each select="Result[@Period != '幕内通算']/Outcome/Writing">
      <xsl:value-of select="." />
    </xsl:for-each>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 力士名の表記取得 -->
  <!--=======================================================================================================-->  
  <xsl:template match="Player/PlayerName" mode="KAKUNIN2">
    <xsl:param name="PlayerAreaLength" select="0"/>
    <xsl:choose>
      <!-- Writing -->
      <xsl:when test="$OS09_PLAYERNAME_DISPLAY_SET = 1 and Writing">
        <xsl:value-of select="Writing"/>
      </xsl:when>
      <!-- Formal -->
      <xsl:when test="$OS09_PLAYERNAME_DISPLAY_SET = 2 and Formal[not(@*)]">
        <xsl:choose>
          <!-- ２字以下の名前は３文字幅で字取り編集 -->
          <xsl:when test="string-length(Formal[not(@*)]) &lt; 3">
            <xsl:call-template name="FillSpace_UTL">
              <xsl:with-param name="Data">
                <xsl:value-of select="Formal[not(@*)]"/>
              </xsl:with-param>
              <xsl:with-param name="AreaLength">
                <xsl:value-of select="3"/>
              </xsl:with-param>
            </xsl:call-template>
          </xsl:when>
          <!-- ３文字以上はそのまま編集 -->
          <xsl:otherwise>
            <xsl:value-of select="Formal[not(@*)]"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:when>
      <!-- 想定外の表示設定、タグ無し -->
      <xsl:otherwise>
        <xsl:text>　　</xsl:text>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 力士名の最大長を取得 -->
  <!--=======================================================================================================-->
  <xsl:template name="GetPlayerNameMaxLength">
    <!-- 力士の位置（1:上段、2:下段） -->
    <xsl:param name="PlayerIdx"/>
    <!-- 力士名の表示対象 -->
    <xsl:variable name="PLAYERNAME_DISPLAY_NODE">
      <xsl:choose>
        <!-- Writing -->
        <xsl:when test="$OS09_PLAYERNAME_DISPLAY_SET = 1">
          <xsl:value-of select="'Writing'"/>
        </xsl:when>
        <!-- Formal -->
        <xsl:when test="$OS09_PLAYERNAME_DISPLAY_SET = 2">
          <xsl:value-of select="'Formal'"/>
        </xsl:when>
      </xsl:choose>
    </xsl:variable>
    <!-- 指定された力士の位置、表示対象の最大長を取得 -->
    <xsl:choose>
      <xsl:when test="count(Match/Player[$PlayerIdx]) &gt; 0">
        <xsl:for-each select="Match/Player[$PlayerIdx]">
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
  <!-- 過去の取組結果の最大長を取得 -->
  <!--=======================================================================================================-->
  <xsl:template name="GetResultMaxLength">
    <xsl:choose>
      <xsl:when test="count(Match/Player) &gt; 0">
        <xsl:for-each select="Match/Player">
          <xsl:sort select="count(Result/Result[@Period != '幕内通算'])" data-type="number" order="descending"/>
          <xsl:if test="position() = 1">
            <xsl:value-of select="count(Result/Result[@Period != '幕内通算'])"/>
          </xsl:if>
        </xsl:for-each>
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="0"/>
      </xsl:otherwise>
    </xsl:choose>  
  </xsl:template>
	<!--=======================================================================================================-->
	<!-- 本文内注釈編集 -->
	<!--=======================================================================================================-->
  <xsl:template match="Body/TextNote" mode="KAKUNIN2">
    <xsl:value-of select="." />
    <xsl:value-of select="$LineFeed_UTL"/>
  </xsl:template>
	<!--=======================================================================================================-->
	<!-- 字解編集 -->
	<!--=======================================================================================================-->
	<xsl:template name="Gaiji_KAKUNIN2">
		<!-- 字解編集 -->
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
                  <xsl:when test="$OS09_PLAYERNAME_DISPLAY_SET = 1 and $ParentName='Writing'">
                    <xsl:call-template name="Gaiji_EDT"/>
                  </xsl:when>
                  <!-- Formal表示時（フル表記の字解を編集） -->
                  <xsl:when test="$OS09_PLAYERNAME_DISPLAY_SET = 2 and $ParentName='Formal' and not(@*)">
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
