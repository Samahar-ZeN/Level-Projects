/////click on the start button..........



//function start(){
    let n=new Promise(function(resolve,reject){
        setTimeout(function(){
            resolve('')}, 4000);
    })
    async function start(){
        await n;
        console.log(n)
    let a;
    a=document.createElement('p').innerHTML='1) Where was the first example of paper money used?'
    let b;
    b=document.createElement('button')
    b.innerText='China'
    let c;
    c=document.createElement('button')
    c.innerHTML='Turkiye'
    let d;
    d=document.createElement('button')
    d.innerHTML='Greece'
    document.getElementById('text1').append(a)
    document.getElementById('container2').append(b)
    document.getElementById('container2').append(c,d)
    c.style.color='blue'
    d.style.color='blue'
    b.style.color='blue'
    c.style.fontSize='15px'
    d.style.fontSize='15px'
    b.style.fontSize='15px'
    b.addEventListener('click',function(){
        document.getElementById('text1').remove()
        document.getElementById('container2').remove()
        document.getElementById('text').remove()
        document.getElementById('btn').remove()
        document.getElementById('image').remove()
        let e;
        e=document.createElement('p').innerHTML='2) Who is generally considered the inventor of the motor car?'
        document.getElementById('text2').append(e)
        let f;
        f=document.createElement('button')
        f.innerText='Henry Ford'
        let g;
        g=document.createElement('button')
        g.innerHTML='Karl Benz'
        let h;
        h=document.createElement('button')
        h.innerHTML='Henry M. Leland'
        document.getElementById('container4').append(f,g,h)
        f.style.color='blue'
        g.style.color='blue'
        h.style.color='blue'
        f.style.fontSize='15px'
        g.style.fontSize='15px'
        h.style.fontSize='15px'
        g.addEventListener('click',function(){
        document.getElementById('text2').remove()
        document.getElementById('container4').remove()
        let i;
        i=document.createElement('p').innerHTML='9) What number was the Apollo mission that successfully put a man on the moon for the first time in human history? '
        document.getElementById('text3').append(i)
        let j;
        j=document.createElement('button')
        j.innerText='Apollo 11'
        let k;
        k=document.createElement('button')
        k.innerHTML='Apollo 12'
        let l;
        l=document.createElement('button')
        l.innerHTML='Apollo 13'
        document.getElementById('container6').append(j)
        document.getElementById('container6').append(k)
        document.getElementById('container6').append(l)
        k.style.color='blue'
        l.style.color='blue'
        j.style.color='blue'
        k.style.fontSize='15px'
        l.style.fontSize='15px'
        j.style.fontSize='15px'
        j.addEventListener('click',function(){
            document.getElementById('text3').remove()
            document.getElementById('container6').remove()
            let m;
            m=document.createElement('p').innerHTML='4) Which of the following languages has the longest alphabet?'
            document.getElementById('text4').append(m)
        let n;
        n=document.createElement('button')
        n.innerText='Greek'
        let o;
        o=document.createElement('button')
        o.innerHTML='Russian'
        let p;
        p=document.createElement('button')
        p.innerHTML='Arabic'
        document.getElementById('container8').append(n)
        document.getElementById('container8').append(o,p)
        o.style.color='blue'
        p.style.color='blue'
        n.style.color='blue'
        o.style.fontSize='15px'
        p.style.fontSize='15px'
        n.style.fontSize='15px'
        o.addEventListener('click',function(){
            document.getElementById('text4').remove()
            document.getElementById('container8').remove()
            let q;
            q=document.createElement('p').innerHTML='5) Which horoscope sign is a fish?'
            document.getElementById('text5').append(q)
            let r;
        r=document.createElement('button')
        r.innerHTML='Aquarius'
        let s;
        s=document.createElement('button')
        s.innerHTML='Cancer'
        let t;
        t=document.createElement('button')
        t.innerText='Pisces'
        document.getElementById('container10').append(r)
        document.getElementById('container10').append(s,t)
        r.style.color='blue'
        s.style.color='blue'
        t.style.color='blue'
        r.style.fontSize='15px'
        s.style.fontSize='15px'
        t.style.fontSize='15px'
        t.addEventListener('click',function(){
            document.getElementById('text5').remove()
            document.getElementById('container10').remove()
            let u;
            u=document.createElement('p').innerHTML='Excellent Job!!'
            document.getElementById('text6').append(u)
            let image;
            image=document.createElement('img');
            image.setAttribute("src" , "https://purepng.com/public/uploads/thumbnail//purepng.com-mickey-mousemickey-mousemickeymouseanimal-cartooncharacterwalt-disneyub-iwerksstudioslarge-yellow-shoered-shortswhite-glovesnetflix-1701528649837nczlu.png")
            document.getElementById('greet').append(image)
            image.style.height='270px'
            image.style.width='230px'
        })
        })
         })
     })
    })
}

