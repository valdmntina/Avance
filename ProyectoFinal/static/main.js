const correo = document.getElementById('id_correo');
const telefono = document.getElementById('id_telefono');

function validarSoloLetras(event) {
    const key = event.key
    const regex = /^[a-zA-ZñÑ\s]*$/;
    if (!regex.test(key)) {
        event.preventDefault();
    }
}

document.getElementById("id_nombre").addEventListener('keydown', validarSoloLetras);
document.getElementById("id_apellido").addEventListener('keydown', validarSoloLetras);


function validarTelefono(event) {
    const key = event.key
    const regex = /^[0-9]*$/;
    const specialKeys = ['Backspace', 'Delete', 'ArrowLeft', 'ArrowRigth', 'Tab', 'Enter'];
    if (!regex.test(key) && !specialKeys.includes(key)) {
        event.preventDefault();
    }
}

document.getElementById("id_telefono").addEventListener('keydown', validarTelefono);        


function validarCorreo(element) {
    element.addEventListener('blur', ()=>{
    const regex = /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/;
    if (!regex.test(element.value)){
        element.style.borderColor = 'salmon';
    } else{
        element.style.borderColor = 'green';
        
    }
    })
  }

function validarCel(element) {
    element.addEventListener('blur', ()=>{
    if (element.value.length < 10){
        element.style.borderColor = 'salmon';
    } else{
        element.style.borderColor = 'green';
        
    }
    })
  }

validarCel(telefono);
validarCorreo(correo);


// const formulario = document.getElementsByClassName('formulario')[0];

// formulario.addEventListener('submit', function(event) {
//     event.preventDefault();

//     const elementosFormulario = document.getElementsByClassName('formulario');
//     for (let i = 0; i < elementosFormulario.length; i++) //oculta los elementos del formulario iterando sobre ellos 

//     alert('¡Formulario enviado exitosamente :D!');
// })