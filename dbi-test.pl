#!/usr/bin/perl -w
# DbMailAdministrator (DBMA) V3.2.x Copyright 2004-2016 **
#      Trouble? Contact: micheal@dbma.ca
#################################################################
use strict;
use DBI;
print "DBI drivers:\n";
my @drivers = DBI->available_drivers('quiet');
my $driver;
foreach $driver (@drivers)
{
    print "$driver\n";
}
exit;


