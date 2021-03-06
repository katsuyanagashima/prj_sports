<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">
  <!-- ================================================================================= -->
  <!--　編集者用「共通スタイルシート」大相撲・階級別成績上位力士 -->
	<!--  4.0版 2015.06.30 プレーンテキスト版のプレーンテキスト表示用として新規公開　-->
	<!--  4.01版 2015.●.● pタグのOikomiStartクラス（追い込み開始情報）を追加 -->
  <!-- ================================================================================= -->
  <!-- ================================================================================= -->
  <!--【commonsetting定義】-->
  <!-- ================================================================================= -->
  <!-- 縦書き/横書き設定 -->
  <xsl:variable name="PTEXT_TATEYOKO_OS18_SET">
    <xsl:call-template name="PTEXT_TATEYOKO_OS18_SET"/>
  </xsl:variable>
  <!-- 力士名表示切替 -->
  <xsl:variable name="OS18_PLAYERNAME_DISPLAY_SET">
    <!-- Writing固定(Formalと一致するため) -->
    <xsl:value-of select="1"/>
  </xsl:variable>
  <!-- 部屋名表示切替 -->
  <xsl:variable name="OS18_BELONG_DISPLAY_SET">
    <xsl:call-template name="OS18_BELONG_DISPLAY_SET"/>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- 縦書き/横書き設定 -->
  <!-- ================================================================================= -->
  <xsl:variable name="OS18_PTEXT_TATEYOKO">
    <xsl:choose>
      <xsl:when test="$PTEXT_TATEYOKO_OS18_SET = 0">
        <!-- 共通設定を適用 -->
        <xsl:value-of select="$PTEXT_TATEYOKO_SET"/>
      </xsl:when>
      <xsl:otherwise>
        <!-- 個別設定を適用 -->
        <xsl:value-of select="$PTEXT_TATEYOKO_OS18_SET"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- １ページ最大行数を取得 -->
  <!-- 判断条件は「印刷方向定義」「縦書き/横書き設定」 -->
  <!-- ================================================================================= -->
  <xsl:variable name="OS18_PRINT_MAXLINE">
    <xsl:choose>
      <!--Ａ４タテ印刷-->
      <xsl:when test="$PRINT_F_SET=1">
        <xsl:choose>
          <xsl:when test="$OS18_PTEXT_TATEYOKO=1">
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
          <xsl:when test="$OS18_PTEXT_TATEYOKO=1">
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
  <xsl:variable name="OS18_MAXLENGTH">
    <xsl:choose>
      <!--Ａ４タテ印刷-->
      <xsl:when test="$PRINT_F_SET=1">
        <xsl:choose>
          <xsl:when test="$OS18_PTEXT_TATEYOKO=1">
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
          <xsl:when test="$OS18_PTEXT_TATEYOKO=1">
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
  </xsl:variable>
	<!--=======================================================================================================-->
	<!--【プレーンテキスト版】スポーツデータタグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="SportsData" mode="KAKUNIN2">
    <!-- 力士名の最大長を取得 -->
    <xsl:variable name="PlayerNameMaxLength">
      <xsl:call-template name="GetPlayerNameMaxLength"/>
    </xsl:variable>
    <!-- レイアウト開始 -->
    <xsl:call-template name="KAKUNIN2_DIVS_NORMAL_LAYOUT_UTL">
      <!-- 本文要素 -->
      <xsl:with-param name="HONBUN_DATA">
        <!-- 縦書き／横書きで編集処理を振り分け -->
        <xsl:choose>
          <!-- 縦書き -->
          <xsl:when test="$OS18_PTEXT_TATEYOKO = 1">
            <xsl:apply-templates select="Body" mode="KAKUNIN2_TATE"/>
          </xsl:when>
          <!-- 横書き -->
          <xsl:otherwise>
            <xsl:apply-templates select="Body" mode="KAKUNIN2_YOKO">
              <xsl:with-param name="PlayerNameMaxLength" select="$PlayerNameMaxLength"/>
            </xsl:apply-templates>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:with-param>
      <!-- 字解 -->
      <xsl:with-param name="JIKAI_DATA">
        <xsl:call-template name="Gaiji_KAKUNIN2"/>
      </xsl:with-param>
      <xsl:with-param name="LINE_MAX_LENGTH" select="$OS18_MAXLENGTH"/>
      <xsl:with-param name="PAGE_LINE_MAX" select="$OS18_PRINT_MAXLINE"/>
      <xsl:with-param name="ADD_LINE_COUNT_FLG" select="$ADD_LINE_COUNT_FLG_SET"/>
      <xsl:with-param name="TATEYOKO_FLG" select="$OS18_PTEXT_TATEYOKO"/>
      <xsl:with-param name="ADD_OIKOMI_CLASS_FLG" select="1"/>
    </xsl:call-template>
	</xsl:template>
  <!--=======================================================================================================-->
	<!-- 階級別成績上位力士の縦書き編集 -->
	<!--=======================================================================================================-->
  <xsl:template match="Body" mode="KAKUNIN2_TATE">
    <!--==================-->
    <!-- 変数定義 -->
    <!--==================-->
    <!-- タイトルの個数 -->
    <xsl:variable name="TitleCnt" select="count(Meta/Title)"/>
    <!-- 区切り文字 -->
    <xsl:variable name="Delimiter" select="'、'"/>
    <!--==================-->
    <!-- 編集開始 -->
    <!--==================-->
    <!-- タイトル -->
    <xsl:for-each select="Meta/Title">
      <!-- インデント -->
      <xsl:value-of select="$WhiteSpaceZenkaku_UTL"/>
      <!-- タイトル出力 -->
      <xsl:value-of select="."/>
      <!-- タイトルの種別で処理振り分け -->
      <xsl:choose>
        <!-- 階級の場合は改行 -->
        <xsl:when test="$TitleCnt > 1 and position() = 1">
          <xsl:value-of select="$LineFeed_UTL"/>
        </xsl:when>
        <!-- 勝利数の場合は空白 -->
        <xsl:otherwise>
          <xsl:value-of select="$WhiteSpaceZenkaku_UTL"/>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:for-each>
    <!-- 力士情報 -->
    <xsl:for-each select="Standing/Player">
      <!-- 力士名 -->
      <xsl:apply-templates select="PlayerName" mode="KAKUNIN2"/>
      <!-- 部屋名 -->
      <xsl:apply-templates select="Belong" mode="KAKUNIN2"/>
      <xsl:choose>
        <!-- 最後は改行 -->
        <xsl:when test="position() = last()">
          <xsl:value-of select="$LineFeed_UTL"/>
        </xsl:when>
        <!-- 力士が続く場合は区切り文字を挿入 -->
        <xsl:otherwise>
          <xsl:value-of select="$Delimiter"/>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:for-each>
  </xsl:template>
  <!--=======================================================================================================-->
	<!-- 階級別成績上位力士の縦書き編集 -->
	<!--=======================================================================================================-->
  <xsl:template match="Body" mode="KAKUNIN2_YOKO">
    <!-- 力士名最大長 -->
    <xsl:param name="PlayerNameMaxLength"/>
    <!--==================-->
    <!-- 編集開始 -->
    <!--==================-->
    <!-- ２つ目以降の行間 -->
    <xsl:if test="position() > 1">
      <xsl:value-of select="$LineFeed_UTL"/>
    </xsl:if>
    <!-- タイトル -->
    <xsl:for-each select="Meta/Title">
      <!-- 出力 -->
      <xsl:value-of select="."/>
      <!-- 改行 -->
      <xsl:value-of select="$LineFeed_UTL"/>
    </xsl:for-each>
    <!-- 力士情報 -->
    <xsl:for-each select="Standing/Player">
      <!-- インデント -->
      <xsl:value-of select="$WhiteSpaceZenkaku_UTL"/>
      <!-- 力士名 -->
      <xsl:variable name="PlayerName">
        <xsl:apply-templates select="PlayerName" mode="KAKUNIN2"/>
      </xsl:variable>
      <xsl:value-of select="$PlayerName"/>
      <!-- 部屋名 -->
      <xsl:variable name="Belong">
        <xsl:apply-templates select="Belong" mode="KAKUNIN2"/>
      </xsl:variable>
      <!-- 部屋名の出力有り -->
      <xsl:if test="$Belong != ''">
        <!-- 力士名～部屋名の空白調整 -->
        <xsl:call-template name="PrintSpaceZenkaku_UTL">
          <xsl:with-param name="count" select="$PlayerNameMaxLength - string-length($PlayerName)"/>
        </xsl:call-template>
        <!-- 部屋名出力 -->
        <xsl:value-of select="$Belong"/>
      </xsl:if>
      <!-- 改行 -->
      <xsl:value-of select="$LineFeed_UTL"/>
    </xsl:for-each>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 力士名の最大長を取得 -->
  <!--=======================================================================================================-->
  <xsl:template name="GetPlayerNameMaxLength">
    <!-- 力士名の表示対象 -->
    <xsl:variable name="PLAYERNAME_DISPLAY_NODE">
      <xsl:choose>
        <!-- Writing -->
        <xsl:when test="$OS18_PLAYERNAME_DISPLAY_SET = 1">
          <xsl:value-of select="'Writing'"/>
        </xsl:when>
        <!-- Formal -->
        <xsl:when test="$OS18_PLAYERNAME_DISPLAY_SET = 2">
          <xsl:value-of select="'Formal'"/>
        </xsl:when>
      </xsl:choose>
    </xsl:variable>
    <!-- 表示対象の最大長を取得 -->
    <xsl:choose>
      <xsl:when test="count(Body/*/Player) &gt; 0">
        <xsl:for-each select="Body/*/Player">
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
      <xsl:when test="$OS18_PLAYERNAME_DISPLAY_SET = 1 and Writing">
        <xsl:value-of select="Writing"/>
      </xsl:when>
      <!-- Formal -->
      <xsl:when test="$OS18_PLAYERNAME_DISPLAY_SET = 2 and Formal[not(@*)]">
        <xsl:value-of select="Formal[not(@*)]"/>
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
    <xsl:variable name="Belong">
      <xsl:choose>
        <!-- Writing -->
        <xsl:when test="$OS18_BELONG_DISPLAY_SET = 1 and Writing">
          <xsl:value-of select="Writing"/>
        </xsl:when>
        <!-- Formal（フル） -->
        <xsl:when test="$OS18_BELONG_DISPLAY_SET = 2 and Formal[not(@*)]">
          <xsl:value-of select="Formal[not(@*)]"/>
        </xsl:when>
      </xsl:choose>
    </xsl:variable>
    <xsl:if test="$Belong != ''">
      <xsl:text>（</xsl:text>
      <xsl:value-of select="$Belong"/>
      <xsl:text>）</xsl:text>
    </xsl:if>
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
                  <xsl:when test="$OS18_PLAYERNAME_DISPLAY_SET = 1 and $ParentName='Writing'">
                    <xsl:call-template name="Gaiji_EDT"/>
                  </xsl:when>
                  <!-- Formal表示時（フル表記の字解を編集） -->
                  <xsl:when test="$OS18_PLAYERNAME_DISPLAY_SET = 2 and $ParentName='Formal' and not(@*)">
                    <xsl:call-template name="Gaiji_EDT"/>
                  </xsl:when>
                </xsl:choose>
              </xsl:when>
              <!-- 部屋名（表示切替有り） -->
              <xsl:when test="ancestor::Belong">
                <xsl:choose>
                  <!-- Writing表示時 -->
                  <xsl:when test="$OS18_BELONG_DISPLAY_SET = 1 and $ParentName='Writing'">
                    <xsl:call-template name="Gaiji_EDT"/>
                  </xsl:when>
                  <!-- Formal表示時（フル表記の字解を編集） -->
                  <xsl:when test="$OS18_BELONG_DISPLAY_SET = 2 and $ParentName='Formal' and not(@*)">
                    <xsl:call-template name="Gaiji_EDT"/>
                  </xsl:when>
                </xsl:choose>
              </xsl:when>
              <!-- その他（表示切替の無い要素）はWritingのみ字解編集 -->
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
