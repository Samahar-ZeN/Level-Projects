/////qr code generator....

/////qr code generator...

/////qr code generator.......


function clk(){
    image.setAttribute('src','https://api.qrserver.com/v1/create-qr-code/?size=150x150&data='+input.value)
    document.getElementById('container2').append(image)
}
let image;
image=document.createElement('img');
let input;
input=document.getElementById('give');