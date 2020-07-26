$('.form').find('input, textarea').on('keyup blur focus', function (e) {

    var $this = $(this),
        label = $this.prev('label');
  
      label.addClass('active highlight');
  
        if (e.type === 'blur') {
          if( $this.val() === '' ) {
              label.removeClass('active highlight');
              } else {
              label.removeClass('highlight');
              }
      } else if (e.type === 'focus') {
  
        if( $this.val() === '' ) {
              label.removeClass('highlight');
              }
        else if( $this.val() !== '' ) {
              label.addClass('highlight');
              }
      }
  
  });
  
  $('.tab a').on('click', function (e) {
  
    e.preventDefault();
  
    $(this).parent().addClass('active');
    $(this).parent().siblings().removeClass('active');
  
    target = $(this).attr('href');
  
    $('.tab-content > div').not(target).hide();
  
    $(target).fadeIn(600);
  
  });


function demoInsert() {
  var values = {};
  values['email_Id'] = document.getElementById("insert_email_id").value;
  values['GPA_Hours'] = document.getElementById("insert_GPA_HOURS").value;
  values['Letter_Grade'] = document.getElementById("insert_Letter_Grade").value;
  values['Course_Comb'] = document.getElementById("insert_Course_Comb").value;
  console.log(values)
  // $.post("/demo-insert/",
  // values,
  // function(data, status){
  //   console.log("Data: " + data + "\nStatus: " + status);
  // });
}

// function demoQuery() {

// }

// function demoUpdate() {
//   //document.getElementById("demo").style.color = "red";
// }

// function demoDelete() {

// }