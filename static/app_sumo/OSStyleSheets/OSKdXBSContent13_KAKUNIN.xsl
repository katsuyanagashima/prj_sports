<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">
  <!-- ================================================================================= -->
  <!--　編集者用「共通スタイルシート」大相撲・勝負 -->
  <!--  4.0版 2015.06.30 プレーンテキスト化に伴い、確認表示用のファイルを分離　-->
  <!-- ================================================================================= -->
	<!--=======================================================================================================-->
	<!--変数定義-->
	<!--=======================================================================================================-->
	<!--  名前エリア編集文字数  -->
	<xsl:variable name="NAME_AREA_LENGTH">
		<!-- ここを変更する（半角）2以上 -->
		<xsl:value-of select="5" />
	</xsl:variable>
	<!--  記録エリア編集文字数  -->
	<xsl:variable name="RESULT_AREA_LENGTH">
		<!-- ここを変更する（半角）1以上 -->
		<xsl:value-of select="7" />
	</xsl:variable>
	<!--=======================================================================================================-->
	<!--【確認】スポーツデータタグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="SportsData" mode="KAKUNIN">
    <div class="font_size_KAKUNIN">
      <!--勝負編集-->
      <xsl:call-template name="syobu_KAKUNIN" />
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
	<!--勝負テンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="syobu_KAKUNIN">
		<table xsl:use-attribute-sets="table_attribute_set">
			<!--Bodyタグを編集-->
			<xsl:for-each select="Body">
				<!--Title-->
				<tr>
					<td class="font_size_KAKUNIN"><br/></td>
					<td class="font_size_KAKUNIN"><br/></td>
					<td class="font_size_KAKUNIN" align="left">
						<xsl:for-each select="Meta/Title">
							<xsl:value-of select="." />
							<br/>
						</xsl:for-each>
					</td>
					<td class="font_size_KAKUNIN"><br/></td>
					<td class="font_size_KAKUNIN"><br/></td>
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
						<xsl:apply-templates select="Player" mode="syobu_KAKUNIN" />
					</tr>
				</xsl:for-each>
			</xsl:for-each>
		</table>

	</xsl:template>

	<!--=======================================================================================================-->
	<!--勝負選手タグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="Player" mode="syobu_KAKUNIN">
		<!--「幕内通算対戦勝ち星数」-->
		<xsl:if test="position() = 1">
			<td class="font_size_KAKUNIN" valign="top">
				<xsl:choose>
					<xsl:when test="Result/Result[@Period='幕内通算']/ResultForSumo/SumoOutcomeTotal/WinCount">
						<xsl:call-template name="RensuuHenkan">
							<xsl:with-param name="Sts" select="3"/>
							<xsl:with-param name="Pdata" select="Result/Result[@Period='幕内通算']/ResultForSumo/SumoOutcomeTotal/WinCount"/>
						</xsl:call-template>
					</xsl:when>
					<xsl:otherwise>
						<xsl:text>　</xsl:text>
					</xsl:otherwise>
				</xsl:choose>
			</td>
		</xsl:if>

		<!--決まり手＋時間-->
		<xsl:if test="position() != 1">
			<td class="font_size_KAKUNIN" valign="top">
				<xsl:attribute name="style">
					<xsl:value-of select="concat('width:',$RESULT_AREA_LENGTH + 1,'em')"/>
				</xsl:attribute>
				<xsl:call-template name="AddBR_KAKUNIN_OSCOM">
					<xsl:with-param name="Data">
						<xsl:if test="../MatchDetail/WinningTrick/Formal[not(@*)]">
							<!--決まり手-->
							<xsl:value-of select="../MatchDetail/WinningTrick/Formal[not(@*)]" />
						</xsl:if>
					</xsl:with-param>
					<xsl:with-param name="Length" select="$RESULT_AREA_LENGTH"/>
					<xsl:with-param name="EditPattern" select="3"/>
				</xsl:call-template>
				<!--時間-->
				<xsl:apply-templates select="../MatchDetail/ClosingInfo/ClosingTime" mode="KAKUNIN"/>
			</td>
		</xsl:if>

		<td class="font_size_KAKUNIN" valign="top">
			<xsl:attribute name="style">
				<xsl:value-of select="concat('width:',$NAME_AREA_LENGTH + 1,'em')"/>
			</xsl:attribute>

			<xsl:call-template name="AddBR_KAKUNIN_OSCOM">
				<xsl:with-param name="Data">
					<!--力士名-->
					<xsl:value-of select="PlayerName/Formal[not(@*)]" />
					<!--地位-->
					<xsl:if test="PlayerForSumo/SumoGrade/Writing">
						<xsl:text>　</xsl:text>
						<xsl:value-of select="PlayerForSumo/SumoGrade/Writing" />
					</xsl:if>
				</xsl:with-param>
				<xsl:with-param name="Length" select="$NAME_AREA_LENGTH"/>
				<xsl:with-param name="EditPattern" select="3"/>
			</xsl:call-template>

			<xsl:if test="
				PlayerForSumo/NativeCountry/Formal[not(@*)] or 
				PlayerForSumo/NativeArea/Formal[not(@*)] or 
				PlayerForSumo/NativeCity/Formal[not(@*)]
			">
				<!--出身地・出身市町村の編集がある場合は改行を入れる-->
				<br/>
			</xsl:if>

			<xsl:call-template name="AddBR_KAKUNIN_OSCOM">
				<xsl:with-param name="Data">
					<!--出身地・出身市町村-->
					<xsl:if test="
						PlayerForSumo/NativeCountry/Formal[not(@*)] or 
						PlayerForSumo/NativeArea/Formal[not(@*)] or 
						PlayerForSumo/NativeCity/Formal[not(@*)]
					">
						<xsl:text>（</xsl:text>
						<xsl:if test="position() != 1">
							<!--出身地-->
							<xsl:value-of select="PlayerForSumo/NativeCountry/Formal[not(@*)]" />
							<xsl:value-of select="PlayerForSumo/NativeArea/Formal[not(@*)]" />
							<xsl:if test="
								(PlayerForSumo/NativeCountry/Formal[not(@*)] or 
								 PlayerForSumo/NativeArea/Formal[not(@*)]) and 
								PlayerForSumo/NativeCity/Formal[not(@*)]">
								<xsl:text>・</xsl:text>
							</xsl:if>
						</xsl:if>
						<!--出身市町村-->
						<xsl:value-of select="PlayerForSumo/NativeCity/Formal[not(@*)]" />
						<xsl:text>）</xsl:text>
					</xsl:if>
				</xsl:with-param>
				<xsl:with-param name="Length" select="$NAME_AREA_LENGTH"/>
				<xsl:with-param name="EditPattern" select="1"/>
			</xsl:call-template>

			<xsl:if test="Result/Result[@Period='今場所']/ResultForSumo/SumoOutcomeTotal/Writing">
				<!--今場所成績の編集がある場合は改行を入れる-->
				<br/>
			</xsl:if>

			<xsl:call-template name="AddBR_KAKUNIN_OSCOM">
				<xsl:with-param name="Data">
					<!--今場所成績-->
					<xsl:if test="Result/Result[@Period='今場所']/ResultForSumo/SumoOutcomeTotal/Writing">
						<xsl:value-of select="Result/Result[@Period='今場所']/ResultForSumo/SumoOutcomeTotal/Writing" />
					</xsl:if>
				</xsl:with-param>
				<xsl:with-param name="Length" select="$NAME_AREA_LENGTH"/>
				<xsl:with-param name="EditPattern" select="3"/>
			</xsl:call-template>

		</td>

		<!--「幕内通算対戦勝ち星数」-->
		<xsl:if test="position() = 2">
			<td class="font_size_KAKUNIN" valign="top">
				<xsl:choose>
					<xsl:when test="Result/Result[@Period='幕内通算']/ResultForSumo/SumoOutcomeTotal/WinCount">
						<xsl:call-template name="RensuuHenkan">
							<xsl:with-param name="Sts" select="3"/>
							<xsl:with-param name="Pdata" select="Result/Result[@Period='幕内通算']/ResultForSumo/SumoOutcomeTotal/WinCount"/>
						</xsl:call-template>
					</xsl:when>
					<xsl:otherwise>
						<xsl:text>　</xsl:text>
					</xsl:otherwise>
				</xsl:choose>
			</td>
		</xsl:if>

	</xsl:template>

	<!--=======================================================================================================-->
	<!--時間タグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="MatchDetail/ClosingInfo/ClosingTime" mode="KAKUNIN">
		<br/>
		<xsl:call-template name="AddBR_KAKUNIN_OSCOM">
			<xsl:with-param name="Data">
				<xsl:text>（</xsl:text>
				<!--時-->
				<xsl:if test="Hour">
					<xsl:call-template name="RensuuHenkan">
						<xsl:with-param name="Sts" select="10" />
						<xsl:with-param name="Pdata" select="Hour" />
					</xsl:call-template>
					<xsl:text>時間</xsl:text>
				</xsl:if>
				<!--分-->
				<xsl:if test="Minute">
					<xsl:call-template name="RensuuHenkan">
						<xsl:with-param name="Sts" select="10" />
						<xsl:with-param name="Pdata" select="Minute" />
					</xsl:call-template>
					<xsl:text>分</xsl:text>
				</xsl:if>
				<!--秒-->
				<xsl:if test="Second">
					<xsl:call-template name="RensuuHenkan">
						<xsl:with-param name="Sts" select="10" />
						<xsl:with-param name="Pdata" select="Second" />
					</xsl:call-template>
					<xsl:text>秒</xsl:text>
				</xsl:if>

				<!--秒以下-->
				<xsl:call-template name="RensuuHenkan">
					<xsl:with-param name="Sts" select="10" />
					<xsl:with-param name="Pdata" select="concat('＊', Fraction)" />
				</xsl:call-template>

				<xsl:text>）</xsl:text>
			</xsl:with-param>
			<xsl:with-param name="Length" select="$RESULT_AREA_LENGTH"/>
			<xsl:with-param name="EditPattern" select="3"/>
		</xsl:call-template>
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
			<xsl:for-each select=".//MatchDetail/WinningTrick/Formal[not(@*)]">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerName/Formal[not(@*)]">
				<xsl:call-template name="Gaiji_com_KAKUNIN_OSCOM"/>
			</xsl:for-each>
			<xsl:for-each select=".//PlayerForSumo/SumoGrade/Writing">
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
			<xsl:for-each select=".//Result/Result[@Period='今場所']/ResultForSumo/SumoOutcomeTotal/Writing">
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
