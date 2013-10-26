$(function(){

  // Newsticker
  $("#header ul").newsticker(6000);

  // Main Source Code
  if($.browser.msie) $("#source span").html(" ");
  else {
    $('<pre><code class="javascript"/></pre>').hide().appendTo("#source").hide();
    $.ajax({url:"jquery.idTabs.js", dataType: "text", success:function(m){
      $("#source pre code").html( m.replace(/</g,"&lt;").replace(/>/g,"&gt;")).chili();
    }});
    $("#source span").toggle(
      function(){ $("#source pre").slideDown(); },
      function(){ $("#source pre").slideUp(); });
  }

  // Example Source Code
  $(".example").each(function(){
    var str = $(this).find(">div").html()
      .replace(/&/g,"&amp;")
      .replace(/</g,"&lt;")
      .replace(/>/g,"&gt;")
      .replace(/ opacity: 0\.9999;/ig,"")
      .replace(/ style="display: block;?"/ig,"")
      .replace(/ style="display: inline;?"/ig,"")
      .replace(/ style="display: none;?"/ig,"")
      .replace(/ class=""/ig,"")
      .replace(/ jQuery\d*="\d*"/ig,"")
      .replace(/ oldblock="\w*"/ig,"")
      .split("\n");
    while(str.length && /^\s*$/.test(str[0])) str.shift(1);
    while(str.length && /^\s*$/.test(str[str.length-1])) str.pop();
    if(!str.length) return;
    var n = str[0].match(/^\s*/)[0].length;
    for(var i=0; i<str.length; i++) str[i] = str[i].substr(n);
    str = str.join("\n");
    str = str.replace(/&lt;script\s*type="text\/javascript"\s*&gt;/g,'&lt;script type="text/javascript"&gt;</code><code class="javascript">');
    str = str.replace(/&lt;\/script&gt;/g,'</code><code class="html">&lt;\/script&gt;');
    str = '<code class="html">' + str + '</code>';
    $(this).find(">pre").hide().html(str);
    $("code",this).chili();
    $(this).find(">span").toggle(
      function(){ $(this.parentNode).find(">pre").slideDown(); },
      function(){ $(this.parentNode).find(">pre").slideUp(); });
  });

  // Hack
  if($.browser.msie)
    $("pre>code").each(function(){
      $(this).html($(this).html().replace(/&lt;\/(\w*)&gt;/g,"&lt;/$1&gt;<br/>"));
    });

});
