villodv.svg: carto.xml villo-data.xml villodv.xsl
	java -jar saxon.jar -t -s:$< -xsl:villodv.xsl -o:$@

