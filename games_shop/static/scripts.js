function change(objName, min, max, step, cont=0) {
    let obj = document.getElementById(objName);
    let tmp = +obj.value + step;
    if (tmp < min) tmp = min;
    if (tmp > max) tmp = max;
    obj.value = tmp;

    if(cont){
        updateCart()
    }
}


function updateCart() {
    let btn = document.getElementById('update-button');
    btn.style.visibility= 'visible';
}
