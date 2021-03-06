<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">

<!-- 3.0版　2014.2.26 html関連タグの小文字化 -->

<!--=============================================================================
編集者用「共通スタイルシート」
大相撲・郷土力士取組　　　ＤＴＤ：KdXBSContentv1.0.dtd
 1.0版　2007.10.10 編集者用「共通スタイルシート」として新規作成
 1.1版　2007.12.10 「一覧表ページ」にて全角スペース（0x3000）を（0xEAF0）に置換していた部分を
　　　　　　　　　 置換せずにそのまま全角スペースで表示するように修正
 1.2版　2008.05.30 HTML変換した際に共通ヘッダ部の挿入位置の不具合を解消
 1.3版　2008.12.19 <head>部に記述されていたスタイル定義を<pre>付きで<body>部に移動
 1.4版  2009.02.20 スタイル宣言を記述した<pre>内で不要な改行を削除
================================================================================-->

	<!-- 内容情報部表示シートをインポートする。-->
	<xsl:import href="../Stylesheets/commonheader.xsl" />
	<xsl:import href="../Stylesheets/numconverttbl.xsl" />
	<xsl:import href="OS_CommonEdit.xsl" />

	<xsl:output method="html" indent="no" encoding="UTF-16" />

	<!--「確認用ページ出力」のみ出力は　　　SHORI_Fを「１」にする-->
	<!--「確認用」＋「一覧表」ページ出力は　SHORI_Fを「２」にする-->
	<!--「一覧表ページ」のみ出力は　　　　　SHORI_Fを「３」にする-->
	<xsl:variable name="SHORI_F">
		<!--ここを変更する（半角）-->
		<xsl:value-of select="1" />
	</xsl:variable>

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
	<!--ルートタグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="/">

		<xsl:choose>
			<!--フルタグ書式内容部　ルートタグを判定する。-->
			<xsl:when test="//SportsData">
				<xsl:choose>
					<!--SHORI_Fの値によって処理を分岐する-->
					<xsl:when test="$SHORI_F=1">
						<!--処理１の場合-->
						<!--確認用ページを表示-->
						<xsl:apply-templates select="//SportsData" mode="KAKUNIN">
							<xsl:with-param name="PF" select="1" />
						</xsl:apply-templates>
					</xsl:when>
					<xsl:when test="$SHORI_F=2">
						<!--処理２の場合-->
						<!--確認用ページを表示-->
						<xsl:apply-templates select="//SportsData" mode="KAKUNIN">
							<xsl:with-param name="PF" select="1" />
						</xsl:apply-templates>
						<!--改ページ-->
						<p class="pb" />
						<!--一覧ページを表示-->
						<xsl:text>【一覧表】</xsl:text>
						<xsl:apply-templates select="//SportsData" mode="ICHIRAN">
							<xsl:with-param name="PF" select="2" />
						</xsl:apply-templates>
					</xsl:when>
					<xsl:when test="$SHORI_F=3">
						<!--処理３の場合-->
						<!--一覧ページを表示-->
						<xsl:apply-templates select="//SportsData" mode="ICHIRAN">
							<xsl:with-param name="PF" select="2" />
						</xsl:apply-templates>
					</xsl:when>
				</xsl:choose>
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

	<!--#######################################################################################################-->
	<!--確認-->
	<!--#######################################################################################################-->
	<!--=======================================================================================================-->
	<!--【確認】スポーツデータタグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="SportsData" mode="KAKUNIN">
		<html>
				<body style="font-family:'U-PRESS'">
					<pre><style type="text/css">
							p.pb{page-break-before:always;} 
							.font_size_KAKUNIN{font-size:12pt;}
						</style></pre>
					<div class="font_size_KAKUNIN">
					<!--処理フラグが「１」か「２」の場合のみ内容情報部を表記-->
					<xsl:if test="$SHORI_F=1 or $SHORI_F=2">
						<!--内容情報部を表記するスタイルシートのimport記述をした場合は、下記の１行は必須-->
						<xsl:call-template name="InContent_InMetadata" />
					</xsl:if>

					<!--郷土力士取組編集-->
					<xsl:call-template name="kyodorikisitorikumi_KAKUNIN" />
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
				</body>
		</html>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--郷土力士取組テンプレート-->
	<!--=======================================================================================================-->
	<xsl:template name="kyodorikisitorikumi_KAKUNIN">
		<!--Bodyタグを編集-->
		<xsl:for-each select="Body">
			<!--Title-->
			<table xsl:use-attribute-sets="table_attribute_set">
				<tr>
					<td class="font_size_KAKUNIN">
						<xsl:for-each select="Meta/Title">
							<xsl:value-of select="." />
							<br/>
						</xsl:for-each>
					</td>
				</tr>
			</table>

			<!--Article-->
			<table xsl:use-attribute-sets="table_attribute_set">
				<xsl:if test="Article/Paragraph">
					<tr>
						<td class="font_size_KAKUNIN">
							<xsl:text>　</xsl:text>
							<xsl:value-of select="Article/Paragraph" />
						</td>
					</tr>
				</xsl:if>
			</table>

			<!--Match-->
			<table xsl:use-attribute-sets="table_attribute_set">
				<xsl:for-each select="Match">
					<tr>
						<xsl:apply-templates select="Player" mode="kyodorikisitorikumi_KAKUNIN" />
					</tr>
				</xsl:for-each>
			</table>
		</xsl:for-each>

	</xsl:template>

	<!--=======================================================================================================-->
	<!--郷土力士取組選手タグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="Player" mode="kyodorikisitorikumi_KAKUNIN">
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

	<!--#######################################################################################################-->
	<!--一覧-->
	<!--#######################################################################################################-->
	<!--=======================================================================================================-->
	<!--【一覧】スポーツデータタグテンプレート-->
	<!--=======================================================================================================-->
	<xsl:template match="SportsData" mode="ICHIRAN">
		<xsl:variable name="SportsData" select="." />
		<xsl:apply-templates select="$HtmlFromNewsML/*" mode="ICHIRAN">
			<xsl:with-param name="SportsData" select="$SportsData" />
		</xsl:apply-templates>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--=======================================================================================================-->
	<xsl:template match="*" mode="ICHIRAN">
		<xsl:param name="SportsData" />
		<xsl:param name="datatype" />
		<xsl:choose>
			<xsl:when test="count(*)&gt;0">
				<xsl:copy>
					<xsl:copy-of select="@*" />
					<xsl:apply-templates select="text()|*" mode="ICHIRAN">
						<xsl:with-param name="SportsData" select="$SportsData" />
						<xsl:with-param name="datatype" select="$datatype" />
					</xsl:apply-templates>
				</xsl:copy>
			</xsl:when>
			<xsl:otherwise>
				<xsl:copy-of select="." />
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--=======================================================================================================-->
	<xsl:template match="div[@class='Head']" mode="ICHIRAN">
		<xsl:param name="SportsData" />
		<xsl:param name="datatype" />
		<xsl:copy>
			<xsl:copy-of select="@*" />
			<xsl:apply-templates select="$SportsData/ancestor::InContent/InMetadata" mode="ICHIRAN" />
			<xsl:apply-templates select="text()|*" mode="ICHIRAN">
				<xsl:with-param name="SportsData" select="$SportsData" />
				<xsl:with-param name="datatype" select="$datatype" />
			</xsl:apply-templates>
		</xsl:copy>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--=======================================================================================================-->
	<xsl:template match="th[@class='HeadTitle']" mode="ICHIRAN">
		<xsl:param name="SportsData" />
		<xsl:copy>
			<xsl:copy-of select="@*" />
			<xsl:value-of select="$SportsData/ancestor::NewsComponent//HeadLine" />
		</xsl:copy>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--=======================================================================================================-->
	<xsl:template match="link[@rel='stylesheet']" mode="ICHIRAN">
		<xsl:copy-of select="document(@href)" />
	</xsl:template>

	<!--=======================================================================================================-->
	<!--=======================================================================================================-->
	<xsl:template name="HeaderSet_ICHIRAN">
		<xsl:param name="node" />
		<xsl:if test="boolean($node)">
			<xsl:variable name="tr" select="." />
			<xsl:for-each select="$node">
				<xsl:variable name="value" select="text()" />
				<xsl:variable name="position" select="position()" />
				<xsl:element name="tr">
					<xsl:copy-of select="$tr/@*" />
					<xsl:for-each select="$tr/th">
						<xsl:choose>
							<xsl:when test="position()=3">
								<xsl:copy>
									<xsl:copy-of select="@*" />
									<xsl:value-of select="$value" />
								</xsl:copy>
							</xsl:when>
							<xsl:when test="position()=1 and $position &gt; 1">
								<xsl:copy>
									<xsl:copy-of select="@*" />
								</xsl:copy>
							</xsl:when>
							<xsl:otherwise>
								<xsl:copy-of select="." />
							</xsl:otherwise>
						</xsl:choose>
					</xsl:for-each>
				</xsl:element>
			</xsl:for-each>
		</xsl:if>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--=======================================================================================================-->
	<xsl:template match="tr[@id='Title'][boolean(parent::tbody[@class='header'])]" mode="ICHIRAN">
		<xsl:param name="SportsData" />
		<xsl:call-template name="HeaderSet_ICHIRAN">
			<xsl:with-param name="node" select="$SportsData/Head/Meta/Title" />
		</xsl:call-template>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--=======================================================================================================-->
	<xsl:template match="tr[@id='Competition'][boolean(parent::tbody[@class='header'])]" mode="ICHIRAN">
		<xsl:param name="SportsData" />
		<xsl:call-template name="HeaderSet_ICHIRAN">
			<xsl:with-param name="node" select="$SportsData/Head/Meta/Competition/Formal" />
		</xsl:call-template>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--=======================================================================================================-->
	<xsl:template match="tr[@id='CompetitionDay'][boolean(parent::tbody[@class='header'])]" mode="ICHIRAN">
		<xsl:param name="SportsData" />
		<xsl:call-template name="HeaderSet_ICHIRAN">
			<xsl:with-param name="node" select="$SportsData/Head/Meta/CompetitionDay" />
		</xsl:call-template>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--=======================================================================================================-->
	<xsl:template match="tr[@id='Discipline'][boolean(parent::tbody[@class='header'])]" mode="ICHIRAN">
		<xsl:param name="SportsData" />
		<xsl:call-template name="HeaderSet_ICHIRAN">
			<xsl:with-param name="node" select="$SportsData/Head/Meta/Discipline/Formal" />
		</xsl:call-template>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--=======================================================================================================-->
	<xsl:template match="tr[@id='Limited'][boolean(parent::tbody[@class='header'])]" mode="ICHIRAN">
		<xsl:param name="SportsData" />
		<xsl:call-template name="HeaderSet_ICHIRAN">
			<xsl:with-param name="node" select="$SportsData/Head/Limited/LocalInfo" />
		</xsl:call-template>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--=======================================================================================================-->
	<xsl:template match="tr[@id='TextNote'][boolean(parent::tbody[@class='header'])]" mode="ICHIRAN">
		<xsl:param name="SportsData" />
		<xsl:call-template name="HeaderSet_ICHIRAN">
			<xsl:with-param name="node" select="$SportsData/TextNote" />
		</xsl:call-template>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--=======================================================================================================-->
	<xsl:template match="div[@class = 'Body']" mode="ICHIRAN">
		<xsl:param name="SportsData" />
		<xsl:copy>
			<xsl:copy-of select="@*" />
			<xsl:variable name="div" select="." />
			<xsl:choose>
				<xsl:when test="boolean(@id)">
					<xsl:variable name="datatype" select="@id" />
					<xsl:for-each select="$SportsData/Body[Meta/DataType = $datatype]">
						<xsl:apply-templates select="$div/*" mode="ICHIRAN">
							<xsl:with-param name="SportsData" select="." />
							<xsl:with-param name="datatype" select="$datatype" />
						</xsl:apply-templates>
						<xsl:call-template name="KdGaiji_ICHIRAN" />
					</xsl:for-each>
				</xsl:when>
				<xsl:otherwise>
					<xsl:for-each select="$SportsData/Body">
						<xsl:apply-templates select="$div/*" mode="ICHIRAN">
							<xsl:with-param name="SportsData" select="." />
						</xsl:apply-templates>
						<xsl:call-template name="KdGaiji_ICHIRAN" />
					</xsl:for-each>
				</xsl:otherwise>
			</xsl:choose>
		</xsl:copy>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--=======================================================================================================-->
	<xsl:template name="BrockSet_ICHIRAN">
		<xsl:param name="node" />
		<xsl:if test="boolean($node)">
			<xsl:choose>
				<xsl:when test="@class='block_title'">
					<xsl:copy-of select="." />
				</xsl:when>
				<xsl:otherwise>
					<xsl:variable name="attribute" select="@*" />
					<xsl:for-each select="$node">
						<xsl:element name="th">
							<xsl:copy-of select="$attribute" />
							<xsl:value-of select="text()" />
						</xsl:element>
					</xsl:for-each>
				</xsl:otherwise>
			</xsl:choose>
		</xsl:if>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--=======================================================================================================-->
	<xsl:template match="th[@id='DataType'][boolean(ancestor::table[@class='block'])]" mode="ICHIRAN">
		<xsl:param name="SportsData" />
		<xsl:call-template name="BrockSet_ICHIRAN">
			<xsl:with-param name="node" select="$SportsData/Meta/DataType" />
		</xsl:call-template>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--=======================================================================================================-->
	<xsl:template match="th[@id='FormatType'][boolean(ancestor::table[@class='block'])]" mode="ICHIRAN">
		<xsl:param name="SportsData" />
		<xsl:call-template name="BrockSet_ICHIRAN">
			<xsl:with-param name="node" select="$SportsData/Meta/FormatType" />
		</xsl:call-template>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--=======================================================================================================-->
	<xsl:template match="th[@id='Class'][boolean(ancestor::table[@class='block'])]" mode="ICHIRAN">
		<xsl:param name="SportsData" />
		<xsl:call-template name="BrockSet_ICHIRAN">
			<xsl:with-param name="node" select="$SportsData/Meta/Class" />
		</xsl:call-template>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--=======================================================================================================-->
	<xsl:template match="th[@id='Scope'][boolean(ancestor::table[@class='block'])]" mode="ICHIRAN">
		<xsl:param name="SportsData" />
		<xsl:call-template name="BrockSet_ICHIRAN">
			<xsl:with-param name="node" select="$SportsData/Meta/Scope" />
		</xsl:call-template>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--=======================================================================================================-->
	<xsl:template match="th[@id='Title'][boolean(ancestor::table[@class='block'])]" mode="ICHIRAN">
		<xsl:param name="SportsData" />
		<xsl:call-template name="BrockSet_ICHIRAN">
			<xsl:with-param name="node" select="$SportsData/Meta/Title" />
		</xsl:call-template>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--=======================================================================================================-->
	<xsl:template match="th[@id='Article'][boolean(ancestor::table[@class='block'])]" mode="ICHIRAN">
		<xsl:param name="SportsData" />
		<xsl:call-template name="BrockSet_ICHIRAN">
			<xsl:with-param name="node" select="$SportsData/Article/Paragraph" />
		</xsl:call-template>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--=======================================================================================================-->
	<xsl:template match="th[@id='TextNote'][boolean(ancestor::table[@class='block'])]" mode="ICHIRAN">
		<xsl:param name="SportsData" />
		<xsl:call-template name="BrockSet_ICHIRAN">
			<xsl:with-param name="node" select="$SportsData/TextNote" />
		</xsl:call-template>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--=======================================================================================================-->
	<xsl:template name="KdGaiji_ICHIRAN">
		<xsl:param name="node" select="." />
		<xsl:if test="boolean($node//KdGaiji)">
			<table style="page-break-before:always;">
				<thead>
					<tr class="head_sub">
						<th class="single">№</th>
						<th class="single">字解を含む文字</th>
						<th class="single">字解</th>
					</tr>
				</thead>
				<tbody>
					<xsl:for-each select="$node//KdGaiji">
						<tr>
							<xsl:choose>
								<xsl:when test="(position() mod 2)">
									<xsl:attribute name="class">odd</xsl:attribute>
								</xsl:when>
								<xsl:otherwise>
									<xsl:attribute name="class">even</xsl:attribute>
								</xsl:otherwise>
							</xsl:choose>
							<td class="single" align="center">
								<xsl:value-of select="position()" />
							</td>
							<td class="single" align="center">
								<xsl:value-of select="translate(parent::*,'　','　')" />
							</td>
							<td class="single" align="center">
								<xsl:value-of select="@KdJikai" />
							</td>
						</tr>
					</xsl:for-each>
				</tbody>
			</table>
			<br />
		</xsl:if>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--=======================================================================================================-->
	<xsl:template match="table[@class='data']" mode="ICHIRAN">
		<xsl:param name="SportsData" />
		<xsl:param name="datatype" />
		<xsl:variable name="nodes" select="$SportsData/Standing/Player|$SportsData/Match" />
		<xsl:variable name="omit">
			<xsl:call-template name="LineOmitCheck_ICHIRAN">
				<xsl:with-param name="SportsData" select="$SportsData" />
				<xsl:with-param name="datatype" select="$datatype" />
			</xsl:call-template>
		</xsl:variable>
		<xsl:variable name="page">
			<xsl:choose>
				<xsl:when test="boolean(string($omit))">
					<xsl:value-of select="@page * 2" />
				</xsl:when>
				<xsl:otherwise>
					<xsl:value-of select="@page" />
				</xsl:otherwise>
			</xsl:choose>
		</xsl:variable>
		<xsl:if test="boolean($nodes)">
			<xsl:copy>
				<xsl:copy-of select="@*" />
				<xsl:element name="thead">
					<xsl:copy-of select="thead/@*" />
					<xsl:apply-templates select="thead/tr[not(boolean(@id)) or not(contains($omit,@id))]" mode="ICHIRAN">
						<xsl:with-param name="SportsData" select="$SportsData" />
					</xsl:apply-templates>
				</xsl:element>
				<xsl:variable name="thead" select="thead" />
				<xsl:variable name="tbody" select="tbody" />
				<xsl:element name="tbody">
					<xsl:copy-of select="$tbody/@*" />
					<xsl:for-each select="$nodes">
						<xsl:variable name="node" select="." />
						<xsl:variable name="dposition" select="position()" />
						<xsl:variable name="pposition">
							<xsl:choose>
								<xsl:when test="(position()=1)or($page &gt; 4)">
									<xsl:value-of select="$dposition + 1" />
								</xsl:when>
								<xsl:otherwise>
									<xsl:value-of select="$dposition" />
								</xsl:otherwise>
							</xsl:choose>
						</xsl:variable>
						<xsl:if test="(($pposition mod $page) = 1) ">
							<xsl:for-each select="$thead/tr[not(boolean(@id)) or not(contains($omit,@id))]">
								<xsl:copy>
									<xsl:copy-of select="@*" />
									<xsl:if test="position()=1">
										<xsl:attribute name="style">page-break-before:always;</xsl:attribute>
									</xsl:if>
									<xsl:apply-templates select="*" mode="ICHIRAN">
										<xsl:with-param name="SportsData" select="$SportsData" />
										<xsl:with-param name="datatype" select="$datatype" />
									</xsl:apply-templates>
								</xsl:copy>
							</xsl:for-each>
						</xsl:if>
						<xsl:for-each select="$tbody/tr[@class='odd'][not(boolean(@id)) or not(contains($omit,@id))]">
							<xsl:copy>
								<xsl:copy-of select="@*" />
								<xsl:choose>
									<xsl:when test="($dposition mod 2)">
										<xsl:attribute name="class">odd</xsl:attribute>
									</xsl:when>
									<xsl:otherwise>
										<xsl:attribute name="class">even</xsl:attribute>
									</xsl:otherwise>
								</xsl:choose>
								<xsl:apply-templates select="*" mode="ICHIRAN">
									<xsl:with-param name="SportsData" select="$node" />
									<xsl:with-param name="datatype" select="$datatype" />
								</xsl:apply-templates>
							</xsl:copy>
						</xsl:for-each>
					</xsl:for-each>
				</xsl:element>
			</xsl:copy>
		</xsl:if>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--=======================================================================================================-->
	<xsl:template match="th[@class='direction']" mode="ICHIRAN">
		<xsl:param name="SportsData" />
		<xsl:variable name="position" select="count(preceding-sibling::th[@class='direction']) + 1" />
		<xsl:copy>
			<xsl:copy-of select="@*" />
			<xsl:value-of select="$SportsData//Match[1]/Player[$position]//Direction" />
		</xsl:copy>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--=======================================================================================================-->
	<xsl:template match="td[boolean(parent::tr[@class='odd'])]" mode="ICHIRAN">
		<xsl:param name="SportsData" />
		<xsl:param name="datatype" />
		<xsl:variable name="position">
			<xsl:number level="single" count="tr[@class='odd']" format="1" />
		</xsl:variable>
		<xsl:copy>
			<xsl:copy-of select="@*" />
			<xsl:variable name="position_col" select="position()" />
			<xsl:variable name="value">
				<xsl:call-template name="ContentDataSet_ICHIRAN">
					<xsl:with-param name="row" select="$position" />
					<xsl:with-param name="col" select="position()" />
					<xsl:with-param name="node" select="$SportsData" />
					<xsl:with-param name="datatype" select="$datatype" />
				</xsl:call-template>
			</xsl:variable>
			<xsl:choose>
				<xsl:when test="boolean(string($value))">
					<xsl:value-of select="translate($value,'　','　')" />
				</xsl:when>
				<xsl:when test="boolean(br)">
					<xsl:copy-of select="br" />
				</xsl:when>
				<xsl:otherwise>
					<xsl:element name="br" />
				</xsl:otherwise>
			</xsl:choose>
		</xsl:copy>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--=======================================================================================================-->
	<xsl:template match="th[@class='match'][text()='年']" mode="ICHIRAN">
		<xsl:param name="SportsData" />
		<xsl:variable name="position" select="count(preceding-sibling::th[@class='match'][text()='年'])" />
		<xsl:copy>
			<xsl:copy-of select="@*" />
			<xsl:variable name="Results"
				select="$SportsData//Match/Player[1]/Result[boolean(Result[boolean(Outcome)])][1]/Result[boolean(Outcome)]" />
			<xsl:choose>
				<xsl:when
					test="substring($Results[$position]/@Period,1,2) = substring($Results[$position + 1]/@Period,1,2)">
					<xsl:text>＝＝</xsl:text>
				</xsl:when>
				<xsl:otherwise>
					<xsl:value-of select="substring($Results[$position + 1]/@Period,1,2)" />
				</xsl:otherwise>
			</xsl:choose>
		</xsl:copy>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--=======================================================================================================-->
	<xsl:template match="th[@class='match'][text()='場所']" mode="ICHIRAN">
		<xsl:param name="SportsData" />
		<xsl:variable name="position" select="count(preceding-sibling::th[@class='match'][text()='場所'])" />
		<xsl:copy>
			<xsl:copy-of select="@*" />
			<xsl:variable name="Results"
				select="$SportsData//Match/Player[1]/Result[boolean(Result[boolean(Outcome)])][1]/Result[boolean(Outcome)]" />
			<xsl:value-of select="substring($Results[$position + 1]/@Period,3)" />
		</xsl:copy>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--=======================================================================================================-->
	<xsl:template name="LineOmitCheck_ICHIRAN" />

	<!--=======================================================================================================-->
	<!--=======================================================================================================-->
	<xsl:template match="InMetadata" mode="ICHIRAN" />

	<!--=======================================================================================================-->
	<!--=======================================================================================================-->
	<xsl:template match="ITalk|NewsML" mode="ICHIRAN">
		<xsl:choose>
			<xsl:when test="boolean(//SportsData)">
				<xsl:apply-templates select="//SportsData" mode="ICHIRAN" />
			</xsl:when>
			<xsl:otherwise>
				<html>
					<body>
						<xsl:text>ＤＴＤ実行エラーまたは、タグに誤りがあります。</xsl:text>
						<xsl:copy-of select="." />
					</body>
				</html>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>

	<!--=======================================================================================================-->
	<!--=======================================================================================================-->
	<xsl:param name="HtmlFileXml">
		<html>
			<head>
				<title>6.郷土力士取組</title>
			</head>
			<body style="font-family:'U-PRESS';">
				<pre>
					<style type="text/css">
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
					</style>
				</pre>
				<div class="Head">
					<table border="0">
						<thead align="left">
							<tr>
								<th colspan="3" class="HeadTitle">郷土力士取組</th>
							</tr>
						</thead>
						<tbody align="left" class="header">
							<tr id="Competition">
								<th>■場所</th>
								<th>：</th>
								<th>春場所</th>
							</tr>
							<tr id="CompetitionDay">
								<th>■日目</th>
								<th>：</th>
								<th>場所前</th>
							</tr>
							<tr id="Discipline">
								<th>■種別</th>
								<th>：</th>
								<th>相撲</th>
							</tr>
							<tr id="Limited">
								<th>■地域</th>
								<th>：</th>
								<th>福岡</th>
							</tr>
						</tbody>
					</table>
				</div>
				<div class="Body">
					<br />
					<table class="block">
						<tbody>
							<tr>
								<th class="block_title" id="FormatType">フォーマット</th>
								<th class="block_data" id="FormatType">Ｍ－Ｐ</th>
								<th class="block_title" id="DataType">データ</th>
								<th class="block_data" id="DataType">新番付</th>
								<th class="block_title" id="Title">見出し</th>
								<th class="block_data" id="Title">【序ノ口】</th>
								<th class="block_title" id="Class">階級</th>
								<th class="block_data" id="Class">序ノ口</th>
								<th class="block_title" id="Article">補足情報</th>
								<th class="block_data" id="Article">関係地向け取組なし</th>
							</tr>
						</tbody>
					</table>
					<br />
					<table class="data" width="100%" page="11">
						<thead>
							<tr class="head_main">
								<th colspan="2" class="single">力士名</th>
								<th class="single">ID</th>
								<th class="single">地位</th>
								<th class="single">出身地</th>
								<th colspan="2" class="single">出身市町村</th>
								<th class="match">対戦</th>
								<th colspan="2" class="single">力士名</th>
								<th class="single">ID</th>
								<th class="single">地位</th>
								<th class="single">出身地</th>
								<th colspan="2" class="single">出身市町村</th>
							</tr>
							<tr class="head_sub">
								<th class="top">表記</th>
								<th class="top">３字</th>
								<th rowspan="3" class="single">ID</th>
								<th class="top">正式名</th>
								<th class="top">正式名</th>
								<th class="top">表記</th>
								<th class="top">２字</th>
								<th rowspan="3" class="match">ID</th>
								<th class="top">表記</th>
								<th class="top">３字</th>
								<th rowspan="3" class="single">ID</th>
								<th class="top">正式名</th>
								<th class="top">正式名</th>
								<th class="top">表記</th>
								<th class="top">２字</th>
							</tr>
							<tr class="head_sub">
								<th class="middle">正式名</th>
								<th class="middle">４字</th>
								<th class="middle">
									<br />
								</th>
								<th class="middle">２字</th>
								<th class="middle">正式名</th>
								<th class="middle">３字</th>
								<th class="middle">正式名</th>
								<th class="middle">４字</th>
								<th class="middle">表記</th>
								<th class="middle">２字</th>
								<th class="middle">正式名</th>
								<th class="middle">３字</th>
							</tr>
							<tr class="head_sub">
								<th colspan="2" class="bottom">よみがな</th>
								<th class="bottom">
									<br />
								</th>
								<th class="bottom">
									<br />
								</th>
								<th colspan="2" class="bottom">市町村付</th>
								<th colspan="2" class="bottom">よみがな</th>
								<th class="bottom">
									<br />
								</th>
								<th class="bottom">表記</th>
								<th colspan="2" class="bottom">市町村付</th>
							</tr>
						</thead>
						<tbody>
							<tr class="odd">
								<td class="top" align="center">北勝洋　</td>
								<td class="top" align="center">北勝洋</td>
								<td rowspan="3" class="single" align="center">005250</td>
								<td class="top" align="center">三段目</td>
								<td class="top" align="center">北海道</td>
								<td class="top" align="center">札　幌</td>
								<td class="top" align="center">札幌</td>
								<td rowspan="3" class="match" align="center">M005</td>
								<td class="top" align="center">魁千龍</td>
								<td class="top" align="center">魁千龍</td>
								<td rowspan="3" class="single" align="center">003300</td>
								<td class="top" align="center">三段目</td>
								<td class="top" align="center">千葉</td>
								<td class="top" align="center">旭　川</td>
								<td class="top" align="center">旭川</td>
							</tr>
							<tr class="odd">
								<td class="middle" align="center">北勝洋</td>
								<td class="middle" align="center">北勝洋　</td>
								<td class="middle" align="center">
									<br />
								</td>
								<td class="middle" align="center">北海</td>
								<td class="middle" align="center">札幌</td>
								<td class="middle" align="center">札　幌</td>
								<td class="middle" align="center">魁千龍</td>
								<td class="middle" align="center">魁千龍　</td>
								<td class="middle" align="center">表記</td>
								<td class="middle" align="center">千葉</td>
								<td class="middle" align="center">旭川</td>
								<td class="middle" align="center">旭　川</td>
							</tr>
							<tr class="odd">
								<td colspan="2" class="bottom" align="center">ほくとなだ</td>
								<td class="bottom" align="center">
									<br />
								</td>
								<td class="bottom" align="center">
									<br />
								</td>
								<td colspan="2" class="bottom" align="center">札幌市</td>
								<td colspan="2" class="bottom" align="center">かいせんりゅう</td>
								<td class="bottom">
									<br />
								</td>
								<td class="bottom" align="center">千葉</td>
								<td colspan="2" class="bottom" align="center">旭川市</td>
							</tr>
						</tbody>
					</table>
					<br />
				</div>
			</body>
		</html>
	</xsl:param>

	<!--=======================================================================================================-->
	<!--=======================================================================================================-->
	<xsl:param name="HtmlFromNewsML" select="document('')/xsl:stylesheet/xsl:param[@name='HtmlFileXml']" />

	<!--=======================================================================================================-->
	<!--=======================================================================================================-->
	<xsl:template name="ContentDataSet_ICHIRAN">
		<xsl:param name="row" />
		<xsl:param name="col" />
		<xsl:param name="node" />
		<xsl:choose>
			<xsl:when test="$row=1">
				<xsl:choose>
					<xsl:when test="$col=1">
						<xsl:value-of select="$node/Player[1]/PlayerName/Writing" />
					</xsl:when>
					<xsl:when test="$col=2">
						<xsl:value-of select="$node/Player[1]/PlayerName/Formal[@Display='3字']" />
					</xsl:when>
					<xsl:when test="$col=3">
						<xsl:value-of select="$node/Player[1]/@PlayerId" />
					</xsl:when>
					<xsl:when test="$col=4">
						<xsl:value-of select="$node/Player[1]/PlayerForSumo/SumoGrade/SumoRank" />
					</xsl:when>
					<xsl:when test="$col=5">
						<xsl:value-of select="$node/Player[1]/PlayerForSumo/NativeArea/Formal[not(boolean(@Display))]" />
					</xsl:when>
					<xsl:when test="$col=6">
						<xsl:value-of select="$node/Player[1]/PlayerForSumo/NativeCity/Writing" />
					</xsl:when>
					<xsl:when test="$col=7">
						<xsl:value-of select="$node/Player[1]/PlayerForSumo/NativeCity/Formal[@Display='2字']" />
					</xsl:when>
					<xsl:when test="$col=8">
						<xsl:value-of select="$node/@BlockId" />
					</xsl:when>
					<xsl:when test="$col=9">
						<xsl:value-of select="$node/Player[2]/PlayerName/Writing" />
					</xsl:when>
					<xsl:when test="$col=10">
						<xsl:value-of select="$node/Player[2]/PlayerName/Formal[@Display='3字']" />
					</xsl:when>
					<xsl:when test="$col=11">
						<xsl:value-of select="$node/Player[2]/@PlayerId" />
					</xsl:when>
					<xsl:when test="$col=12">
						<xsl:value-of select="$node/Player[2]/PlayerForSumo/SumoGrade/SumoRank" />
					</xsl:when>
					<xsl:when test="$col=13">
						<xsl:value-of
							select="concat($node/Player[2]/PlayerForSumo/NativeCountry/Formal[not(boolean(@Display))],$node/Player[2]/PlayerForSumo/NativeArea/Formal[not(boolean(@Display))])" />
					</xsl:when>
					<xsl:when test="$col=14">
						<xsl:value-of select="$node/Player[2]/PlayerForSumo/NativeCity/Writing" />
					</xsl:when>
					<xsl:when test="$col=15">
						<xsl:value-of select="$node/Player[2]/PlayerForSumo/NativeCity/Formal[@Display='2字']" />
					</xsl:when>
				</xsl:choose>
			</xsl:when>
			<xsl:when test="$row=2">
				<xsl:choose>
					<xsl:when test="$col=1">
						<xsl:value-of select="$node/Player[1]/PlayerName/Formal[not(boolean(@Display))]" />
					</xsl:when>
					<xsl:when test="$col=2">
						<xsl:value-of select="$node/Player[1]/PlayerName/Formal[@Display='4字']" />
					</xsl:when>
					<xsl:when test="$col=4">
						<xsl:value-of select="$node/Player[1]/PlayerForSumo/NativeArea/Formal[@Display='2字']" />
					</xsl:when>
					<xsl:when test="$col=5">
						<xsl:value-of select="$node/Player[1]/PlayerForSumo/NativeCity/Formal[not(boolean(@Display))]" />
					</xsl:when>
					<xsl:when test="$col=6">
						<xsl:value-of select="$node/Player[1]/PlayerForSumo/NativeCity/Formal[@Display='3字']" />
					</xsl:when>
					<xsl:when test="$col=7">
						<xsl:value-of select="$node/Player[2]/PlayerName/Formal[not(boolean(@Display))]" />
					</xsl:when>
					<xsl:when test="$col=8">
						<xsl:value-of select="$node/Player[2]/PlayerName/Formal[@Display='4字']" />
					</xsl:when>
					<xsl:when test="$col=9">
						<xsl:value-of select="$node/Player[2]/PlayerForSumo/SumoGrade/Writing" />
					</xsl:when>
					<xsl:when test="$col=10">
						<xsl:value-of
							select="concat($node/Player[2]/PlayerForSumo/NativeCountry/Formal[@Display='2字'],$node/Player[2]/PlayerForSumo/NativeArea/Formal[@Display='2字'])" />
					</xsl:when>
					<xsl:when test="$col=11">
						<xsl:value-of select="$node/Player[2]/PlayerForSumo/NativeCity/Formal[not(boolean(@Display))]" />
					</xsl:when>
					<xsl:when test="$col=12">
						<xsl:value-of select="$node/Player[2]/PlayerForSumo/NativeCity/Formal[@Display='3字']" />
					</xsl:when>
				</xsl:choose>
			</xsl:when>
			<xsl:when test="$row=3">
				<xsl:choose>
					<xsl:when test="$col=1">
						<xsl:value-of select="$node/Player[1]/PlayerName/Formal[@Display='よみがな']" />
					</xsl:when>
					<xsl:when test="$col=4">
						<xsl:value-of select="$node/Player[1]/PlayerForSumo/NativeCity/Formal[@Display='市町村付']" />
					</xsl:when>
					<xsl:when test="$col=5">
						<xsl:value-of select="$node/Player[2]/PlayerName/Formal[@Display='よみがな']" />
					</xsl:when>
					<xsl:when test="$col=7">
						<xsl:value-of
							select="concat($node/Player[2]/PlayerForSumo/NativeCountry/Writing,$node/Player[2]/PlayerForSumo/NativeArea/Writing)" />
					</xsl:when>
					<xsl:when test="$col=8">
						<xsl:value-of select="$node/Player[2]/PlayerForSumo/NativeCity/Formal[@Display='市町村付']" />
					</xsl:when>
				</xsl:choose>
			</xsl:when>
		</xsl:choose>
	</xsl:template>
</xsl:stylesheet>
