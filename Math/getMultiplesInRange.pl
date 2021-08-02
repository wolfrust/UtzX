if ($^O eq "MSWin32") { #$^O returns MSWin32 on windows & Posix on Linux & Mac
    system("cls");
} else {
    system("clear");
}
print "\n";

print " Number: ";
$num = <STDIN>; #number to get multiples of
chomp $num;

print " Range {x-y}: ";
$range = <STDIN>; #range of multiples
chomp $range;

#get lower limit & upper limit of range input
$lowlim = substr($range, 0, index($range, '-'));
$upplim = substr($range, index($range, '-') + 1);

@multiples = (); #holds multiples in range

for $x (0..$upplim) {
  #we multiply the number by every number between 0 and the upper limit
  #we stop at the upper limit because $num * $upplim is the last possible number in the given range
  push(@multiples, $num * $x) if ($num * $x >= $lowlim and $num * $x <= $upplim); #add it to @multiples if it's in the given range
}

#now we output the multiples

print "\n\n  Multiples of $num in range $range: ";

print "[";
foreach (@multiples) { #for every multiple in the given range,
  print($_); #print the multiple
  if ($_ != @multiples[@multiples - 1]) { #if it's not the last multiple in the array,
    print(", "); #print a comma & a whitespace
  } else { #otherwise,
    print "]"; #print the array closing bracket
  }
}

print "\n\n";
