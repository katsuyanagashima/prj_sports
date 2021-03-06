<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">
<!-- ================================================================================= -->
<!--　編集者用「共通スタイルシート」大相撲・十両星取表　　　DTD=KdXBSContentv1.1.dtd -->
<!--  4.0版 2015.06.30 プレーンテキスト版として新規公開 -->
<!-- ================================================================================= -->
<!-- 3.0版　2014.2.26 html関連タグの小文字化 -->
<!--=============================================================================
編集者用「共通スタイルシート」
大相撲・十両星取表　　　ＤＴＤ：KdXBSContentv1.1.dtd
 1.0版　2007.10.10 編集者用「共通スタイルシート」として新規作成
 1.1版　2007.12.10「一覧表ページ」にて全角スペース（0x3000）を（0xEAF0）に置換していた部分を
　　　　　　　　　 置換せずにそのまま全角スペースで表示するように修正
 1.2版　2008.05.30 HTML変換した際に共通ヘッダ部の挿入位置の不具合を解消
 1.3版　2008.12.19 <head>部に記述されていたスタイル定義を<pre>付きで<body>部に移動
 1.4版  2009.02.20 スタイル宣言を記述した<pre>内で不要な改行を削除
================================================================================-->
	<!-- 内容情報部表示シートをインポートする。-->
  <xsl:import href="../Stylesheets/commonutil.xsl"/>
  <xsl:import href="../Stylesheets/commonsetting.xsl"/>
  <xsl:import href="../Stylesheets/commonedit.xsl"/>
  <xsl:import href="../Stylesheets/commonheader2.xsl"/>
  <xsl:import href="../Stylesheets/numconverttbl.xsl"/>
	<xsl:import href="../OSStylesheets/OS_CommonEdit.xsl" />
  <xsl:import href="../OSStylesheets/OSKdXBSContent21_KAKUNIN.xsl"/>
  <xsl:import href="../OSStylesheets/OSKdXBSContent21_ICHIRAN.xsl"/>
  <xsl:import href="../OSStylesheets/OSKdXBSContent21_KAKUNIN2.xsl"/>
	<!--=======================================================================================================-->
	<!--ルートタグテンプレート-->
	<!--=======================================================================================================-->
  <xsl:template match="/">
    <xsl:choose>
      <!--フルタグ書式内容部　ルートタグを判定する。-->
      <xsl:when test="//SportsData">
        <xsl:apply-templates select="//SportsData" mode="MAIN"/>
      </xsl:when>
      <!--フルタグ書式内容部　ルートタグがなければ下記のメッセージを表示-->
      <xsl:otherwise>
        <html>
          <body>
            <xsl:text>ＤＴＤ実行エラーまたは、タグに誤りがあります。</xsl:text>
          </body>
        </html>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
	<!--=======================================================================================================-->
	<!--【メイン】スポーツデータタグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="SportsData" mode="MAIN">
    <html>
      <head>
        <title><xsl:value-of select="//InHeadLine"/></title>
        <style type="text/css">
          <!-- KAKUNIN -->
          p.pb{page-break-before:always;} 
          .font_size_KAKUNIN{font-size:12pt;}
          <!-- ICHIRAN -->
          tbody.header{font-size:12pt;} table.header{font-size:12pt;text-align:left;empty-cells:
          show;border-collapse:separate;} table.block{page-break-before:always;font-size:12pt;empty-cells:
          show;border-collapse:separate;} table.data{font-size:9pt;empty-cells:
          show;border-collapse:separate;} th.HeadTitle{font-size:18pt; }
          th.block_title{background-color:#FF99FF;border:1px ridge #b0e0b6;}
          th.block_data{background-color:#CCFFCC;border:1px solid #b0e0b6;}
          tr.head_main{background-color:#FF99FF;font-size:12pt;border:1px solid #b0e0b6;}
          tr.head_sub{background-color:#FFCCFF; } tr.odd{background-color:#CCFFCC;}
          tr.even{background-color:#CCFFFF;} th.single{border-top:1px ridge #b0e0b6;border-right:1px ridge
          #b0e0b6;border-bottom:1px ridge #b0e0b6;border-left:1px ridge #b0e0b6;} th.top{border-top:1px
          ridge #b0e0b6;border-right:1px ridge #b0e0b6;border-bottom:1px none #b0e0b6;border-left:1px
          ridge #b0e0b6;} th.middle{border-top:1px none #b0e0b6;border-right:1px ridge
          #b0e0b6;border-bottom:1px none #b0e0b6;border-left:1px ridge #b0e0b6;} th.bottom{border-top:1px
          none #b0e0b6;border-right:1px ridge #b0e0b6;border-bottom:1px ridge #b0e0b6;border-left:1px
          ridge #b0e0b6;} th.match{background-color:lightskyblue;border:1px ridge #b0e0b6;}
          th.direction{background-color:#FFCCFF;border:1px ridge #b0e0b6;} td.single{border-top:1px solid
          #b0e0b6;border-right:1px solid #b0e0b6;border-bottom:1px solid #b0e0b6;border-left:1px solid
          #b0e0b6;} td.top{border-top:1px solid #b0e0b6;border-right:1px solid #b0e0b6;border-bottom:1px
          none #b0e0b6;border-left:1px solid #b0e0b6;} td.middle{border-top:1px none
          #b0e0b6;border-right:1px solid #b0e0b6;border-bottom:1px none #b0e0b6;border-left:1px solid
          #b0e0b6;} td.bottom{border-top:1px none #b0e0b6;border-right:1px solid #b0e0b6;border-bottom:1px
          solid #b0e0b6;border-left:1px solid #b0e0b6;} td.match{background-color:aquamarine;border:1px
          solid #b0e0b6;} @page{ size: landscape; }
          <xsl:call-template name="CommonCSS_SET"/>
          <!-- Ａ４縦印刷・力士名と部屋がフル表記の時は９pt -->
          <xsl:choose>
            <xsl:when test="($PRINT_F_SET = 1) and ($OS21_PLAYERNAME_DISPLAY_SET =2) and ($OS21_BELONG_DISPLAY_SET = 2)">
              <xsl:call-template name="CommonCSS_FontSizeSmall_SET"/>
            </xsl:when>
            <xsl:otherwise>
              <xsl:call-template name="CommonCSS_SET"/>
            </xsl:otherwise>
          </xsl:choose>
        </style>
      </head>
      <body style="font-family:'U-PRESS';">
        <!-- 外部テンプレート呼び出し用 -->
        <xsl:call-template name="commonTemplate_SET"/>
        <!-- 内容情報部 -->
        <xsl:if test="$NAIYOU_F_SET=1">
          <xsl:call-template name="InContent_InMetadata"/>
        </xsl:if>
        <xsl:choose>
          <!--■「１」：「プレーンテキスト」-->
          <xsl:when test="$SHORI_F_SET=1">
            <!--プレーンテキスト-->
						<xsl:apply-templates select="." mode="KAKUNIN2"/>
          </xsl:when>
          <!--■「２」：「プレーンテキスト」＋「一覧」-->
          <xsl:when test="$SHORI_F_SET=2">
            <!-- プレーンテキスト -->
						<xsl:apply-templates select="." mode="KAKUNIN2"/>
            <!-- 改ページ -->
            <hr class="pageBreakAfter"/>
            <!-- 一覧 -->
            <xsl:text>【一覧表】</xsl:text>
						<xsl:apply-templates select="." mode="ICHIRAN"/>
          </xsl:when>
          <!--■「３」：「一覧」-->
          <xsl:when test="$SHORI_F_SET=3">
            <!-- 一覧 -->
						<xsl:apply-templates select="." mode="ICHIRAN"/>
          </xsl:when>
          <!--■「７」「８」：「確認」-->
          <xsl:when test="$SHORI_F_SET=7 or $SHORI_F_SET=8">
            <!-- 確認 -->
						<xsl:apply-templates select="." mode="KAKUNIN"/>
          </xsl:when>
          <!--■「９」：「プレーンテキスト」＋「確認」＋「一覧」-->
          <xsl:when test="$SHORI_F_SET=9">
            <!-- プレーンテキスト -->
						<xsl:apply-templates select="." mode="KAKUNIN2"/>
            <!-- 改ページ -->
            <hr class="pageBreakAfter"/>
            <!-- 確認 -->
						<xsl:apply-templates select="." mode="KAKUNIN"/>
            <!-- 改ページ -->
            <hr class="pageBreakAfter"/>
            <!-- 一覧 -->
            <xsl:text>【一覧表】</xsl:text>
						<xsl:apply-templates select="." mode="ICHIRAN"/>
          </xsl:when>
        </xsl:choose>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
