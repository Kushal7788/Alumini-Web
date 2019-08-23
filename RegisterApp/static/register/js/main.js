let form = $("#wizard").show();
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
        form.validate().settings.ignore = ":disabled,:hidden";
        if(form.valid())
        {
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



      return form.valid();
    },

    onFinishing: function(event, currentIndex) {
            alert("Hello");
            $('#wizard').submit();

      },


            
    }).validate({
      errorPlacement: function errorPlacement(error, element) {
        element.before(error);
      },
      rules: {
        // The key name on the left side is the name attribute
        // of an input field. Validation rules are defined
        // on the right side
        first_name: "required",
        middle_name:"required",
        last_name: "required",
        email_username: {
          required: true,
          // Specify that email should be validated
          // by the built-in "email" rule
          email: true
        },
        date_of_birth: "required",
        passout_batch: "required",
        gender: "required",
        phone_number: "required",
        school_street_address: "required",
        school_landmark: "required",
        school_pincode: "required",
        school_district: "required",
        school_taluka: "required",
        school_city: "required",
        hostel: "required",
        current_street_address: "required",
        current_landmark: "required",
        current_pincode: "required",
        current_country: "required",
        current_state: "required",
        current_city: "required",
        higher_studies: "required",
        course_taken: "required",
        college_name: "required",
        college_country: "required",
        college_state: "required",
        college_city: "required",
        company_name: "required",
        position: "required",
        work_experience: "required",
        company_country: "required",
        company_state: "required",
        company_city: "required",


      },
      // Specify validation error messages
      messages: {},
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
