// Wait for the document to be ready
$(document).ready(function () {
  // Define the API URL
  const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/';

  // Listen for a click event on the "Translate" button
  $('INPUT#btn_translate').click(function () {
    // Get the language code from the input field
    const langCode = $('INPUT#language_code').val();

    // Make an AJAX GET request to the API with the language code as a parameter
    $.get(apiUrl, { lang: langCode }, function (data) {
      // Update the "Hello" text in the HTML with the translated text from the API
      $('DIV#hello').html(data.hello);
    });
  });

  // Listen for an "enter" key press event on the language code input field
  $('INPUT#language_code').keypress(function (event) {
    // Check if the "enter" key was pressed
    if (event.which === 13) {
      // Prevent the default form submission behavior
      event.preventDefault();

      // Trigger a click event on the "Translate" button
      $('INPUT#btn_translate').click();
    }
  });
});
