<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">
  <!-- ================================================================================= -->
  <!--　編集者用「共通スタイルシート」大相撲・勝負 -->
  <!--  4.0版 2015.06.30 プレーンテキスト化に伴い、一覧表示用のファイルを分離　-->
  <!-- ================================================================================= -->
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
    <div class="Head">
      <table border="0">
        <thead align="left">
          <tr>
            <th colspan="3" class="HeadTitle">勝負</th>
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
        </tbody>
      </table>
    </div>
    <div class="Body">
      <br />
      <table class="block">
        <tbody>
          <tr>
            <th class="block_title" id="FormatType">フォーマット</th>
            <th class="block_data" id="FormatType">Ｍ－Ｐ－Ｒ－Ｄ</th>
            <th class="block_title" id="DataType">データ</th>
            <th class="block_data" id="DataType">勝負</th>
            <th class="block_title" id="Title">見出し</th>
            <th class="block_data" id="Title">＝中入り後＝</th>
          </tr>
        </tbody>
      </table>
      <br />
      <table class="data" width="100%" page="7">
        <thead>
          <tr class="head_sub">
            <th colspan="6" class="top" style="font-size:12pt;">勝ち</th>
            <th colspan="3" class="match" style="font-size:12pt;">対戦</th>
            <th colspan="6" class="top" style="font-size:12pt;">負け</th>
          </tr>
          <tr class="head_main">
            <th class="single">勝敗</th>
            <th class="single">力士名</th>
            <th class="single">ID</th>
            <th colspan="2" class="single">今場所成績</th>
            <th class="single">地位</th>
            <th class="match">ID</th>
            <th class="match">決まり手</th>
            <th class="match">勝負時間</th>
            <th class="single">力士名</th>
            <th class="single">ID</th>
            <th colspan="2" class="single">今場所成績</th>
            <th class="single">地位</th>
            <th class="single">勝敗</th>
          </tr>
          <tr class="head_sub">
            <th rowspan="4" class="single">勝敗</th>
            <th class="top">表記</th>
            <th rowspan="4" class="single">ID</th>
            <th rowspan="4" class="single">表記</th>
            <th class="top">勝ち</th>
            <th rowspan="4" class="single">正式名</th>
            <th rowspan="4" class="match">ID</th>
            <th class="match">表記</th>
            <th class="match">表記</th>
            <th class="top">表記</th>
            <th rowspan="4" class="single">ID</th>
            <th rowspan="4" class="single">表記</th>
            <th class="top">勝ち</th>
            <th rowspan="4" class="single">正式名</th>
            <th rowspan="4" class="single">勝敗</th>
          </tr>
          <tr class="head_sub">
            <th class="middle">正式名</th>
            <th class="middle">負け</th>
            <th class="match">正式名</th>
            <th class="match">分</th>
            <th class="middle">正式名</th>
            <th class="middle">負け</th>
          </tr>
          <tr class="head_sub">
            <th class="middle">３字</th>
            <th class="middle">分け</th>
            <th class="match">７字</th>
            <th class="match">秒</th>
            <th class="middle">３字</th>
            <th class="middle">分け</th>
          </tr>
          <tr class="head_sub">
            <th class="bottom">よみがな</th>
            <th class="bottom">休み</th>
            <th class="match">
              <br />
            </th>
            <th class="match">以下</th>
            <th class="bottom">よみがな</th>
            <th class="bottom">休み</th>
          </tr>
        </thead>
        <tbody>
          <tr class="odd">
            <td rowspan="4" class="single" align="center">勝敗</td>
            <td class="top" align="center">表記</td>
            <td rowspan="4" class="single" align="center">ID</td>
            <td rowspan="4" class="single" align="center">表記</td>
            <td class="top" align="center">勝ち</td>
            <td rowspan="4" class="single" align="center">正式名</td>
            <td rowspan="4" class="match" align="center">ID</td>
            <td class="match" align="center">表記</td>
            <td class="match" align="center">表記</td>
            <td class="top" align="center">表記</td>
            <td rowspan="4" class="single" align="center">ID</td>
            <td rowspan="4" class="single" align="center">表記</td>
            <td class="top" align="center">勝ち</td>
            <td rowspan="4" class="single" align="center">正式名</td>
            <td rowspan="4" class="single" align="center">勝敗</td>
          </tr>
          <tr class="odd">
            <td class="middle" align="center">正式名</td>
            <td class="middle" align="center">負け</td>
            <td class="match" align="center">正式名</td>
            <td class="match" align="center">分</td>
            <td class="middle" align="center">正式名</td>
            <td class="middle" align="center">負け</td>
          </tr>
          <tr class="odd">
            <td class="middle" align="center">３字</td>
            <td class="middle" align="center">分け</td>
            <td class="match" align="center">７字</td>
            <td class="match" align="center">秒</td>
            <td class="middle" align="center">３字</td>
            <td class="middle" align="center">分け</td>
          </tr>
          <tr class="odd">
            <td class="bottom" align="center">よみがな</td>
            <td class="bottom" align="center">休み</td>
            <td class="match" align="center">
              <br />
            </td>
            <td class="match" align="center">以下</td>
            <td class="bottom" align="center">よみがな</td>
            <td class="bottom" align="center">休み</td>
          </tr>
        </tbody>
      </table>
      <br />
    </div>
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
						<xsl:value-of select="$node/MatchDetail/MatchResult[1]/Outcome/Formal" />
					</xsl:when>
					<xsl:when test="$col=2">
						<xsl:value-of select="$node/Player[1]/PlayerName/Writing" />
					</xsl:when>
					<xsl:when test="$col=3">
						<xsl:value-of select="$node/Player[1]/@PlayerId" />
					</xsl:when>
					<xsl:when test="$col=4">
						<xsl:value-of select="$node/Player[1]/Result/Result/ResultForSumo/SumoOutcomeTotal/Writing" />
					</xsl:when>
					<xsl:when test="$col=5">
						<xsl:value-of select="$node/Player[1]/Result/Result/ResultForSumo/SumoOutcomeTotal/WinCount" />
					</xsl:when>
					<xsl:when test="$col=6">
						<xsl:value-of select="$node/Player[1]/PlayerForSumo/SumoGrade/SumoRank" />
					</xsl:when>
					<xsl:when test="$col=7">
						<xsl:value-of select="$node/@BlockId" />
					</xsl:when>
					<xsl:when test="$col=8">
						<xsl:value-of select="$node/MatchDetail/WinningTrick/Writing" />
					</xsl:when>
					<xsl:when test="$col=9">
						<xsl:value-of select="$node/MatchDetail/ClosingInfo/ClosingTime/Writing" />
					</xsl:when>
					<xsl:when test="$col=10">
						<xsl:value-of select="$node/Player[2]/PlayerName/Writing" />
					</xsl:when>
					<xsl:when test="$col=11">
						<xsl:value-of select="$node/Player[2]/@PlayerId" />
					</xsl:when>
					<xsl:when test="$col=12">
						<xsl:value-of select="$node/Player[2]/Result/Result/ResultForSumo/SumoOutcomeTotal/Writing" />
					</xsl:when>
					<xsl:when test="$col=13">
						<xsl:value-of select="$node/Player[2]/Result/Result/ResultForSumo/SumoOutcomeTotal/WinCount" />
					</xsl:when>
					<xsl:when test="$col=14">
						<xsl:value-of select="$node/Player[2]/PlayerForSumo/SumoGrade/SumoRank" />
					</xsl:when>
					<xsl:when test="$col=15">
						<xsl:value-of select="$node/MatchDetail/MatchResult[2]/Outcome/Formal" />
					</xsl:when>
				</xsl:choose>
			</xsl:when>
			<xsl:when test="$row=2">
				<xsl:choose>
					<xsl:when test="$col=1">
						<xsl:value-of select="$node/Player[1]/PlayerName/Formal[not(boolean(@Display))]" />
					</xsl:when>
					<xsl:when test="$col=2">
						<xsl:value-of select="$node/Player[1]/Result/Result/ResultForSumo/SumoOutcomeTotal/LossCount" />
					</xsl:when>
					<xsl:when test="$col=3">
						<xsl:value-of select="$node/MatchDetail/WinningTrick/Formal[not(boolean(@Display))]" />
					</xsl:when>
					<xsl:when test="$col=4">
						<xsl:value-of select="$node/MatchDetail/ClosingInfo/ClosingTime/Minute" />
					</xsl:when>
					<xsl:when test="$col=5">
						<xsl:value-of select="$node/Player[2]/PlayerName/Formal[not(boolean(@Display))]" />
					</xsl:when>
					<xsl:when test="$col=6">
						<xsl:value-of select="$node/Player[2]/Result/Result/ResultForSumo/SumoOutcomeTotal/LossCount" />
					</xsl:when>
				</xsl:choose>
			</xsl:when>
			<xsl:when test="$row=3">
				<xsl:choose>
					<xsl:when test="$col=1">
						<xsl:value-of select="$node/Player[1]/PlayerName/Formal[@Display='3字']" />
					</xsl:when>
					<xsl:when test="$col=2">
						<xsl:value-of select="$node/Player[1]/Result/Result/ResultForSumo/SumoOutcomeTotal/DrawCount" />
					</xsl:when>
					<xsl:when test="$col=3">
						<xsl:value-of select="$node/MatchDetail/WinningTrick/Formal[@Display='7字']" />
					</xsl:when>
					<xsl:when test="$col=4">
						<xsl:value-of select="$node/MatchDetail/ClosingInfo/ClosingTime/Second" />
					</xsl:when>
					<xsl:when test="$col=5">
						<xsl:value-of select="$node/Player[2]/PlayerName/Formal[@Display='3字']" />
					</xsl:when>
					<xsl:when test="$col=6">
						<xsl:value-of select="$node/Player[2]/Result/Result/ResultForSumo/SumoOutcomeTotal/DrawCount" />
					</xsl:when>
				</xsl:choose>
			</xsl:when>
			<xsl:when test="$row=4">
				<xsl:choose>
					<xsl:when test="$col=1">
						<xsl:value-of select="$node/Player[1]/PlayerName/Formal[@Display='よみがな']" />
					</xsl:when>
					<xsl:when test="$col=2">
						<xsl:value-of
							select="$node/Player[1]/Result/Result/ResultForSumo/SumoOutcomeTotal/AbsenceCount" />
					</xsl:when>
					<xsl:when test="$col=4">
						<xsl:value-of select="$node/MatchDetail/ClosingInfo/ClosingTime/Fraction" />
					</xsl:when>
					<xsl:when test="$col=5">
						<xsl:value-of select="$node/Player[2]/PlayerName/Formal[@Display='よみがな']" />
					</xsl:when>
					<xsl:when test="$col=6">
						<xsl:value-of
							select="$node/Player[2]/Result/Result/ResultForSumo/SumoOutcomeTotal/AbsenceCount" />
					</xsl:when>
				</xsl:choose>
			</xsl:when>
		</xsl:choose>
	</xsl:template>
</xsl:stylesheet>
