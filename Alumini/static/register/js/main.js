
$(function(){
	$("#wizard").steps({
        headerTag: "h4",
        bodyTag: "section",
        transitionEffect: "fade",
        enableAllSteps: true,
        transitionEffectSpeed: 300,
        labels: {
            next: "Next",
            previous: "Back"
        },
        onStepChanging: function (event, currentIndex, newIndex) {
        if (newIndex === 1) {
        $(".steps ul").addClass("step-2");
      } else {
        $(".steps ul").removeClass("step-2");
      }
      if (newIndex === 2) {
        $(".steps ul").addClass("step-3");
        $(".actions ul").addClass("mt-7");
      } else {
        $(".steps ul").removeClass("step-3");
        $(".actions ul").removeClass("mt-7");
      }
      if (newIndex === 3) {
        $(".steps ul").addClass("step-4");
        $(".actions ul").addClass("mt-7");
      } else {
        $(".steps ul").removeClass("step-4");
        $(".actions ul").removeClass("mt-7");
      }
      if (newIndex === 4) {
        $(".steps ul").addClass("step-5");
        $(".actions ul").addClass("mt-7");
      } else {
        $(".steps ul").removeClass("step-5");
        $(".actions ul").removeClass("mt-7");
      }
//        if(currentIndex == 1)
//        {
//            $.ajax({
//            type: "POST",
//            url: 'submit_form/',
//            data: {
//            'name': "name.value",
//            'middle':"mid.value",
//            },
//            dataType: 'json',
//
//      });
//        }


      return true;
    },

    onFinishing: function(event, currentIndex) {
            alert("Hello");
            $('#wizard').submit();

      },


            
    });
    // Custom Button Jquery Steps
    $('.forward').click(function(){
    	$("#wizard").steps('next');
    });
    $('.backward').click(function(){
        $("#wizard").steps('previous');
    });

    // Click to see password 
    $('.password i').click(function(){
        if ( $('.password input').attr('type') === 'password' ) {
            $(this).next().attr('type', 'text');
        } else {
            $('.password input').attr('type', 'password');
        }
    }) 
    // Date Picker
    let dp1 = $('#dp1').datepicker().data('datepicker');
    dp1.selectDate( new Date( ));
});
