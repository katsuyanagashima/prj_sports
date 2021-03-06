<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/TR/WD-xsl" xml:lang="ja">

	<xsl:template match="/">
		<html lang="ja">
         	<head>
				<title>Identification</title>
              <style type="text/css">
                   .color1  {color:brown;} 
                   .color2  {color:purple;font-weight:bold}
                   .color3  {color:green;font-size:12pt} 
                   .bgcolor1  {background-color:silver;font-weight:bold;color:black;font-size:10pt}
                   .bgcolor2 {background-color:white}
               </style>
		</head>
			<body>
                    <div style="font-weight:bold;font-size:20pt;color:#483B8D">Identification</div>
                   <xsl:for-each select="NewsML/NewsItem/Identification">
                   <table bgcolor="#000000" cellpadding="0" cellspacing="0">
                         <tr><td>
                   <table border="0" cellpadding="4" cellspacing="1"  width="800">
                    <tr class="bgcolor2"><td class="color1" >項目名</td><td class="color1">内容</td></tr>
				<xsl:apply-templates select="NewsIdentifier"/>
                    </table>
                    </td></tr>
                    </table>
                  <p></p>
                   </xsl:for-each>
			</body>
		</html>
	</xsl:template>

 	<xsl:template match="NewsIdentifier">

		<xsl:if test="ProviderId[not(.='')]">
              <tr class="bgcolor2"><td class="bgcolor1">ProviderId</td>
              <td><span class="color3"><xsl:value-of select="ProviderId"/></span></td></tr>
		</xsl:if>

		<xsl:if test="DateId[not(.='')]">
             <tr class="bgcolor2"><td class="bgcolor1">DateId</td>
             <td><span class="color3"><xsl:value-of select="DateId"/></span></td></tr>
		</xsl:if>

		<xsl:if test="NewsItemId[not(.='')]">
             <tr class="bgcolor2"><td class="bgcolor1">NewsItemId</td>
             <td><span class="color3"><xsl:value-of select="NewsItemId"/></span>
             <xsl:if test="NewsItemId/@Vocabulary[not(.='')]">
                <span class="color3">（Vocabulary=<xsl:value-of select="NewsItemId/@Vocabulary"/>）</span>
             </xsl:if>
             </td></tr>
      	</xsl:if>

		<xsl:if test="RevisionId[not(.='')]">
            <tr class="bgcolor2"><td class="bgcolor1">RevisionId</td>
            <td><span class="color3"><xsl:value-of select="RevisionId"/></span>
            <xsl:if test="RevisionId/@PreviousRevision[not(.='')]">
                <span class="color3">（PreviousRevision=<xsl:value-of select="RevisionId/@PreviousRevision"/>）</span>
            </xsl:if>
            <xsl:if test="RevisionId/@Update[not(.='')]">
                <span class="color3">（Update=<xsl:value-of select="RevisionId/@Update"/>）</span>
            </xsl:if>
            </td></tr>
          </xsl:if>

		<xsl:if test="PublicIdentifier[not(.='')]">
              <tr class="bgcolor2"><td class="bgcolor1">PublicIdentifier</td>
              <td><span class="color3"><xsl:value-of select="PublicIdentifier"/></span></td></tr>
		</xsl:if>

 	</xsl:template>
    </xsl:stylesheet>    


 

