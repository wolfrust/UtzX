use Text::SimpleTable::AutoWidth;

$raw = `netsh wlan show profiles`;
@rl = split /\n/, $raw;
@rawprofiles = ();
foreach $line (@rl) {
    if (index($line, "All User Profile") != -1) {
        push(@rawprofiles, $line);
    }
};

@profiles = ();
foreach $rp (@rawprofiles) {
    my ($profile) = $rp =~ /:\s*(.+)$/;
    push(@profiles, $profile);
}

@rauth = ();
@rkeys = ();
foreach $profile (@profiles) {
    $done = 0;
    $ap = 0;
    $exec = `netsh wlan show profiles name="$profile" key=clear`;
    @rp = split /\n/, $exec;
    foreach $line (@rp) {
        if (index($line, "Key Content") != -1) {
            push(@rkeys, $line);
            $done = 1;
        }
        if (index($line, "Authentication") != -1) {
            if ($ap == 0) {
                push(@rauth, $line);
                $ap = 1;
            }
            
        }
    }
    if ($done == 0) {
            push(@rkeys, ": ------")
    }
}

@auth = ();
foreach $ra (@rauth) {
    my ($mech) = $ra =~ /:\s*(.+)$/;
    push(@auth, $mech);
}

@keys = ();
foreach $rk (@rkeys) {
    my ($key) = $rk =~ /:\s*(.+)$/;
    push(@keys, $key);
}

$l = scalar @profiles - 1;

for $i (0..$l) {
    print Text::SimpleTable::AutoWidth
    ->new( max_width => 150, captions => [qw/ SSID Passwd Auth /] )
    ->row( @profiles[$i], @keys[$i], @auth[$i] )
    ->draw();
}

<STDIN>;

