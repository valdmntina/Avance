const correo = document.getElementById('id_correo');
const telefono = document.getElementById('id_telefono');

function validarSoloLetras(event) {
    const key = event.key
    const regex = /^[a-zA-Z\s]*$/;
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

//const key = event.key;

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
//    const regex = /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/;
    if (element.value.length < 10){
        element.style.borderColor = 'salmon';
    } else{
        element.style.borderColor = 'green';
        
    }
    })
  }

validarCel(telefono);
validarCorreo(correo);
    /*    
    if (!regex.test(key)) {
        //event.preventDefault();
        c.value.style.bor
    }
}
*/
//document.getElementById("id_correo").addEventListener('blur', validarCorreo);