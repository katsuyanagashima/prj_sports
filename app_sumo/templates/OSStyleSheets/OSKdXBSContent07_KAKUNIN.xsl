<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">
  <!-- ================================================================================= -->
  <!--　編集者用「共通スタイルシート」大相撲・幕下以下取組 -->
	<!--  4.0版 2015.06.30 プレーンテキスト化に伴い、確認表示用のファイルを分離　-->
  <!-- ================================================================================= -->
	<!--=======================================================================================================-->
	<!--変数定義-->
	<!--=======================================================================================================-->
	<!--  名前エリア編集文字数  -->
	<xsl:variable name="NAME_AREA_LENGTH">
		<!-- ここを変更する（半角）2以上 -->
		<xsl:value-of select="10" />
	</xsl:variable>

	<!--  記録エリア編集文字数  -->
	<xsl:variable name="RESULT_AREA_LENGTH">
		<!-- ここを変更する（半角）1以上 -->
		<xsl:value-of select="5" />
	</xsl:variable>
	<!--=======================================================================================================-->
	<!--【確認】スポーツデータタグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="SportsData" mode="KAKUNIN">
    <div class="font_size_KAKUNIN">
      <!--幕下以下取組編集-->
      <xsl:call-template name="makusitaikatorikumi_KAKUNIN" />
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
	<!--幕下以下取組テンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="makusitaikatorikumi_KAKUNIN">
		<table xsl:use-attribute-sets="table_attribute_set">
			<!--Bodyタグを編集-->
			<xsl:for-each select="Body">
				<!--Title-->
				<tr>
					<td class="font_size_KAKUNIN" colspan="20">
						<xsl:for-each select="Meta/Title">
							<xsl:value-of select="." />
							<br/>
						</xsl:for-each>
					</td>
				</tr>

				<!--Article-->
				<xsl:if test="Article/Paragraph">
					<tr>
						<td class="font_size_KAKUNIN" colspan="20">
							<xsl:text>　</xsl:text>
							<xsl:value-of select="Article/Paragraph" />
						</td>
					</tr>
				</xsl:if>

				<!--Match-->
				<xsl:for-each select="Match">
					<tr>
						<xsl:apply-templates select="Player" mode="makusitaikatorikumi_KAKUNIN" />
					</tr>
				</xsl:for-each>
			</xsl:for-each>
		</table>

	</xsl:template>

	<!--=======================================================================================================-->
	<!--幕下以下取組選手タグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="Player" mode="makusitaikatorikumi_KAKUNIN">
		<!--「―」-->
		<xsl:if test="position() != 1">
			<td class="font_size_KAKUNIN" valign="top" align="left">
				<xsl:attribute name="style">
					<xsl:value-of select="concat('width:',$RESULT_AREA_LENGTH,'em')"/>
				</xsl:attribute>

				<xsl:text>―</xsl:text>
			</td>
		</xsl:if>

		<!--「　」-->
		<xsl:if test="position() = 1">
			<td class="font_size_KAKUNIN" valign="top" align="center"><table xsl:use-attribute-sets="table_attribute_set" width="14"><td/></table></td>
		</xsl:if>

		<td class="font_size_KAKUNIN" valign="top">
			<xsl:attribute name="style">
				<xsl:value-of select="concat('width:',$NAME_AREA_LENGTH + 1,'em')"/>
			</xsl:attribute>

			<xsl:call-template name="AddBR_KAKUNIN_OSCOM">
				<xsl:with-param name="Data">
					<!--力士名-->
					<xsl:value-of select="PlayerName/Formal[not(@*)]" />
					<!--出身地・出身市町村-->
					<xsl:if test="
						PlayerForSumo/NativeCountry/Formal[not(@*)] or 
						PlayerForSumo/NativeArea/Formal[not(@*)] or 
						PlayerForSumo/NativeCity/Formal[not(@*)]
					">
						<xsl:text>（</xsl:text>
						<!--出身地-->
						<xsl:value-of select="PlayerForSumo/NativeCountry/Formal[not(@*)]" />
						<xsl:value-of select="PlayerForSumo/NativeArea/Formal[not(@*)]" />
						<xsl:if test="
							(PlayerForSumo/NativeCountry/Formal[not(@*)] or 
							 PlayerForSumo/NativeArea/Formal[not(@*)]) and 
							PlayerForSumo/NativeCity/Formal[not(@*)]">
							<xsl:text>・</xsl:text>
						</xsl:if>
						<!--出身市町村-->
						<xsl:value-of select="PlayerForSumo/NativeCity/Formal[not(@*)]" />
						<xsl:text>）</xsl:text>
					</xsl:if>
					<!--地位-->
					<xsl:if test="PlayerForSumo/SumoGrade/Writing">
						<xsl:text>　</xsl:text>
						<xsl:value-of select="PlayerForSumo/SumoGrade/Writing" />
					</xsl:if>
				</xsl:with-param>
				<xsl:with-param name="Length" select="$NAME_AREA_LENGTH"/>
				<xsl:with-param name="EditPattern" select="1"/>
			</xsl:call-template>
		</td>
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
			<xsl:for-each select=".//Meta/Title">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//Article/Paragraph">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerName/Formal[not(@*)]">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/NativeCountry/Formal[not(@*)]">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/NativeArea/Formal[not(@*)]">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/NativeCity/Formal[not(@*)]">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/SumoGrade/Writing">
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
