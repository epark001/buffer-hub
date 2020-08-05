$(function() {

  $("#agetext").hide();

  $(".age").click(function() {
      if ($('input[name="age"]:checked').val() == "no")
          $("#agetext").show();
      else if ($('input[name="age"]:checked').val() == "yes") 
          $("#agetext").hide();
 
  
  });
});