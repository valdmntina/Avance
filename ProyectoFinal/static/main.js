const correo = document.getElementById('id_correo');
const telefono = document.getElementById('id_telefono'); 

//con estas validacion lo que se logra es que el nombre y apellido que se ingresen en el formulario no se le permitan ingresar numeros 
function validarSoloLetras(event) {
    const key = event.key
    const regex = /^[a-zA-ZñÑ\s]*$/;
    if (!regex.test(key)) {
        event.preventDefault();
    }
}

document.getElementById("id_nombre").addEventListener('keydown', validarSoloLetras);
document.getElementById("id_apellido").addEventListener('keydown', validarSoloLetras);


//con esta validacion lo que se logra es que el numero de telefono que se ingresa no se puedan ingresar letras, se pueda eliminar y modificar y en que caso de que se ingresen valores 
//menores a 10 se vea color rojo y si esta correcto muetssre verde
function validarTelefono(event) {
    const key = event.key
    const regex = /^[0-9]*$/;
    const specialKeys = ['Backspace', 'Delete', 'ArrowLeft', 'ArrowRigth', 'Tab', 'Enter'];
    if (!regex.test(key) && !specialKeys.includes(key)) {
        event.preventDefault();
    }
}

document.getElementById("id_telefono").addEventListener('keydown', validarTelefono);        


//con esta validacion lo que se logra es que el correo ingresado sea valido y se muestre de color verde y que en caso de no se muestre color salmon
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

//con esta validacion al momento de enviar el formulario muestra un alert que indica que se envio y refresca el formulario
const formulario = document.getElementsByClassName('formulario')[0];

formulario.addEventListener('submit', function(event) {
    

    const elementosFormulario = document.getElementsByClassName('formulario');
    for (let i = 0; i < elementosFormulario.length; i++) //oculta los elementos del formulario iterando sobre ellos 

    alert('¡Formulario enviado exitosamente :D!');
})