const form = document.querySelector("form[name='mi_form']");
if (form) {
  form.addEventListener("submit", async (event) => {
    // evita que el formulario se envíe de forma predeterminada, recargando la web
    event.preventDefault();

    let respuesta_valida = true;
    if (!validar_archivo()) {
      respuesta_valida = false;
    }

    console.log(respuesta_valida);
    if (respuesta_valida) {
      document.querySelector(".btn_send").setAttribute("disabled", true);
      console.log("entreee");
      // crea un objeto FormData con los datos del formulario
      const formData = new FormData(form);

      /**
       * Como esta llegando un input file vacio, lo que estoy haciendo es eliminarlo de la data y enviar solo
       * los que contienen imagen.
       */
      document.querySelectorAll("input[type=file]").forEach((el) => {
        if (el.files.length === 0) formData.delete(`${el.name}`);
      });

      /**
       * Recorriendo toda la informacion que esta llegando desde el formulario
       */
      /*
      for (const [key, value] of formData.entries()) {
        if (value instanceof File) {
          console.log(`${key}: ${value.name}`);
        } else {
          console.log(`${key}: ${value}`);
        }
      }
      */

      try {
        // envía los datos del formulario al servidor
        const response = await axios.post(
          "/procesar-formulario-album",
          formData
        );

        if (!response.status) {
          console.log(`HTTP error! status: ${response.status} 😭`);
        }
        console.log(response.data);

        // procesa la respuesta del servidor
        if (response.status === 200) {
          if (response.data.status_server == 1) {
            alert(response.data.mensaje);
            window.location.href = "/";
          } else {
            document.querySelector(".btn_send").removeAttribute("disabled");
            alert(response.data.mensaje);
            return;
          }
        } else {
          console.log("Hubo un error en el servidor.");
        }
      } catch (error) {
        console.log("Hubo un error al enviar los datos.");
      }
    }
  });
}

/**
 * Validar si existe archivo (foto) adjunto
 */
const validar_archivo = () => {
  let inputs_file = document.querySelectorAll("#fileInputs input[type='file']");
  // Filtrar los input para excluir aquellos con name="archivo_0"
  let inputs = Array.from(inputs_file).filter((input) => {
    return input.name !== "archivo_0";
  });

  let valido = false; // Suponemos que no hay archivos cargados inicialmente
  for (let i = 0; i < inputs.length; i++) {
    if (inputs.length) {
      // Si se encuentra al menos un archivo cargado, marcamos como válido y salimos del bucle
      valido = true;
      break;
    }
  }
  if (!valido) {
    const div_msj = document.querySelector(".mensaje");
    console.log(div_msj);
    if (div_msj) {
      // Eliminar todos los elementos hijos del div
      while (div_msj.firstChild) {
        div_msj.removeChild(div_msj.firstChild);
      }
      div_msj.style.display = "block";
      div_msj.innerHTML = "Deber cargar mínimo una foto 😭";

      setTimeout(() => {
        div_msj.style.display = "none";
      }, 1000);
    }
  }
  return valido;
};
