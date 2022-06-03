const tabs = ["pitch", "devlog", "faq", "about"];
const tabCount = 4;

const devTabs = ["devHelp", "release0", "patch0-1"]
const devTabsCount = 3;

window.onload = function startup() {
  for (let i = 0; i < tabCount; i++) {
    document.querySelector('.' + tabs[i] + '-tab').style.display = 'none';
    document.querySelector('#' + tabs[i]).addEventListener('click', openTab)
  }
  
  for (let j = 0; j < devTabsCount; j++) {
    document.querySelector('.' + devTabs[j] + '-tab').style.display = 'none';
    document.querySelector('#' + devTabs[j]).addEventListener('click', openDevTab);
  }
}

const openTab = (e) => {
  if (tabs.includes(e.target.id)) {
    for (let i = 0; i < tabCount; i++) {
      if (tabs[i] == e.target.id) {
        document.querySelector('.' + tabs[i] + '-tab').style.display = '';
    } else {
      document.querySelector('.' + tabs[i] + '-tab').style.display = 'none';
      }
    }
  }
}

const openDevTab = (e) => {
  if (devTabs.includes(e.target.id)) {
    for (let i = 0; i < devTabsCount; i++) {
      if (devTabs[i] == e.target.id) {
        document.querySelector('.' + devTabs[i] + '-tab').style.display = '';
      } else {
        document.querySelector('.' + devTabs[i] + '-tab').style.display = 'none';
      }
    }
  }
}
