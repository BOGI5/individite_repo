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
    const test_passowrd = document.createTextNode("Test");
    const site_name = document.createElement("p");
    const site_password = document.createElement("p");
    const delete_button = document.createElement("button");
    const copy_button = document.createElement("button");
    const test_button = document.createElement("button");
    delete_button.classList.add('delete_pass');
    delete_button.appendChild(delete_text);
    copy_button.appendChild(copy_text);
    copy_button.classList.add('copy_pass');
    test_button.appendChild(test_passowrd);
    test_button.classList.add('delete_pass');
    test_button.setAttribute("onclick", `test_password('${name_string}')`);
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
    const test = document.getElementById('test');
    level += 75;
    site_password.id = num;
    num += 1;
    site_name.style.top = level;
    site_password.style.top = level;
    delete_button.style.top = level-4;
    copy_button.style.top = level-4;
    test_button.style.top = level;
    test_button.style.left = 1000;
    name.appendChild(site_name);
    password.appendChild(site_password);
    delete_but.appendChild(delete_button);
    copy.appendChild(copy_button);
    test.appendChild(test_button);
}

function copyToClipboard(id){
    let text = document.getElementById(String(id)).innerHTML;
    navigator.clipboard.writeText(text);
}


function delete_password(web){
    location.href = "/delete/?del=" + web;

}

function test_password(web){
    location.href = "/test/?test=" + web;
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

function logout(){
    location.href = "/logout";
}

function set_password(){
    var generated_password = {};
    generated_password.full_length = document.getElementsByClassName("VERY_IMPORTANT2").length;
    generated_password.password = "";

    for(var i = 0; i<generated_password.full_length; i++){
        generated_password.password += document.getElementsByClassName("VERY_IMPORTANT2")[i].innerText;
    }

    navigator.clipboard.writeText(generated_password.password);
    
    location.href = "/passwords"
}


function display_level(){
    var length = document.getElementsByClassName("VERY_IMPORTANT3").length;
    var level = "";
    for(var i = 0; i<length; i++){
        level += document.getElementsByClassName("VERY_IMPORTANT3")[i].innerText;
    }
    
    if(level == "{}" || level == "None"){
        return 0;
    }

    
    var level_object = JSON.parse(level);

    var common_text = "";
    if(level_object.IsCommon === "True"){
        common_text = "Your password is very commonly used";
    }
    else{
        common_text = "Your password is not that commonly used";
    }

    document.getElementsByClassName("notification")[0].style.display = "flex";
    document.getElementById("N_T_1").innerText = "1: Your password is " + level_object.Level;
    document.getElementById("N_T_2").innerText = "2: " + common_text;
}

function notification_button(){
    location.href = "/test/";
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
        document.getElementById('c0').style.display = "none";
        
    }

    display_level();

    call_funcs();

    if(document.title = "Log in (2)"){
        autofill();
    }
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

function gotoHome(){
    location.href = "/";
}
function gotoLogin(){
    location.href = "/login";
}
function gotoSignup(){
    location.href = "/signup";
}

/*function autofill(){
    document.getElementById('Name').value = "test";
    console.log(document.getElementById('Name').value);
    document.getElementById('Password').value = "test";
}*/
