var menu=1;
function Menu(){
    if(menu==0) {
        document.getElementById("MainMenu").style.display="block";
        menu=1;
    } else {
        document.getElementById("MainMenu").style.display="none";
        menu=0;
    }
}