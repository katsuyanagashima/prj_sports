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
                    <div style="font-weight:bold;font-size:20pt;color:#483B8D">NewsManagement</div>
                   <xsl:for-each select="NewsML/NewsItem">
                   <table bgcolor="#000000" cellpadding="0" cellspacing="0">
                         <tr><td>
                   <table border="0" cellpadding="4" cellspacing="1"  width="800">
                    <tr class="bgcolor2"><td class="color1" >項目名</td><td class="color1">内容</td></tr>
				<xsl:apply-templates select="NewsManagement"/>
                    </table>
                    </td></tr>
                    </table>
                  <p></p>
                   </xsl:for-each>
			</body>
		</html>
	</xsl:template>

 	<xsl:template match="NewsManagement">

		<xsl:if test="NewsItemType/@FormalName[not(.='')]">
              <tr class="bgcolor2"><td class="bgcolor1">NewsItemType</td>
              <td>	
              <span class="color3"><xsl:value-of select="NewsItemType/@FormalName"/></span></td></tr>
		</xsl:if>

		<xsl:if test="FirstCreated[not(.='')]">
             <tr class="bgcolor2"><td class="bgcolor1">FirstCreated</td>
             <td><span class="color3"><xsl:value-of select="FirstCreated"/></span></td></tr>
		</xsl:if>

		<xsl:if test="ThisRevisionCreated[not(.='')]">
             <tr class="bgcolor2"><td class="bgcolor1">ThisRevisionCreated</td>
             <td><span class="color3"><xsl:value-of select="ThisRevisionCreated"/></span></td></tr>
		</xsl:if>

		<xsl:if test="Status/@FormalName[not(.='')]">
             <tr class="bgcolor2"><td class="bgcolor1">Status</td>
             <td><span class="color3"><xsl:value-of select="Status/@FormalName"/></span></td></tr>
		</xsl:if>

		<xsl:if test="StatusWillChange/FutureStatus/@FormalName[not(.='')]">
             <tr class="bgcolor2"><td class="bgcolor1">StatusWillChange</td>
             <td><span class="color3">（FutureStatus@FormalName=<xsl:value-of select="StatusWillChange/FutureStatus/@FormalName"/>）</span>
             <span class="color3"><xsl:value-of select="StatusWillChange/DateAndTime"/></span></td></tr>
		</xsl:if>

		<xsl:if test="Urgency/@FormalName[not(.='')]">
             <tr class="bgcolor2"><td class="bgcolor1">Urgency</td>
             <td><span class="color3"><xsl:value-of select="Urgency/@FormalName"/></span></td></tr>
		</xsl:if>

          <xsl:for-each select="DerivedFrom">
              <xsl:if test="@NewsItem[not(.='')]">
                 <tr class="bgcolor2"><td class="bgcolor1">DerivedFrom</td>
                 <td><span class="color3">（NewsItem=<xsl:value-of select="@NewsItem"/>）</span>
                 <xsl:for-each select="Comment">
                     <span class="color3">／<xsl:value-of select="."/></span>
                 </xsl:for-each>
                 </td></tr>
             </xsl:if>
         </xsl:for-each>

         <xsl:for-each select="AssociatedWith">
             <xsl:if test="@NewsItem[not(.='')]">
                <tr class="bgcolor2"><td class="bgcolor1">AssociatedWith</td>
                <td><span class="color3">（NewsItem=<xsl:value-of select="@NewsItem"/>）</span>
                <xsl:for-each select="Comment">
                    <span class="color3">／<xsl:value-of select="."/></span>
                </xsl:for-each>
                </td></tr>
            </xsl:if>
        </xsl:for-each>


    </xsl:template>

  </xsl:stylesheet>    


 

