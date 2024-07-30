let protocolo = window.location.protocol; // http: o https:
let host = window.location.host; // dominio.com:puerto
let pathname = window.location.pathname; // /ruta/al/recuro/

// Si desearas solo tener el dominio base (sin rutas ni subdirectorios), puedes hacerlo así:
let BASE_URL = `${protocolo}//${host}/`;

if(host === "localhost"){

    let segmentos = pathname.split('/');
    if (segmentos[1]) {
        BASE_URL += segmentos[1];
    }
}
window.BASE_URL = BASE_URL;
