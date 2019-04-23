var currentCallback;

// override default browser alert
window.alert = function(msg, callback){
  $('.message').text(msg);
  $('.customAlert').css('animation', 'fadeIn 0.3s linear');
  $('.customAlert').css('display', 'inline');
  setTimeout(function(){
    $('.customAlert').css('animation', 'none');
  }, 300);
  currentCallback = callback;
}

$(function(){
  
  // add listener for when our confirmation button is clicked
	$('.buttons').click(function(){
    $('.customAlert').css('animation', 'fadeOut 0.3s linear');
    setTimeout(function(){
     $('.customAlert').css('animation', 'none');
		$('.customAlert').css('display', 'none');
    }, 300);
    currentCallback();
  })
  
  $('.rab').click(function(){
    alert("No Data to Display.", function(){
      console.log("Callback executed");
    })
  });
  
  // our custom alert box
  setTimeout(function(){
    alert('No Data to Display.', function(){
        console.log("Callback executed");
      });
  }, 500);
});

