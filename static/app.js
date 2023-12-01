

$(document).ready(function() {
    //Muestra la vista previa de la imagen al seleccionar un archivo
    $("#id_image").change(function() {
      readURL(this);
    })
})

function readURL(input) {
    if (input.files && input.files[0]) {
      var reader = new FileReader()

      reader.onload = function (e) {
        $('#previewImage').attr('src', e.target.result).show()
      }

      reader.readAsDataURL(input.files[0])
    }
}