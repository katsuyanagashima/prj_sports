<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">
  <!-- ================================================================================= -->
  <!--　編集者用「共通スタイルシート」大相撲・郷土力士星取表 -->
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
				<td class="font_size_KAKUNIN" colspan="8">
					<xsl:text>　　☆☆</xsl:text>
					<xsl:value-of select="Head/Meta/Title" />
					<xsl:text>☆☆　</xsl:text>
					<xsl:if test="Head/Limited/LocalInfo">
						<xsl:text>【</xsl:text>
						<xsl:value-of select="Head/Limited/LocalInfo" />
						<xsl:text>】</xsl:text>
					</xsl:if>
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
			</xsl:for-each>
		</table>

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
								<xsl:text>▽</xsl:text>
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

			<!--空白-->
			<td class="font_size_KAKUNIN" valign="bottom">
				<table xsl:use-attribute-sets="table_attribute_set" width="14">
					<xsl:text>　</xsl:text>
				</table>
			</td>

			<!--出身市町村-->
			<td class="font_size_KAKUNIN" valign="bottom">
				<xsl:choose>
					<xsl:when test="PlayerForSumo/NativeCity/Formal[not(@*)]">
						<xsl:value-of select="PlayerForSumo/NativeCity/Formal[not(@*)]" />
					</xsl:when>
					<xsl:otherwise>
						<xsl:text>　</xsl:text>
					</xsl:otherwise>
				</xsl:choose>
			</td>

			<!--出身部屋-->
			<td class="font_size_KAKUNIN" valign="bottom">
				<xsl:choose>
					<xsl:when test="Belong/Formal[not(@*)]">
						<xsl:text>（</xsl:text>
						<xsl:value-of select="Belong/Formal[not(@*)]" />
						<xsl:text>）</xsl:text>
					</xsl:when>
					<xsl:otherwise>
						<xsl:text>　</xsl:text>
					</xsl:otherwise>
				</xsl:choose>
			</td>

			<!--引退 or 今場所成績-->
			<td class="font_size_KAKUNIN" valign="bottom">
				<xsl:choose>
					<xsl:when test="PlayerForSumo/Retirement/Formal[not(@*)]">
						<!--引退-->
						<xsl:value-of select="PlayerForSumo/Retirement/Formal[not(@*)]" />
					</xsl:when>
					<xsl:otherwise>
						<!--今場所成績-->
						<xsl:choose>
							<xsl:when test="Result/ResultForSumo/SumoOutcomeTotal/Writing">
								<xsl:value-of select="Result/ResultForSumo/SumoOutcomeTotal/Writing" />
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
			<xsl:for-each select=".//Head/Limited/LocalInfo">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//Meta/Title">
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
