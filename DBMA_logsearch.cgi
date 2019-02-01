#!/usr/bin/perl --
use strict;
use Carp;
# DbMailAdministrator (DBMA) V3.2.x Copyright 2004-2016 **
#      Trouble? Contact: micheal@dbma.ca
#################################################################
# Copyright 2004-2008 & supported by M. J. [Mike] O'Brien in Canada
#  Updates: http://www.dbma.ca/
#  Contact: http://library.mobrien.com/e-me.htm
print "Content-type: text/html\n\n";
my $method = $ENV{'REQUEST_METHOD'};
my $server = $ENV{'SERVER_NAME'};
my $date   = "" . scalar localtime(time) . "";
my ($output, $execute, $value, $pair, $buffer, $FORM, $name, %FORM, @pairs);
unless ($method eq 'POST')
{
    my $keyword = $ENV{'QUERY_STRING'};
}
read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
@pairs = split(/&/, $buffer);
foreach $pair (@pairs)
{
    ($name, $value) = split(/=/, $pair);
    $value =~ s/\%40/\@/g;
    $value =~ tr/+/ /;
    $value =~ s/%([a-fA-F0-9]{2,2})/chr(hex($1))/eg;
    $value =~ s/<!--(.|\n)*-->//g;
    $FORM{$name} = $value;
}
my $keyword = $FORM{'keyword'};
my $logfile = $FORM{'logfile'};
print <<"DBMA";
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">>
<title>DBMA Log Search Tool</title>
<link rel="stylesheet" type="text/css" href="DBMA.css" />
</head>
	<body>
	<div align="center"><center><table>
	<tr><td style="text-align:left"><form action="#">
	<select style="border-style:none;color:blue;background:#f0edf3;font-size:10px;font-family:sans-serif" name="menu" size="4" onchange="location.href=this.form.menu.options[this.form.menu.selectedIndex].value">	
	<option value="DBMA.cgi">DBMA Administration Menu</option>
	<option value="DBMA_installation_configuration.htm">Installation Help</option>
        <option value="DBMA_User_Management.htm">DBMA User Management</option>
	<option value="http://www.dbmail.org">DbMail.org Site</option></select></form><small>$logfile Log Search on $server [<a href="dbmail_sql_help.htm" rel="external"><b>Help</b></a>]</small></td></tr>
	<tr><td class="c6" style="font-weight:bold"><a title="Return To Admin Page" href="DBMA.cgi">DbMail SQL Administrator (DBMA) Admin</a> <small>$date</small></td></tr>
	</td></tr></table></div>
	<div><form method="post" action="DBMA_logsearch.cgi"><center><table><tr><td>Search Term: <input type="text" name="keyword" value="$keyword" /> Log File:<input title="If you don't enter a location for this file I will try to find the Mail Log." type="text" name="logfile" value ="$logfile" /> <input type="submit" value="Search" name="submit"  style="background-color:#D6CFDE; color:#4602A0" /></td></tr></table></form></div>
DBMA
if ($FORM{'keyword'})
{
    &do_search;
}
else
{
    print "</body></head>";
    exit;
}
###################################################################### - sub do_search
sub do_search
{
    if ($FORM{'logfile'})
    {
        $logfile = $FORM{'logfile'};
    }
    else
    {
        $logfile = $ENV{MAILLOG} || "/var/log/maillog";
    }
    my $logfiletest = `ls -lh $logfile`;
    chop($logfiletest);
    my $user = `whoami`;
    chop($user);
    print
      "	<div style=\"text-align:left\"><table><tr><td style=\"text-align:left\">Searched for<strong>\n";
    print "$keyword";
    print "	</strong> in:<br />\n";
    print
      "	<span style=\"text-align:left;font-family:courier,serif;font-size:10px;color:#000000\">
$logfiletest <small>(should be readable by HTTPD user <b>$user</b>)</small></span></td></tr><td><tr>\n";
    print <<"DBMA";
	<div style="text-align:center"><center><table><tr><td style="text-align:left;width:100%">
DBMA
    print
      "<pre style=\"font-family:arial,helvetica,sans-serif;font-size:10px;color:#000090;background-color:#ffffff\">\n";
    open(LOG, "$logfile") or die "Unable to open logfile:$!\n";
    while (<LOG>)
    {
        my $content = print if /$keyword/;
        $output = $content;
        $output =~ s/  / /g;
        $output =~ s/$keyword/<b>$keyword<\/b>/g;
        $output =~ s/^[<>]+//;
        $output =~ s/\%0A//g;
        $output =~ s/\%0D//g;
        $output =~ s/\s+$//;
        print $output;
    }
    close(LOG);
    print "	</pre></td></tr></table></div></body></head>";
    exit;
}
############################################################### -  end
# Copyright 2004-2005 and supported by Mike O'Brien mike@dbma.ca
