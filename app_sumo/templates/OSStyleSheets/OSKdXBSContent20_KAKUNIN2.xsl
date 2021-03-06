<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">
  <!-- ================================================================================= -->
  <!--　編集者用「共通スタイルシート」大相撲・幕下以下全成績 -->
	<!--  4.0版 2015.06.30 プレーンテキスト版のプレーンテキスト表示用として新規公開　-->
  <!-- ================================================================================= -->
  <!-- ================================================================================= -->
  <!--【commonsetting定義】-->
  <!-- ================================================================================= -->
  <!-- 縦書き/横書き設定 -->
  <xsl:variable name="PTEXT_TATEYOKO_OS20_SET">
    <xsl:call-template name="PTEXT_TATEYOKO_OS20_SET"/>
  </xsl:variable>
  <!-- 力士名表示切替 -->
  <xsl:variable name="OS20_PLAYERNAME_DISPLAY_SET">
    <xsl:call-template name="OS20_PLAYERNAME_DISPLAY_SET"/>
  </xsl:variable>
  <!-- 部屋名表示切替 -->
  <xsl:variable name="OS20_BELONG_DISPLAY_SET">
    <xsl:call-template name="OS20_BELONG_DISPLAY_SET"/>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- 縦書き/横書き設定 -->
  <!-- ================================================================================= -->
  <xsl:variable name="OS20_PTEXT_TATEYOKO">
    <xsl:choose>
      <xsl:when test="$PTEXT_TATEYOKO_OS20_SET = 0">
        <!-- 共通設定を適用 -->
        <xsl:value-of select="$PTEXT_TATEYOKO_SET"/>
      </xsl:when>
      <xsl:otherwise>
        <!-- 個別設定を適用 -->
        <xsl:value-of select="$PTEXT_TATEYOKO_OS20_SET"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:variable>
  <!-- ================================================================================= -->
  <!-- １ページ最大行数を取得 -->
  <!-- 判断条件は「印刷方向定義」「縦書き/横書き設定」 -->
  <!-- ================================================================================= -->
  <xsl:variable name="OS20_PRINT_MAXLINE">
    <xsl:choose>
      <!--Ａ４タテ印刷-->
      <xsl:when test="$PRINT_F_SET=1">
        <xsl:choose>
          <xsl:when test="$OS20_PTEXT_TATEYOKO=1">
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
          <xsl:when test="$OS20_PTEXT_TATEYOKO=1">
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
  <xsl:variable name="OS20_MAXLENGTH">
    <xsl:choose>
      <!--Ａ４タテ印刷-->
      <xsl:when test="$PRINT_F_SET=1">
        <xsl:choose>
          <xsl:when test="$OS20_PTEXT_TATEYOKO=1">
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
          <xsl:when test="$OS20_PTEXT_TATEYOKO=1">
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
    <!-- 幕下以下成績編集 -->
    <xsl:apply-templates select="Body" mode="KAKUNIN2"/>
	</xsl:template>
  <!--=======================================================================================================-->
	<!-- 幕下以下成績テンプレート-->
	<!--=======================================================================================================-->
  <xsl:template match="Body" mode="KAKUNIN2">
    <!--==================-->
    <!-- 変数定義 -->
    <!--==================-->
    <!-- 枚目の最大長 -->
    <xsl:variable name="SumoRankMaxLength">
      <xsl:call-template name="GetSumoRankMaxLength"/>
    </xsl:variable>
    <!-- 力士名の最大長 -->
    <xsl:variable name="PlayerNameMaxLength">
      <xsl:call-template name="GetPlayerNameMaxLength"/>
    </xsl:variable>
    <!-- 部屋名の最大長 -->
    <xsl:variable name="BelongMaxLength">
      <xsl:call-template name="GetBelongMaxLength"/>
    </xsl:variable>
    <!-- 本文 -->
    <xsl:variable name="HonbunText">
      <!-- 表見出しを編集 -->
      <xsl:call-template name="EditTableHeader">
        <xsl:with-param name="SumoRankMaxLength" select="$SumoRankMaxLength"/>
        <xsl:with-param name="PlayerNameMaxLength" select="$PlayerNameMaxLength"/>
        <xsl:with-param name="BelongMaxLength" select="$BelongMaxLength"/>
      </xsl:call-template>
      <!-- 全力士の成績を編集 -->
      <xsl:apply-templates select="Standing/Player" mode="KAKUNIN2">
        <xsl:with-param name="SumoRankMaxLength" select="$SumoRankMaxLength"/>
        <xsl:with-param name="PlayerNameMaxLength" select="$PlayerNameMaxLength"/>
        <xsl:with-param name="BelongMaxLength" select="$BelongMaxLength"/>
      </xsl:apply-templates>
    </xsl:variable>
    <!--==================-->
    <!-- レイアウト -->
    <!--==================-->
    <xsl:choose>
      <!-- 縦書きで力士名または部屋名がフル表記"Formal"の場合は縦ロングでレイアウト -->
      <xsl:when test="$OS20_PTEXT_TATEYOKO = 1 and ($OS20_PLAYERNAME_DISPLAY_SET = 2 or $OS20_BELONG_DISPLAY_SET = 2)">
        <!-- レイアウト開始 -->
        <xsl:call-template name="KAKUNIN2_DIVS_TATELONG_LAYOUT_UTL">
          <!-- 本文要素 -->
          <xsl:with-param name="HONBUN_DATA" select="$HonbunText"/>
          <!-- 字解 -->
          <xsl:with-param name="JIKAI_DATA">
            <xsl:call-template name="Gaiji_KAKUNIN2"/>
          </xsl:with-param>
          <xsl:with-param name="LINE_MAX_LENGTH" select="20"/>
          <xsl:with-param name="PAGE_LINE_MAX" select="$OS20_PRINT_MAXLINE"/>
          <xsl:with-param name="ADD_LINE_COUNT_FLG" select="$ADD_LINE_COUNT_FLG_SET"/>
          <xsl:with-param name="TATEYOKO_FLG" select="$OS20_PTEXT_TATEYOKO"/>
        </xsl:call-template>
      </xsl:when>
      <!-- その他は共通DIVでレイアウト -->
      <xsl:otherwise>
        <!-- レイアウト開始 -->
        <xsl:call-template name="KAKUNIN2_DIVS_NORMAL_LAYOUT_UTL">
          <!-- 本文要素 -->
          <xsl:with-param name="HONBUN_DATA">
            <!-- 本文 -->
            <xsl:value-of select="$HonbunText"/>
          </xsl:with-param>
          <!-- 字解 -->
          <xsl:with-param name="JIKAI_DATA">
            <xsl:call-template name="Gaiji_KAKUNIN2"/>
          </xsl:with-param>
          <xsl:with-param name="LINE_MAX_LENGTH" select="$OS20_MAXLENGTH"/>
          <xsl:with-param name="PAGE_LINE_MAX" select="$OS20_PRINT_MAXLINE"/>
          <xsl:with-param name="ADD_LINE_COUNT_FLG" select="$ADD_LINE_COUNT_FLG_SET"/>
          <xsl:with-param name="TATEYOKO_FLG" select="$OS20_PTEXT_TATEYOKO"/>
        </xsl:call-template>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 枚目の最大長を取得 -->
  <!--=======================================================================================================-->
  <xsl:template name="GetSumoRankMaxLength">
    <xsl:call-template name="GetTagsMaxLength_UTL">
      <xsl:with-param name="TargetPath" select="Standing/Player/PlayerForSumo/SumoGrade/Writing"/>
    </xsl:call-template>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 力士名の最大長を取得 -->
  <!--=======================================================================================================-->
  <xsl:template name="GetPlayerNameMaxLength">
    <!-- 力士名の表示対象 -->
    <xsl:variable name="PLAYERNAME_DISPLAY_NODE">
      <xsl:choose>
        <!-- Writing -->
        <xsl:when test="$OS20_PLAYERNAME_DISPLAY_SET = 1">
          <xsl:value-of select="'Writing'"/>
        </xsl:when>
        <!-- Formal -->
        <xsl:when test="$OS20_PLAYERNAME_DISPLAY_SET = 2">
          <xsl:value-of select="'Formal'"/>
        </xsl:when>
      </xsl:choose>
    </xsl:variable>
    <!-- 表示対象の最大長を取得 -->
    <xsl:choose>
      <xsl:when test="count(Standing/Player) &gt; 0">
        <xsl:for-each select="Standing/Player">
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
  <!-- 部屋名の最大長を取得 -->
  <!--=======================================================================================================-->
  <xsl:template name="GetBelongMaxLength">
    <!-- 部屋名の表示対象 -->
    <xsl:variable name="BELONG_DISPLAY_NODE">
      <xsl:choose>
        <!-- Writing -->
        <xsl:when test="$OS20_BELONG_DISPLAY_SET = 1">
          <xsl:value-of select="'Writing'"/>
        </xsl:when>
        <!-- Formal -->
        <xsl:when test="$OS20_BELONG_DISPLAY_SET = 2">
          <xsl:value-of select="'Formal'"/>
        </xsl:when>
      </xsl:choose>
    </xsl:variable>
    <!-- 表示対象の最大長を取得 -->
    <xsl:choose>
      <xsl:when test="count(Standing/Player) &gt; 0">
        <xsl:for-each select="Standing/Player">
          <xsl:sort select="string-length(Belong/*[name()=$BELONG_DISPLAY_NODE and not(@*)])" data-type="number" order="descending"/>
          <xsl:if test="position() = 1">
            <xsl:value-of select="string-length(Belong/*[name()=$BELONG_DISPLAY_NODE and not(@*)])"/>
          </xsl:if>
        </xsl:for-each>
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="0"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 表見出しを編集 -->
  <!--=======================================================================================================-->
  <xsl:template name="EditTableHeader">
    <!-- 枚目の最大長 -->
    <xsl:param name="SumoRankMaxLength"/>
    <!-- 力士名最大長 -->
    <xsl:param name="PlayerNameMaxLength"/>
    <!-- 部屋名最大長 -->
    <xsl:param name="BelongMaxLength"/>
    <!-- 中見出し -->
    <xsl:variable name="Title">
      <xsl:choose>
        <xsl:when test="Meta/Title">
          <xsl:value-of select="Meta/Title"/>
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>　　　　</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <xsl:value-of select="$Title"/>
    <xsl:call-template name="PrintSpaceZenkaku_UTL">
      <xsl:with-param name="count" select="$SumoRankMaxLength + $PlayerNameMaxLength - string-length($Title)"/>
    </xsl:call-template>
    <!-- 部屋名 -->
    <xsl:text>　</xsl:text>
    <xsl:variable name="Belong" select="'部屋'"/>
    <xsl:value-of select="$Belong"/>
    <xsl:call-template name="PrintSpaceZenkaku_UTL">
      <xsl:with-param name="count" select="$BelongMaxLength - string-length($Belong)"/>
    </xsl:call-template>
    <xsl:text>　</xsl:text>
    <!-- 勝敗内容 -->
    <xsl:text>勝休負</xsl:text>
    <!-- 改行 -->
    <xsl:value-of select="$LineFeed_UTL"/>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 力士の成績を編集 -->
  <!--=======================================================================================================-->
  <xsl:template match="Standing/Player" mode="KAKUNIN2">
    <!-- 枚目の最大長 -->
    <xsl:param name="SumoRankMaxLength"/>
    <!-- 力士名最大長 -->
    <xsl:param name="PlayerNameMaxLength"/>
    <!-- 部屋名最大長 -->
    <xsl:param name="BelongMaxLength"/>
    <!--==============-->
    <!-- 枚目 -->
    <!--==============-->
    <xsl:variable name="Rank">
      <xsl:choose>
        <xsl:when test="PlayerForSumo/SumoGrade/Writing">
          <xsl:value-of select="PlayerForSumo/SumoGrade/Writing"/>
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>　</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <xsl:call-template name="PrintSpaceZenkaku_UTL">
      <xsl:with-param name="count" select="$SumoRankMaxLength - string-length($Rank)"/>
    </xsl:call-template>
    <xsl:value-of select="$Rank"/>
    <!--==============-->
    <!-- 力士名 -->
    <!--==============-->
    <xsl:variable name="Name">
      <xsl:apply-templates select="PlayerName" mode="KAKUNIN2">
        <xsl:with-param name="PlayerNameMaxLength" select="$PlayerNameMaxLength"/>
      </xsl:apply-templates>
    </xsl:variable>
    <xsl:value-of select="$Name"/>
    <xsl:call-template name="PrintSpaceZenkaku_UTL">
      <xsl:with-param name="count" select="$PlayerNameMaxLength - string-length($Name)"/>
    </xsl:call-template>
    <!--==============-->
    <!-- 部屋名 -->
    <!--==============-->
    <xsl:variable name="Belong">
      <xsl:apply-templates select="Belong" mode="KAKUNIN2">
        <xsl:with-param name="BelongMaxLength" select="$BelongMaxLength"/>
      </xsl:apply-templates>
    </xsl:variable>
    <xsl:text>（</xsl:text>
    <xsl:value-of select="$Belong"/>
    <xsl:text>）</xsl:text>
    <xsl:call-template name="PrintSpaceZenkaku_UTL">
      <xsl:with-param name="count" select="$BelongMaxLength - string-length($Belong)"/>
    </xsl:call-template>
    <!--==============-->
    <!-- 勝敗内容 -->
    <!--==============-->
    <xsl:variable name="Result">
      <xsl:choose>
        <!-- 引退・廃業 -->
        <xsl:when test="PlayerForSumo/Retirement/Writing">
          <xsl:value-of select="PlayerForSumo/Retirement/Writing"/>
        </xsl:when>
        <!-- 勝敗内容 -->
        <xsl:when test="Result/ResultForSumo/SumoOutcomeTotal/Writing">
          <xsl:value-of select="Result/ResultForSumo/SumoOutcomeTotal/Writing"/>
        </xsl:when>
      </xsl:choose>
    </xsl:variable>
    <xsl:value-of select="$Result"/>
    <!-- 空白調整（引き分け含む） -->
    <xsl:call-template name="PrintSpaceZenkaku_UTL">
      <xsl:with-param name="count" select="4- string-length($Result)"/>
    </xsl:call-template>
    <!--==============-->
    <!-- 付け出し力士 -->
    <!--==============-->
    <xsl:if test="PlayerForSumo/Debut/Writing">
      <xsl:value-of select="PlayerForSumo/Debut/Writing"/>
    </xsl:if>
    <!-- 改行 -->
    <xsl:value-of select="$LineFeed_UTL"/>
  </xsl:template>
  <!--=======================================================================================================-->
  <!-- 力士名の編集 -->
  <!--=======================================================================================================-->  
  <xsl:template match="Player/PlayerName" mode="KAKUNIN2">
    <xsl:param name="PlayerNameMaxLength" select="0"/>
    <xsl:choose>
      <!-- Writing -->
      <xsl:when test="$OS20_PLAYERNAME_DISPLAY_SET = 1 and Writing">
        <xsl:value-of select="Writing"/>
      </xsl:when>
      <!-- Formal -->
      <xsl:when test="$OS20_PLAYERNAME_DISPLAY_SET = 2 and Formal[not(@*)]">
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
    <xsl:param name="BelongMaxLength" select="0"/>
    <xsl:choose>
      <!-- Writing -->
      <xsl:when test="$OS20_BELONG_DISPLAY_SET = 1 and Writing">
        <xsl:value-of select="Writing"/>
      </xsl:when>
      <!-- Formal -->
      <xsl:when test="$OS20_BELONG_DISPLAY_SET = 2 and Formal[not(@*)]">
        <xsl:choose>
          <!-- ２字以下の部屋名は３文字幅で字取り編集 -->
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
                  <xsl:when test="$OS20_PLAYERNAME_DISPLAY_SET = 1 and $ParentName='Writing'">
                    <xsl:call-template name="Gaiji_EDT"/>
                  </xsl:when>
                  <!-- Formal表示時（フル表記の字解を編集） -->
                  <xsl:when test="$OS20_PLAYERNAME_DISPLAY_SET = 2 and $ParentName='Formal' and not(@*)">
                    <xsl:call-template name="Gaiji_EDT"/>
                  </xsl:when>
                </xsl:choose>
              </xsl:when>
              <!-- 部屋名（表示切替有り） -->
              <xsl:when test="ancestor::Belong">
                <xsl:choose>
                  <!-- Writing表示時 -->
                  <xsl:when test="$OS20_BELONG_DISPLAY_SET = 1 and $ParentName='Writing'">
                    <xsl:call-template name="Gaiji_EDT"/>
                  </xsl:when>
                  <!-- Formal表示時（フル表記の字解を編集） -->
                  <xsl:when test="$OS20_BELONG_DISPLAY_SET = 2 and $ParentName='Formal' and not(@*)">
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
