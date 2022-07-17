let cookie = document.cookie;
let csrfToken = getCookie("csrftoken");

$(document).ready(function () {
    let font = getCookie('fontSize');
    if (font != "") { document.querySelector('html').style.fontSize = font; }

    let color1 = getCookie('color1');
    let color2 = getCookie('color2');

    if (color1 != "")
    {
      document.documentElement.style.setProperty('--color-primary-1', color1);
      document.documentElement.style.setProperty('--color-primary-2', color2);
    }
    
    let colorWhite = getCookie('colorWhite');

    if (colorWhite != "")
    { 
      document.documentElement.style.setProperty('--color-white', colorWhite);
      document.documentElement.style.setProperty('--color-light', getCookie("colorLight"));
      document.documentElement.style.setProperty('--color-dark', getCookie("colorDark"));
      document.documentElement.style.setProperty('--color-black', getCookie("colorBlack"));
    }
  });

function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
  }