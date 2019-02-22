$.ajax({
  url: 'https://fourtonfish.com/hellosalut/',
  data: {
    lang: 'en'
  },
  type: 'GET',
  dataType: 'json'
})

.done(function (json) {
  $('DIV#hello').text('In English is: "' + json.hello + '"')
  .animate({
    'font-size': '100px'
  });
});
