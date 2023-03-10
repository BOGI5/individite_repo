function formCheck(){
    let error = formValidate();

    if(error===0){
        document.getElementById('alert').style.display="none";
        document.getElementById('Form').style.height="12cm";
        document.getElementById('check').style.display="none";
        document.getElementById('reset').style.display="none";
        document.getElementById('submit').style.display="block";
        document.getElementById('Name').style.display="none";
        document.getElementById('send').style.display="block";
    } else {
        document.getElementById('alert').style.display="block";
        document.getElementById('Form').style.height="13cm";
        document.getElementById('check').style.top="76.5%";
    }
}

function formValidate(){
    let error = 0;
    let formReq = document.querySelectorAll('._req');
    for (let index=0; index<formReq.length; index++){
        const input = formReq[index];
        formRemoveError(input);
        if(input.classList.contains('_email')){
            if(emailTest(input)){
                formAddError(input);
                error++;
            } 
        } else {
            if(input.value === ''){
                formAddError(input);
                error++;
            }
        }
    }
    return error;
}
function formAddError(input){
    input.parentElement.classList.add('_error');
    input.classList.add('_error');
}
function formRemoveError(input){
    input.parentElement.classList.remove('_error');
    input.classList.remove('_error');
}
function emailTest(input){
    return !/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,8})+$/.test(input.value);
};

function fullReset(){
    let formReq = document.querySelectorAll('._req');
    for (let index=0; index<formReq.length; index++){
        const input = formReq[index];
        formRemoveError(input);
    }
    /*document.getElementById('alert').style.display="none";*/
    document.getElementById('Form').style.height="3cm";
    //document.getElementById('check').style.top="72%";
    document.getElementById('video').style.display ="block";
    document.getElementById('takenpic').style.display="none";
}

function Form(){
    document.getElementById('Food').style.display="none";
    document.getElementById('Next').style.display="none";
    document.getElementById('Form').style.display="block";
    document.getElementById('check').style.display="block"; 
    document.getElementById('Copyright').style.top="16.5cm";
}


function empty() {

}

function takephoto(){
    var canvas = document.getElementById('takenpic');
    const context=canvas.getContext('2d');
    context.drawImage(video , 0, 0, 250, 150);
    document.getElementById('video').style.display="none";
    document.getElementById('takenpic').style.display="block";
}
