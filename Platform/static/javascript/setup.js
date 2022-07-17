const tabs = ["avatar", "general", "gaming", "premium"];
const tabCount = 4;

var activeTab = 0;

const errorText = document.querySelector("#setupError")

let favGame = "";
let secFavGame = "";
let thirdFavGame = "";

const gameOptions = [ 
  { image: "Minecraft.png", name: "Minecraft", font: "MC", alt: "Both Java & Bedrock", value: "Minecraft" },
  { image: "LoL.png", name: "League of Lengends", font: "", alt: "<i>'House, always wins.'</i>", value: "LoL" },
  { image: "GTAV.jpg", name: "Grand Theft Auto V", font: "", alt: "OH SHI- Its an oppressor!", value: "GTA V" },
  { image: "Valorant.png", name: "Valorant", font: "", alt: "vAnGUarD nOt InItiaLiZeD", value: "Valorant" },
  { image: "CSGO.png", name: "CS : GO", font: "", alt: "Defusing without hands since 1999", value: "CSGO" },
  { image: "Apex.png", name: "Apex Legends", font: "", alt: "When I ping the Mozambique as a joke<br>but they pick it up: <b>NANI?!?</b>", value: "Apex" },
  { image: "Dota2.jpg", name: "Dota 2", font: "", alt: "<i>Looks at LoL</i> ... Uncultured b*stards", value: "Dota" },
  { image: "Fortnite.png", name: "Fortnite", font: "", alt: "STOP CRANKING 90S PLEEASE", value: "Fortnite" },
  { image: "FallGuys.png", name: "Fall Guys", font: "", alt: "Me when someone grabs me in Roll Out:<br><b>You are dead to me</b>", value: "Fall Guys" },
  { image: "TFT.jpg", name: "Teamfight Tactics", font: "", alt: "<b>Expectations:</b> Strategy & 200iq moves<br><b>Reality:</b> Roulette", value: "Teamfight Tactics" },
  { image: "Rust.jpg", name: "Rust", font: "", alt: "Get offline raided nerd >:)", value: "Rust" },
  { image: "DBD.png", name: "Dead by Daylight", font: "", alt: "Huh, I can't honestly think of a good meme here :/", value: "Dead by Daylight" },
  { image: "Fifa.png", name: "Fifa", font: "", alt: "Pumping out clones since the 90s", value: "Fifa" },
  { image: "WoW.jpg", name: "World of Warcraft", font: "", alt: "<b>Blizzard:</b> The best I can do for<br>you is more elf skins :/", value: "WoW" },
  { image: "Dayz.jpg", name: "DAYZ", font: "", alt: "When your walking through the woods and<br>the bush starts moving: 😮", value: "DAYZ" },
  { image: "Hearthstone.png", name: "Hearthstone", font: "", alt: "<b>Opponent:</b><i>Heals</i><br><b>Agro Players:</b> NOooooooo", value: "Hearthstone" },
  { image: "Raft.png", name: "Raft", font: "", alt: "Shark go chomp", value: "Raft" },
  { image: "RocketLeague.jpg", name: "Rocket League", font: "", alt: "Too .. much .. terminology", value: "Rocket League" },
  { image: "PUBG.jpeg", name: "PUBG", font: "", alt: "Just hit them with a pan", value: "PUBG" },
  { image: "WoT.png", name: "World of Tanks", font: "", alt: "Load in, run in with light, die, repeat", value: "World of Tanks" },
  { image: "Overwatch.png", name: "Overwatch", font: "", alt: "Providing unbalanced heroes since 2016", value: "Overwatch" },
  { image: "Amongus.jpg", name: "Among Us", font: "", alt: "<i>Red is sus</i>", value: "Among Us" },
  { image: "RDD.png", name: "Red Dead Redemption", font: "", alt: "Rootin Tootin Cowboy Shooting", value: "Red Dead Redemption" },
  //{ image: "", name: "", font: "", alt: "", value: "" },
];

$(document).ready(function () {
  for (let i = 0; i < tabCount; i++) {
    document.querySelector('.' + tabs[i] + '-tab').style.display = 'none';
    try { document.querySelector('#' + tabs[i]).addEventListener('click', openTab) } catch {}
  }
  
  document.querySelector('.' + tabs[0] + '-tab').style.display = '';

  $.ajax({
    url : '/actions/preview-avatar',
    data : $('#ppForm').serialize(),
    success : function (r) {
      if (r.response == true) {
        document.querySelector(".avatarImg").src = 'data:image/png;base64,' + r.image;
      }
    },
    method : 'POST',
  });

  document.querySelectorAll(".game-dd .options ul").forEach(function(element) {
    for (let i = 0; i < gameOptions.length; i++) {
      element.insertAdjacentHTML("beforeend", `
                  <li><a href="#" class="animate fadeIn" style="display: grid; grid-template-columns: min-content auto; grid-column-gap: 0.7rem;">
                  <img src="static/images/Games/` + gameOptions[i].image + `" style="margin-top: auto; margin-bottom: auto; width: auto; height: 3rem; border-radius: 0.25rem;">
                    <div>
                      <h4 style="margin: 0;">` + gameOptions[i].name + `</h4>
                      <p style="color: var(--color-gray); font-size: 0.8rem;">` + gameOptions[i].alt + `</p>
                    </div>
                    
                    <span class="value">` + gameOptions[i].value + `</span>
                  </a></li>
      `);
    }
  });

  $('.drop-down').each(function() {
    var dd = $(this);
  
    dd.find(".selected a").click(function() {
      dd.find(".options ul").toggle();
    });
  
    dd.find(".options ul li a").click(function() {
      var text = $(this).find(".value").html();

      if (dd.hasClass("game1")) { favGame = text; }
      if (dd.hasClass("game2")) { secFavGame = text; }
      if (dd.hasClass("game3")) { thirdFavGame = text; }

      dd.find(".selected a span").html(text);
      dd.find(".options ul").hide();
    });
  });

  errorText.innerHTML = "";
  errorText.style.display = "none";
});

$("select[form='ppForm']").change(function(){
  $.ajax({
    url : '/actions/preview-avatar',
    data : $('#ppForm').serialize(),
    success : function (r) {
      if (r.response == true) {
        document.querySelector(".avatarImg").src = 'data:image/png;base64,' + r.image;
      }
    },
    method : 'POST',
  });
});

function submitAvatar() {
  $.ajax({
    url : '/actions/submit-avatar',
    data : $('#ppForm').serialize(),
    success : function (r) {
      if (r.response == true) {
        rawOpenTab(1);
      }
    },
    method : 'POST',
  });

  return false;
}

function checkGeneral() {
  if ($('.general-tab input').filter(function() { return !this.value; }).length > 0) { 
    errorText.style.display = '';
    errorText.innerHTML = "You left some inputs empty, we can't have that here :/"; 
  }
  else {
    rawOpenTab(2);
    errorText.style.display = 'none';
  }
}

function submitSetup() {
  $.ajax({
    url : '/actions/finish-setup',
    data : {
      "csrfmiddlewaretoken": csrfToken,
      "first_name" : $("input[name='first_name']").val(),
      "last_name" : $("input[name='last_name']").val(),
      "sex" : $("select[name='sex']").val(),
      "preference" : $("select[name='preference']").val(),
      "bio" : $("textarea[name='bio']").val(),
      "age" : $("input[name='age'").val(),
      "birth_date" : $("input[name='birth_date']").val(),
      "fav_game_1" : favGame,
      "fav_game_2" : secFavGame,
      "fav_game_3" : thirdFavGame
    },
    success : function (r) {
      if (r.response == true) {
        window.location.replace("/");
      }
    },
    method : 'POST',
  });
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

function rawOpenTab(e) {
  for (let i = 0; i < tabCount; i++) {
    if (i == e) {
      document.querySelector('.' + tabs[i] + '-tab').style.display = '';
  } else {
    document.querySelector('.' + tabs[i] + '-tab').style.display = 'none';
    }
  }
}

//HIDE OPTIONS IF CLICKED ANYWHERE ELSE ON PAGE
$(document).bind('click', function(e) {
  var $clicked = $(e.target);
  if (! $clicked.parents().hasClass("drop-down"))
      $(".drop-down .options ul").hide();
});