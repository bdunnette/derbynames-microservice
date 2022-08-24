$.getJSON( "/name", function( data ) {
    var items = [];
    $.each( data, function( key, val ) {
        console.log(key + ": " + val);
      items.push( "<li id='" + key + "'>" + val + "</li>" );
    });

    $( "<ul/>", {
      "class": "my-new-list",
      html: items.join( "" )
    }).appendTo( "body" );
  });
