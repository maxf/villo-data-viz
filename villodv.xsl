<x:transform xmlns:x="http://www.w3.org/1999/XSL/Transform" version="2.0" 
             xmlns:f="http://lapin-bleu.net/ns"
             xmlns:xs="http://www.w3.org/2001/XMLSchema"
             xmlns="http://www.w3.org/2000/svg"
             xmlns:xlink="http://www.w3.org/1999/xlink">

  <x:output indent="yes"/>

  <x:variable name="samples" select="document('villo-data.xml')/samples"/>

  <x:variable name="start_time" select="$samples/sample[1]/@updated"/>


  <x:function name="f:t" as="xs:float">
    <x:param name="timestamp"/>
    <x:value-of select="($timestamp - $start_time) div 1000"/>
  </x:function> 


  <x:function name="f:x" as="xs:float">
    <x:param name="lon"/>
    <x:value-of select="($lon - 4.280548)"/>
  </x:function> 

  <x:function name="f:y" as="xs:float">
    <x:param name="lat"/>
    <x:value-of select="(50.90 - $lat)"/>
  </x:function> 


  <x:template match="/"><x:apply-templates/></x:template>
  
  <x:template match="carto">
    <svg viewBox="0 0 0.17 0.10">
      <x:apply-templates select="markers/marker"/>
    </svg>
  </x:template>

  <x:template match="marker">
    <x:comment>Station: <x:value-of select="@number"/></x:comment>
    <circle cx="{f:x(@lng)}" cy="{f:y(@lat)}" r="0.0002" fill="{if (@open=1) then 'red' else 'black'}">

      <x:variable name="s">
        <x:perform-sort select="$samples/sample[@stationid = current()/@number]">
          <x:sort select="@updated"/>
        </x:perform-sort>
      </x:variable>

      <x:for-each select="$s/sample">
        <x:if test="position() != last()">
          <x:variable name="next" select="following-sibling::sample[1]"/>
          <x:if test="not(@updated = $next/@updated)">
            <animate attributeName="r" begin="{f:t(@updated)}" end="{f:t($next/@updated)}" from="{@available * 0.0001}" to="{$next/@available * 0.0001}"/>
          </x:if>
        </x:if>
      </x:for-each>

    </circle>
  </x:template>
</x:transform>

