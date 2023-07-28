const form = document.querySelector("#mi_form");
if (form) {
  form.addEventListener("submit", async (event) => {
    // evita que el formulario se envíe de forma predeterminada, recargando la web
    event.preventDefault();

    document.querySelector("#btn_send_consig").setAttribute("disabled", true);

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

    //console.log(formData);
    for (const [key, value] of formData.entries()) {
      if (value instanceof File) {
        console.log(`${key}: ${value.name}`);
      } else {
        console.log(`${key}: ${value}`);
      }
    }

    try {
      const response = await axios.post("/procesar-formulario", formData); // envía los datos del formulario al servidor

      if (!response.status) {
        console.log(`HTTP error! status: ${response.status} 😭`);
      }

      // procesa la respuesta del servidor
      if (response.status === 200) {
        // console.log(response.data);
        if (response.data.status_server == 1) {
          alert(response.data.mensaje);
        } else {
          document
            .querySelector("#btn_send_consig")
            .removeAttribute("disabled");
          alert(response.data.mensaje);
          return;
        }
      } else {
        console.log("Hubo un error en el servidor.");
      }
    } catch (error) {
      console.log("Hubo un error al enviar los datos.");
    }
  });
}
