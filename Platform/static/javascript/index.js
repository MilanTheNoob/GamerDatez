const tabs = ["home", "dates", "messages", "settings"];
const tabCount = 4;

var activeTab = 0;

window.onload = function startup() {
  for (let i = 0; i < tabCount; i++) {

    document.querySelector('.' + tabs[i] + '-tab').style.visibility = 'hidden';
    document.querySelector('.' + tabs[i] + '-tab').style.display = 'none';
    document.querySelector('#' + tabs[i]).addEventListener('click', openTab)
  }

  document.querySelector('.' + tabs[0] + '-tab').style.visibility = 'visible';
  document.querySelector('.' + tabs[0] + '-tab').style.display = 'block';

}

const openTab = (e) => {
  if (tabs.includes(e.target.id)) {
    for (let i = 0; i < tabCount; i++) {
      if (tabs[i] == e.target.id) {
        document.querySelector('.' + tabs[i] + '-tab').style.visibility = 'visible';
        document.querySelector('.' + tabs[i] + '-tab').style.display = 'block';
    } else {
      document.querySelector('.' + tabs[i] + '-tab').style.visibility = 'hidden';
      document.querySelector('.' + tabs[i] + '-tab').style.display = 'none';
      }
    }
  }
}
