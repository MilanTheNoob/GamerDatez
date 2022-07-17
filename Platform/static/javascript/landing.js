const toggle_btn = document.querySelectorAll(".toggle");
const main = document.querySelector("main");
const images = document.querySelectorAll(".image");
const passRequirements = document.querySelectorAll("#login-input-wrap");
const nameRequirements = document.querySelector("#sign-input-wrap");

var iter = 0;
var titleTxt = `A safe place conecting you to people with video games, what? Are you waiting for me to woo you with an essay you will never read?`;

$(document).ready(function () {
  if (iter < titleTxt.length) {
    document.getElementById("title").insertAdjacentHTML("beforeend", titleTxt.charAt(iter));
    iter++;
    setTimeout(typeWriter, 1);
  }

  $('#signupUsername').keyup(function () {
    var data = $(this).val();

    if (data.length <= 4) { nameRequirements.style.background = "linear-gradient(to right, #D4145A, #FBB03B)"; }
    else if (data.includes(' ')) { nameRequirements.style.background = "linear-gradient(to right, #D4145A, #FBB03B)"; }
    else 
    {
      $.ajax({
        url : '/actions/check-username',
        data : {
          "csrfmiddlewaretoken": csrfToken,
          "value" : data,
        },
        success : function (r) {
          if (r.response != true) {
            nameRequirements.style.background = "linear-gradient(to right, #009245, #00ff00)";
          } else {
            nameRequirements.style.background = "linear-gradient(to right, #D4145A, #FBB03B)";
          }
        },
        error : function (r) {
          nameRequirements.style.background = "linear-gradient(to right, #D4145A, #FBB03B)";
        },
        method : 'POST',
      });
    }
  });
});

toggle_btn.forEach((btn) => {
  btn.addEventListener("click", () => {
    main.classList.toggle("sign-up-mode");
  });
});

function login() {
  $.ajax({
    url : '/actions/login',
    data : {
      "csrfmiddlewaretoken": csrfToken,
      "lusername" : $("input[name='lusername']").val(),
      "lpassword" : $("input[name='lpassword']").val(),
    },
    success : function (r) {
      console.log("1");
      if (r.response == true) {
        window.location.href ="/";
      }
      else {
        console.log("2");
        passRequirements[0].style.background = "linear-gradient(to right, #D4145A, #FBB03B)";
        passRequirements[1].style.background = "linear-gradient(to right, #D4145A, #FBB03B)";
      }
    },
    error : function (r) {
      passRequirements[0].style.background = "linear-gradient(to right, #D4145A, #FBB03B)";
      passRequirements[1].style.background = "linear-gradient(to right, #D4145A, #FBB03B)";
    },
    method : 'POST',
  });
}

function signup() {
  $.ajax({
    url : '/actions/signup',
    data : {
      "csrfmiddlewaretoken": csrfToken,
      "username" : $("input[name='username']").val(),
    },
    success : function (r) {
      window.location.href = "/";
    },
    error : function (r) {
    },
    method : 'POST',
  });
}

function typeWriter() {
  if (iter < titleTxt.length) {
    document.getElementById("title").innerHTML += titleTxt.charAt(iter);
    iter++;
    setTimeout(typeWriter, 50);
  }
}