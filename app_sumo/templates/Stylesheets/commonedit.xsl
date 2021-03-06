<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja">
<!--=============================================================================
　プレーンテキスト・全スタイルシート共通編集用
4.0版　 2014.12.19 プレーンテキスト版として新規公開
4.01版　2015.05.29 改行コードをCRLFに統一
================================================================================-->
  <!--=======================================================================================================-->
  <!--本文内注釈（SportsData単位、Body単位、Match単位）の編集-->
  <!--=======================================================================================================-->
  <xsl:template match="TextNote" mode="KAKUNIN2_EDT">
    <xsl:text>（</xsl:text>
    <xsl:value-of select="."/>
    <xsl:text>）</xsl:text>
    <!--改行文字-->
    <xsl:value-of select="$LineFeed_UTL"/>
  </xsl:template>
  <!--=======================================================================================================-->
  <!--共同クレジットの編集-->
  <!--=======================================================================================================-->
  <xsl:template name="CreditLabel_EDT">
    <xsl:if test="//CreditLabel">
      <xsl:text>（</xsl:text>
      <xsl:value-of select="//CreditLabel"/>
      <xsl:text>）</xsl:text>
      <!--改行文字-->
      <xsl:value-of select="$LineFeed_UTL"/>
    </xsl:if>
  </xsl:template>
  <!--=======================================================================================================-->
  <!--字解の編集-->
  <!--=======================================================================================================-->
  <xsl:template name="Gaiji_EDT">
    <xsl:for-each select="KdGaiji">
      <xsl:value-of select="parent::*"/>
      <xsl:text>　</xsl:text>
      <xsl:text>☆</xsl:text>
      <xsl:value-of select="@KdJikai"/>
      <xsl:value-of select="$LineFeed_UTL"/>
    </xsl:for-each>
  </xsl:template>
  <!--=======================================================================================================-->
  <!--仮見出しの編集-->
  <!--=======================================================================================================-->
  <xsl:template name="PTateHeadLine_EDT">
    <xsl:call-template name="TranslateChar_UTL">
      <xsl:with-param name="Before" select="'－'"/>
      <xsl:with-param name="After" select="'―'"/>
      <xsl:with-param name="Data">
        <xsl:if test="//InHeadLine">
          <xsl:text>◎</xsl:text>
          <xsl:call-template name="TranslateToRensuuText_UTL">
            <xsl:with-param name="Data" select="//InHeadLine"/>
          </xsl:call-template>
          <!--改行文字-->
          <xsl:value-of select="$LineFeed_UTL"/>
        </xsl:if>
        <xsl:if test="//InSubHeadLine">
          <xsl:for-each select="//InSubHeadLine">
            <xsl:text>　　</xsl:text>
            <xsl:value-of select="."/>
            <!--改行文字-->
            <xsl:value-of select="$LineFeed_UTL"/>
          </xsl:for-each>
        </xsl:if>
        <xsl:value-of select="$LineFeed_UTL"/>
      </xsl:with-param>
    </xsl:call-template>
  </xsl:template>
</xsl:stylesheet>
