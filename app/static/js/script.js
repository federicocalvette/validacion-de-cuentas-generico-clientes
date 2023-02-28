function send_data() {
  var pais = document.getElementById("codigo_pais").value;
  var cuenta = document.getElementById("numero_cuenta").value;
  var banco = document.getElementById("codigo_banco").value;

  body_request = {
    numero_cuenta: cuenta,
    codigo_banco: banco,
    codigo_pais: pais,
  }
  const options = {
    mode: "cors",
    headers: {
      "Access-Control-Allow-Origin": "*",
    },
    method: "POST",
    body: new URLSearchParams(body_request),
  };
  fetch('/validation/', options)
    .then((response) => response.text())
    .then(function (response) {
      console.log(response);
      if (response.includes('El titular de la cuenta')) {
        swal("", response, "success");
      }
      else {
        swal("", response, "error");
      }
    })
    .catch((err) => console.error(err));
}