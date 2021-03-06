<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">
  <!-- ================================================================================= -->
  <!--　編集者用「共通スタイルシート」大相撲・外国力士成績表 -->
	<!--  4.0版 2015.06.30 プレーンテキスト版のプレーンテキスト表示用として新規公開　-->
  <!-- ================================================================================= -->
  <!-- ================================================================================= -->
  <!--【commonsetting定義】-->
  <!-- ================================================================================= -->
  <!-- 縦書き/横書き設定 -->
  <xsl:variable name="PTEXT_TATEYOKO_OS16_SET">
    <xsl:call-template name="PTEXT_TATEYOKO_OS16_SET"/>
  </xsl:variable>
  <!-- 力士の表示切替 -->
  <xsl:variable name="OS16_PLAYERNAME_DISPLAY_SET">
    <xsl:call-template name="OS16_PLAYERNAME_DISPLAY_SET"/>
  </xsl:variable>
  <!-- 出身の表示切替 -->
  <xsl:variable name="OS16_BELONG_DISPLAY_SET">
    <!-- 切り替わる項目は下記のとおり -->
    <!-- ● 両力士の部屋名（紙面表記：２字）-->
    <!-- ● 上段力士の出身国（紙面表記：フル表記の空白埋め） -->
    <!-- ● 上段力士の出身市町村（紙面表記：フル表記の市町村名無し） -->
    <!-- ● 下段力士の出身都道府県（紙面表記：２字）※日本力士で出現-->
    <!-- ● 下段力士の出身国（紙面表記：２字）※外国力士で出現-->
    <!-- ● 下段力士の出身市町村（紙面表記：非表示） -->
    <xsl:call-template name="OS16_BELONG_DISPLAY_SET"/>
  </xsl:variable>
  <!--==================-->
  <!-- 変数定義 -->
  <!--==================-->
  <!-- ================================================================================= -->
  <!-- 縦書き/横書き設定 -->
  <!-- ================================================================================= -->
  <xsl:variable name="OS16_PTEXT_TATEYOKO">
    <xsl:choose>
      <xsl:when test="$PTEXT_TATEYOKO_OS16_SET = 0">
        <!-- 共通設定を適用 -->
        <xsl:value-of select="$PTEXT_TATEYOKO_SET"/>
      </xsl:when>
      <xsl:otherwise>
        <!-- 個別設定を適用 -->
        <xsl:value-of select="$PTEXT_TATEYOKO_OS16_SET"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- １ページ最大行数を取得 -->
  <!-- 判断条件は「印刷方向定義」「縦書き/横書き設定」 -->
  <!-- ================================================================================= -->
  <xsl:variable name="OS16_PRINT_MAXLINE">
    <xsl:choose>
      <!--Ａ４タテ印刷-->
      <xsl:when test="$PRINT_F_SET=1">
        <xsl:choose>
          <!-- 縦書き -->
          <xsl:when test="$OS16_PTEXT_TATEYOKO=1">
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
          <xsl:when test="$OS16_PTEXT_TATEYOKO=1">
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
  <xsl:variable name="OS16_MAXLENGTH">
    <xsl:choose>
      <!--Ａ４タテ印刷-->
      <xsl:when test="$PRINT_F_SET=1">
        <xsl:choose>
          <!-- 縦書き -->
          <xsl:when test="$OS16_PTEXT_TATEYOKO=1">
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
          <xsl:when test="$OS16_PTEXT_TATEYOKO=1">
            <xsl:value-of select="$PRINT_MAXTEXT_YOKO_TATE_SET"/>
          </xsl:when>
          <xsl:otherwise>
            <!-- 横書き -->
            <xsl:value-of select="$PRINT_MAXTEXT_YOKO_YOKO_SET"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- 上段力士の最大長を取得 -->
  <!-- ================================================================================= -->
  <xsl:variable name="UpperPlayerNameMaxLength">
    <xsl:call-template name="GetPlayerNameMaxLength">
      <xsl:with-param name="PlayerIdx" select="1"/>
    </xsl:call-template>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- 下段力士の最大長を取得 -->
  <!-- ================================================================================= -->
  <xsl:variable name="LowerPlayerNameMaxLength">
    <xsl:call-template name="GetPlayerNameMaxLength">
      <xsl:with-param name="PlayerIdx" select="2"/>
    </xsl:call-template>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- 力士名表示切替フラグを設定 -->
  <!-- ================================================================================= -->
  <xsl:variable name="PLAYERNAME_DISPLAY_SET">
    <xsl:value-of select="$OS16_PLAYERNAME_DISPLAY_SET"/>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- 部屋名表示切替フラグを設定 -->
  <!-- ================================================================================= -->
  <xsl:variable name="BELONG_DISPLAY_SET">
    <xsl:value-of select="$OS16_BELONG_DISPLAY_SET"/>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- 上段力士の出身国表示切替フラグを設定 -->
  <!-- ================================================================================= -->
  <xsl:variable name="UPPER_COUNTRY_DISPLAY_SET">
    <xsl:value-of select="$OS16_BELONG_DISPLAY_SET"/>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- 下段力士の出身国表示切替フラグを設定 -->
  <!-- ================================================================================= -->
  <xsl:variable name="LOWER_COUNTRY_DISPLAY_SET">
    <xsl:value-of select="$OS16_BELONG_DISPLAY_SET"/>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- 出身都道府県表示切替フラグを設定 -->
  <!-- ================================================================================= -->
  <xsl:variable name="AREA_DISPLAY_SET">
    <xsl:value-of select="$OS16_BELONG_DISPLAY_SET"/>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- 出身市町村表示切替フラグを設定 -->
  <!-- ================================================================================= -->
  <xsl:variable name="CITY_DISPLAY_SET">
    <xsl:value-of select="$OS16_BELONG_DISPLAY_SET"/>
  </xsl:variable>
	<!--=======================================================================================================-->
	<!--【プレーンテキスト版】スポーツデータタグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="SportsData" mode="KAKUNIN2">
    <!-- 本文テキスト -->
    <xsl:variable name="BodyText">
      <!-- ボディ編集 -->
      <xsl:apply-templates select="Body" mode="KAKUNIN2"/>
    </xsl:variable>
    <xsl:choose>
      <!-- 縦書きのフル表記は縦ロングでレイアウト -->
      <xsl:when test="$OS16_PTEXT_TATEYOKO = 1 and ($OS16_PLAYERNAME_DISPLAY_SET = 2 or $OS16_BELONG_DISPLAY_SET = 2)">
        <xsl:call-template name="KAKUNIN2_DIVS_TATELONG_LAYOUT_UTL">
          <!-- 本文要素 -->
          <xsl:with-param name="HONBUN_DATA">
            <!-- 本文テキスト -->
            <xsl:value-of select="$BodyText"/>
          </xsl:with-param>
          <!-- 字解 -->
          <xsl:with-param name="JIKAI_DATA">
            <xsl:call-template name="Gaiji_KAKUNIN2"/>
          </xsl:with-param>
          <xsl:with-param name="LINE_MAX_LENGTH" select="25"/>
          <xsl:with-param name="PAGE_LINE_MAX" select="$OS16_PRINT_MAXLINE"/>
          <xsl:with-param name="ADD_LINE_COUNT_FLG" select="$ADD_LINE_COUNT_FLG_SET"/>
          <xsl:with-param name="TATEYOKO_FLG" select="$OS16_PTEXT_TATEYOKO"/>
        </xsl:call-template>
      </xsl:when>
      <!-- その他は共通DIVでレイアウト -->
      <xsl:otherwise>
        <xsl:call-template name="KAKUNIN2_DIVS_NORMAL_LAYOUT_UTL">
          <!-- 本文要素 -->
          <xsl:with-param name="HONBUN_DATA">
            <!-- 本文テキスト -->
            <xsl:value-of select="$BodyText"/>
          </xsl:with-param>
          <!-- 字解 -->
          <xsl:with-param name="JIKAI_DATA">
            <xsl:call-template name="Gaiji_KAKUNIN2"/>
          </xsl:with-param>
          <xsl:with-param name="LINE_MAX_LENGTH" select="$OS16_MAXLENGTH"/>
          <xsl:with-param name="PAGE_LINE_MAX" select="$OS16_PRINT_MAXLINE"/>
          <xsl:with-param name="ADD_LINE_COUNT_FLG" select="$ADD_LINE_COUNT_FLG_SET"/>
          <xsl:with-param name="TATEYOKO_FLG" select="$OS16_PTEXT_TATEYOKO"/>
        </xsl:call-template>
      </xsl:otherwise>
    </xsl:choose>
	</xsl:template>
  <!--=======================================================================================================-->
	<!-- 外国力士成績の編集 -->
	<!--=======================================================================================================-->
	<xsl:template match="Body" mode="KAKUNIN2">
    <!-- タイトル -->
    <xsl:for-each select="Meta/Title">
      <xsl:value-of select="."/>
      <!-- 改行 -->
      <xsl:value-of select="$LineFeed_UTL"/>
    </xsl:for-each>
    <!-- 外国力士の有無で処理振り分け -->
    <xslchoose>
      <xsl:choose>
        <!-- 力士無し（記事型） -->
        <xsl:when test="Article/Paragraph">
          <!-- インデント -->
          <xsl:value-of select="$WhiteSpaceZenkaku_UTL"/>
          <!-- 記事 -->
          <xsl:value-of select="Article/Paragraph"/>
          <!-- 改行 -->
          <xsl:value-of select="$LineFeed_UTL"/>
        </xsl:when>
        <!-- 力士有り -->
        <xsl:when test="Match">
          <!-- 取組情報の編集 -->
          <xsl:apply-templates select="Match" mode="KAKUNIN2"/>
        </xsl:when>
      </xsl:choose>
    </xslchoose>    
	</xsl:template>
  <!--=======================================================================================================-->
	<!-- 取組情報の編集 -->
	<!--=======================================================================================================-->
	<xsl:template match="Match" mode="KAKUNIN2">
    <!--===================-->
    <!-- １行目 -->
    <!--===================-->
    <xsl:choose>
      <!-- 勝敗結果 -->
      <xsl:when test="MatchDetail/MatchResult/Outcome/Writing">
        <xsl:value-of select="MatchDetail/MatchResult/Outcome/Writing"/>
      </xsl:when>
      <!-- 勝敗結果（休み情報） -->
      <xsl:when test="Player/Result/Outcome/Writing">
        <xsl:value-of select="Player/Result/Outcome/Writing"/>
      </xsl:when>
      <!-- 引退 -->
      <xsl:otherwise>
        <!-- 空白 -->
        <xsl:value-of select="$WhiteSpaceZenkaku_UTL"/>
      </xsl:otherwise>
    </xsl:choose>
    <!-- 上段力士名 -->
    <xsl:variable name="UpperPlayerName">
      <xsl:apply-templates select="Player[1]/PlayerName" mode="KAKUNIN2">
        <xsl:with-param name="PlayerAreaLength" select="$UpperPlayerNameMaxLength"/>
      </xsl:apply-templates>
    </xsl:variable>
    <xsl:value-of select="$UpperPlayerName"/>
    <xsl:call-template name="PrintSpaceZenkaku_UTL">
      <xsl:with-param name="count" select="$UpperPlayerNameMaxLength - string-length($UpperPlayerName)"/>
    </xsl:call-template>
    <!-- 「―」 -->
    <xsl:text>―</xsl:text>
    <!-- 下段力士情報 -->
    <xsl:if test="Player[2]">
      <!-- 力士名 -->
      <xsl:apply-templates select="Player[2]/PlayerName" mode="KAKUNIN2">
        <xsl:with-param name="PlayerAreaLength" select="$LowerPlayerNameMaxLength"/>
      </xsl:apply-templates>
      <xsl:text>（</xsl:text>
      <!-- 部屋名 -->
      <xsl:apply-templates select="Player[2]/Belong" mode="KAKUNIN2"/>
      <!-- 点切り -->
      <xsl:text>・</xsl:text>
      <!-- 出身国（外国力士のみ） -->
      <xsl:apply-templates select="Player[2]/PlayerForSumo/NativeCountry" mode="KAKUNIN2_LOWER"/>
      <!-- 出身都道府県（日本力士のみ） -->
      <xsl:apply-templates select="Player[2]/PlayerForSumo/NativeArea" mode="KAKUNIN2"/>
      <!-- 市町村がフル表記の場合は編集 -->
      <xsl:variable name="LowerCountry">
        <xsl:apply-templates select="Player[2]/PlayerForSumo/NativeCity" mode="KAKUNIN2"/>
      </xsl:variable>
      <xsl:if test="$CITY_DISPLAY_SET = 2 and $LowerCountry != ''">
        <!-- 点切り -->
        <xsl:text>・</xsl:text>
        <!-- 出身市町村名 -->
        <xsl:value-of select="$LowerCountry"/>
      </xsl:if>
      <xsl:text>）</xsl:text>
    </xsl:if>
    <!-- 改行 -->
    <xsl:value-of select="$LineFeed_UTL"/>
    <!--===================-->
    <!-- ２行目 -->
    <!--===================-->
    <xsl:variable name="OutcomeTotal">
      <!-- インデント -->
      <xsl:value-of select="$WhiteSpaceZenkaku_UTL"/>
      <!-- 今場所成績 -->
      <xsl:if test="Player[1]/Result/ResultForSumo/SumoOutcomeTotal/Writing">
        <xsl:value-of select="Player[1]/Result/ResultForSumo/SumoOutcomeTotal/Writing" />
      </xsl:if>
    </xsl:variable>
    <xsl:value-of select="$OutcomeTotal"/>
    <!-- 空白 -->
    <xsl:call-template name="PrintSpaceZenkaku_UTL">
      <xsl:with-param name="count" select="9 - string-length($OutcomeTotal)"/>
    </xsl:call-template>
    <!-- 枚目（上段力士） -->
    <xsl:if test="Player[1]/PlayerForSumo/SumoGrade/Writing">
      <xsl:value-of select="Player[1]/PlayerForSumo/SumoGrade/Writing" />
    </xsl:if>
    <!-- 空白-->
    <xsl:value-of select="$WhiteSpaceZenkaku_UTL"/>
    <!-- 部屋名（上段力士） -->
    <xsl:apply-templates select="Player[1]/Belong" mode="KAKUNIN2"/>
    <!-- 改行 -->
    <xsl:value-of select="$LineFeed_UTL"/>
    <!--===================-->
    <!-- ３行目 -->
    <!--===================-->
    <!-- インデント -->
    <xsl:value-of select="$WhiteSpaceZenkaku_UTL"/>
    <!-- 出身国（上段力士） -->
    <xsl:apply-templates select="Player[1]/PlayerForSumo/NativeCountry" mode="KAKUNIN2_UPPER"/>
    <!-- 出身市町村名（上段力士） -->
    <xsl:variable name="UpperCountry">
      <xsl:apply-templates select="Player[1]/PlayerForSumo/NativeCity" mode="KAKUNIN2"/>
    </xsl:variable>
    <xsl:if test="$UpperCountry != ''">
      <!-- 点切り -->
      <xsl:text>・</xsl:text>
      <!-- 出身市町村名 -->
      <xsl:value-of select="$UpperCountry"/>
    </xsl:if>
    <!-- 改行 -->
    <xsl:value-of select="$LineFeed_UTL"/>
	</xsl:template>
  <!--=======================================================================================================-->
  <!-- 力士名の編集 -->
  <!--=======================================================================================================-->  
  <xsl:template match="Player/PlayerName" mode="KAKUNIN2">
    <xsl:param name="PlayerAreaLength" select="0"/>
    <xsl:choose>
      <!-- Writing（３字） -->
      <xsl:when test="$PLAYERNAME_DISPLAY_SET = 1 and Writing">
        <xsl:value-of select="Writing"/>
      </xsl:when>
      <!-- Formal（フル） -->
      <xsl:when test="$PLAYERNAME_DISPLAY_SET = 2 and Formal[not(@*)]">
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
        <xsl:text>　　　</xsl:text>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 部屋名の編集 -->
  <!--=======================================================================================================-->  
  <xsl:template match="Player/Belong" mode="KAKUNIN2">
    <xsl:choose>
      <!-- Writing（２字） -->
      <xsl:when test="$BELONG_DISPLAY_SET = 1 and Writing">
        <xsl:value-of select="Writing"/>
      </xsl:when>
      <!-- Formal（フル） -->
      <xsl:when test="$BELONG_DISPLAY_SET = 2 and Formal[not(@*)]">
        <xsl:value-of select="Formal[not(@*)]"/>
      </xsl:when>
    </xsl:choose>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 上段力士の出身国の編集 -->
  <!--=======================================================================================================-->  
  <xsl:template match="PlayerForSumo/NativeCountry" mode="KAKUNIN2_UPPER">
    <xsl:choose>
      <!-- Writing（フル）※字取り有り -->
      <xsl:when test="$UPPER_COUNTRY_DISPLAY_SET = 1 and Writing">
        <xsl:value-of select="Writing"/>
      </xsl:when>
      <!-- Formal（フル） -->
      <xsl:when test="$UPPER_COUNTRY_DISPLAY_SET = 2 and Formal[not(@*)]">
        <xsl:value-of select="Formal[not(@*)]"/>
      </xsl:when>
    </xsl:choose>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 下段力士の出身国の編集 -->
  <!--=======================================================================================================-->  
  <xsl:template match="PlayerForSumo/NativeCountry" mode="KAKUNIN2_LOWER">
    <xsl:choose>
      <!-- Writing（２字） -->
      <xsl:when test="$LOWER_COUNTRY_DISPLAY_SET = 1 and Writing">
        <xsl:value-of select="Writing"/>
      </xsl:when>
      <!-- Formal（フル） -->
      <xsl:when test="$LOWER_COUNTRY_DISPLAY_SET = 2 and Formal[not(@*)]">
        <xsl:value-of select="Formal[not(@*)]"/>
      </xsl:when>
    </xsl:choose>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 出身都道府県の編集 -->
  <!--=======================================================================================================-->  
  <xsl:template match="PlayerForSumo/NativeArea" mode="KAKUNIN2">
    <xsl:choose>
      <!-- Writing（２字） -->
      <xsl:when test="$AREA_DISPLAY_SET = 1 and Writing">
        <xsl:value-of select="Writing"/>
      </xsl:when>
      <!-- Formal（フル） -->
      <xsl:when test="$AREA_DISPLAY_SET = 2 and Formal[not(@*)]">
        <xsl:value-of select="Formal[not(@*)]"/>
      </xsl:when>
    </xsl:choose>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 出身市町村の編集 -->
  <!--=======================================================================================================-->  
  <xsl:template match="PlayerForSumo/NativeCity" mode="KAKUNIN2">
    <xsl:choose>
      <!-- Writing（正式名）-->
      <xsl:when test="$CITY_DISPLAY_SET = 1 and Writing">
        <xsl:value-of select="Writing"/>
      </xsl:when>
      <!-- Formal（市町村付き）-->
      <xsl:when test="$CITY_DISPLAY_SET = 2 and Formal[@Display='市町村付']">
        <xsl:value-of select="Formal[@Display='市町村付']"/>
      </xsl:when>
      <!-- Formal（市町村付きが無い場合）-->
      <xsl:when test="$CITY_DISPLAY_SET = 2 and Formal[not(@*)]">
        <xsl:value-of select="Formal[not(@*)]"/>
      </xsl:when>
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
        <!-- Writing（３字） -->
        <xsl:when test="$PLAYERNAME_DISPLAY_SET = 1">
          <xsl:value-of select="'Writing'"/>
        </xsl:when>
        <!-- Formal（フル） -->
        <xsl:when test="$PLAYERNAME_DISPLAY_SET = 2">
          <xsl:value-of select="'Formal'"/>
        </xsl:when>
      </xsl:choose>
    </xsl:variable>
    <!-- 指定された力士の位置、表示対象の最大長を取得 -->
    <xsl:choose>
      <xsl:when test="count(.//Match/Player[$PlayerIdx]) &gt; 0">
        <xsl:for-each select=".//Match/Player[$PlayerIdx]">
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
                  <xsl:when test="$PLAYERNAME_DISPLAY_SET = 1 and $ParentName='Writing'">
                    <xsl:call-template name="Gaiji_EDT"/>
                  </xsl:when>
                  <!-- Formal表示時（フル表記の字解を編集） -->
                  <xsl:when test="$PLAYERNAME_DISPLAY_SET = 2 and $ParentName='Formal' and not(@*)">
                    <xsl:call-template name="Gaiji_EDT"/>
                  </xsl:when>
                </xsl:choose>
              </xsl:when>
              <!-- 部屋（表示切替有り） -->
              <xsl:when test="ancestor::Belong">
                <xsl:choose>
                  <!-- Writing表示時 -->
                  <xsl:when test="$BELONG_DISPLAY_SET = 1 and $ParentName='Writing'">
                    <xsl:call-template name="Gaiji_EDT"/>
                  </xsl:when>
                  <!-- Formal表示時（フル表記の字解を編集） -->
                  <xsl:when test="$BELONG_DISPLAY_SET = 2 and $ParentName='Formal' and not(@*)">
                    <xsl:call-template name="Gaiji_EDT"/>
                  </xsl:when>
                </xsl:choose>
              </xsl:when>
              <!-- 出身国（表示切替有り） -->
              <xsl:when test="ancestor::NativeCountry">
                <!-- 選手IDを取得 -->
                <xsl:variable name="PlayerId" select="ancestor::Player/@PlayerId"/>
                <!-- 選手IDから位置を取得 -->
                <xsl:variable name="Position">
                  <xsl:for-each select="ancestor::Match/Player">
                    <xsl:if test="@PlayerId = $PlayerId">
                      <xsl:value-of select="position()"/>
                    </xsl:if>
                  </xsl:for-each>
                </xsl:variable>
                <!-- 位置から対応する表示切替フラグを判定 -->
                <xsl:variable name="COUNTRY_DISPLAY_SET">
                  <xsl:choose>
                    <!-- 1.上段 -->
                    <xsl:when test="$Position = 1">
                      <xsl:value-of select="$UPPER_COUNTRY_DISPLAY_SET"/>
                    </xsl:when>
                    <!-- 2.下段 -->
                    <xsl:when test="$Position = 2">
                      <xsl:value-of select="$LOWER_COUNTRY_DISPLAY_SET"/>
                    </xsl:when>
                  </xsl:choose>
                </xsl:variable>
                <!-- 表示切替フラグと対応する字解を編集 -->
                <xsl:choose>
                  <!-- Writing表示時 -->
                  <xsl:when test="$COUNTRY_DISPLAY_SET = 1 and $ParentName='Writing'">
                    <xsl:call-template name="Gaiji_EDT"/>
                  </xsl:when>
                  <!-- Formal表示時（フル表記）-->
                  <xsl:when test="$COUNTRY_DISPLAY_SET = 2 and $ParentName='Formal' and not(@*)">
                    <xsl:call-template name="Gaiji_EDT"/>
                  </xsl:when>
                </xsl:choose>
              </xsl:when>
              <!-- 出身都道府県（表示切替有り）-->
              <xsl:when test="ancestor::NativeArea">
                <xsl:choose>
                  <!-- Writing表示時 -->
                  <xsl:when test="$AREA_DISPLAY_SET = 1 and $ParentName='Writing'">
                    <xsl:call-template name="Gaiji_EDT"/>
                  </xsl:when>
                  <!-- Formal表示時（フル表記の字解を編集） -->
                  <xsl:when test="$AREA_DISPLAY_SET = 2 and $ParentName='Formal' and not(@*)">
                    <xsl:call-template name="Gaiji_EDT"/>
                  </xsl:when>
                </xsl:choose>
              </xsl:when>
              <!-- 出身市町村（表示切替有り）-->
              <xsl:when test="ancestor::NativeCity">
                <xsl:choose>
                  <!-- Writing表示時 -->
                  <xsl:when test="$CITY_DISPLAY_SET = 1 and $ParentName='Writing'">
                    <xsl:call-template name="Gaiji_EDT"/>
                  </xsl:when>
                  <!-- Formal表示時（フル表記の字解を編集） -->
                  <xsl:when test="$CITY_DISPLAY_SET = 2 and $ParentName='Formal' and not(@*)">
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
      <!-- 横書きの場合は改ページ -->
      <xsl:if test="$OS16_PTEXT_TATEYOKO = 2">
        <xsl:value-of select="$PageBreak_UTL"/>
      </xsl:if>
      <!--字解見出し-->
      <xsl:text>字解情報</xsl:text>
      <xsl:value-of select="$LineFeed_UTL"/>
      <!--字解情報-->
      <xsl:value-of select="$JIKAI_DATA"/>
    </xsl:if>
	</xsl:template>
</xsl:stylesheet>
