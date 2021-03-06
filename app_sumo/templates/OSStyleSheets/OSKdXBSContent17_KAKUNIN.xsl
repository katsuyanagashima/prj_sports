<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">
  <!-- ================================================================================= -->
  <!--　編集者用「共通スタイルシート」大相撲・優勝三賞受賞力士 -->
  <!--  4.0版 2015.06.30 プレーンテキスト化に伴い、確認表示用のファイルを分離　-->
  <!-- ================================================================================= -->
	<!--=======================================================================================================-->
	<!--【確認】スポーツデータタグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="SportsData" mode="KAKUNIN">
    <div class="font_size_KAKUNIN">

      <!--優勝三賞受賞力士編集-->
      <xsl:call-template name="yuusyousannsyoujusyou_KAKUNIN" />
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
	<!--優勝三賞受賞力士テンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="yuusyousannsyoujusyou_KAKUNIN">
		<!--Title-->
		<table xsl:use-attribute-sets="table_attribute_set" width="650">
			<tr>
				<td class="font_size_KAKUNIN" valign="top">
					<xsl:value-of select="./Head/Meta/Title" />
				</td>
			</tr>
		</table>

		<!--Bodyタグを編集-->
		<!--優勝力士-->
		<xsl:text>▽優勝力士</xsl:text>
		<table xsl:use-attribute-sets="table_attribute_set">
			<xsl:for-each select="Body[Meta/DataType='優勝力士']">
				<tr>
					<!--Title-->
					<td class="font_size_KAKUNIN" valign="top" align="left">
						<xsl:value-of select="Meta/Title" />
					</td>

					<!--Paragraphタグ-->
					<td class="font_size_KAKUNIN" valign="center" align="left">
						<xsl:for-each select="Article/Paragraph">
							<table xsl:use-attribute-sets="table_attribute_set">
								<tr>
									<td class="font_size_KAKUNIN" valign="center" align="left">
										<xsl:text>　</xsl:text>
										<xsl:value-of select="." />
									</td>
								</tr>
							</table>
						</xsl:for-each>
					</td>

					<!--選手情報-->
					<xsl:apply-templates select="Standing/Player" mode="yuusyousannsyoujusyou_KAKUNIN" />
				</tr>
			</xsl:for-each>
		</table>

		<!--空白行-->
		<xsl:if test="Body[Meta/DataType='優勝力士'] and Body[Meta/DataType='三賞受賞力士']">
			<table xsl:use-attribute-sets="table_attribute_set">
				<tr><td class="font_size_KAKUNIN"><br/></td></tr>
			</table>
		</xsl:if>

		<!--三賞受賞力士-->
		<xsl:text>▽三賞受賞力士</xsl:text>
		<table xsl:use-attribute-sets="table_attribute_set">
			<xsl:for-each select="Body[Meta/DataType='三賞受賞力士']">
				<tr>
					<!--Title-->
					<td class="font_size_KAKUNIN" valign="top" align="left">
						<xsl:value-of select="Meta/Title" />
					</td>

					<!--Paragraphタグ-->
					<xsl:for-each select="Article/Paragraph">
						<td class="font_size_KAKUNIN" valign="center" align="left">
							<xsl:value-of select="." />
						</td>
					</xsl:for-each>

					<!--選手情報-->
					<xsl:if test="Standing">
					<td class="font_size_KAKUNIN" valign="top" align="left">
						<table xsl:use-attribute-sets="table_attribute_set">
							<xsl:for-each select="Standing/Player">
								<tr>
									<xsl:apply-templates select="." mode="yuusyousannsyoujusyou_KAKUNIN" />
								</tr>
							</xsl:for-each>
						</table>
					</td>
					</xsl:if>
				</tr>
			</xsl:for-each>

		</table>

	</xsl:template>

	<!--=======================================================================================================-->
	<!--優勝三賞受賞力士選手タグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="Player" mode="yuusyousannsyoujusyou_KAKUNIN">
			<!--力士名-->
			<xsl:if test="//Standing/Player/PlayerName/Formal[not(@*)]">
				<td class="font_size_KAKUNIN" valign="bottom">
					<xsl:if test="PlayerForSumo/PreviousName/Formal[not(@*)]">
						<xsl:text>　</xsl:text>
						<nobr>
							<xsl:value-of select="PlayerForSumo/PreviousName/Formal[not(@*)]" />
							<xsl:text>改め</xsl:text>
						</nobr>
						<br/>
					</xsl:if>
					<nobr>
						<!--力士名-->
						<xsl:value-of select="PlayerName/Formal[not(@*)]" />

						<!--優勝の場合の「○度目」「初優勝」など-->
						<!--殊勲賞、敢闘賞、技能賞の「初」など-->
						<xsl:if test="Result/Award/Count/Writing">
							<xsl:text>（</xsl:text>
							<xsl:value-of select="Result/Award/Count/Writing" />
							<xsl:text>）</xsl:text>
						</xsl:if>
					</nobr>
					<br/>
				</td>
			</xsl:if>

			<!--場所成績-->
			<xsl:if test="//Standing/Player/Result[not(@*)]/ResultForSumo/SumoOutcomeTotal/Writing">
				<td class="font_size_KAKUNIN" valign="bottom" align="left">
					<nobr>
						<xsl:text>　</xsl:text>
						<xsl:value-of select="Result[not(@*)]/ResultForSumo/SumoOutcomeTotal/Writing" />
					</nobr>
					<br/>
				</td>
			</xsl:if>

			<!--部屋・出身地-->
			<xsl:if test="Belong/Formal[not(@*)]">
				<td class="font_size_KAKUNIN" valign="bottom">
					<nobr>
						<xsl:text>（</xsl:text>
						<!--部屋-->
						<xsl:value-of select="PlayerForSumo/NativeCountry/Formal[not(@*)]" />
						<xsl:value-of select="PlayerForSumo/NativeArea/Formal[not(@*)]" />
						<xsl:text>・</xsl:text>
						<!--出身地-->
						<xsl:value-of select="Belong/Formal[not(@*)]" />
						<xsl:text>）</xsl:text>
					</nobr>
					<br/>
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
			<xsl:for-each select=".//Head/Meta/Title">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//Article/Paragraph">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//Meta/Title">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/PreviousName/Formal[not(@*)]">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerName/Formal[not(@*)]">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//Result/Award/Count/Writing">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//Belong/Formal[not(@*)]">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/NativeCountry/Formal[not(@*)]">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/NativeArea/Formal[not(@*)]">
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
