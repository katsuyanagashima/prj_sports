<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/TR/WD-xsl" xml:lang="ja">

	<xsl:template match="/">
		<html lang="ja">
			<head>
				<title>NewsEnvelope</title>
                <style type="text/css">
                   .color1  {color:brown;} 
                   .color2  {color:purple;font-weight:bold}
                   .color3  {color:green;font-size:12pt} 
                   .bgcolor1  {background-color:silver;font-weight:bold;color:black;font-size:10pt}
                   .bgcolor2 {background-color:white}
                </style>
               </head>
			<body>
                    <div style="font-weight:bold;font-size:20pt;color:#483B8D">NewsEnvelope</div>
                   <table bgcolor="#000000" cellpadding="0" cellspacing="0">
                         <tr><td>
                   <table border="0" cellpadding="4" cellspacing="1"  width="800">
                    <tr class="bgcolor2"><td class="color1" >項目名</td><td class="color1">内容</td></tr>
				<xsl:apply-templates select="NewsML/NewsEnvelope"/>
                    </table>
                    </td></tr>
                    </table>
			</body>
		</html>
	</xsl:template>

 	<xsl:template match="NewsML/NewsEnvelope">
		<xsl:if test="TransmissionId[not(.='')]">
             <tr class="bgcolor2"><td class="bgcolor1">TransmissonId</td>
             <td>	
             <span class="color3"><xsl:value-of select="TransmissionId"/></span>
     	   <xsl:if test="TransmissionId/@Repeat[not(.='')]">
                 <span class="color3">（Repeat=<xsl:value-of select="TransmissionId/@Repeat"/>）</span>
             </xsl:if>
             </td></tr>
          </xsl:if>

		<xsl:if test="DateAndTime[not(.='')]">
             <tr class="bgcolor2"><td class="bgcolor1">DateAndTime</td>
             <td><span class="color3"><xsl:value-of select="DateAndTime"/></span></td></tr>
		</xsl:if>

          <xsl:for-each select="NewsProduct">
             <xsl:if test="@FormalName[not(.='')]">
                <tr class="bgcolor2"><td class="bgcolor1">NewsProduct</td>
                <td>	
                <span class="color3">（FormalName=<xsl:value-of select="@FormalName"/>）</span></td></tr>
             </xsl:if>
         </xsl:for-each>

	</xsl:template>

    </xsl:stylesheet>    


 

