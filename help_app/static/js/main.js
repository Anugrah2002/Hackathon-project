function showPassword() {
  var x = document.getElementById("password");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}

function validateEmail(){
    let emailAddress = document.getElementById('email').value;
    myArray = emailAddress.split("@");
    if (myArray[1] != null){
        if (myArray[1].toLowerCase() == "vitbhopal.ac.in" ){
            document.getElementById("message").innerHTML = ""
            $.ajax({
                type:'POST',
                url:'/send_OTP/',
                data:{
                    email:emailAddress,
                    csrfmiddlewaretoken: $('[name="csrfmiddlewaretoken"]').val()
                },
                success:function(data){
                    if (data == "send"){
                        document.getElementById('otpRow').hidden = false;
                        document.getElementById('otpButtonRow').hidden = false;
                        document.getElementById('validate-button').hidden = true;
                    }
                }
            });
        }
        else{
            document.getElementById("message").innerHTML = "Email should have @vitbhopal.ac.in"
        }
    }
    else{
         document.getElementById("message").innerHTML = "Email should have @vitbhopal.ac.in"
    }
}

function verifyOTP(){
    otp = document.getElementById('otp').value;
    $.ajax({
        type:'POST',
        url:'/verify_OTP/',
        data:{
            otp:otp,
            csrfmiddlewaretoken: $('[name="csrfmiddlewaretoken"]').val()
        },
        success:function(data){
            if (data == "verified"){
                document.getElementById('otpRow').hidden = true;
                document.getElementById('otpButtonRow').hidden = true;
                for(i=0;i<verifiedFrom.length;i++){
                    verifiedFrom[i].hidden = false;
                }
            }
        }
    });
}