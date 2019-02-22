$.get('https://swapi.co/api/films/?format=json', function (data) {
  $('header').animate({
    'font-size': '40px'
  }).css('text-decoration', 'underline');

  $.each(data.results, function () {
    $('<li></li>')
    .text(this.title)
    .appendTo('UL#list_movies')
    .css('list-style', 'none')
    .css('position', 'relative')
    .fadeIn(100)
    .animate({
      'opacity': '0.5',
      'right': '35px',
      'font-size': '30px',
      'bottom': '30px'
    }, 300);
  });

  $('footer').animate({
    'font-size': '30px'
  }, 500).css('text-decoration', 'underline');
});
