<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">
  <!-- ================================================================================= -->
  <!--　編集者用「共通スタイルシート」大相撲・中入り取組 -->
	<!--  4.0版 2015.06.30 プレーンテキスト化に伴い、確認表示用のファイルを分離　-->
  <!-- ================================================================================= -->
	<!--=======================================================================================================-->
	<!--【確認】スポーツデータタグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="SportsData" mode="KAKUNIN">
    <div class="font_size_KAKUNIN">
      <!--中入り取組編集-->
      <xsl:call-template name="nakairitorikumi_KAKUNIN" />
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
	<!--中入り取組テンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="nakairitorikumi_KAKUNIN">
		<table xsl:use-attribute-sets="table_attribute_set">
			<!--Bodyタグを編集-->
			<xsl:for-each select="Body">
				<!--Title-->
				<tr>
					<td class="font_size_KAKUNIN">
						<br/>
					</td>
					<td class="font_size_KAKUNIN">
						<br/>
					</td>
					<td class="font_size_KAKUNIN">
						<br/>
					</td>
					<td class="font_size_KAKUNIN" colspan="6" align="center">
						<xsl:for-each select="Meta/Title">
							<xsl:value-of select="." />
							<br/>
						</xsl:for-each>
					</td>
					<td class="font_size_KAKUNIN">
						<br/>
					</td>
					<td class="font_size_KAKUNIN">
						<br/>
					</td>
					<td class="font_size_KAKUNIN">
						<br/>
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
				<tr>
					<td class="font_size_KAKUNIN" valign="bottom">
						<xsl:text>（</xsl:text>
						<xsl:value-of select="Match[1]/Player[1]/PlayerForSumo/SumoGrade/Direction" />
						<xsl:text>）</xsl:text>
					</td>
					<td class="font_size_KAKUNIN">
						<br/>
					</td>
					<td class="font_size_KAKUNIN">
						<br/>
					</td>
					<xsl:for-each select="Match[Player/Result/Result/Outcome][1]/Player[1]/Result/Result">
						<xsl:if test="position() != 1">
							<td class="font_size_KAKUNIN" valign="top">
								<xsl:value-of select="substring(@Period,3,1)" />
								<br/>
								<xsl:if test="substring(preceding-sibling::Result[1]/@Period,1,2) != substring(@Period,1,2)">
									<xsl:call-template name="RensuuHenkan">
										<xsl:with-param name="Sts" select="4"/>
										<xsl:with-param name="Pdata" select="substring(@Period,1,2)"/>
									</xsl:call-template>
								</xsl:if>
							</td>
						</xsl:if>
					</xsl:for-each>
					<td class="font_size_KAKUNIN">
						<br/>
					</td>
					<td class="font_size_KAKUNIN">
						<br/>
					</td>
					<td class="font_size_KAKUNIN" valign="bottom">
						<xsl:text>（</xsl:text>
						<xsl:value-of select="Match[1]/Player[2]/PlayerForSumo/SumoGrade/Direction" />
						<xsl:text>）</xsl:text>
					</td>
				</tr>
				<xsl:for-each select="Match">
					<tr>
						<xsl:apply-templates select="Player" mode="nakairitorikumi_KAKUNIN" />
					</tr>
				</xsl:for-each>
			</xsl:for-each>
		</table>

	</xsl:template>

	<!--=======================================================================================================-->
	<!--中入り取組選手タグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="Player" mode="nakairitorikumi_KAKUNIN">
		<xsl:choose>
			<xsl:when test="position()=1">
				<td class="font_size_KAKUNIN" valign="bottom">
					<nobr>
						<!--力士名-->
						<xsl:value-of select="PlayerName/Formal[not(@*)]" />
					</nobr>
				</td>
				<td class="font_size_KAKUNIN" valign="bottom">
					<nobr>
						<!--地位-->
						<xsl:if test="PlayerForSumo/SumoGrade/Writing">
							<xsl:value-of select="PlayerForSumo/SumoGrade/Writing" />
						</xsl:if>
						<!--勝敗-->
						<xsl:if test="Result/Result[@Period='幕内通算']/ResultForSumo/SumoOutcomeTotal/WinCount">
							<xsl:call-template name="RensuuHenkan">
								<xsl:with-param name="Sts" select="3"/>
								<xsl:with-param name="Pdata" select="Result/Result[@Period='幕内通算']/ResultForSumo/SumoOutcomeTotal/WinCount"/>
							</xsl:call-template>
						</xsl:if>
					</nobr>
				</td>
			</xsl:when>
			<xsl:otherwise>
				<td class="font_size_KAKUNIN" valign="bottom">
					<nobr>
						<!--地位-->
						<xsl:if test="PlayerForSumo/SumoGrade/Writing">
							<xsl:value-of select="PlayerForSumo/SumoGrade/Writing" />
						</xsl:if>
						<!--勝敗-->
						<xsl:if test="Result/Result[@Period='幕内通算']/ResultForSumo/SumoOutcomeTotal/WinCount">
							<xsl:call-template name="RensuuHenkan">
								<xsl:with-param name="Sts" select="3"/>
								<xsl:with-param name="Pdata" select="Result/Result[@Period='幕内通算']/ResultForSumo/SumoOutcomeTotal/WinCount"/>
							</xsl:call-template>
						</xsl:if>
					</nobr>
				</td>
				<td class="font_size_KAKUNIN" valign="bottom">
					<nobr>
						<!--力士名-->
						<xsl:value-of select="PlayerName/Formal[not(@*)]" />
					</nobr>
				</td>
			</xsl:otherwise>
		</xsl:choose>
		<xsl:if test="position()=1">
			<td class="font_size_KAKUNIN" valign="bottom">
				<xsl:text>（</xsl:text>
			</td>
			<xsl:choose>
				<xsl:when test="Result/Result/Outcome/Writing">
					<xsl:for-each select="Result/Result/Outcome/Writing">
						<td class="font_size_KAKUNIN" valign="top">
							<xsl:value-of select="." />
						</td>
					</xsl:for-each>
				</xsl:when>
				<xsl:otherwise>
					<td class="font_size_KAKUNIN" valign="bottom"><br/></td>
					<td class="font_size_KAKUNIN" valign="bottom"><br/></td>
					<td class="font_size_KAKUNIN" valign="bottom"><br/></td>
					<td class="font_size_KAKUNIN" valign="bottom"><br/></td>
					<td class="font_size_KAKUNIN" valign="bottom"><br/></td>
					<td class="font_size_KAKUNIN" valign="bottom"><br/></td>
				</xsl:otherwise>
			</xsl:choose>
			<td class="font_size_KAKUNIN" valign="bottom">
				<xsl:text>）</xsl:text>
			</td>
		</xsl:if>
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
			<xsl:for-each select=".//PlayerForSumo/SumoGrade/Writing">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//Result/Result/Outcome/Writing">
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
