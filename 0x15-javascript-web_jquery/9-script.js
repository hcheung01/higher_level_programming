$.ajax({
  url: 'https://fourtonfish.com/hellosalut/',
  data: {
    lang: 'en'
  },
  type: 'GET',
  dataType: 'json'
})

.done(function (json) {
  $('DIV#hello').text(json.hello)
  .animate({
    'font-size': '100px'
  });

  $('header').text('In English is: ').animate({
    'font-size': '80px'
  });
});
