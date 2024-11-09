//////Countdown timer....


/////Countdown Timer....


/////Expired/Deadline Date.....

document.getElementById('btn1').innerHTML='00'
document.getElementById('btn2').innerHTML='00'
document.getElementById('btn3').innerHTML='00'
document.getElementById('btn4').innerHTML='00'
let expdate;
expdate='Jan,3 2025 12:00 AM'

function start(){
    let enddate;
    enddate=new Date(expdate);
    let nowdate;
    nowdate=new Date();
    let diff;
    diff=(enddate-nowdate)/1000;
    let days;
    days=Math.floor(diff/24/60/60);
    let hours;
    hours=Math.floor(diff/60/60) % 24;
    let min;
    min=Math.floor(diff/60) % 60;
    let sec;
    sec=Math.floor(diff % 60)
    document.getElementById('btn1').innerHTML=days+ 'Days'
    document.getElementById('btn2').innerHTML=hours+ 'hr'
    document.getElementById('btn3').innerHTML=min+ 'min'
    document.getElementById('btn4').innerHTML=sec+ 'sec'
   let x=setInterval(function() {
        start()
    }, 1000);
    b.addEventListener('click',function(){
        clearInterval(x)
    })
    r.addEventListener('click',function(){
        start()
    })
}
let p=document.getElementById('hello')
let b;
    b=document.createElement('button');
    b.innerText='Stop!'
    document.getElementById('container1').append(b)
    let r;
    r=document.createElement('button');
    r.innerHTML='Restart!'
    document.getElementById('container1').append(r)
    b.style.borderRadius='100px'
    b.style.fontSize='15px'
    b.style.padding='10px'
    b.style.fontWeight='900'
    r.style.borderRadius='100px'
    r.style.fontSize='15px'
    r.style.padding='10px'
    r.style.fontWeight='900'
    b.style.position='relative'
    b.style.top='183px'
    b.style.left='450px'
    r.style.position='relative'
    r.style.top='183px'
    r.style.left='480px'
    b.style.color='green'
    r.style.color='brown'
    
    