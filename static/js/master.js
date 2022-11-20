const hamburger = document.querySelector('.hamburger');
const mobile_menu = document.querySelector('.mobile-menu')

hamburger.addEventListener('click', function(){
    this.classList.toggle('is-active');
    mobile_menu.classList.toggle('is-open');
})



let intro = document.querySelector('.intro');
let transition_main = document.querySelector('.logo-header'); 
let transition_span = document.querySelectorAll('.trans');

window.addEventListener('DOMContentLoaded', () => {

    setTimeout(() =>{

        transition_span.forEach((span, idx) => {
            setTimeout(() =>{
                span.classList.add('active');
            }, (idx + 1) * 400)
        });

        setTimeout( () => {
            transition_span.forEach( (span,idx) =>{
                setTimeout(() =>{
                    span.classList.remove('active');
                    span.classList.add('fade');
                }, (idx + 1) * 50)
            })
        }, 2000);

        setTimeout(() =>{
            intro.style.top = '-100vh';
        }, 2300)
    })
})