voted_count = 0

function vote_for(letter) {
  var url = "/vote/" + letter;

  $.get(url, '', function(data) {
    if (data.content == 1) {
      $('#box_' + letter).css('opacity', '0');
      $('#link_' + letter).click(function() {
        return false;
      });

      voted_count = voted_count + 1

      if (voted_count == 3) {
        window.location.href = "/results";
      }
    }
  })
}