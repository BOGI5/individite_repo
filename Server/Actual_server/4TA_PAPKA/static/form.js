// var passwords = JSON.parse("{{ passwords|safe }}");
// console.log(JSON.parse('{{ passwords }}'));
// console.log(passwords);

// var passwords = '{{ new_json|safe }}';
// console.log(passwords);

// wait until in paragraph will be written and get it
var passwords = "";
function call_me() {
const length = document.getElementsByClassName('VERY_IMPORTANT');


for(i=0; i < length.length; i++){
    passwords += document.getElementsByClassName('VERY_IMPORTANT')[i].innerText;
    document.getElementsByClassName('VERY_IMPORTANT')[i].style.display = "none";
}


passwords = passwords.replace(/'/g, '"');
console.log(passwords);
passwords = JSON.parse(passwords);

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
}



function add_password() {
    document.getElementById('add_pass').style.display = "none";
    document.getElementById('site_url').style.display = "block";
    document.getElementById('site_pass').style.display = "block";
    document.getElementById('save_sinfo').style.display = "block";
    document.getElementById('cancel_pass').style.display = "block";
}

function copyToClipboard() {
    let text = document.getElementById('site_password').innerHTML;
    const copyContent = async () => {
    try {
      await navigator.clipboard.writeText(text);
      console.log('Content copied to clipboard');
    } catch (err) {
      console.error('Failed to copy: ', err);
    }

}
}

var level = 4;
var num = 0;
var flag = 0;


function read_passwords(){
    if(flag > 0){
        add_after(passwords.website, passwords.password);
    }
    flag += 1;
}


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
    copy_button.classList.add('copy_pass');
    copy_button.appendChild(copy_text);
    site_name.classList.add('site_name');
    site_name.appendChild(site_name_text);
    site_password.classList.add('site_password');
    site_password.appendChild(site_password_text);
    const name = document.getElementById('name');
    const password = document.getElementById('password');
    const delete_but = document.getElementById('delete');
    const copy = document.getElementById('copy');
    level += 75;
    site_name.id = num;
    site_password.id = num;
    delete_button.id = num;
    copy_button.id = num;
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


function delete_password(id){
    const element = document.getElementById(id);
    element.parentNode.removeChild(element);
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


window.addEventListener('load', function () {
    document.getElementById('Name').addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
            e.preventDefault();
        }
    }, false);
    
    document.getElementById('Password').addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
            e.preventDefault();
        }
    }, false);
});



