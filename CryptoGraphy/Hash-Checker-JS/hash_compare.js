var origHash = "";
var dervHash = "";
function getHash() {
    origHash = prompt("Enter the hash given at the download link: ");
    dervHash = prompt("Enter the hash you got: ");
    origHash = origHash.toLowerCase();
    dervHash = dervHash.toLowerCase();
}
var origArray = [];
var dervArray = [];
function removeSpace() {
    for (i=0; i<origHash.length; i++) {
        if (origHash.charAt(i) != " ") {
            origArray.push(origHash.charAt(i));
        }
    }
    for (i=0; i<dervHash.length; i++) {
        if (dervHash.charAt(i) != " ") {
            dervArray.push(dervHash.charAt(i));
        }
    }
}
getHash();
removeSpace();
while (origArray.length != dervArray.length) {
    alert("Quit the crap and gimme the real hashes!");
    origArray = []; // Reset the value
    dervArray = []; // Reset the value
    getHash();
    removeSpace();
}
var checkArray = [];
for (i=0; i<origArray.length; i++) {
    origVar = origArray[i];
    dervVar = dervArray[i];
    if (origVar != dervVar) {
        checkArray.push(1);
    } else {
        checkArray.push(0);
    }
}
var output = "";
for (i=0; i<checkArray.length; i++) {
    if (checkArray[i] == 1) {
        output = "Hash INVALID!";
    } 
}
if (output != "Hash INVALID!") {
    output = "Hash VALID";
}
alert(output);