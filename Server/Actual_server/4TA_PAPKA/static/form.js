// var passwords = JSON.parse("{{ passwords|safe }}");
// console.log(JSON.parse('{{ passwords }}'));
// console.log(passwords);

// var passwords = '{{ new_json|safe }}';
// console.log(passwords);

// wait until in paragraph will be written and get it
var passwords = "";
function call_me() {
const length = document.getElementsByClassName('VERY_IMPORTANT');

if (length.length === 0) {
    return 0;
}

for(i=0; i < length.length; i++){
    passwords += document.getElementsByClassName('VERY_IMPORTANT')[i].innerText;
    document.getElementsByClassName('VERY_IMPORTANT')[i].style.display = "none";
}
var eligibleForRed=true;

passwords = passwords.replace(/'/g, '"');
passwords = JSON.parse(passwords);
return 1;
//console.log(passwords);
}

// passwords.password - parola  &&  passwords.website - site-url
// Sled dobavqne na parola trqbva da se refreshne za da se vidi json-a
//Za sega butona add q izpolzva
// molqqq te opravi izpisvaneto na json-a po mestata si



function formValidate(){
    let error = 0;
    let formReq = document.querySelectorAll('._req');
    for (let index=0; index<formReq.length; index++){
        const input = formReq[index];
        formRemoveError(input);
        if(input.value === ''){
            formAddError(input);
            error++;
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

function fullReset(){
    let formReq = document.querySelectorAll('._req');
    for (let index=0; index<formReq.length; index++){
        const input = formReq[index];
        formRemoveError(input);
    }
    document.getElementById('video').style.display ="block";
    document.getElementById('takenpic').style.display="none";
    document.getElementById('Name').value = "";
    document.getElementById('Password').value = "";
    document.getElementById('takePhoto').style.display="block";
    document.getElementById('submit').style.display="none";
    document.getElementById('Name').readOnly = false;
    document.getElementById('Password').readOnly = false;
    document.getElementById('site_url').classList.remove('_error');
    document.getElementById('site_pass').classList.remove('_error');
}



function add_password() {
    document.getElementById('add_pass').style.display = "none";
    document.getElementById('site_url').style.display = "block";
    document.getElementById('site_pass').style.display = "block";
    document.getElementById('save_sinfo').style.display = "block";
    document.getElementById('cancel_pass').style.display = "block";
    document.getElementById('site_url').classList.remove('_error');
    document.getElementById('site_pass').classList.remove('_error');
}

var level = 4;
var num = 0;


function read_passwords(){
    for(var i = 0; i<passwords.length; i++){
        add_after(passwords[i].website, passwords[i].password)
    }
}


var flag = 0;

function add_after(name_string, password_string){
    /*'name', 'password', 'site_name', 'site_password'*/
    const site_name_text = document.createTextNode(name_string);
    const site_password_text = document.createTextNode(password_string);
    const delete_text = document.createTextNode("Delete");
    const copy_text = document.createTextNode("Copy");
    const site_name = document.createElement("p");
    const site_password = document.createElement("p");
    const delete_button = document.createElement("button");
    const copy_button = document.createElement("button");
    delete_button.classList.add('delete_pass');
    delete_button.appendChild(delete_text);
    copy_button.appendChild(copy_text);
    copy_button.classList.add('copy_pass');
    copy_button.setAttribute("onclick", `copyToClipboard(${num})`);
    delete_button.setAttribute("onclick", `delete_password('${name_string}')`);
    site_name.classList.add('site_name');
    site_name.appendChild(site_name_text);
    site_password.classList.add('site_password');
    site_password.appendChild(site_password_text);
    const name = document.getElementById('name');
    const password = document.getElementById('password');
    const delete_but = document.getElementById('delete');
    const copy = document.getElementById('copy');
    level += 75;
    site_password.id = num;
    delete_button.id = "d"+String(num);
    copy_button.id = "c"+String(num);
    num += 1;
    site_name.style.top = level;
    site_password.style.top = level;
    delete_button.style.top = level;
    copy_button.style.top = level;
    name.appendChild(site_name);
    password.appendChild(site_password);
    delete_but.appendChild(delete_button);
    copy.appendChild(copy_button);
}

function copyToClipboard(id){
    let text = document.getElementById(String(id)).innerHTML;
    navigator.clipboard.writeText(text);
}


function delete_password(web){
    location.href = "/delete/?del=" + web;

}


function cancel_password(){
    document.getElementById('add_pass').style.display = "block";
    document.getElementById('site_url').style.display = "none";
    document.getElementById('site_pass').style.display = "none";
    document.getElementById('save_sinfo').style.display = "none";
    document.getElementById('cancel_pass').style.display = "none";
}

var dataURL;

function takephoto(){
    if(formValidate() === 0)
    {
        var canvas = document.getElementById('takenpic');
        const context=canvas.getContext('2d');
        context.drawImage(video , 0, 0, 250, 150);

        var highres = document.getElementById('highres');
        const context2=highres.getContext('2d');
        context2.drawImage(video , 0, 0, 400, 300);

        dataURL = highres.toDataURL();
        console.log(dataURL);

        console.log(video.videoWidth)
        document.getElementById('video').style.display="none";
        document.getElementById('takenpic').style.display="block";
        document.getElementById('takePhoto').style.display="none";
        document.getElementById('submit').style.display="block";
        document.getElementById('Name').readOnly = true;
        document.getElementById('Password').readOnly = true;

        document.getElementById("dataURLfield").value = dataURL;
    }

}


function call_funcs(){
    if(call_me() === 1){
        read_passwords();
    }
}


window.addEventListener('load', function () {
    
    if(document.getElementById('Name') != null){
        document.getElementById('Name').addEventListener('keypress', function (e) {
            if (e.key === 'Enter') {
                e.preventDefault();
            }
        }, false);
    }
    
    if(document.getElementById('Password') != null){
        document.getElementById('Password').addEventListener('keypress', function (e) {
            if (e.key === 'Enter') {
                e.preventDefault();
            }
        }, false);
    }

    if(document.getElementById('site_url') != null){
        document.getElementById('delete').style.display = "none";
        document.getElementById('copy').style.display = "none";
    }

    call_funcs();
});



//for better validation
/*document.addEventListener("DOMContentLoaded", function() {
    var elements = document.getElementsByTagName("INPUT");
    for (var i = 0; i < elements.length; i++) {
        elements[i].oninvalid = function(e) {
            e.target.setCustomValidity("");
            if (!e.target.validity.valid) {
                //e.target.setCustomValidity("abv");
            }
        };
        elements[i].oninput = function(e) {
            e.target.setCustomValidity("");
        };
    }
  })*/

//for better validation 2
document.addEventListener('invalid', (function(){
    return function(e) {
      //prevent the browser from showing default error bubble / hint
      e.preventDefault();

    //red border for invalid fields
       // if(eligibleForRed)
            e.target.classList.add('_error');

      // optionally fire off some custom validation handler
      // myValidation();
    };
})(), true);
