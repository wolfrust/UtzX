if ($^O eq "MSWin32") { #$^O contains the name of the operating system
    system("cls");
} else {
    system("clear");
}

print "\n";

@factors = (); #holds all factors
@prime = (); #holds prime factors
@notprime = (); #holds non-prime factors

print "Number to factorise: ";
$tof = <STDIN>;
chomp $tof;

for $f (1..$tof) { #for every number ($f) between 1 and the number you have to factorise ($tof) (inclusive),
    if ($tof % $f == 0) { #if $f is a factor of $tof,
        push(@factors, $f); #add it to the factors array

        $prime = 1; #initialize the value of prime as 1 (true)
        for $x (2..($f-1)) { # test with every number except 1 & the number itself
          if ($f % $x == 0) { # if it is divisible,
            $prime = 0; # it's not prime, as a prime number is only divisible by 1 & the number itself [0=false]
            last; #break the loop
          }
        }
        if ($prime) {
          push(@prime, $f);
        } else {
          push(@notprime, $f);
        }
    }
}

print "\n----------------------------------------\n";

print "\nFactors (All): ";

print "[";
foreach $factor (@factors) { #for every factor in @factors
    if ($factor != @factors[$#factors]) { #if the factor is not the last factor in @factors,
        print $factor . ", "; #print the factor, a comma & a whitespace,
    } else {
        print $factor; #otherwise, just print the factor
    }
}
print "]\n\n";

print "\nFactors (Prime): ";

print "[";

#following loop is the similar to the one on line 40
foreach $factor (@prime) {
    if ($factor != @prime[$#prime]) {
        print $factor . ", ";
    } else {
        print $factor;
    }
}
print "]\n\n";

print "\nFactors (Not Prime): ";

print "[";

#following loop is the similar to the one on line 40
foreach $factor (@notprime) {
    if ($factor != @notprime[$#notprime]) {
        print $factor . ", ";
    } else {
        print $factor;
    }
}
print "]\n\n";

print "----------------------------------------\n\n";

print "[Exit] ";
<STDIN>;
