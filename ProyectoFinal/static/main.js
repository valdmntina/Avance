
const nombre = document.getElementById('id_nombre')
const apellido = document.getElementById('id_apellido')
const telefono = document.getElementById('id_telefono')
const correo = document.getElementById('id_correo')

let n_nombre = /^[a-zA-Z]+(?: [a-zA-Z]+){0,19}$/;
let t_telefono = /^[0-9]{10}$/;
let c_correo = /^(([^<>()\[\]\\.,;:\s@”]+(\.[^<>()\[\]\\.,;:\s@”]+)*)|(“.+”))@((\[[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}])|(([a-zA-Z\-0–9]+\.)+[a-zA-Z]{2,}))$/;

const validarLetras = function(campo) {
    if (n_nombre.test(campo.value)) {
        return true;
    } else {
        return false;
    }
}

const validarTelefono = function (campo) {
    if (t_telefono.test(telefono.value)) {
        return true;
    } else {
        return false;
}
}