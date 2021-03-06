const tabs = ["pitch", "faq", "about"];
const tabCount = 3;

const devTabs = ["devHelp"]
const devTabsCount = 1;

$(document).ready(function () {
  for (let i = 0; i < tabCount; i++) {
    document.querySelector('.' + tabs[i] + '-tab').style.display = 'none';
    document.querySelector('#' + tabs[i]).addEventListener('click', openTab)
  }
  
  for (let j = 0; j < devTabsCount; j++) {
    document.querySelector('.' + devTabs[j] + '-tab').style.display = 'none';
    document.querySelector('#' + devTabs[j]).addEventListener('click', openDevTab);
  }
});

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
