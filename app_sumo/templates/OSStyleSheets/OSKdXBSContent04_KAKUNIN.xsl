<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">
  <!-- ================================================================================= -->
  <!--　編集者用「共通スタイルシート」大相撲・郷土力士新番付 -->
	<!--  4.0版 2015.06.30 プレーンテキスト化に伴い、確認表示用のファイルを分離　-->
  <!-- ================================================================================= -->
	<!--=======================================================================================================-->
	<!--【確認】スポーツデータタグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="SportsData" mode="KAKUNIN">
    <div class="font_size_KAKUNIN">
      <!--郷土力士新番付編集-->
      <xsl:call-template name="kyoudorikisisinbanduke_KAKUNIN" />
      <!--本文内注釈編集-->
      <xsl:for-each select="Body/TextNote">
        <table xsl:use-attribute-sets="table_attribute_set">
          <tr>
            <td class="font_size_KAKUNIN">
              <xsl:value-of select="." />
            </td>
          </tr>
        </table>
      </xsl:for-each>
      <xsl:for-each select="TextNote">
        <table xsl:use-attribute-sets="table_attribute_set">
          <tr>
            <td class="font_size_KAKUNIN">
              <xsl:value-of select="." />
            </td>
          </tr>
        </table>
      </xsl:for-each>
      <!--字解-->
      <xsl:call-template name="Gaiji_KAKUNIN" />
    </div>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--郷土力士新番付テンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="kyoudorikisisinbanduke_KAKUNIN">
		<table xsl:use-attribute-sets="table_attribute_set" width="650">
			<!--Bodyタグを編集-->
			<xsl:for-each select="Body">
				<!--Titleタグ-->
				<xsl:for-each select="Meta/Title">
					<tr>
						<td class="font_size_KAKUNIN" valign="center" align="left" colspan="20">
							<xsl:value-of select="." />
						</td>
					</tr>
				</xsl:for-each>

				<!--Paragraphタグ-->
				<xsl:for-each select="Article/Paragraph">
					<tr>
						<td class="font_size_KAKUNIN" valign="center" align="left" colspan="20">
							<xsl:text>　</xsl:text>
							<xsl:value-of select="." />
						</td>
					</tr>
				</xsl:for-each>

				<!--選手情報-->
				<xsl:apply-templates select="Standing/Player" mode="kyoudorikisisinbanduke_KAKUNIN" />
			</xsl:for-each>
		</table>

	</xsl:template>

	<!--=======================================================================================================-->
	<!--郷土力士新番付選手タグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="Player" mode="kyoudorikisisinbanduke_KAKUNIN">
		<tr>
			<td class="font_size_KAKUNIN">
				<!--力士名-->
				<xsl:if test="//Standing/Player/PlayerName/Formal[not(@*)]">
					<xsl:if test="PlayerForSumo/PreviousName/Formal[not(@*)]">
						<nobr>
							<xsl:value-of select="PlayerForSumo/PreviousName/Formal[not(@*)]" />
							<xsl:text>改め</xsl:text>
						</nobr>
						<br/>
					</xsl:if>
					<nobr>
						<xsl:value-of select="PlayerName/Formal[not(@*)]" />
						<xsl:text>　</xsl:text>
					</nobr>
				</xsl:if>
			</td>
			<td class="font_size_KAKUNIN" valign="bottom" width="650">
				<xsl:text>　</xsl:text>
				<!--新位置-->
				<xsl:if test="//Standing/Player/PlayerForSumo/SumoGrade[@Kind='新位置']/Direction">
					<xsl:value-of select="PlayerForSumo/SumoGrade[@Kind='新位置']/Direction" />
				</xsl:if>
				<xsl:if test="//Standing/Player/PlayerForSumo/SumoGrade[@Kind='新位置']/SumoRank">
					<xsl:call-template name="replace_KAKUNIN_OSCOM">
						<xsl:with-param name="str" select="PlayerForSumo/SumoGrade[@Kind='新位置']/SumoRank" />
						<xsl:with-param name="match" select="../../Meta/Class" />
						<xsl:with-param name="replace" select="''" />
					</xsl:call-template>
				</xsl:if>
				<!--出身地（都市）-->
				<xsl:if test="//Standing/Player/PlayerForSumo/NativeCity/Formal[not(@*)]">
					<xsl:text>（</xsl:text>
					<xsl:value-of select="PlayerForSumo/NativeCity/Formal[not(@*)]" />
					<xsl:text>）</xsl:text>
				</xsl:if>
				<!--部屋-->
				<xsl:if test="//Standing/Player/Belong/Formal[not(@*)]">
					<xsl:value-of select="Belong/Formal[not(@*)]" />
				</xsl:if>
			</td>
		</tr>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--Gaijiテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="Gaiji_KAKUNIN">

		<!-- 字解編集 -->
		<xsl:variable name="JIKAI_DATA">
			<xsl:for-each select=".//Body/TextNote">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//Body/Meta/Title">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//Article/Paragraph">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/PreviousName/Formal[not(@*)]">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerName/Formal[not(@*)]">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/SumoGrade[@Kind='新位置']/Direction">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/SumoGrade[@Kind='新位置']/SumoRank">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/NativeCity/Formal[not(@*)]">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//Belong/Formal[not(@*)]">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
		</xsl:variable>

		<xsl:if test="($JIKAI_DATA!='')">
			<!--字解が存在した場合-->
			<!--改ページ-->
			<p class="pb" />

			<!--字解見出し-->
			<div class="font_size_KAKUNIN">
				<xsl:text>字解情報</xsl:text>
			</div>

			<!--字解-->
			<xsl:value-of disable-output-escaping="yes" select="$JIKAI_DATA" />

			<!--改行-->
			<br />
		</xsl:if>

	</xsl:template>
</xsl:stylesheet>
