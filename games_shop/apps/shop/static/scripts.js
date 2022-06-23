function change(objName, min, max, step, cont = 0) {
    let obj = document.getElementById(objName);
    let tmp = +obj.value + step;
    if (tmp < min) tmp = min;
    if (tmp > max) tmp = max;
    obj.value = tmp;

    if (cont) {
        updateCart()
    }
}


function msgDecor() {
    let msg = document.getElementById("msg-add")
    msg.style.opacity = 0;
    msg.style.transition = "2s"
    msg.style.visibility = 'hidden'
}


function autoHide() {
    setTimeout(msgDecor, 700);
}

function showFiltersBlock() {
    let filtersBlock = document.getElementById('filters')
    filtersBlock.style.display = filtersBlock.style.display === 'none' ? 'block' : 'none'


}
