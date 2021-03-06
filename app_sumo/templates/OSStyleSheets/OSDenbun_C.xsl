<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">

<!-- 3.0版　2014.2.26 html関連タグの小文字化 -->

<xsl:output method="html" encoding="UTF-16" indent="yes" />
<xsl:output doctype-public="-//W3C//DTD HTML 4.01 Transitional//EN" />
<xsl:param name="HtmlFileXml">
<html>
<head>
<meta http-equiv="Content-Style-Type" content="text/css" />
<meta http-equiv="Content-Script-Type" content="text/javascript" />
<title>電文書式</title>
<style type="text/css">
			body{direction:rtl;overflow-x:scroll;overflow-y:auto;font-family:U-PRESS;}
			td{ direction:ltr;writing-mode:tb-rl;line-height:120%;font-size:12pt;margin:1px;}
			th{ direction:ltr;writing-mode:lr-tb;line-height:120%;font-size:12pt;margin:1px;}
		</style>
</head>
<body>
<table border="1" align="right">
<tbody>
<tr class="Header">
<th nowrap="nowrap" style="direction:ltr;writing-mode:lr-tb;font-size:9pt;" bgcolor="#99FFFF" align="right">右タイトル</th>
<th nowrap="nowrap" style="direction:ltr;writing-mode:lr-tb;font-size:12pt;" bgcolor="#99FFFF" align="left">左タイトル</th>
</tr>
<tr class="Denbun">
<td nowrap="nowrap" align="left" valign="top" bgcolor="#DDFFDD" colspan="2">　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">　</span>へ<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">　</span><br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">　</span>共角３ヲ０６３相撲３Ｔ③完③<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">　</span>◇相撲<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">　</span>【●ＣＰ中日ＡＫ日ス名<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">　</span>古】<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">　</span>◎郷土力士番付表<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">　</span>０４年５月夏場所<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">　</span><br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">･</span>◇愛知<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">･</span>【三段目】<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">･</span>暁司西１（名古屋）入間川<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">･</span>東輝龍西４（名古屋）玉ノ井<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">５</span>若春日西７（一宮）春日山<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">･</span>清東東１４（春日井）玉ノ井<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">･</span>木曽満東１６（犬山）時津風<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">･</span>冨士ノ国西１８（名古屋）中村<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">･</span>御田乃山西２３（名古屋）高田川<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS"></span>高稲沢東２４（稲沢）高砂<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">･</span>鶴嶺山東２５（刈谷）井筒<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">･</span>安咲海西２５（名古屋）安治川<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">･</span>竜司東４０（日進）入間川<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">･</span>成竜東４３（刈谷）二所関<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS"></span>薩摩錦東４８（豊田）松ケ根<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">･</span>豊海西５２（七宝）中村<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">･</span>幸司東５４（春日井）入間川<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">･</span>吉村東７６（名古屋）田子浦<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">･</span>清城東７８（半田）二所関<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS"></span>玉剣東８０（名古屋）玉ノ井<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">･</span>哲光西８５（一宮）式秀<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">･</span>貴ノ昇東８８（田原）貴乃花<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">･</span>吉の龍東９１（春日井）出羽海<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">･</span>追風城西９８（岡崎）追手風<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS"></span>【幕下】<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">･</span>玉飛鳥西１６（名古屋）片男波<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">･</span>双瀬川東４０（豊橋）桐山<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">･</span>早瀬川東５２（渥美）桐山<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">･</span>立豊西６０（名古屋）立浪<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">　</span>（了）（）８<br />　<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">　</span><br />
</td>
</tr>
<tr class="Page">
<td style="background-color:#dcdcdc ;margin:1px;height:5pt;" colspan="2" />
</tr>
<tr class="Header">
<th nowrap="nowrap" style="page-Break-before:always;direction:ltr;writing-mode:lr-tb;font-size:9pt;" bgcolor="#99FFFF" align="right">右タイトル</th>
<th nowrap="nowrap" style="page-Break-before:always;direction:ltr;writing-mode:lr-tb;font-size:12pt;" bgcolor="#99FFFF" align="left">左タイトル</th>
</tr>
<tr class="Page">
<td style="background-color:#dcdcdc ;margin:1px;height:5pt;page-Break-before:always;" colspan="2" />
</tr>
</tbody>
</table>
</body>
</html>
</xsl:param>
<xsl:param name="HtmlFromNewsML" select="document('')/xsl:stylesheet/xsl:param[@name='HtmlFileXml']" />
<xsl:param name="PB">
<xsl:text>58</xsl:text>
</xsl:param>
<xsl:param name="TLB">
<xsl:text>32</xsl:text>
</xsl:param>
<xsl:param name="NLB">
<xsl:text>11</xsl:text>
</xsl:param>
<xsl:param name="NCL">
<xsl:text></xsl:text>
</xsl:param>
<xsl:param name="KZCL">
<xsl:text>←</xsl:text>
</xsl:param>
<xsl:param name="tate">﹁﹂︵︶︻︼‖－　</xsl:param>
<xsl:param name="yoko">「」（）、。【】＝｜－ー〓―</xsl:param>
<xsl:variable name="ren">０１２３４５６７８９</xsl:variable>
<xsl:template match="/">
<xsl:variable name="NewsML" select="//NewsML" />
<xsl:apply-templates select="$HtmlFromNewsML/*">
<xsl:with-param name="NewsML" select="$NewsML" />
</xsl:apply-templates>
</xsl:template>
<xsl:template match="*">
<xsl:param name="NewsML" />
<xsl:choose>
<xsl:when test="count(*)&gt;0">
<xsl:copy>
<xsl:copy-of select="@*" />
<xsl:apply-templates select="text()|*">
<xsl:with-param name="NewsML" select="$NewsML" />
</xsl:apply-templates>
</xsl:copy>
</xsl:when>
<xsl:otherwise>
<xsl:copy-of select="." />
</xsl:otherwise>
</xsl:choose>
</xsl:template>
<xsl:template match="title">
<xsl:param name="NewsML" />
<xsl:copy>
<xsl:copy-of select="@*" />
<xsl:value-of select="$NewsML//InNewsGenre/text()" />
<xsl:text>電文書式</xsl:text>
</xsl:copy>
</xsl:template>
<xsl:template match="tr[@class='Header']" />
<xsl:template match="tr[@class='Page']" />
<xsl:template match="tr[@class='Denbun']">
<xsl:param name="NewsML" />
<xsl:choose>
<xsl:when test="$NewsML//Denbun">
<xsl:variable name="TD" select="td" />
<xsl:variable name="PAGE" select="following-sibling::tr[@class='Page']" />
<xsl:variable name="HEADER" select="preceding-sibling::tr[@class='Header']/th" />
<xsl:variable name="HEADER2" select="following-sibling::tr[@class='Header']/th" />
<xsl:for-each select="$NewsML">
<xsl:variable name="LB">
<xsl:choose>
<xsl:when test="(.//InFormatComment/text())='定型'">
<xsl:value-of select="$TLB" />
</xsl:when>
<xsl:otherwise>
<xsl:value-of select="$NLB" />
</xsl:otherwise>
</xsl:choose>
</xsl:variable>
<xsl:variable name="HeaderLine1">
<xsl:value-of select=".//HeadLine/text()" />
<xsl:variable name="InClass" select=".//InClass" />
<xsl:if test="count($InClass/*)&gt;0">
<xsl:text>【</xsl:text>
<xsl:for-each select="$InClass/*">
<xsl:if test="not(position() = 1)">
<xsl:text>－</xsl:text>
</xsl:if>
<xsl:value-of select="text()" />
</xsl:for-each>
<xsl:text>】</xsl:text>
</xsl:if>
</xsl:variable>
<xsl:variable name="HeaderLine2">
<xsl:variable name="date" select=".//ThisRevisionCreated/text()" />
<xsl:text>《</xsl:text>
<xsl:if test="boolean(./ancestor::ITalk//IhSendMode)">
<xsl:value-of select="concat(ancestor::ITalk//IhSendMode,'－')" />
</xsl:if>
<xsl:choose>
<xsl:when test="boolean(.//InTestClass)">
<xsl:value-of select=".//InTestClass" />
</xsl:when>
<xsl:otherwise>
<xsl:text>通常</xsl:text>
</xsl:otherwise>
</xsl:choose>
<xsl:if test="boolean(.//InModifyInfo)">
<xsl:value-of select="concat('：',.//InModifyInfo)" />
</xsl:if>
<xsl:text>》</xsl:text>
<xsl:value-of select="concat(substring($date,1,4),'/')" />
<xsl:value-of select="concat(substring($date,5,2),'/')" />
<xsl:value-of select="substring($date,7,2)" />
<xsl:value-of select="concat(' ',substring($date,10,2),':')" />
<xsl:value-of select="concat(substring($date,12,2),':')" />
<xsl:value-of select="substring($date,14,2)" />
</xsl:variable>
<xsl:for-each select=".//Denbun">
<xsl:variable name="pos" select="position()" />
<xsl:variable name="CL">
<xsl:choose>
<xsl:when test="not(contains(text(),$NCL)) and (contains(text(),$KZCL))">
<xsl:value-of select="$KZCL" />
</xsl:when>
<xsl:otherwise>
<xsl:value-of select="$NCL" />
</xsl:otherwise>
</xsl:choose>
</xsl:variable>
<xsl:element name="tr">
<xsl:choose>
<xsl:when test="$pos = 1">
<xsl:for-each select="$HEADER">
<xsl:copy>
<xsl:copy-of select="@*" />
<xsl:choose>
<xsl:when test="position()=1">
<xsl:value-of select="$HeaderLine2" />
</xsl:when>
<xsl:when test="position()=2">
<xsl:value-of select="$HeaderLine1" />
</xsl:when>
</xsl:choose>
</xsl:copy>
</xsl:for-each>
</xsl:when>
<xsl:otherwise>
<xsl:for-each select="$HEADER2">
<xsl:copy>
<xsl:copy-of select="@*" />
<xsl:choose>
<xsl:when test="position()=1">
<xsl:value-of select="$HeaderLine2" />
</xsl:when>
<xsl:when test="position()=2">
<xsl:value-of select="$HeaderLine1" />
</xsl:when>
</xsl:choose>
</xsl:copy>
</xsl:for-each>
</xsl:otherwise>
</xsl:choose>
</xsl:element>
<xsl:call-template name="AddTags">
<xsl:with-param name="TEXT" select="text()" />
<xsl:with-param name="LB" select="$LB" />
<xsl:with-param name="PAGE" select="$PAGE" />
<xsl:with-param name="TD" select="$TD" />
<xsl:with-param name="CL" select="$CL" />
</xsl:call-template>
</xsl:for-each>
</xsl:for-each>
</xsl:when>
<xsl:otherwise>
<xsl:element name="th">
<xsl:text>ＤＴＤ実行エラーまたは、表示する電文がありません。</xsl:text>
</xsl:element>
</xsl:otherwise>
</xsl:choose>
</xsl:template>
<xsl:template name="AddTags">
<xsl:param name="TEXT" />
<xsl:param name="LB" />
<xsl:param name="PAGE" />
<xsl:param name="TD" />
<xsl:param name="CL" select="$NCL" />
<xsl:param name="LINE" select="1" />
<xsl:param name="LINES" select="0" />
<xsl:param name="DATA" />
<xsl:variable name="BEFORE" select="substring-before($TEXT,$CL)" />
<xsl:variable name="AFTER" select="substring-after($TEXT,$CL)" />
<xsl:choose>
<xsl:when test="$BEFORE or starts-with($TEXT,$CL)">
<xsl:call-template name="AddTag">
<xsl:with-param name="TEXT" select="concat($BEFORE,$CL)" />
<xsl:with-param name="AFTER" select="$AFTER" />
<xsl:with-param name="LB" select="$LB" />
<xsl:with-param name="PAGE" select="$PAGE" />
<xsl:with-param name="TD" select="$TD" />
<xsl:with-param name="LINE" select="$LINE" />
<xsl:with-param name="LINES" select="$LINES" />
<xsl:with-param name="DATA" select="$DATA" />
<xsl:with-param name="CL" select="$CL" />
</xsl:call-template>
</xsl:when>
<xsl:when test="$TEXT">
<xsl:call-template name="AddTag">
<xsl:with-param name="TEXT" select="$TEXT" />
<xsl:with-param name="LB" select="$LB" />
<xsl:with-param name="PAGE" select="$PAGE" />
<xsl:with-param name="LINE" select="$LINE" />
<xsl:with-param name="LINES" select="$LINES" />
<xsl:with-param name="TD" select="$TD" />
<xsl:with-param name="DATA" select="$DATA" />
<xsl:with-param name="CL" select="$CL" />
</xsl:call-template>
</xsl:when>
<xsl:otherwise>
<xsl:if test="$DATA">
<xsl:element name="tr">
<xsl:element name="td">
<xsl:copy-of select="$TD/@*" />
<xsl:copy-of select="$DATA" />
</xsl:element>
</xsl:element>
</xsl:if>
</xsl:otherwise>
</xsl:choose>
</xsl:template>
<xsl:template name="AddTag">
<xsl:param name="TEXT" />
<xsl:param name="AFTER" />
<xsl:param name="LB" />
<xsl:param name="PAGE" />
<xsl:param name="TD" />
<xsl:param name="LINE" select="1" />
<xsl:param name="LINES" select="0" />
<xsl:param name="DATA" />
<xsl:param name="CL" select="$NCL" />
<xsl:variable name="LINESC">
<xsl:choose>
<xsl:when test="($LINES = 0) and (contains($TEXT,''))">
<xsl:value-of select="$LINE" />
</xsl:when>
<xsl:when test="not($LINES = 0) and (starts-with($TEXT,'︵続︶') or starts-with($TEXT ,'︵了︶'))">
<xsl:text>-1</xsl:text>
</xsl:when>
<xsl:otherwise>
<xsl:value-of select="$LINES" />
</xsl:otherwise>
</xsl:choose>
</xsl:variable>
<xsl:choose>
<xsl:when test="(($LINE mod $PB) = 0) and ($DATA)">
<xsl:element name="tr">
<xsl:element name="td">
<xsl:copy-of select="$TD/@*" />
<xsl:copy-of select="$DATA" />
</xsl:element>
</xsl:element>
<xsl:choose>
<xsl:when test="(($LINE div $PB) mod 2) = 1">
<xsl:copy-of select="$PAGE[position()=1]" />
</xsl:when>
<xsl:otherwise>
<xsl:copy-of select="$PAGE[position()=2]" />
</xsl:otherwise>
</xsl:choose>
<xsl:call-template name="AddTag">
<xsl:with-param name="TEXT" select="$TEXT" />
<xsl:with-param name="AFTER" select="$AFTER" />
<xsl:with-param name="LB" select="$LB" />
<xsl:with-param name="PAGE" select="$PAGE" />
<xsl:with-param name="TD" select="$TD" />
<xsl:with-param name="LINE" select="$LINE" />
<xsl:with-param name="LINES" select="$LINESC" />
<xsl:with-param name="CL" select="$CL" />
</xsl:call-template>
</xsl:when>
<xsl:when test="($LINES = 0) or ($LINESC = -1)">
<xsl:variable name="NewDATA">
<xsl:copy-of select="$DATA" />
<xsl:call-template name="SetGage">
<xsl:with-param name="LINE" select="$LINE" />
<xsl:with-param name="LINES" select="$LINES" />
<xsl:with-param name="LINESC" select="$LINESC" />
</xsl:call-template>
<xsl:call-template name="TextWrite">
<xsl:with-param name="TEXT" select="$TEXT" />
</xsl:call-template>
<xsl:element name="br" />
</xsl:variable>
<xsl:call-template name="AddTags">
<xsl:with-param name="TEXT" select="$AFTER" />
<xsl:with-param name="LB" select="$LB" />
<xsl:with-param name="PAGE" select="$PAGE" />
<xsl:with-param name="TD" select="$TD" />
<xsl:with-param name="LINE" select="$LINE + 1" />
<xsl:with-param name="LINES" select="$LINESC" />
<xsl:with-param name="DATA" select="$NewDATA" />
<xsl:with-param name="CL" select="$CL" />
</xsl:call-template>
</xsl:when>
<xsl:when test="string-length($TEXT) &gt; ($LB + 1)">
<xsl:variable name="NewDATA">
<xsl:copy-of select="$DATA" />
<xsl:call-template name="SetGage">
<xsl:with-param name="LINE" select="$LINE" />
<xsl:with-param name="LINES" select="$LINES" />
<xsl:with-param name="LINESC" select="$LINESC" />
</xsl:call-template>
<xsl:call-template name="TextWrite">
<xsl:with-param name="TEXT" select="substring($TEXT,1,$LB)" />
</xsl:call-template>
<xsl:element name="br" />
</xsl:variable>
<xsl:call-template name="AddTag">
<xsl:with-param name="TEXT" select="substring($TEXT,$LB + 1)" />
<xsl:with-param name="AFTER" select="$AFTER" />
<xsl:with-param name="LB" select="$LB" />
<xsl:with-param name="PAGE" select="$PAGE" />
<xsl:with-param name="TD" select="$TD" />
<xsl:with-param name="LINE" select="$LINE + 1" />
<xsl:with-param name="LINES" select="$LINESC" />
<xsl:with-param name="DATA" select="$NewDATA" />
<xsl:with-param name="CL" select="$CL" />
</xsl:call-template>
</xsl:when>
<xsl:otherwise>
<xsl:variable name="NewDATA">
<xsl:copy-of select="$DATA" />
<xsl:call-template name="SetGage">
<xsl:with-param name="LINE" select="$LINE" />
<xsl:with-param name="LINES" select="$LINES" />
<xsl:with-param name="LINESC" select="$LINESC" />
</xsl:call-template>
<xsl:call-template name="TextWrite">
<xsl:with-param name="TEXT" select="$TEXT" />
</xsl:call-template>
<xsl:element name="br" />
</xsl:variable>
<xsl:call-template name="AddTags">
<xsl:with-param name="TEXT" select="$AFTER" />
<xsl:with-param name="LB" select="$LB" />
<xsl:with-param name="PAGE" select="$PAGE" />
<xsl:with-param name="TD" select="$TD" />
<xsl:with-param name="LINE" select="$LINE + 1" />
<xsl:with-param name="LINES" select="$LINESC" />
<xsl:with-param name="DATA" select="$NewDATA" />
<xsl:with-param name="CL" select="$CL" />
</xsl:call-template>
</xsl:otherwise>
</xsl:choose>
</xsl:template>
<xsl:template name="TextWrite">
<xsl:param name="TEXT" />
<xsl:if test="$TEXT">
<xsl:variable name="Tip" select="substring($TEXT,1,1)" />
<xsl:choose>
<xsl:when test="contains($yoko,$Tip)">
<span style="writing-mode:lr-tb;line-height:100%;">
<xsl:value-of select="$Tip" />
</span>
</xsl:when>
<!--xsl:when test="$Tip = '｜'">
					<span style="writing-mode:lr-tb;line-height:100%;">
						<xsl:value-of select="$Tip"/>
					</span>
				</xsl:when-->
<xsl:otherwise>
<xsl:value-of select="translate($Tip,$tate,$yoko)" />
</xsl:otherwise>
</xsl:choose>
<xsl:call-template name="TextWrite">
<xsl:with-param name="TEXT" select="substring($TEXT,2)" />
</xsl:call-template>
</xsl:if>
</xsl:template>
<xsl:template name="SetGage">
<xsl:param name="LINE" select="1" />
<xsl:param name="LINES" select="0" />
<xsl:param name="LINESC" select="0" />
<!--span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS"!-->
<xsl:text>　</xsl:text>
<span style="writing-mode:lr-tb;line-height:200%;font-size:10pt;font-family:U-PRESS">
<xsl:choose>
<xsl:when test="not($LINES = 0) and not($LINESC = -1)">
<xsl:choose>
<xsl:when test="(($LINE - $LINES) mod 5)=0">
<xsl:value-of select="substring($ren,($LINE - $LINES)+1,1)" />
</xsl:when>
<xsl:otherwise>
<!--xsl:text>・</xsl:text-->
<xsl:text>･</xsl:text>
</xsl:otherwise>
</xsl:choose>
</xsl:when>
<xsl:otherwise>
<xsl:text>　</xsl:text>
</xsl:otherwise>
</xsl:choose>
</span>
</xsl:template>
</xsl:stylesheet>
