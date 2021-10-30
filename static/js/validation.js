$.validator.addMethod("alpha", function(value, element) {
    return this.optional(element) || value == value.match(/^[a-zA-Z\s]+$/);
    // --                                    or leave a space here ^^
});

jQuery.validator.addMethod("noSpace", function(value, element) {
    return value == '' || value.trim(' ').length >=4;
  }, "At least four characters");

//email
$.validator.addMethod("isEmail", function(value, element) {
    return this.optional(element) || value == value.match(/\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}\b/i);

});
//ajax call


$(document).ready(function (e) {
        $("#form").validate({
            rules:{
                first_name:{

                    required:true,
                    minlength:4,
                    alpha: true,
                    noSpace: true,
                },
                last_name:{

                    required:true,
                    minlength:1,
                    alpha: true,

                },
                username:{

                    required:true,
                    minlength:5,

                },

                phone_no:{
                    minlength:10,
                    maxlength:10,
                    number: true
                },
                email:{
                    required:true,
                    isEmail:true
                },


            },
            
            messages:{
                first_name:{
                    alpha:"Please enter letters only"
                },
                username:{
                    alpha:"Please enter at least 5 digit"
                },
                phone_no:{
                    number:"Please enter a valid mobile",
                    minlength:"Please enter at least 10 digit",
                    maxlength:"mobile number maximum contain 10 digit",
                },

                email:{
                    isEmail:"Email not valid"
                },



            },
        })

    })