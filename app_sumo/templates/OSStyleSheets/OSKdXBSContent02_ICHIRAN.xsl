<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="ja" version="1.0">
  <!-- ================================================================================= -->
  <!--　編集者用「共通スタイルシート」大相撲・新番付資料（補正） -->
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
							<td class="single">
								<xsl:value-of select="position()" />
							</td>
							<td class="single">
								<xsl:value-of select="translate(parent::*,'　','　')" />
							</td>
							<td class="single">
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
					<xsl:apply-templates select="thead/tr[not(boolean(@id)) or not(contains($omit,@id))]"
						mode="ICHIRAN">
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
            <th colspan="3" class="HeadTitle">新番付資料（補正）</th>
          </tr>
        </thead>
        <tbody align="left" class="header">
          <tr id="Title">
            <th>■横見出し</th>
            <th>：</th>
            <th>年大相撲春場所新番付資料（２月日現在）</th>
          </tr>
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
            <th class="block_data" id="FormatType">Ｓ－Ｐ－Ｒ</th>
            <th class="block_title" id="DataType">データ</th>
            <th class="block_data" id="DataType">新番付資料（補正）</th>
            <th class="block_title" id="Title">見出し</th>
            <th class="block_data" id="Title">東</th>
          </tr>
        </tbody>
      </table>
      <br />
      <table class="data" width="100%" page="8">
        <thead>
          <tr class="head_main">
            <th class="single">新地位</th>
            <th colspan="2" class="single">力士名</th>
            <th class="single">ID</th>
            <th class="single">年齢</th>
            <th class="single">部屋</th>
            <th class="single">出身地</th>
            <th class="single">最高位</th>
            <th colspan="2" class="single">成績</th>
            <th class="single">優勝三賞</th>
            <th class="single">与奪金星</th>
            <th class="single">体格</th>
            <th class="single">旧名</th>
          </tr>
          <tr class="head_sub">
            <th class="top">東西区分</th>
            <th class="top">表記</th>
            <th class="top">３字</th>
            <th rowspan="4" class="single">ID</th>
            <th rowspan="4" class="single">年齢</th>
            <th class="top">表記</th>
            <th class="top">表記</th>
            <th class="top">表記</th>
            <th rowspan="2" class="single">場所数</th>
            <th class="top">勝ち</th>
            <th class="top">優勝</th>
            <th class="top">与金星</th>
            <th class="top">身長(cm)</th>
            <th class="top">正式名</th>
          </tr>
          <tr class="head_sub">
            <th class="middle">表記</th>
            <th class="middle">正式名</th>
            <th class="middle">２字</th>
            <th class="middle">正式名</th>
            <th class="middle">正式名</th>
            <th class="middle">正式名</th>
            <th class="middle">負け</th>
            <th class="middle">殊勲賞</th>
            <th class="middle">表記</th>
            <th class="middle">体重(kg)</th>
            <th class="middle">３字</th>
          </tr>
          <tr class="head_sub">
            <th class="middle">正式名</th>
            <th class="middle">よみがな</th>
            <th class="middle">
              <br />
            </th>
            <th class="middle">３字</th>
            <th class="middle">３字</th>
            <th class="middle">
              <br />
            </th>
            <th class="top">勝率</th>
            <th class="middle">分け</th>
            <th class="middle">敢闘賞</th>
            <th class="middle">奪金星</th>
            <th class="middle">前比(kg)</th>
            <th class="middle">よみがな</th>
          </tr>
          <tr class="head_sub">
            <th class="bottom">
              <br />
            </th>
            <th class="bottom">４字</th>
            <th class="bottom">
              <br />
            </th>
            <th class="bottom">よみがな</th>
            <th class="bottom">
              <br />
            </th>
            <th class="bottom">
              <br />
            </th>
            <th class="bottom">休負</th>
            <th class="bottom">休み</th>
            <th class="bottom">技能賞</th>
            <th class="bottom">表記</th>
            <th class="bottom">
              <br />
            </th>
            <th class="bottom">
              <br />
            </th>
          </tr>
        </thead>
        <tbody>
          <tr class="odd">
            <td class="top">東</td>
            <td class="top">朝青龍</td>
            <td class="top">朝青龍</td>
            <td rowspan="4" class="single">002121</td>
            <td rowspan="4" class="single">２３</td>
            <td class="top">高　砂</td>
            <td class="top">モンゴ</td>
            <td class="top">横綱</td>
            <td rowspan="2" class="single">１９</td>
            <td class="top">２０１</td>
            <td class="top">５</td>
            <td class="top">７</td>
            <td class="top">１８４</td>
            <td class="top">正式名</td>
          </tr>
          <tr class="odd">
            <td class="middle">横綱</td>
            <td class="middle">正式名</td>
            <td class="middle">３字</td>
            <td class="middle">正式名</td>
            <td class="middle">正式名</td>
            <td class="middle">正式名</td>
            <td class="middle">負け</td>
            <td class="middle">殊勲賞</td>
            <td class="middle">表記</td>
            <td class="middle">１４０</td>
            <td class="middle">３字</td>
          </tr>
          <tr class="odd">
            <td class="middle">横綱</td>
            <td class="middle">よみがな</td>
            <td class="middle">
              <br />
            </td>
            <td class="middle">３字</td>
            <td class="middle">３字</td>
            <td class="middle">
              <br />
            </td>
            <td class="top">．７１８</td>
            <td class="middle">分け</td>
            <td class="middle">敢闘賞</td>
            <td class="middle">奪金星</td>
            <td class="middle">－８</td>
            <td class="middle">よみがな</td>
          </tr>
          <tr class="odd">
            <td class="bottom">
              <br />
            </td>
            <td class="bottom">
              <br />
            </td>
            <td class="bottom">
              <br />
            </td>
            <td class="bottom">よみがな</td>
            <td class="bottom">
              <br />
            </td>
            <td class="bottom">
              <br />
            </td>
            <td class="bottom">．７７７</td>
            <td class="bottom">休み</td>
            <td class="bottom">技能賞</td>
            <td class="bottom">表記</td>
            <td class="bottom">
              <br />
            </td>
            <td class="bottom">
              <br />
            </td>
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
						<xsl:value-of select="$node/PlayerForSumo/SumoGrade[@Kind='新位置']/Direction" />
					</xsl:when>
					<xsl:when test="$col=2">
						<xsl:value-of select="$node/PlayerName/Writing" />
					</xsl:when>
					<xsl:when test="$col=3">
						<xsl:value-of select="$node/PlayerName/Formal[@Display='3字']" />
					</xsl:when>
					<xsl:when test="$col=4">
						<xsl:value-of select="$node/@PlayerId" />
					</xsl:when>
					<xsl:when test="$col=5">
						<xsl:value-of select="$node/Age" />
					</xsl:when>
					<xsl:when test="$col=6">
						<xsl:value-of select="$node/Belong/Writing" />
					</xsl:when>
					<xsl:when test="$col=7">
						<xsl:value-of
							select="concat($node/PlayerForSumo/NativeCountry/Writing,$node/PlayerForSumo/NativeArea/Writing)" />
					</xsl:when>
					<xsl:when test="$col=8">
						<xsl:value-of select="$node/PlayerForSumo/SumoGrade[@Kind='最高位']/Writing" />
					</xsl:when>
					<xsl:when test="$col=9">
						<xsl:value-of select="$node/Result/ResultForSumo/SumoOutcomeTotal/BashoCount" />
					</xsl:when>
					<xsl:when test="$col=10">
						<xsl:value-of select="$node/Result/ResultForSumo/SumoOutcomeTotal/WinCount" />
					</xsl:when>
					<xsl:when test="$col=11">
						<xsl:value-of
							select="concat($node/Result/Award[@Kind='優勝']/Count/CountValue,'（',$node/Result/Award[@Kind='優勝']/Count/Writing,'）')" />
					</xsl:when>
					<xsl:when test="$col=12">
						<xsl:value-of select="$node/Result/Record[@Kind='与金星']/IntegerPart" />
					</xsl:when>
					<xsl:when test="$col=13">
						<xsl:value-of select="$node/Height" />
					</xsl:when>
					<xsl:when test="$col=14">
						<xsl:value-of select="$node/PlayerForSumo/PreviousName/Formal[not(boolean(@Display))]" />
					</xsl:when>
				</xsl:choose>
			</xsl:when>
			<xsl:when test="$row=2">
				<xsl:choose>
					<xsl:when test="$col=1">
						<xsl:value-of select="$node/PlayerForSumo/SumoGrade[@Kind='新位置']/Writing" />
					</xsl:when>
					<xsl:when test="$col=2">
						<xsl:value-of select="$node/PlayerName/Formal[not(boolean(@Display))]" />
					</xsl:when>
					<xsl:when test="$col=3">
						<xsl:value-of select="$node/PlayerName/Formal[@Display='2字']" />
					</xsl:when>
					<xsl:when test="$col=4">
						<xsl:value-of select="$node/Belong/Formal[not(boolean(@Display))]" />
					</xsl:when>
					<xsl:when test="$col=5">
						<xsl:value-of
							select="concat($node/PlayerForSumo/NativeCountry/Formal[not(boolean(@Display))],$node/PlayerForSumo/NativeArea/Formal[not(boolean(@Display))])" />
					</xsl:when>
					<xsl:when test="$col=6">
						<xsl:value-of select="$node/PlayerForSumo/SumoGrade[@Kind='最高位']/SumoRank" />
					</xsl:when>
					<xsl:when test="$col=7">
						<xsl:value-of select="$node/Result/ResultForSumo/SumoOutcomeTotal/LossCount" />
					</xsl:when>
					<xsl:when test="$col=8">
						<xsl:value-of
							select="concat($node/Result/Award[@Kind='殊勲賞']/Count/CountValue,'（',$node/Result/Award[@Kind='殊勲賞']/Count/Writing,'）')" />
					</xsl:when>
					<xsl:when test="$col=9">
						<xsl:value-of select="$node/Result/Record[@Kind='与金星']/Writing" />
					</xsl:when>
					<xsl:when test="$col=10">
						<xsl:value-of select="$node/Weight" />
					</xsl:when>
					<xsl:when test="$col=11">
						<xsl:value-of select="$node/PlayerForSumo/PreviousName/Formal[@Display='3字']" />
					</xsl:when>
				</xsl:choose>
			</xsl:when>
			<xsl:when test="$row=3">
				<xsl:choose>
					<xsl:when test="$col=1">
						<xsl:value-of select="$node/PlayerForSumo/SumoGrade[@Kind='新位置']/SumoRank" />
					</xsl:when>
					<xsl:when test="$col=2">
						<xsl:value-of select="$node/PlayerName/Formal[@Display='よみがな']" />
					</xsl:when>
					<xsl:when test="$col=4">
						<xsl:value-of select="$node/Belong/Formal[@Display='3字']" />
					</xsl:when>
					<xsl:when test="$col=5">
						<xsl:value-of
							select="concat($node/PlayerForSumo/NativeCountry/Formal[@Display='3字'],$node/PlayerForSumo/NativeArea/Formal[@Display='3字'])" />
					</xsl:when>
					<xsl:when test="$col=7">
						<xsl:value-of select="$node/Result/ResultForSumo/WinningPercentage[not(boolean(@Kind))]" />
					</xsl:when>
					<xsl:when test="$col=8">
						<xsl:value-of select="$node/Result/ResultForSumo/SumoOutcomeTotal/DrawCount" />
					</xsl:when>
					<xsl:when test="$col=9">
						<xsl:value-of
							select="concat($node/Result/Award[@Kind='敢闘賞']/Count/CountValue,'（',$node/Result/Award[@Kind='敢闘賞']/Count/Writing,'）')" />
					</xsl:when>
					<xsl:when test="$col=10">
						<xsl:value-of select="$node/Result/Record[@Kind='奪金星']/IntegerPart" />
					</xsl:when>
					<xsl:when test="$col=11">
						<xsl:value-of select="$node/PlayerForSumo/WeightDefference" />
					</xsl:when>
					<xsl:when test="$col=12">
						<xsl:value-of select="$node/PlayerForSumo/PreviousName/Formal[@Display='よみがな']" />
					</xsl:when>
				</xsl:choose>
			</xsl:when>
			<xsl:when test="$row=4">
				<xsl:choose>
					<xsl:when test="$col=2">
						<xsl:value-of select="$node/PlayerName/Formal[@Display='4字']" />
					</xsl:when>
					<xsl:when test="$col=4">
						<xsl:value-of select="$node/Belong/Formal[@Display='よみがな']" />
					</xsl:when>
					<xsl:when test="$col=7">
						<xsl:value-of select="$node/Result/ResultForSumo/WinningPercentage[@Kind='休みを負とした']" />
					</xsl:when>
					<xsl:when test="$col=8">
						<xsl:value-of select="$node/Result/ResultForSumo/SumoOutcomeTotal/AbsenceCount" />
					</xsl:when>
					<xsl:when test="$col=9">
						<xsl:value-of
							select="concat($node/Result/Award[@Kind='技能賞']/Count/CountValue,'（',$node/Result/Award[@Kind='技能賞']/Count/Writing,'）')" />
					</xsl:when>
					<xsl:when test="$col=10">
						<xsl:value-of select="$node/Result/Record[@Kind='奪金星']/Writing" />
					</xsl:when>
				</xsl:choose>
			</xsl:when>
		</xsl:choose>
	</xsl:template>
</xsl:stylesheet>
