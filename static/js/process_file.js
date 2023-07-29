let arrayImagen = [];
let fileCounter = 1; // Nuevo contador para generar id y name
const maxSizeInBytes = 2 * 1024 * 1024; //Maximo 2 MB
const output = document.querySelector("output");
const mensajeError = document.querySelector(".mensaje");

function createNewFileInput() {
  const fileInputsContainer = document.getElementById("fileInputs");
  const newFileInput = document.createElement("input");
  newFileInput.type = "file";
  newFileInput.name = `archivo_${fileCounter}`; // Usar el contador para el nombre
  newFileInput.accept = "image/*";
  newFileInput.addEventListener("change", function () {
    manejarCambioArchivo(newFileInput);
  });
  fileInputsContainer.appendChild(newFileInput);
  fileCounter++; // Aumentar el contador para el siguiente input
}

function manejarCambioArchivo(fileInput) {
  const file = fileInput.files;
  if (file && file.length > 0) {
    if (!file[0].type.startsWith("image/")) {
      mensajeError.innerText =
        "Por favor, seleccione solo imágenes (JPG o PNG).";
      mensajeError.style.display = "block";
      return;
    }
    if (file[0].size > maxSizeInBytes) {
      mensajeError.innerText =
        "El tamaño máximo permitido para cada imagen es de 2 MB.";
      mensajeError.style.display = "block";
      return;
    }

    /**
     * Valiando si ya existe el archivo, para evitar subirlo de nuevo
     */
    const fileName = file[0].name;
    const isDuplicate = arrayImagen.some((image) => image.name === fileName);
    if (isDuplicate) {
      mensajeError.innerText = "La imagen ya ha sido seleccionada.";
      mensajeError.style.display = "block";
      return;
    }
    arrayImagen.push(file[0]);
    createNewFileInput();
  }

  displayImages();
  recalculateTotalFileSize(); // Recalcular el tamaño total de archivos
}

function displayImages() {
  let images = "";
  arrayImagen.forEach((image) => {
    let nameImg = image.name;
    images += `<div class="image" data-name="${nameImg}">
      <img src="${URL.createObjectURL(
        image
      )}" data-name="${nameImg}" alt="image">
      <span onclick="borrar_imagen('${nameImg}')"><i class="bi bi-x"></i></span>
    </div>`;
  });
  output.innerHTML = images;
}

function borrar_imagen(nombreImagen) {
  // Buscar el índice de la imagen en el array arrayImagen
  const indexToRemove = arrayImagen.findIndex(
    (image) => image.name === nombreImagen
  );

  if (indexToRemove !== -1) {
    // Eliminar imagen del array arrayImagen
    arrayImagen.splice(indexToRemove, 1);

    // Recargar las imágenes en el output
    displayImages();

    // Eliminar el elemento del div "fileInputs"
    const fileInputsContainer = document.getElementById("fileInputs");
    const fileInputToRemove = fileInputsContainer.querySelector(
      `input[name="archivo_${indexToRemove}"][type="file"]`
    );
    if (fileInputToRemove) {
      fileInputToRemove.remove();
    }

    // Actualizar los nombres de los elementos input restantes en "fileInputs"
    const remainingFileInputs =
      fileInputsContainer.querySelectorAll('input[type="file"]');
    fileCounter = 0; // Reiniciar el contador
    remainingFileInputs.forEach((input) => {
      input.name = `archivo_${fileCounter}`;
      fileCounter++; // Aumentar el contador para el siguiente input
    });

    // Recalcular el tamaño total de archivos
    recalculateTotalFileSize();
  }
}

function recalculateTotalFileSize() {
  let btn_send = document.querySelector(".btn_send");
  let totalSize = 0;
  arrayImagen.forEach((image) => {
    totalSize += image.size;
  });
  const maxSizeInMB = maxSizeInBytes / (1024 * 1024);
  const totalSizeInMB = totalSize / (1024 * 1024);
  if (totalSizeInMB > maxSizeInMB) {
    mensajeError.innerText =
      "El tamaño total de las imágenes supera el límite de 2 MB.";
    mensajeError.style.display = "block";
    btn_send.style.backgroundColor = "#c1c1c1";

    btn_send.disabled = true;
  } else {
    mensajeError.style.display = "none";
    btn_send.style.backgroundColor = "";
    btn_send.removeAttribute("disabled");
  }
}

const initialFileInput = document.querySelector('input[type="file"]');
if (initialFileInput) {
  initialFileInput.addEventListener("change", function () {
    manejarCambioArchivo(initialFileInput);
  });
}
