const menuIcon = document.querySelector('.menu');
const images = document.querySelector('#myimages')
const anim = document.querySelectorAll('.anim');

observer = new IntersectionObserver((entries)=>{
    entries.forEach(entry => {
        if(entry.intersectionRatio > 0){
            entry.target.style.animation = `fade1 1s linear`;
        }else{
            entry.target.style.animation = `none`;
        }
    });
})

anim.forEach(element => {
    observer.observe(element);
});


/* var myModal = new bootstrap.Modal(document.getElementById('myModal'), {
    keyboard: false
}) */

/* if (window.matchMedia('(display-mode: standalone)').matches) {
        console.log('Running in standalone');
      }else{
        myModal.show();
        setTimeout(() => {
            myfunc();
        }, 9000);
      } */
/* function myfunc(){
    myModal.hide();
} */