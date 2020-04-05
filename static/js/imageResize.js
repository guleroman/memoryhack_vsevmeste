window.addEventListener('load', function() {
    var images = document.querySelectorAll('img');
    images.forEach(function(image) {
        image.addEventListener('click', viewFullImage);
        image.addEventListener('mouseover', function(){this.style.cursor='pointer'});
        image.addEventListener('mouseout', function(){this.style.cursor='default'});
        });
      })

viewFullImage = function(){
    ad = $(this).attr('src')
    $("#overlay_pop_up_text").html(`<img id="profile_image" class="rounded-lg mr-4" src="${ad}">`)
    $("#overlay_pop_up").attr("style","display: inline;")
    }