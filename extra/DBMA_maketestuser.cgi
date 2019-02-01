#!/usr/bin/perl
# maketestusers.cgiDbMailAdministrator (DBMA) V3.2.x Copyright 2004-2016 **
#      Trouble? Contact: micheal@dbma.ca
#################################################################
use CGI::Carp qw(fatalsToBrowser);
use strict;
###########Copyright Mike O'Brien ####################
my (
    $FORM,     $adddata,      $aliases,  $buffer,   $char,
    $GroupID, $date,         $i,        $list,     $log_data,
    $maxmail,  $mythisscript, $name,     $pair,     $password,
    $server,   $target_file,  $thispart, $userID,     $value,
    $nextuserID, $variable,     %FORM,     %required, @pairs, $userID
   );
$date         = "" . scalar localtime(time) . "";
$server       = $ENV{'SERVER_NAME'};
$mythisscript = ($ENV{'SCRIPT_NAME'} || 'DBMA_maketestuser.cgi');
read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
@pairs = split(/&/, $buffer);
foreach $pair (@pairs)
{
    ($name, $value) = split(/=/, $pair);
    $value =~ tr/+/ /;
    $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
    $FORM{$name} = $value;
}
$aliases  = $FORM{'aliases'};
$userID     = $FORM{'userID'};
$password = $FORM{'password'} || "pass";
$GroupID = $FORM{'GroupID'} || "10";
$maxmail  = $FORM{'maxmail'} || "5000";
&check_form;
if ($FORM{'password'})
{
    &add_user;
}
else
{
    &make_add_user_page;
}
################################################ -  sub add_user
sub add_user
{
    print "Content-type: text/html\n\n";
    print <<"EOM";
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8" />
<meta http-equiv="Pragma" content="no-cache" />
<meta http-equiv="Cache-control" content="no-cache" />
<link rel="stylesheet" type="text/css" href="../DBMA.css" />
<title>ADD TEST USERS</title>
</head>
<body>
<div align="center"><center>
<table border="0" style="font-family: sans-serif; font-size: 12pt; text-align: center; margin-left: 5px" cellspacing="0" cellpadding="0">
<tr><td style="text-align:left" width="500px">
</td></tr></table></center></form></div>
<div align="center"><table width="500px" border="0" style="color:#000070; border-style:solid; background-color:#ffffff; border-color:#ffffff;font-family: Trebuchet MS; font-size: 12pt; text-align: left; margin-left: 1px" cellspacing="0" cellpadding="0"><tr><td width="500px">
EOM
    $adddata =
      `/usr/local/sbin/dbmail-users \-a $userID \-w $password \-p md5sum \-g $GroupID \-m $maxmail \-s$aliases`;
    chop($adddata);
    my $thispart = $adddata;
    $thispart =~ s/Check the man page//g;
    $thispart =~ s/\*\*\* dbmail-user \*\*\*//g;
    $thispart =~ s/Opening connection to database...//g;
    $thispart =~ s/Opening connection to authentication...//g;
    $thispart =~ s/Ok. Connected//g;
    $thispart =~ s/Info for user [testuser]//g;
    $thispart =~ s/with/<br \/>/g;
    $thispart =~ s/and/<br \/>/g;
    $thispart =~ s/password/Password: /g;
    $thispart =~ s/,/<br \/>/g;
    $thispart =~ s/Adding/<br \/>Creating/g;
    $thispart =~ s/added id /added.<br \/>User ID: /g;
    $thispart =~ s/user added./User now created and stored./g;
    $thispart =~ s/GroupID/Group \(Client\) ID:/g;
    $thispart =~ s/Ok//g;
    $thispart =~ s/User ID/User ID of/g;
    $thispart =~ s/Ok. added/<br \/>New user account successfully completed./g;
    $thispart =~ s/adduser done//g;
    $thispart =~ s/\[//g;
    $thispart =~ s/\]//g;
    $thispart =~ s/\%0A//g;
    $thispart =~ s/\%0D//g;
    $thispart =~ s/added/<br \/>Data stored./g;
    $thispart =~ s/Ok//g;
    if (length($thispart) > 1)
    {
        print " $thispart<br />";
        $target_file = "DBMA.test.user.txt";
        open(LOG_FILE, ">>$target_file");
        $log_data = $adddata;
        $log_data =~ s/\*\*\* dbmail-adduser \*\*\*//g;
        $log_data =~ s/Opening connection to database...//g;
        $log_data =~ s/Opening connection to authentication...//g;
        $log_data =~ s/Ok. Connected//g;
        $log_data =~ s/Adding INBOX for new user//g;
        $log_data =~ s/Ok. added//g;
        $log_data =~ s/adduser done//g;
        $log_data =~ tr/\n\t\f/ /;
        $log_data =~ s/     / /g;
        $log_data =~ s/  / /g;
        $log_data =~ s/  / /g;
        $log_data =~ s/\s+$//;
        print LOG_FILE
          "$date  | $server | $ENV{'REMOTE_ADDR'} |User: $userID|$log_data \n";
        close(LOG_FILE);
    }
    print <<"EOM";
	</td></tr></table></div>

	<div><center><table><tr><td style="text-align:left;width:37%"><form method="post" action="../DBMA.cgi"><input type="hidden" name="RQT" value="2" />
	<input type="hidden" value="$userID" name="userID" />
	<input title="View $userID Account" type="submit" style="background:#D0F4D2; color:#4602A0" value="View $userID Account" /></form></td>
	<td style="text-align:left;width:31%"><form method="post" action="../DBMA.cgi"><input type="hidden" value="all_in_this_group" name="RQT" />
	<input type="hidden" value="$GroupID" name="GroupID" />
	<input title="All Users in Group" type="submit" value="List Users in Group $GroupID" style="background:#D0F4D2; color:#4602A0" /><input type="hidden" name="required" value="GroupID" /></form></td>
	</tr></table></center></div>




EOM
    &make_another_user_page;
    print <<"EOM";
</body></html>
EOM
    exit;
}
################################################ -  sub check_form
sub check_form
{
    %required = qw(userID);
    foreach $variable (keys(%required))
    {
        &make_add_user_page unless ($FORM{$variable});
    }
}
################################################ -  sub make_add_user_page
sub make_add_user_page
{
    for ($i = 0 ; $i < 8 ; $i++)
    {
        $list = int(rand 3) + 1;
        if ($list == 1)
        {
            $char = int(rand 7) + 50;
        }
        if ($list == 2)
        {
            $char = int(rand 25) + 65;
        }
        if ($list == 3)
        {
            $char = int(rand 25) + 97;
        }
        $char = chr($char);
        $userID .= $char;
    }
    print "Content-type: text/html\n\n";
    print <<"EOM";
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8" />
<meta http-equiv="Pragma" content="no-cache" />
<meta http-equiv="Cache-control" content="no-cache" />
<meta name="author" content="micheal j. o'brien" />
<meta http-equiv="imagetoolbar" content="no" />
<link rel="stylesheet" type="text/css" href="../DBMA.css" />
<title>Make Test Users DbMail Administrator (DBMA)</title>
</head>
<body>
<div><form action="$mythisscript" method="post"><center>
<table class="c5" cellspacing="0" cellpadding="0" width="500" border="0"><tbody><tr>
<tr><td class="gr" colspan="3">
<h1><b>Make test users for $server.</b><a href="../DBMA.cgi"> Back to DBMA</a></h1>
This is intended for early use in your installation and configuration process. The tool uses the /usr/local/sbin/dbmail-users utility and consequently must be run on the DbMail host (upon which you installed DbMail).
<ul><li> You may need to adjust permissions for dbmail.conf and dbmail-users while you use this tool.</li>
<li> If you are unsure of what you are doing, please use the SQL tools of <a href="../DBMA.cgi"> DbMailAdministrator (DBMA)</a>.</li>
<li> You can change the inserted values below to what you like.</li>
<li> All but the username and the domain will persist. </li>
<li> This tool is primarily for testing purposes. </li>
<li> A log of all users created is stored at <a href="DBMA.test.user.txt">DBMA.test.user.txt</a></li></ul>
<hr class="c9">
</td></tr>
<tr><td class="c2 c2">User Name</td>
<td class="c2 c2"><input name="userID" value="$userID" size="20" /></td>
<td class="c2 c2"></td></tr>
<tr><td class="c2 c2">Password</td>
<td class="c2 c2"><input name="password" value="$password" size="20" /></td>
<td class="c2 c2"></td></tr>
<tr><td class="c2 c2">Client ID</td>
<td class="c2 c2"><input size="4" value="$GroupID" name="GroupID" /></td>
<td class="c2 c2"></td></tr>
<tr><td class="c2 c2">MailBox Size</td>
<td class="c2 c2"><input size="9" value="$maxmail" name="maxmail" /></td>
<td class="c2 c2"></td></tr>
<tr><td class="c2 c2">Aliases</td><td class="c2 c2" colspan="2">
<input type="text" name="aliases" size="35" value="$userID\@$server" /><br />
<input class="c7" type="submit" value="Add New User" name="submit" /></td></tr></tbody></table></center></form></div></body></html>
EOM
    exit;
}
################################################ -  sub make_another_user_page
sub make_another_user_page
{
    for ($i = 0 ; $i < 8 ; $i++)
    {
        $list = int(rand 3) + 1;
        if ($list == 1)
        {
            $char = int(rand 7) + 50;
        }
        if ($list == 2)
        {
            $char = int(rand 25) + 65;
        }
        if ($list == 3)
        {
            $char = int(rand 25) + 97;
        }
        $char = chr($char);
        $nextuserID .= $char;
    }
    print <<"EOM";
<div><form action="$mythisscript" method="post"><center>
<table class="c5" cellspacing="0" cellpadding="0" width="500" border="0"><tbody><tr>
<tr><td class="c1" colspan="3">
<h1><b>Make another test user for $server. <a href="../DBMA.cgi"> Back to DBMA</a></b></h1></td></tr>
<tr><td class="c2 c2">User Name</td>
<td class="c2 c2"><input name="userID" value="$nextuserID" size="20" /></td>
<td class="c2 c2"></td></tr>
<tr><td class="c2 c2">Password</td>
<td class="c2 c2"><input name="password" value="$password" size="20" /></td>
<td class="c2 c2"></td></tr>
<tr><td class="c2 c2">Client ID</td>
<td class="c2 c2"><input size="4" value="$GroupID" name="GroupID" /></td>
<td class="c2 c2"></td></tr>
<tr><td class="c2 c2">MailBox Size</td>
<td class="c2 c2"><input size="9" value="$maxmail" name="maxmail" /></td>
<td class="c2 c2"></td></tr>
<tr><td class="c2 c2">Aliases</td><td class="c2 c2" colspan="2">
<input type="text" name="aliases" size="35" value="$nextuserID\@$server" /><br />
<input class="c7" type="submit" value="Add New User" name="submit" /></td></tr></tbody></table></center></form></div>
EOM
exit;
}
############################################################### -  end
# Copyright 2004-2006 and supported by Mike O'Brien mike@dbma.ca
