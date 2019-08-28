let form = $("#wizard").show();


$(function () {
    /*$("#is_working").click(function () {

        alert("h1");
        x = document.getElementById('is_checked')
        if (x.checked) {
            $("#dp3").prop("disabled", true);

        } else {
            $("#dp3").prop("disabled", false);
        }
    });*/


    $("#wizard").steps({
        headerTag: "h4",
        bodyTag: "section",
        transitionEffect: "fade",
        enableAllSteps: true,
        transitionEffectSpeed: 1,
        labels: {
            next: "Next",
            previous: "Back"
        },
        onStepChanging: function (event, currentIndex, newIndex) {
            form.validate().settings.ignore = ":disabled,:hidden";
            if (form.valid()) {
                if (newIndex === 1) {
                    //alert("Step 1 Complete");
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
                if (newIndex === 5) {
                    $(".steps ul").addClass("step-6");
                    $(".actions ul").addClass("mt-7");
                } else {
                    $(".steps ul").removeClass("step-6");
                    $(".actions ul").removeClass("mt-7");
                }
                if (newIndex === 6) {
                    $(".steps ul").addClass("step-7");
                    $(".actions ul").addClass("mt-7");
                } else {
                    $(".steps ul").removeClass("step-7");
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

        onStepChanged: function (event, currentIndex, priorIndex) {

            var con1 = document.getElementById('higher_edu').checked;
            var con2 = document.getElementById('job').checked;
            if (currentIndex === 3 && priorIndex === 4 && !con1) {
                $(this).steps("previous");
                return;
            }
            if (currentIndex === 3 && !con1) {
                form.steps("next");
            }
            if (currentIndex === 4 && priorIndex === 5 && !con2) {
                $(this).steps("previous");
                return;
            }
            if (currentIndex === 4 && !con2) {
                form.steps("next");
            }
            // Used to skip the "Warning" step if the user is old enough and wants to the previous step.


        },

        onFinishing: function (event, currentIndex) {
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
            middle_name: "required",
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
            school_district: "required",
            school_city: "required",
            school_state: "required",
            school_country: "required",
            hostel: "required",
            current_street_address: "required",
            current_landmark: "required",
            current_pincode: "required",
            current_country: "required",
            current_state: "required",
            current_city: "required",
            current_district: "required",
            higher_studies: "required",
            course_taken: "required",
            college_name: {
                required:'#higher_edu:checked'
            },
            college_country:{
                required:'#higher_edu:checked'
            },
            college_state: {
                required:'#higher_edu:checked'
            },
            college_city: {
                required:'#higher_edu:checked'
            },
            company_name: {
                required:'#job:checked'
            },
    
            position: {
                required:'#job:checked'
            },
            company_country: {
                required:'#job:checked'
            },
            company_state: {
                required:'#job:checked'
            },
            company_city: {
                required:'#job:checked'
            },
            password: "required",
            conf_password: {
                equalTo: "#password"
            }

        },
        // Specify validation error messages
        messages: {},
    });
    // Custom Button Jquery Steps
    $('.forward').click(function () {
        $("#wizard").steps('next');
    });
    $('.backward').click(function () {
        $("#wizard").steps('previous');
    });

    // Click to see password 
    $('.password i').click(function () {
        if ($('.password input').attr('type') === 'password') {
            $(this).next().attr('type', 'text');
        } else {
            $('.password input').attr('type', 'password');
        }
    })
    // Date Picker
    let dp1 = $('#dp1').datepicker().data('datepicker');
    dp1.selectDate(new Date());
    let dp2 = $('#dp2').datepicker().data('datepicker');
    dp2.selectDate(new Date());
    let dp3 = $('#dp3').datepicker().data('datepicker');
    dp3.selectDate(new Date());
});
