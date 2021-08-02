if ($^O eq "MSWin32") { #$^O returns MSWin32 on windows & Posix on Linux & Mac
    system("cls");
} else {
    system("clear");
}

print "\n";
print "Start index: "; #inclusive
$start = <STDIN>;
chomp $start;

print "End index: "; #inclusive
$end = <STDIN>;
chomp $end;

@even = ();
@odd = ();

for $num ($start..$end) { #for every number between the start and end index (inclusive)
  if ($num % 2 == 0) { #check if it's even
    push(@even, $num);
  } else {
    push(@odd, $num);
  }
}

print "\n-----------------------------------\n";
print "\nOdd: [";

foreach (@odd) { #for every number in @odd
  print($_); #print that number
  if ($_ != @odd[@odd - 1]) { #unless it's the last number in the array,
    print(", "); #print a comma and whitespace
  }
}

print "]\n\n";

print "Even: [";

#now we do the same thing we did with @odd, this time with @even
foreach (@even) {
  print($_);
  if ($_ != @even[@even - 1]) {
    print(", ");
  }
}

print "]\n";
print "\n-----------------------------------\n\n";

print "[Exit] ";
<STDIN>; #if not run from terminal, sure it doesn't exit abruptly
print "\n"; #so it looks nice in the terminal
