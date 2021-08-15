function importData() {
    var file = document.getElementById('input').files[0];
    var reader = new FileReader();
    reader.readAsText(file);
    reader.onload = function(e) {
        var key = reader.result;
        var element = document.getElementById("id_Password")
        var password = element.value;
        var key_256 = aesjs.utils.utf8.toBytes(key)
        var textBytes = aesjs.utils.utf8.toBytes(password);
        var aesCtr = new aesjs.ModeOfOperation.ctr(key_256);
        var encryptedBytes = aesCtr.encrypt(textBytes);
        var encryptedHex = aesjs.utils.hex.fromBytes(encryptedBytes);
        element.value = encryptedHex;   
    };
}
