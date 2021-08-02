var instr = prompt("What do I encrypt?");
var shift = prompt("Shift?");
var alphabet = "abcdefghijklmnopqrstuvwxyz";

shift = parseInt(shift)
instr = instr.toLowerCase()

/* var tempArray = []
var f=0
var g=0

while (f<=instr.length) {
	if (instr.charAt(f) == alphabet.charAt(g)) {
		tempArray.push(instr.charAt(f))
	}
	f++
}
*/

var outArray = []

var i=0
var w=0


while (w<=instr.length) {
	for (i=0; i<alphabet.length; i++) {
		if (instr.charAt(w) == alphabet.charAt(i)) {
			if (i + shift > 25) {
				outArray.push(alphabet.charAt(0 + (i + shift - 26)))
			} else {
				outArray.push(alphabet.charAt(i + shift))
			}
		}
	}
	w++
}

var outstr = ""
var z=0

while (z<outArray.length) {
	outstr = outstr + outArray[z]
	z++
}


console.log(outArray);
console.log(outstr)





 /* i + shift > 26, you need to push alphabet.charAt(0 + (i+shift - 26)) 
 But, right now what's happening is, */