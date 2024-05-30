#!/usr/bin/node

$(document).ready(function() {
  $('#btn_translate').click(function() {
    const languageCode = $('#language_code').val();
    if (languageCode) {
      const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;
      $.get(apiUrl, function(data) {
        $('#hello').text(data.hello);
      }).fail(function() {
        $('#hello').text('Error fetching translation');
      });
    } else {
      $('#hello').text('Please enter a language code');
    }
  });
});

