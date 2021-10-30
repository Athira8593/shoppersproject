    $.validator.addMethod("alpha", function(value, element) {
    return this.optional(element) || value == value.match(/^[a-zA-Z\s]+$/);
    // --                                    or leave a space here ^^
});

jQuery.validator.addMethod("noSpace", function(value, element) {
    return value == '' || value.trim(' ').length >=4;
  }, "Enter four characters");

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
                noSpace: true,
                },

                phone_no:{

                    required:true,
                    minlength:10,
                    maxlength:10,
                    noSpace: true,
                },

            },
            
        })

    })

