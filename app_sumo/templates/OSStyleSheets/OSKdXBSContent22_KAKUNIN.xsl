<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">
  <!-- ================================================================================= -->
  <!--　編集者用「共通スタイルシート」大相撲・幕内星取表 -->
  <!--  4.0版 2015.06.30 プレーンテキスト化に伴い、確認表示用のファイルを分離　-->
  <!-- ================================================================================= -->
	<!--=======================================================================================================-->
	<!--【確認】スポーツデータタグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="SportsData" mode="KAKUNIN">
    <div class="font_size_KAKUNIN">
      <!--星取表編集-->
      <xsl:call-template name="hositorihyou_KAKUNIN" />
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
	<!--星取表テンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="hositorihyou_KAKUNIN">
		<table xsl:use-attribute-sets="table_attribute_set">
			<!--Head/Meta/Title-->
			<tr>
				<td class="font_size_KAKUNIN" colspan="6">
					<xsl:text>　　☆☆</xsl:text>
					<xsl:value-of select="Head/Meta/Title" />
					<xsl:text>☆☆　</xsl:text>
					<xsl:if test="Head/Limited/LocalInfo">
						<xsl:text>【</xsl:text>
						<xsl:value-of select="Head/Limited/LocalInfo" />
						<xsl:text>】</xsl:text>
					</xsl:if>
					<xsl:value-of select="Head/Limited/LocalInfo" />
				</td>

				<!--今場所成績（詳細）の見出し-->
				<td class="font_size_KAKUNIN" valign="bottom">
					<table xsl:use-attribute-sets="table_attribute_set">
						<tr>
							<xsl:call-template name="seisekimidasi_KAKUNIN"/>
						</tr>
					</table>
				</td>
			</tr>

			<!--Bodyタグを編集-->
			<xsl:for-each select="Body">
				<xsl:if test="Meta/DataType='幕内力士'">
					<!--Title-->
					<tr>
						<td class="font_size_KAKUNIN" colspan="20">
							<xsl:for-each select="Meta/Title">
								<xsl:value-of select="." />
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

					<!--Standing-->
					<xsl:for-each select="Standing">
						<xsl:apply-templates select="Player" mode="hositorihyou_KAKUNIN" />
					</xsl:for-each>
				</xsl:if>
			</xsl:for-each>
		</table>

		<!--空白行-->
		<xsl:if test="Body[Meta/DataType='幕内力士'] and (Body[Meta/DataType='優勝力士'] or Body[Meta/DataType='三賞受賞力士'])">
			<table xsl:use-attribute-sets="table_attribute_set">
				<tr><td class="font_size_KAKUNIN"><br/></td></tr>
			</table>
		</xsl:if>

		<!--優勝力士-->
		<xsl:if test="Body[Meta/DataType='優勝力士']">
			<xsl:text>▽優勝力士</xsl:text>
			<table xsl:use-attribute-sets="table_attribute_set">
				<xsl:for-each select="Body[Meta/DataType='優勝力士']">
					<tr>
						<!--Class-->
						<td class="font_size_KAKUNIN" valign="top" align="left">
							<xsl:text>【</xsl:text>
							<xsl:value-of select="Meta/Class" />
							<xsl:text>】</xsl:text>
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
		</xsl:if>

		<!--空白行-->
		<xsl:if test="Body[Meta/DataType='優勝力士'] and Body[Meta/DataType='三賞受賞力士']">
			<table xsl:use-attribute-sets="table_attribute_set">
				<tr><td class="font_size_KAKUNIN"><br/></td></tr>
			</table>
		</xsl:if>

		<!--三賞受賞力士-->
		<xsl:if test="Body[Meta/DataType='三賞受賞力士']">
			<xsl:text>▽三賞受賞力士</xsl:text>
			<table xsl:use-attribute-sets="table_attribute_set">
				<xsl:for-each select="Body[Meta/DataType='三賞受賞力士']">
					<tr>
						<!--Scope-->
						<td class="font_size_KAKUNIN" valign="top" align="left">
							<xsl:text>【</xsl:text>
							<xsl:value-of select="Meta/Scope" />
							<xsl:text>】</xsl:text>
						</td>

						<!--Paragraphタグ-->
						<xsl:for-each select="Article/Paragraph">
							<td class="font_size_KAKUNIN" valign="center" align="left">
								<xsl:value-of select="." />
							</td>
						</xsl:for-each>

						<!--選手情報-->
						<td class="font_size_KAKUNIN" valign="top" align="left">
							<table xsl:use-attribute-sets="table_attribute_set">
								<xsl:for-each select="Standing/Player">
									<tr>
										<xsl:apply-templates select="." mode="yuusyousannsyoujusyou_KAKUNIN" />
									</tr>
								</xsl:for-each>
							</table>
						</td>
					</tr>
				</xsl:for-each>
			</table>
		</xsl:if>

	</xsl:template>

	<!--=======================================================================================================-->
	<!--成績見出しテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="seisekimidasi_KAKUNIN">
		<xsl:call-template name="seisekimidasi_kobetu_KAKUNIN">
			<xsl:with-param name="POSITION" select="1"/>
		</xsl:call-template>
		<xsl:call-template name="seisekimidasi_kobetu_KAKUNIN">
			<xsl:with-param name="POSITION" select="2"/>
		</xsl:call-template>
		<xsl:call-template name="seisekimidasi_kobetu_KAKUNIN">
			<xsl:with-param name="POSITION" select="3"/>
		</xsl:call-template>
		<xsl:call-template name="seisekimidasi_kobetu_KAKUNIN">
			<xsl:with-param name="POSITION" select="4"/>
		</xsl:call-template>
		<xsl:call-template name="seisekimidasi_kobetu_KAKUNIN">
			<xsl:with-param name="POSITION" select="5"/>
		</xsl:call-template>
		<xsl:call-template name="seisekimidasi_kobetu_KAKUNIN">
			<xsl:with-param name="POSITION" select="6"/>
		</xsl:call-template>
		<xsl:call-template name="seisekimidasi_kobetu_KAKUNIN">
			<xsl:with-param name="POSITION" select="7"/>
		</xsl:call-template>
		<xsl:call-template name="seisekimidasi_kobetu_KAKUNIN">
			<xsl:with-param name="POSITION" select="8"/>
		</xsl:call-template>
		<xsl:call-template name="seisekimidasi_kobetu_KAKUNIN">
			<xsl:with-param name="POSITION" select="9"/>
		</xsl:call-template>
		<xsl:call-template name="seisekimidasi_kobetu_KAKUNIN">
			<xsl:with-param name="POSITION" select="10"/>
		</xsl:call-template>
		<xsl:call-template name="seisekimidasi_kobetu_KAKUNIN">
			<xsl:with-param name="POSITION" select="11"/>
		</xsl:call-template>
		<xsl:call-template name="seisekimidasi_kobetu_KAKUNIN">
			<xsl:with-param name="POSITION" select="12"/>
		</xsl:call-template>
		<xsl:call-template name="seisekimidasi_kobetu_KAKUNIN">
			<xsl:with-param name="POSITION" select="13"/>
		</xsl:call-template>
		<xsl:call-template name="seisekimidasi_kobetu_KAKUNIN">
			<xsl:with-param name="POSITION" select="14"/>
		</xsl:call-template>
		<xsl:call-template name="seisekimidasi_kobetu_KAKUNIN">
			<xsl:with-param name="POSITION" select="15"/>
		</xsl:call-template>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--成績見出しテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="seisekimidasi_kobetu_KAKUNIN">
		<xsl:param name="POSITION" />

		<xsl:if test="Body/Standing/Player/Result/Result[$POSITION]/@Period">
			<td class="font_size_KAKUNIN" valign="bottom">
				<xsl:call-template name="RensuuHenkan">
					<xsl:with-param name="Sts" select="3"/>
					<xsl:with-param name="Pdata" select="Body/Standing/Player/Result/Result[$POSITION]/@Period[1]"/>
				</xsl:call-template>
			</td>
		</xsl:if>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--星取表選手タグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="Player" mode="hositorihyou_KAKUNIN">
		<tr>
			<!--「勝負越」-->
			<td class="font_size_KAKUNIN" valign="bottom">
				<xsl:choose>
					<xsl:when test="Result/ResultForSumo/OutcomeAttribute/Writing">
						<xsl:value-of select="Result/ResultForSumo/OutcomeAttribute/Writing" />
					</xsl:when>
					<xsl:otherwise>
						<xsl:text>　</xsl:text>
					</xsl:otherwise>
				</xsl:choose>
			</td>

			<!--力士名-->
			<td class="font_size_KAKUNIN" valign="bottom">
				<xsl:choose>
					<xsl:when test="PlayerName/Formal[not(@*)]">
						<xsl:if test="PlayerForSumo/PreviousName/Formal[not(@*)]">
							<nobr>
								<xsl:value-of select="PlayerForSumo/PreviousName/Formal[not(@*)]" />
								<xsl:text>改め</xsl:text>
							</nobr>
							<br/>
						</xsl:if>
						<nobr>
							<xsl:value-of select="PlayerName/Formal[not(@*)]" />
						</nobr>
						<br/>
					</xsl:when>
					<xsl:otherwise>
						<xsl:text>　</xsl:text>
					</xsl:otherwise>
				</xsl:choose>
			</td>

			<!--空白-->
			<td class="font_size_KAKUNIN" valign="bottom">
				<table xsl:use-attribute-sets="table_attribute_set" width="14">
					<xsl:text>　</xsl:text>
				</table>
			</td>

			<!--地位-->
			<td class="font_size_KAKUNIN" valign="bottom">
				<xsl:choose>
					<xsl:when test="PlayerForSumo/SumoGrade/Writing">
						<xsl:value-of select="PlayerForSumo/SumoGrade/Writing" />
					</xsl:when>
					<xsl:otherwise>
						<xsl:text>　</xsl:text>
					</xsl:otherwise>
				</xsl:choose>
			</td>

			<!--出身地・出身部屋-->
			<td class="font_size_KAKUNIN" valign="bottom">
				<xsl:if test="
					PlayerForSumo/NativeArea/Formal[not(@*)] or
					PlayerForSumo/NativeCountry/Formal[not(@*)] or
					Belong/Formal[not(@*)]
				">
					<xsl:text>（</xsl:text>
				</xsl:if>

				<xsl:value-of select="PlayerForSumo/NativeArea/Formal[not(@*)]" />
				<xsl:value-of select="PlayerForSumo/NativeCountry/Formal[not(@*)]" />

				<xsl:if test="
					(PlayerForSumo/NativeArea/Formal[not(@*)] or
					PlayerForSumo/NativeCountry/Formal[not(@*)]) and
					Belong/Formal[not(@*)]
				">
					<xsl:text>・</xsl:text>
				</xsl:if>

				<xsl:value-of select="Belong/Formal[not(@*)]" />

				<xsl:if test="
					PlayerForSumo/NativeArea/Formal[not(@*)] or
					PlayerForSumo/NativeCountry/Formal[not(@*)] or
					Belong/Formal[not(@*)]
				">
					<xsl:text>）</xsl:text>
				</xsl:if>
			</td>

			<!--引退 or 今場所成績-->
			<td class="font_size_KAKUNIN" valign="bottom">
				<xsl:choose>
					<xsl:when test="PlayerForSumo/Retirement/Formal[not(@*)]">
						<!--今場所成績-->
						<xsl:value-of select="PlayerForSumo/Retirement/Formal[not(@*)]" />
					</xsl:when>
					<xsl:otherwise>
						<!--今場所成績-->
						<xsl:choose>
							<xsl:when test="Result/ResultForSumo/SumoOutcomeTotal/Writing">
								<xsl:call-template name="RensuuHenkan_KAKUNIN_OSCOM">
									<xsl:with-param name="str" select="Result/ResultForSumo/SumoOutcomeTotal/Writing"/>
								</xsl:call-template>
							</xsl:when>
							<xsl:otherwise>
								<xsl:text>　</xsl:text>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:otherwise>
				</xsl:choose>
			</td>

			<!--今場所成績（詳細）-->
			<td class="font_size_KAKUNIN" valign="bottom">
				<table xsl:use-attribute-sets="table_attribute_set">
					<tr>
						<xsl:for-each select="Result/Result/Outcome/Writing">
							<td class="font_size_KAKUNIN" valign="bottom">
								<xsl:value-of select="." />
							</td>
						</xsl:for-each>
					</tr>
				</table>
			</td>

		</tr>
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
			<xsl:for-each select=".//Meta/Title">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//Head/Limited/LocalInfo">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//Article/Paragraph">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//Result/ResultForSumo/OutcomeAttribute/Writing">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/PreviousName/Formal[not(@*)]">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerName/Formal[not(@*)]">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/SumoGrade/Writing">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/NativeCity/Formal[not(@*)]">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//Belong/Formal[not(@*)]">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//Result/ResultForSumo/SumoOutcomeTotal/Writing">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//Result/Result/Outcome/Writing">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/Retirement/Formal[not(@*)]">
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
