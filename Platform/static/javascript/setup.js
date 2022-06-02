const tabs = ["avatar", "general", "personality", "gaming", "premium"];
const tabCount = 5;

var activeTab = 0;

window.onload = function startup() {
  for (let i = 0; i < tabCount; i++) {
    document.querySelector('.' + tabs[i] + '-tab').style.display = 'none';
    try { document.querySelector('#' + tabs[i]).addEventListener('click', openTab) } catch {}
  }
  var cookie = getCookie("tab");
  if (cookie == "") {
    document.querySelector('.' + tabs[0] + '-tab').style.display = 'block';
  } else {
    document.querySelector('.' + tabs[parseInt(cookie)] + '-tab').style.display = 'block';
  }
}

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

const openTab = (e) => {
  if (tabs.includes(e.target.id)) {
    for (let i = 0; i < tabCount; i++) {
      if (tabs[i] == e.target.id) {
        document.querySelector('.' + tabs[i] + '-tab').style.display = 'block';
        document.cookie = "tab=" + i + "path=/";
    } else {
      document.querySelector('.' + tabs[i] + '-tab').style.display = 'none';
      }
    }
  }
}








/*
const theme = document.querySelector('#theme');
const themeModal = document.querySelector('.settings')

const openSettingsModal = () => {
  themeModal.style.display = 'grid';
}

const closeSettingsModal = (e) => {
  if (e.target.classList.contains('settings')) {
    themeModal.style.display = 'none';
  }
}

themeModal.addEventListener('click', closeSettingsModal);
theme.addEventListener('click', openSettingsModal);
*/
