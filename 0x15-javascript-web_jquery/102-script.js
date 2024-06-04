// This function will be called when the DOM is fully loaded
$('document').ready(function () {

  // URL of the API endpoint
  const url = 'https://www.fourtonfish.com/hellosalut/?';

  // Attach a click event handler to the translate button
  $('INPUT#btn_translate').click(function () {
    // Construct the URL with the language code entered by the user
    $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
      // Update the hello div with the translated text
      $('DIV#hello').html(data.hello);
    });
  });
});
