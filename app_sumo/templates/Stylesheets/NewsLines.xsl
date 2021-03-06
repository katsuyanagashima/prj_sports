<?xml version="1.0" encoding="UTF-16"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/TR/WD-xsl" xml:lang="ja">

	<xsl:template match="/">
		<html lang="ja">
			<head>
				<title>NewsLines</title>
                 <style type="text/css">
                   .color1  {color:brown;} 
                   .color2  {color:purple;font-weight:bold}
                   .color3  {color:green;font-size:12pt} 
                   .bgcolor1  {background-color:silver;font-weight:bold;color:black;font-size:10pt}
                   .bgcolor2 {background-color:white}
                 </style>
               </head>

			<body>
                    <div style="font-weight:bold;font-size:20pt;color:#483B8D">NewsLines</div>
                  <xsl:for-each select="NewsML/NewsItem/NewsComponent">
                  <table bgcolor="#000000" cellpadding="0" cellspacing="0">
                         <tr><td>
                   <table border="0" cellpadding="4" cellspacing="1"  width="800">
                    <tr class="bgcolor2"><td class="color1" >項目名</td><td class="color1">内容</td></tr>
				<xsl:apply-templates select="NewsLines"/>
                    </table>
                    </td></tr>
                    </table>
                  <p></p>
                   </xsl:for-each>
			</body>
		</html>
	</xsl:template>

 	<xsl:template match="NewsLines">

       <xsl:for-each select="HeadLine">
            <tr class="bgcolor2"><td class="bgcolor1">HeadLine</td>
            <td>	
            <span class="color3"><xsl:value-of select="."/></span>
            <xsl:if test="@xml:lang[not(.='')]">
                 <span class="color3">（xml:lang=<xsl:value-of select="@xml:lang"/>）</span>
            </xsl:if>
            </td></tr>
       </xsl:for-each>

       <xsl:for-each select="SubHeadLine">
          <tr class="bgcolor2"><td class="bgcolor1">SubHeadLine</td>
          <td>	
          <span class="color3"><xsl:value-of select="."/></span>
          <xsl:if test="@xml:lang[not(.='')]">
                <span class="color3">（xml:lang=<xsl:value-of select="@xml:lang"/>）</span>
          </xsl:if>
          </td></tr>
      </xsl:for-each>

      <xsl:for-each select="ByLine">
          <tr class="bgcolor2"><td class="bgcolor1">ByLine</td>
          <td>	
          <span class="color3"><xsl:value-of select="."/></span>
          <xsl:if test="@xml:lang[not(.='')]">
              <span class="color3">（xml:lang=<xsl:value-of select="@xml:lang"/>）</span>
          </xsl:if>
          </td></tr>
      </xsl:for-each>

      <xsl:for-each select="DateLine">
          <tr class="bgcolor2"><td class="bgcolor1">DateLine</td>
          <td>	
          <span class="color3"><xsl:value-of select="."/></span>
          <xsl:if test="@xml:lang[not(.='')]">
               <span class="color3">（xml:lang=<xsl:value-of select="@xml:lang"/>）</span>
          </xsl:if>
          </td></tr>
      </xsl:for-each>

      <xsl:for-each select="CreditLine">
          <tr class="bgcolor2"><td class="bgcolor1">CreditLine</td>
          <td><span class="color3"><xsl:value-of select="."/></span>
          <xsl:if test="@xml:lang[not(.='')]">
               <span class="color3">（xml:lang=<xsl:value-of select="@xml:lang"/>）</span>
          </xsl:if>
          </td></tr>
      </xsl:for-each>

      <xsl:for-each select="CopyRightLine">
          <tr class="bgcolor2"><td class="bgcolor1">CopyRightLine</td>
          <td>	
          <span class="color3"><xsl:value-of select="."/></span>
          <xsl:if test="@xml:lang[not(.='')]">
               <span class="color3">（xml:lang=<xsl:value-of select="@xml:lang"/>）</span>
          </xsl:if>
          </td></tr>
      </xsl:for-each>

      <xsl:for-each select="RightLine">
         <tr class="bgcolor2"><td class="bgcolor1">RightLine</td>
         <td>	
         <span class="color3"><xsl:value-of select="."/></span>
         <xsl:if test="@xml:lang[not(.='')]">
             <span class="color3">（xml:lang=<xsl:value-of select="@xml:lang"/>）</span>
         </xsl:if>
         </td></tr>
         </xsl:for-each>
            <xsl:for-each select="SeriesLine">
               <tr class="bgcolor2"><td class="bgcolor1">SeriesLine</td>
               <td>	
               <span class="color3"><xsl:value-of select="."/></span>
               <xsl:if test="@xml:lang[not(.='')]">
                    <span class="color3">（xml:lang=<xsl:value-of select="@xml:lang"/>）</span>
               </xsl:if>
               </td></tr>
           </xsl:for-each>
           <xsl:for-each select="SlugLine">
              <tr class="bgcolor2"><td class="bgcolor1">SlugLine</td>
              <td>	
              <span class="color3"><xsl:value-of select="."/></span>
              <xsl:if test="@xml:lang[not(.='')]">
                   <span class="color3">（xml:lang=<xsl:value-of select="@xml:lang"/>）</span>
              </xsl:if>
              </td></tr>
          </xsl:for-each>

          <xsl:for-each select="KeywordLine">
              <tr class="bgcolor2"><td class="bgcolor1">KeywordLine</td>
              <td>	
              <span class="color3"><xsl:value-of select="."/></span>
              <xsl:if test="@xml:lang[not(.='')]">
                    <span class="color3">（xml:lang=<xsl:value-of select="@xml:lang"/>）</span>
              </xsl:if>
              </td></tr>
         </xsl:for-each>

         <xsl:if test="NewsLine/NewsLineText[not(.='')]">
            <tr class="bgcolor2"><td class="bgcolor1">NewsLine</td>
            <td>	
            <xsl:if test="@xml:lang[not(.='')]">
                 <span class="color3">（xml:lang=<xsl:value-of select="@xml:lang"/>）</span>
            </xsl:if>
            <span class="color3">（NewsLineType@FormaName=<xsl:value-of select="NewsLine/NewsLineType/@FormalName"/>）</span>
            <xsl:for-each select="NewsLine/NewsLineText">
                  <span class="color3">／<xsl:value-of select="."/></span>
            </xsl:for-each>
            </td></tr>
         </xsl:if>

	</xsl:template>

    </xsl:stylesheet>    


 

