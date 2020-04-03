var removeCartItems = $(".btn-danger")
for (var i = 0; i < removeCartItems.length; i++) {
    var button = removeCartItems[i]
    button.addEventListener('click', function(){
        console.log('clicked')
    });
}




function init(){
    
}


window.onload = init;