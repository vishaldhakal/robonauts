const menuIcon = document.querySelector(".menu");
const images = document.querySelector("#myimages");
const anim = document.querySelectorAll(".anim");

var prevScrollpos = window.pageYOffset;
window.onscroll = function () {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("navbar").style.top = "0";
  } else {
    document.getElementById("navbar").style.top = "-150px";
  }
  prevScrollpos = currentScrollPos;
};

observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.intersectionRatio > 0) {
      entry.target.style.animation = `fade1 1s linear`;
    } else {
      entry.target.style.animation = `none`;
    }
  });
});

anim.forEach((element) => {
  observer.observe(element);
});

const videoopen = document.querySelector("#videoopen");
const videoclose = document.querySelector("#videoclose");
const video = document.querySelector("#myvidd");
let src = video.children[0].src;

window.addEventListener("load", () => {
  video.children[0].src = "";
});

videoopen.addEventListener("click", () => {
  video.children[0].src = src;
  video.muted = false;
  video.play();
});

videoclose.addEventListener("click", () => {
  console.log("video paused");
  video.children[0].src = "";
  video.pause();
});
