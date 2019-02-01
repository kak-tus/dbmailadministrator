#!/usr/bin/perl

use CGI::Carp qw(fatalsToBrowser);
our ($RESTRICTGroupID, $RESTRICTGroupIDName, $path, $path_determined,
     $group_limit);
BEGIN { push @INC, "./" }
&path_determined;

=head
    DBMA v3.0.2 DBMailAdministrator (DBMA) For DBMail 3.2.x
   	Unix or Win32 - Configured From The GUI (web browser).
   	Win32 - Change PERL Shebang unless using PerlIS.dll.
   	Copyright 2004-2016 & supported by M. J. [Mike] O'Brien in Canada
   	UPDATES: http://www.dbma.ca/
   	CONTACT: micheal@dbma.ca



 NOTE: Other than hard-code RESTRICTGroupID below, DBMA is configured from the GUI.

   	** RESTRICTGroupID ** CONFIGURE DBMA FROM THE GUI FIRST!

        TO REDUCE FUNCTION TO ONE GROUP CHANGE $RESTRICTGroupID = 'any' to a number.

   	Created for Level One Support; Help Desk; or External Client
        on SSL PWD-secured access. This mode denies access to other
        groups, configuration tools and all global functions.
        When DBMA has connected to the database and functions to your satisfaction, only then
   	change $RESTRICTGroupIDName to Group number it will be limited to. (See README.)
  	Customize apearance a little by changing "My Mail User Group" to anything you like. 
=cut

$RESTRICTGroupID = 'any';

$RESTRICTGroupIDName = "My Mail User Group";

# DO NOT ALTER ANYTHING BELOW HERE. You could break DBMA and even damage your database.
#######################################################################################

$path = $path_determined || "./";

our (
     $ACL_ctrl,                    $ACLdelete_list,
     $ALIAS_AND_SQL_MATCH,         $CFP,
     $DBMA_DATA,                   $DBMA_DATA_MTA_TEMP,
     $DBMA_GROUP_DATA,             $DBMA_SQL_MTA,
     $DBMA_STATS,                  $DBMA_TIMESTAMP,
     $DBMAcode,                    $DBMAencrypt,
     $DBMail22Version,             $DBMailOldVersion,
     $DBSearchTime,                $FORM,
     $GroupControl,                $GroupID,
     $InnoDB,                      $InnoDB_Free,
     $LIMIT,                       $MTA_GUI,
     $Missing_In_SQL_MTA,          $Not_Found_In_Aliases,
     $PROTECTED_SYS_ACCOUNTS,      $PUBLICuserID,
     $RQT,                         $SMTP_ServerName,
     $_action,                     $_dom,
     $_sender,                     $_sender_,
     $_transport,                  $add_MTA,
     $add_user_form_helper,        $addnewaliases,
     $addnotify,                   $addtext,
     $admin_address,               $administer_flag,
     $alias,                       $alias_idnr,
     $allow_read_mail,             $andgroup,
     $andmoretext,                 $answered_flag,
     $anyone,                      $auto_create_user,
     $buffer,                      $bypass,
     $changecase,                  $changepassword,
     $char,                        $check_secs,
     $clear_user_mapping,          $client_idnr,
     $cmailsize,                   $colortellsastory,
     $count,                       $count_users_per_group,
     $create_first_alias,          $create_flag,
     $cur_mailsize,                $curmail_size,
     $data,                        $date,
     $dbh,                         $dbmail_acl_table,
     $dbmail_aliases_table,        $dbmail_auto_notifications_table,
     $dbmail_auto_replies_table,   $dbmail_ccfield_table,
     $dbmail_datefield_table,      $dbmail_fromfield_table,
     $dbmail_headername_table,     $dbmail_headervalue_table,
     $dbmail_mailboxes_table,      $dbmail_messageblks_table,
     $dbmail_messages_table,       $dbmail_pbsp_table,
     $dbmail_physmessage_table,    $dbmail_referencesfield_table,
     $dbmail_replycache_table,     $dbmail_replytofield_table,
     $dbmail_sievescripts_table,   $dbmail_subjectfield_table,
     $dbmail_subscription_table,   $dbmail_tofield_table,
     $dbmail_usermap_table,        $dbmail_users_table,
     $dbmail_ver,                  $defaultGroup_ID,
     $defaultdomain,               $defaultmailboxsize,
     $delete_MTA,                  $delete_flag,
     $deleted_flag,                $deletegroup,
     $deleteuser,                  $deliver_from,
     $deliver_to,                  $deny_user_access,
     $digest,                      $dir,
     $dom_transport,               $domain,
     $encryption_type,             $encrypttype,
     $endtime,                     $error,
     $errormessage,                $fetch_domains,
     $fetch_mtas,                  $filehash,
     $filename,                    $firstalias,
     $get_message,                 $headers_only,
     $headers_only_sql,            $headers_results,
     $headervalue,                 $i,
     $insert_flag,                 $insertnewuser,
     $internal_date,               $is_header,
     $is_it_new_output,            $is_it_new_userID,
     $is_it_new_username,          $key,
     $last_login,                  $limit,
     $line,                        $list,
     $listall,                     $local_name,
     $login,                       $loginterval,
     $longblob,                    $lookup_flag,
     $mailbox_id,                  $mailbox_idnr,
     $mailbox_name,                $mailboxsize,
     $mailfrom,                    $mailto,
     $maxmail_size,                $maxmailsize,
     $md5,                         $message,
     $message2,                    $messageID,
     $message_idnr,                $messageblk,
     $messagesize,                 $method,
     $mouseover,                   $mtas,
     $myClientID,                  $myDBMA_CONFIG,
     $myDBMA_OPTIONS,              $myGroupID,
     $myUserIDdata,                $mydestination,
     $mymessage,                   $mysqldate,
     $mythisscript,                $name,
     $newRQT,                      $newalias,
     $newuserID,                   $notify_address,
     $notwsctlchar,                $numrows,
     $num_users,                   $onlytime,
     $onoffcrypt,                  $onoffhash,
     $onoffmd5sum,                 $onoffplain,
     $operator,                    $order,
     $orderby,                     $output,
     $owner_idnr,                  $pair,
     $pairs,                       $passwd,
     $password,                    $peopledate,
     $perm_error,                  $physmessage_id,
     $placethisforRESTRICTGroupID, $post_flag,
     $public_mailboxes,            $quotedpair,
     $read_flag,                   $refresh_rate,
     $reply_body,                  $require,
     $required,                    $results,
     $rfcsize,                     $rv,
     $searchterms,                 $seen_flag,
     $selected,                    $server,
     $shared_mailbox,              $smtp,
     $sock_allow,                  $sock_deny,
     $sql,                         $sql_odd_port,
     $sqldb,                       $sqlhost,
     $sqlport,                     $sqltype,
     $sqluser,                     $start_date,
     $starttime,                   $stats_on,
     $status,                      $sth,
     $stop_date,                   $str,
     $str1,                        $str10,
     $str11,                       $str2,
     $str3,                        $str4,
     $str5,                        $str6,
     $str7,                        $str8,
     $stripped_group,              $str9,
     $subject,                     $text,
     $thedomain,                   $title,
     $transport,                   $unique_id,
     $uniquedomain,                $use_DBMA_MTA_Domains,
     $userID,                      $user_ACL_avail_mailboxes,
     $user_id,                     $user_idnr,
     $user_mailboxes,              $usermap_userid,
     $username,                    $usernameDISPLAY,
     $value,                       $variable,
     $view_userID,                 $write_flag,
     $write_secs,                  %FORM,
     %GroupID,                     %alias,
     %data,                        %domain,
     %filehash,                    %grp,
     %key,                         %line,
     %required,                    %seen,
     %thedomain,                   @ERROR,
     @INFO,                        @MESSAGE,
     @components,                  @data,
     @domain,                      @is_it_new_output,
     @keys,                        @message_fields,
     @newdata,                     @output,
     @pairs,                       @required,
     @row,                         @sqldata,
     @values
    )
  = "";
&defaults;

BEGIN
{
    require DBI;
    use strict;
    our $userID;
    undef $str;
    $userID = $FORM{'userID'} || $userID || "";
}
undef $RQT;
undef $sth;
undef $str;
our $version = "DBMA v3.0.2 Stable";
$ALIAS_AND_SQL_MATCH  = $path . 'DBMA_Matched_SQL_And_Aliases.DB';
$DBMA_DATA            = $path . 'DBMA_DATA.DB';
$DBMA_GROUP_DATA      = $path . 'DBMA_GROUP_DATA.DB';
$DBMA_TIMESTAMP       = $path . 'DBMA_TIMESTAMP';
$myDBMA_OPTIONS       = $path . 'DBMA_OPTIONS.DB';
$DBMA_STATS           = $path . 'DBMA_STATS.DB';
$myDBMA_CONFIG        = $path . 'DBMA_CONFIG.DB';
$DBMA_DATA_MTA_TEMP   = $path . 'DBMA_DATA_MTA.DB';
$DBMA_SQL_MTA         = $path . 'DBMA_SQL_MTA.DB';
$Missing_In_SQL_MTA   = $path . 'DBMA_Missing_In_SQL_MTA.DB';
$Not_Found_In_Aliases = $path . 'DBMA_Not_Found_In_Aliases.DB';

&read_configs;

if ($RESTRICTGroupID =~ m/[0-9]/i)
{
    $use_DBMA_MTA_Domains = "0";
}
    $DBMail22Version                 = "1";
    $DBMailOldVersion                = "0";
    $cmailsize                       = "curmail_size, ";
    $order                           = "ORDER BY is_header desc";
    $dbmail_acl_table                = "dbmail_acl";
    $dbmail_aliases_table            = "dbmail_aliases";
    $dbmail_auto_notifications_table = "dbmail_auto_notifications";
    $dbmail_auto_replies_table       = "dbmail_auto_replies";
    $dbmail_ccfield_table            = "dbmail_ccfield";
    $dbmail_datefield_table          = "dbmail_datefield";
    $dbmail_fromfield_table          = "dbmail_fromfield";
    $dbmail_headername_table         = "dbmail_headername";
    $dbmail_headervalue_table        = "dbmail_headervalue";
    $dbmail_mailboxes_table          = "dbmail_mailboxes";
    $dbmail_messageblks_table        = "dbmail_headervalue";
    $dbmail_messages_table           = "dbmail_messages";
    $dbmail_pbsp_table               = "dbmail_pbsp";
    $dbmail_physmessage_table        = "dbmail_physmessage";
    $dbmail_referencesfield_table    = "dbmail_referencesfield";
    $dbmail_replycache_table         = "dbmail_replycache";
    $dbmail_replytofield_table       = "dbmail_replytofield";
    $dbmail_sievescripts_table       = "dbmail_sievescripts";
    $dbmail_subjectfield_table       = "dbmail_subjectfield";
    $dbmail_subscription_table       = "dbmail_subscription";
    $dbmail_tofield_table            = "dbmail_tofield";
    $dbmail_usermap_table            = "dbmail_usermap";
    $dbmail_users_table              = "dbmail_users";



if ($DBMail22Version eq "1")
{
    $dbmail_ver = "DBMail V3.2.x";
}
elsif ($DBMailOldVersion eq "1")
{
    $dbmail_ver = "DBMail V1.2.x";
}
elsif (($DBMailOldVersion eq "0") && ($DBMail22Version eq "0"))
{
    $dbmail_ver = "DBMail V2.0.x";
}
else
{
    $dbmail_ver = "DBMail";
}

print "Content-Type: text/html\015\012\015\012";
$name   = "";
$value  = "";
$pair   = "";
$buffer = "";

if ($ENV{'REQUEST_METHOD'} eq "POST") { $method = 0 }
if ($ENV{'REQUEST_METHOD'} eq "GET")  { $method = 1 }
$method = $method || 0;
if ($method == 0) { read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'}) }
&MTA_show if (($method == 1) && ($ENV{'QUERY_STRING'} eq "MTA"));
if (($method == 1)
    && (($ENV{'QUERY_STRING'}) =~
        m/[0-9a-zA-Z\.\-\_\!\#\$\%\&\*\+\/\=\?\^]+\@/i))
{
    @output         = &split($ENV{'QUERY_STRING'});
    $userID         = $output[0];
    $thedomain      = ($output[1]);
    $FORM{'userID'} = $userID;
}
if (($method == 1) && ($ENV{'QUERY_STRING'}))
{
    $userID = $ENV{'QUERY_STRING'};
    $FORM{'userID'} = $userID;
    $userID =~ s/\'//g;
    $userID =~ s/\"//g;
}
elsif ($method == 1)
{
    $buffer = $ENV{'QUERY_STRING'} ? $ENV{'QUERY_STRING'} : '';
}
@pairs = split(/&/, $buffer);
foreach $pair (@pairs)
{
    ($name, $value) = split(/=/, $pair);
    $value =~ s/\%40/\@/g;
    $value =~ tr/+/ /;
    $value =~ s/%([a-fA-F0-9]{2,2})/chr(hex($1))/eg;
    $value =~ s/<!--(.|\n)*-->//g;
    $FORM{$name} = $value;
    $value =~ s/\'//g;
    $value =~ s/\"//g;
}

$administer_flag = $FORM{'administer_flag'};
$add_MTA         = $FORM{'add_MTA'}
  || 'localhost'
  ;   #(good default initialization of variable--localhost should exist anyway )
$alias = $FORM{'alias'};
$alias =~ s/\'//g if $alias;
$alias_idnr = $FORM{'alias_idnr'};
$anyone     = $FORM{'anyone'};
$bypass     = ($FORM{'bypass'} || 0);
$bypass =~ s/checked/1/g;
$bypass =~ s/on/1/g;
$changepassword   = $FORM{'changepassword'};
$create_flag      = $FORM{'create_flag'};
$deletegroup      = $FORM{'deletegroup'};
$deleted_flag     = $FORM{'deleted_flag'};
$delete_flag      = $FORM{'delete_flag'};
$delete_MTA       = $FORM{'delete_MTA'};
$deny_user_access = $FORM{'deny_user_access'};
$encrypttype      = $FORM{'encrypttype'};
$encrypttype =~ s/md5-hash/md5sum/g if $FORM{'encrypttype'};
$encrypttype =~ s/ //g if $FORM{'encrypttype'};
$headers_only = $FORM{'headers_only'};
$insert_flag  = $FORM{'insert_flag'};
$limit        = ($FORM{'limit'} || "200");
$limit =~ s/K/000/g;
$limit =~ s/k/000/g;
$limit =~ s/[a-jA-J]//g;
$limit =~ s/[l-zL-Z]//g;
$LIMIT              = ("LIMIT $limit") if (defined $limit > 0);
$clear_user_mapping = $FORM{'clear_user_mapping'};
$lookup_flag        = $FORM{'lookup_flag'};
$login              = $FORM{'login'};
$loginterval        = $FORM{loginterval} || "4";
$mailbox_id         = $FORM{'mailbox_id'};
$mailbox_idnr       = $FORM{'mailbox_idnr'};
$mailbox_name       = $FORM{'mailbox_name'};
$mailboxsize        = $FORM{'mailboxsize'};

if ($RESTRICTGroupID =~ m/[0-9]/i)
{
    $mailboxsize = $defaultmailboxsize
      unless ($FORM{'mailboxsize'} < $defaultmailboxsize);
}

$mailboxsize =~ s/g/000000000/g if $FORM{'mailboxsize'};
$mailboxsize =~ s/G/000000000/g if $FORM{'mailboxsize'};
$mailboxsize =~ s/k/000/g       if $FORM{'mailboxsize'};
$mailboxsize =~ s/K/000/g       if $FORM{'mailboxsize'};
$mailboxsize =~ s/m/000000/g    if $FORM{'mailboxsize'};
$mailboxsize =~ s/M/000000/g    if $FORM{'mailboxsize'};
$mailfrom = $FORM{'mailfrom'} || "";
$mailto   = $FORM{'mailto'}   || "";
$messageID      = $FORM{'messageID'};
$message        = $FORM{'message'};
$newalias       = $FORM{'newalias'};
$newuserID      = $FORM{'newuserID'};
$notify_address = $FORM{'notify_address'} || "";
$password       = $FORM{'password'} || "";
$physmessage_id = $FORM{'physmessage_id'};
$post_flag      = $FORM{'post_flag'};
$PUBLICuserID   = $FORM{'PUBLICuserID'};
$read_flag      = $FORM{'read_flag'};
$reply_body     = $FORM{'reply_body'};
$required       = $FORM{'required'};
$searchterms    = $FORM{'searchterms'} || "";
$searchterms =~ s/\'//g;
$searchterms =~ s/\"//g;
$seen_flag      = $FORM{'seen_flag'};
$start_date     = $FORM{'start_date'};
$stop_date      = $FORM{'stop_date'};
$shared_mailbox = $FORM{'shared_mailbox'};
$sock_allow     = $FORM{'sock_allow'};
$sock_deny      = $FORM{'sock_deny'};
$RQT            = $FORM{'RQT'} || "NULL";
$subject        = $FORM{'subject'} || "";
$userID         = $FORM{'userID'};
$userID =~ s/\'//g if $userID;
$usermap_userid = $FORM{'usermap_userid'};
$username = $FORM{'username'} || $FORM{'userID'};
$username =~ s/\'//g if $username;
$write_flag = $FORM{'write_flag'};

&clear if (($method == 1) && (($ENV{'QUERY_STRING'}) eq "makeshortform"));
&connect unless (($RQT eq "29") || ($RQT eq "30"));
&mysql_date;
&LIST_Group  if ($RQT eq "all_in_this_group");
&LIST_Global if ($RQT eq "any");
if    ($RQT eq "aliases_in_this_group") { &List_Group_Aliases; }
elsif ($RQT eq "0")                     { &make_form; }
elsif ($RQT eq "1")                     { &add_user_sql; }
elsif ($RQT eq "2")                     { &Create_User_Account_Window; }
elsif ($RQT eq "3")                     { &add_user_form_sql; }
elsif ($RQT eq "4")                     { &delete_user; }
elsif ($RQT eq "5")                     { &delete_user_form_sql; }
elsif ($RQT eq "6")                     { &create_alias_sql; }
elsif ($RQT eq "6a")                    { &create_group_alias_sql; }
elsif ($RQT eq "7")                     { &create_alias_form_sql; }
elsif ($RQT eq "8")                     { &delete_alias_form_sql; }
elsif ($RQT eq "9")                     { &delete_specific_forwards_sql; }
elsif ($RQT eq "10")                    { &delete_alias_sql; }
elsif ($RQT eq "11")                    { &Create_User_Account_MODIFY_Window; }
elsif ($RQT eq "12")                    { &MODIFY_User_SQL; }
elsif ($RQT eq "13")                    { &Forwards_SQL; }
elsif ($RQT eq "13a")                   { &edit_forward_form_sql; }
elsif ($RQT eq "13b")                   { &Forwards_SQL; }
elsif ($RQT eq "14")                    { &add_forward_form_sql; }
elsif ($RQT eq "15")                    { &add_notify_sql; }
elsif ($RQT eq "16")                    { &add_notify_form_sql; }
elsif ($RQT eq "17")                    { &delete_notify_sql; }
elsif ($RQT eq "18")                    { &delete_notify_form_sql; }
elsif ($RQT eq "19")                    { &List_Global_Aliases; }
elsif ($RQT eq "20")                    { &List_all_Forwards; }
elsif ($RQT eq "21")                    { &mymailform; }
elsif ($RQT eq "22")                    { &List_auto_notifications; }
elsif ($RQT eq "23")                    { &showrecentlogins; }
elsif ($RQT eq "24")                    { &DBMA_ConnectStatus; }
elsif ($RQT eq "25")                    { &mydelete_specific_alias; }
elsif ($RQT eq "26")                    { &password_tools; }
elsif ($RQT eq "27")                    { &password_encrypt; }
elsif ($RQT eq "28")                    { &send_mail; }
elsif ($RQT eq "29")                    { &create_myDBMA_CONFIG; }
elsif ($RQT eq "30")                    { &create_myDBMA_OPTIONS; }
elsif ($RQT eq "31")                    { &delete_mail; }
elsif ($RQT eq "32")                    { &undelete_mail; }
elsif ($RQT eq "33")                    { &search_mail; }
elsif ($RQT eq "33a")                   { &search_mail_extended; }
elsif ($RQT eq "34")                    { &delete_all_mail; }
elsif ($RQT eq "35")                    { &undelete_all_mail; }
elsif ($RQT eq "36")                    { &fix_deleted; }
elsif ($RQT eq "37")                    { &make_shortform; }
elsif ($RQT eq "39")                    { &delete_user_restricted; }
elsif ($RQT eq "40")                    { &delete_group; }
elsif ($RQT eq "41")                    { &delete_from_aliases_sql; }
elsif ($RQT eq "42")                    { &delete_from_aliases_global_admin; }
elsif ($RQT eq "43")                    { &ACL_LIST; }
elsif ($RQT eq "44")                    { &ACL_FORM; }
elsif ($RQT eq "45")                    { &ACL_create; }
elsif ($RQT eq "46")                    { &create_PUBLIC_Account_and_ACL; }
elsif ($RQT eq "47")                    { &delete_ACL_user; }
elsif ($RQT eq "48")                    { &delete_ACL_folder; }
elsif ($RQT eq "49")                    { &update_ACL_user; }
elsif ($RQT eq "50")                    { &add_ACL_user; }
elsif ($RQT eq "51")                    { &add_AutoReply; }
elsif ($RQT eq "52")                    { &delete_AutoReply; }
elsif ($RQT eq "53")                    { &update_AutoReply; }
elsif ($RQT eq "54")                    { &delete_MTA_Domains; }
elsif ($RQT eq "55")                    { &create_DBMA_MTA_Table; }
elsif ($RQT eq "56")                    { &delete_auto_notify; }
elsif ($RQT eq "57")                    { &update_auto_notify; }
elsif ($RQT eq "58")                    { &edit_MTA_Domains; }
elsif ($RQT eq "59")                    { &add_MTA_Domains; }
elsif ($RQT eq "60")                    { &GUI_MTA_Domains; }
elsif ($RQT eq "61")                    { &GUI_MTA_Access; }
elsif ($RQT eq "62")                    { &MTA_Access_SQL; }
elsif ($RQT eq "63")                    { &delete_MTA_Access; }
elsif ($RQT eq "64")                    { &MTA_Access_Migrate; }
elsif ($RQT eq "65")                    { &Update_UserMap; }
elsif ($RQT eq "66")                    { &Create_UserMap; }
elsif (defined $FORM{'mailbox_idnr'})   { &get_mail_list }
elsif (defined $FORM{'physmessage_id'}) { &get_message }
elsif (defined $FORM{'mailto'})         { &send_mail; }
elsif (defined $newuserID)              { &add_user_sql; }
elsif (defined $userID)                 { &Create_User_Account_Window; }
else { &make_form; }
############################################################## - construction subs
sub LIST_Group
{
    $orderby = ($FORM{'orderby'} || "userid");
    $GroupID = $FORM{'GroupID'};
    &List_Group_Users;
}

sub LIST_Global
{
    $userID = "";
    $orderby = ($FORM{'orderby'} || "userid");
    &List_Global_Users;
}

sub MTA_show
{
    $userID = " ";
    &GUI_MTA_Domains;
    exit;
}

sub clear
{
    $userID = " ";
    &make_shortform;
    exit;
}

sub end_HTML
{
    print <<"DBMA";
        </body></html>
DBMA
    exit;
}
############################################################## - sub read_configs
sub read_configs
{
    &check_permissions;
    open CONFIG, $myDBMA_CONFIG;

    while (<CONFIG>)
    {
        chomp;
        (
         $DBMailOldVersion, $DBMail22Version, $sqltype, $sqluser, $DBMAcode,
         $sqldb, $sqlhost, $sql_odd_port
        )
          = split /\|/;
    }
    close CONFIG;
    $sqltype =~ tr/[A-Z]/[a-z]/;
    $sqltype =~ s/psql/pgsql/g;
    $sqltype =~ s/postgres/pgsql/g;
    $sqltype =~ s/postgresql/pgsql/g;
    open OPTIONS, $myDBMA_OPTIONS;
    while (<OPTIONS>)
    {
        chomp;
        (
         $SMTP_ServerName, $admin_address,      $defaultmailboxsize,
         $defaultGroup_ID, $CFP,                $DBMAencrypt,
         $defaultdomain,   $create_first_alias, $stats_on,
         $fetch_domains,   $refresh_rate,       $ACL_ctrl,
         $allow_read_mail, $auto_create_user,   $use_DBMA_MTA_Domains,
         $group_limit,     $count_users_per_group
        )
          = split /\|/;
    }
    close OPTIONS;
}
############################################################## - sub defaults
sub defaults
{
### ACLS

    $lookup_flag     = $FORM{'lookup_flag'}     || "1";
    $read_flag       = $FORM{'read_flag'}       || "1";
    $seen_flag       = $FORM{'seen_flag'}       || "1";
    $write_flag      = $FORM{'write_flag'}      || "1";
    $insert_flag     = $FORM{'insert_flag'}     || "1";
    $post_flag       = $FORM{'post_flag'}       || "1";
    $create_flag     = $FORM{'create_flag'}     || "0";
    $delete_flag     = $FORM{'delete_flag'}     || "0";
    $administer_flag = $FORM{'administer_flag'} || "0";

## MAIN

    $server = $ENV{'SERVER_NAME'};
    our $ACL_ctrl      = ($ACL_ctrl)      || $FORM{'ACL_ctrl'}      || "1";
    our $admin_address = ($admin_address) || $FORM{'admin_address'} || ""
      unless ($admin_address);
    $allow_read_mail = ($allow_read_mail) || $FORM{'allow_read_mail'} || "1";
    our $anyone = ($anyone) || "anyone";
    our $auto_create_user = ($auto_create_user)
      || $FORM{'auto_create_user'}
      || "0"
      unless ($auto_create_user);
    our $changecase =
      "onChange=\"javascript:this.value=this.value.toLowerCase\(\)\;\"";
    our $CFP = ($CFP) || $FORM{'CFP'} || "0";
    our $create_first_alias = ($create_first_alias)
      || $FORM{'create_first_alias'}
      || "0";
    our $colortellsastory = $colortellsastory || "#E7FAE8";
    our $DBMAcode    = ($DBMAcode)    || $FORM{'DBMAcode'}    || "dbmail";
    our $DBMAencrypt = ($DBMAencrypt) || $FORM{'DBMAencrypt'} || "";
    our $DBMailOldVersion = ($DBMailOldVersion)
      || $FORM{'DBMailOldVersion'}
      || "0"
      unless $DBMailOldVersion;
    our $DBMail22Version = ($DBMail22Version)
      || "0"
      unless ($DBMail22Version);
    our $defaultdomain = ($defaultdomain) || $FORM{'defaultdomain'} || $server
      unless $defaultdomain;
    our $defaultGroup_ID = $defaultGroup_ID
      || $FORM{'defaultGroup_ID'}
      || $FORM{'GroupID'}
      || ($myGroupID)
      || ""
      unless $defaultGroup_ID;
    our $defaultmailboxsize = ($defaultmailboxsize)
      || $FORM{'defaultmailboxsize'}
      || "25000000"
      unless ($defaultmailboxsize);
    our $encrypttype   = ($encrypttype)   || $FORM{'encrypttype'}   || "";
    our $fetch_domains = ($fetch_domains) || $FORM{'fetch_domains'} || "";
    $GroupID = ($GroupID) || $FORM{'GroupID'} || $defaultGroup_ID
      if ($RESTRICTGroupID eq "any");

    if ($RESTRICTGroupID =~ m/[0-9]/i)
    {
        $defaultGroup_ID = "$RESTRICTGroupID";
        $GroupID         = "$RESTRICTGroupID";
        $FORM{'GroupID'} = "$RESTRICTGroupID";
    }
    our $last_login  = ($last_login)  || "";
    our $mailboxsize = ($mailboxsize) || $FORM{'mailboxsize'} || "";
    our $mailfrom    = ($mailfrom)    || $FORM{'mailfrom'} || $admin_address;
    our $mailto      = ($mailto)      || $FORM{'mailto'} || "";
    our $message     = ($message)     || "";
    our $mymessage   = ($mymessage)   || "";
    our $mouseover =
      "onmouseover=\"this.className=\'front\'\;\" onmouseout=\"this\.className=\'back\'\;\"";
    our $mythisscript = ($ENV{'SCRIPT_NAME'} || 'DBMA.cgi');
    our $newalias = ($newalias) || $FORM{'newalias'} || "";
    our $newuserID = ($newuserID) || $FORM{'newuserID'} || $username || "";
    our $onlytime         = "" . scalar localtime(time) . "";
    our $onoffcrypt       = $onoffcrypt || "";
    our $onoffhash        = $onoffhash || "";
    our $onoffmd5sum      = $onoffmd5sum || "";
    our $onoffplain       = $onoffplain || "";
    our $password         = ($password) || $FORM{'password'} || "";
    our $public_mailboxes = $public_mailboxes || "";
    our $refresh_rate     = ($refresh_rate) || $FORM{'refresh_rate'} || "0"
      unless ($refresh_rate);
    our $shared_mailbox = ($shared_mailbox) || "";
    our $SMTP_ServerName = ($SMTP_ServerName)
      || $FORM{'SMTP_ServerName'}
      || "127.0.0.1"
      unless ($SMTP_ServerName);
    our $sqldb = ($sqldb) || $FORM{'sqldb'} || "dbmail" unless ($sqldb);
    our $sqlhost = ($sqlhost) || $FORM{'sqlhost'} || "127.0.0.1"
      unless ($sqlhost);
    our $sqltype = ($sqltype) || $FORM{'sqltype'} || "mysql"  unless ($sqltype);
    our $sqluser = ($sqluser) || $FORM{'sqluser'} || "dbmail" unless ($sqluser);
    our $sql_odd_port = ($sql_odd_port) || $FORM{'sql_odd_port'} || ""
      unless ($sql_odd_port);
    our $stats_on = ($stats_on) || $FORM{'stats_on'} || "1" unless ($stats_on);
    our $subject = ($subject) || "Information about your mail account";
    our $transport = ($transport)
      || $FORM{'transport'}
      || "dbmail-lmtp:127.0.0.1:24";
    our $userID         = ($userID)         || $FORM{'userID'}         || "";
    our $username       = ($username)       || $FORM{'username'}       || "";
    our $user_mailboxes = ($user_mailboxes) || $FORM{'user_mailboxes'} || "";
    our $use_DBMA_MTA_Domains = ($use_DBMA_MTA_Domains)
      || $FORM{'use_DBMA_MTA_Domains'}
      || "0"
      unless ($use_DBMA_MTA_Domains);
    our $group_limit = ($group_limit) || $FORM{'group_limit'} || "1000";
    our $count_users_per_group = ($count_users_per_group)
      || $FORM{'count_users_per_group'}
      || '';
}
############################################################## - sub connect
sub connect
{

    if ($sqltype =~ /none/)
    {
        &DBMA_ConnectStatus;
        exit;
    }

    $sqlport = $sql_odd_port || '3306' if $sqltype =~ /mysql/;
    $sqlport = $sql_odd_port || '5432' if $sqltype =~ /pgsql/;
    if ($sqltype eq "mysql")
    {
        unless (
            our $dbh =
            DBI->connect(
                "DBI:mysql:$sqluser=$sqluser;password=$DBMAcode;database=$sqldb;port=$sqlport;host=$sqlhost",
                "$sqluser",
                "secret",
                {AutoCommit => 0}
            )
          )
        {
            $errormessage =
              "ErrorID: $version.err0.01 <br />$DBI::errstr <br />Error status: Db connect FAIL";
            &DBMA_ConnectStatus;
        }
    }
    elsif ($sqltype =~ /pgsql/)
    {
        unless (
                $dbh =
                DBI->connect(
                             "DBI:Pg:dbname=$sqldb;port=$sqlport;host=$sqlhost",
                             $sqluser, $DBMAcode, {AutoCommit => 0}
                            )
               )
        {
            $errormessage = "ErrorID: $version.err0.02 <br />
	$DBI::errstr<br />Error status: Db connect FAIL";
            &DBMA_ConnectStatus;
        }
    }
    else
    {
        $errormessage = "ErrorID: $version.err0.03 <br />
	$DBI::errstr <br />Error: Is DBI installed with correct DBD? Unable to Connect To $sqltype Database";
        &DBMA_ConnectStatus;
    }
}
############################################################## - sub make_form
sub make_form
{
    if ($RESTRICTGroupID =~ m/[0-9]/i)
    {
        &make_shortform;
    }
    else
    {
        print <<"DBMA";
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="author" content="micheal j. o'brien" />
<link rel="shortcut icon" href="/favicon.ico" />
<link rel="stylesheet" type="text/css" href="DBMA.css" />
<script xml:space="preserve" type="text/javascript" language="JavaScript">
//<![CDATA[
	var MTAicon=new Image()
	MTAicon.src="images/MTA.gif"
	var clearicon=new Image()
	clearicon.src="images/clear.jpg"
	var qicon=new Image()
	qicon.src="images/q.gif"
	var helpico=new Image()
	helpico.src="images/helpico.jpg"
	var DBMA_ico=new Image()
	DBMA_ico.src="images/DBMA_ico.jpg"
	var menu_help=new Image()
	menu_help.src="images/menu_help.jpg"
	var log_search=new Image()
	log_search.src="images/log_search.jpg"
	var curmailicon=new Image()
	curmailicon.src="images/curmail.gif"
	var groupIDicon=new Image()
	groupIDicon.src="images/groupID.gif"
	var usericon=new Image()
	usericon.src="images/user.gif"
	var lastloginicon=new Image()
	lastloginicon.src="images/lastlogin.gif"
	var mailquotaicon=new Image()
	mailquotaicon.src="images/mailquota.gif"
    	var undeleteicon=new Image()
    	undeleteicon.src="images/undelete.gif"
    	var modifyicon=new Image()
    	modifyicon.src="images/modify.gif"
    	var usericon=new Image()
    	usericon.src="images/usericon.gif"
    	var dnicon=new Image()
    	dnicon.src="images/dn.gif"
    	var imagedelete=new Image()
    	imagedelete.src="images/delete.gif"
    	var add=new Image()
    	add.src="images/add-alias.gif"
    	var usericonsmall=new Image()
    	usericonsmall.src="images/usericon-small.jpg"
    	var notify=new Image()
    	notify.src="images/notify.gif"
					      }	
//]]>
</script>
DBMA
        &menu;
        &stats;
    }
}
############################################################## - sub make_shortform
sub make_shortform
{
    &connect unless ($dbh);
    print <<"DBMA";
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="author" content="micheal j. o'brien" />
<link rel="shortcut icon" href="/favicon.ico" />
<link rel="stylesheet" type="text/css" href="DBMA.css" />
<script xml:space="preserve" type="text/javascript" language="JavaScript">
//<![CDATA[
	var qicon=new Image()
	qicon.src="images/q.gif"
	var helpico=new Image()
	helpico.src="images/helpico.jpg"
	var DBMA_ico=new Image()
	DBMA_ico.src="images/DBMA_ico.jpg"
	var menu_help=new Image()
	menu_help.src="images/menu_help.jpg"
	var log_search=new Image()
	log_search.src="images/log_search.jpg"
	var curmailicon=new Image()
	curmailicon.src="images/curmail.gif"
	var groupIDicon=new Image()
	groupIDicon.src="images/groupID.gif"
	var usericon=new Image()
	usericon.src="images/user.gif"
	var lastloginicon=new Image()
	lastloginicon.src="images/lastlogin.gif"
	var mailquotaicon=new Image()
	mailquotaicon.src="images/mailquota.gif"
    	var undeleteicon=new Image()
    	undeleteicon.src="images/undelete.gif"
    	var modifyicon=new Image()
    	modifyicon.src="images/modify.gif"
    	var usericon=new Image()
    	usericon.src="images/usericon.gif"
    	var dnicon=new Image()
    	dnicon.src="images/dn.gif"
    	var imagedelete=new Image()
    	imagedelete.src="images/delete.gif"
    	var add=new Image()
    	add.src="images/add-alias.gif"
    	var usericonsmall=new Image()
    	usericonsmall.src="images/usericon-small.jpg"
    	var notify=new Image()
    	notify.src="images/notify.gif"
					      }	

//]]>
</script>
DBMA
    &menu;
    if ($RESTRICTGroupID =~ m/[0-9]/i) { &restrict_group_help; }
    end_HTML;
}
############################################################## - sub Create_User_Account_Window RQT2
sub Create_User_Account_Window ($)
{
    my $deliver_to = "";
    &error('Enter user name, user ID or email address.</small>')
      unless ($userID);

    # SEARCH USER:
    # Possible input: non-alphanumeric, email address as username, mail address as alias, alpha string name,
    # alpha-numeric+RFC2822-allowed-chars name, user_idnr, garbage. Clean input. Some DBMail operators store
    # user names as full email addresses. We need to decide if input is a real user name or if the search is
    # for an alias's account. If address, search it. If not exist, strip name, toss domain, search name, get
    # user_idnr Check if it is an email name with numbers or characters (123^_^456) in it, not to be confused
    # with a user_idnr. If user_idnr is input it bypasses all checks and goes to work. This is accomplished
    # in a sub routine which is also called by other function routines.

    &prepare_input;
    &checkrequired;
## -Get the name of this user. If it doesn't exist, outtahere. If exits, continue.
    my $unGET =
      $dbh->prepare(
          "SELECT userid FROM $dbmail_users_table WHERE user_idnr = '$userID'");
    $unGET->execute();
    if (my $rv = $unGET->fetchrow_hashref())
    {
        my $output = $rv->{'userid'};
        $username = $output;
        $username =~ s/__\@\!internal_delivery_user\!\@__/LocalDeliveryAgent/;
        $username =~ s/__public__/\#Public/;
    }
    else
    {
        &fail;
    }
## -What group does it belong to?
    my $myClientIDGET =
      $dbh->prepare(
        "SELECT client_idnr FROM $dbmail_users_table WHERE user_idnr = '$userID'"
      );
    unless ($myClientIDGET->execute())
    {
        $errormessage = "
	ErrorID: $version.err0.04 <br />$DBI::errstr <br />Failed To get Group Information";
        &DBMA_ConnectStatus;
    }
    while (my $rv = $myClientIDGET->fetchrow_hashref())
    {
        my $myClientID = $rv->{'client_idnr'};
        $myGroupID = $myClientID;
        $GroupID   = $myGroupID;
        &meta;

        # and start building the interface GUI
        if ($RESTRICTGroupID =~ m/[0-9]/i)
        {
            print <<"DBMA";
	<title>$RESTRICTGroupIDName - User Account Window for $username DBMail Administrator (DBMA)</title>
	</head><body><div><form method="post" action="$mythisscript"><center><table>
	<tr><td colspan="4"><span class="out">$version on $server (Administering: $dbmail_ver $sqltype:$sqldb:$sqlhost)</span></td></tr>
	<tr><td colspan="4"><span style="color: #005A9C; background: #F8F8FF;font:140% sans-serif" >User Account Window : $username </span><span style="font:90% sans-serif" >[ <a title="The manual on user management" href="DBMA_User_Management.htm" rel="external">User Management </a> | <a href="DBMA_help.htm" rel="external"> Help </a> ]</span></td></tr>
	<tr><td style="text-align:left">
	<form method="post" action="$mythisscript"><input type="hidden" name="RQT" value="2" /><small>User</small>
	<input type="text" $mouseover $changecase title="Please enter the user ID number or user name." name="userID" value="$userID" size="12" /><input type="hidden" value="$GroupID" name="GroupID" />
	<input title="Search for user." type="submit" onmouseover="this.className='clear';" onmouseout="this.className='letsgo';" class="letsgo" value="User Search" /><input type="hidden" name="RQT" value="2" /></form></td>
	<td style="text-align:left"><form method="post" action="$mythisscript"><input type="hidden" value="all_in_this_group" name="RQT" /><small>Group $RESTRICTGroupID</small><input type="hidden" value="$GroupID" name="GroupID" />
	<input title="All Users in Group" type="submit" value="List Users" onmouseover="this.className='clear';" onmouseout="this.className='letsgo';" class="letsgo" /><input type="hidden" name="required" value="GroupID" /></form></td>
	<td style="text-align:left"><form method="post" action="$mythisscript"><input type="hidden" name="RQT" value="aliases_in_this_group" />
	<small>Group $RESTRICTGroupID</small><input type="hidden" value="$GroupID" name="GroupID" /><input title="List aliases in Group $GroupID" type="submit" onmouseover="this.className='clear';" onmouseout="this.className='letsgo';" class="letsgo" value="List Aliases" /><input type="hidden" name="required" value="GroupID" /></form></td>
	<td style="text-align:left;width:52px"><form method="post" action="$mythisscript"><input type="submit" title="Go To Main Screen" style="background-color:#D6CFDE; color:#4602A0" value="Main" /></form></td></tr>
	<tr><td colspan="4"><hr style="background-color:#D6CFDE; color:#D6CFDE;height:3px" /></td></tr></table></center></form></div>
	<div><center><table><tr><td><span class="gr">User</span><br /><big>$username</big></td><td><span class="gr">UserID</span><br />$userID</td><td><span class="gr">Group</span><br />$GroupID</td>
DBMA
        }
        else
        {
            print <<"DBMA";
	<title>DBMA User Account for $username - DBMail Administrator (DBMA)</title>
	</head><body><div><form method="post" action="$mythisscript"><center><table>
	<tr><td colspan="4"><span class="out">$version on $server(Administering: $dbmail_ver $sqltype : $sqldb : $sqlhost)</span></td></tr>
	<tr><td colspan="4"><span style="color: #005A9C; background-position: top right;background-attachment: fixed; background-repeat: no-repeat;background-image: url(images/bg.jpg);font:140% sans-serif" >User Account : $username </span><span style="font:90% sans-serif" >[ <a title="The manual on user management" href="DBMA_User_Management.htm" rel="external">User Management</a> | <a title="DBMA Help manual" href="DBMA_help.htm" rel="external"> Help </a> ]</span></td></tr>
	<tr><td style="text-align:left">
	<form method="post" action="$mythisscript"><input type="hidden" name="RQT" value="2" /><small>User</small>
	<input type="text" $mouseover $changecase title="Please enter the user ID number or user name." name="userID" value="$userID" size="12" />
	<input title="Search for user." type="submit" onmouseover="this.className='clear';" onmouseout="this.className='letsgo';" class="letsgo" value="User Search" /><input type="hidden" name="RQT" value="2" /></form></td>
	<td style="text-align:left"><form method="post" action="$mythisscript"><input type="hidden" value="all_in_this_group" name="RQT" />
	<input type="hidden" value="$GroupID" name="GroupID" />
	<input title="All Users in Group $GroupID" type="submit" value="List Group $GroupID Users" onmouseover="this.className='clear';" onmouseout="this.className='letsgo';" class="letsgo" /><input type="hidden" name="required" value="GroupID" /></form></td>
	<td style="text-align:left"><form method="post" action="$mythisscript"><input type="hidden" name="RQT" value="aliases_in_this_group" />
	<input type="hidden" value="$GroupID" name="GroupID" />
	<input title="List aliases in Group $GroupID" type="submit" onmouseover="this.className='clear';" onmouseout="this.className='letsgo';" class="letsgo" value="List Group $GroupID Aliases" /><input type="hidden" name="required" value="GroupID" /></form></td>
	<td style="text-align:left;width:52px"><form method="post" action="$mythisscript"><input type="submit" title="Go To Main Screen" style="background-color:#D6CFDE; color:#4602A0" value="Main" /></form></td></tr>
	<tr><td colspan="4"><hr style="background-color:#D6CFDE; color:#D6CFDE;height:20px" /></td></tr></table></center></form></div>
	<div><center><table><tr><td><span class="gr">User</span><br /><big>$username</big></td><td><span class="gr">UserID</span><br />$userID</td><td><span class="gr">Group</span><br />$GroupID</td>
DBMA
        }
        last;
    }
## -See if it has a password and what if any encryption is used.
    my $criptGET =
      $dbh->prepare(
        "SELECT encryption_type FROM $dbmail_users_table WHERE user_idnr = '$userID' LIMIT 1"
      );
    unless ($criptGET->execute())
    {
        $errormessage = "ErrorID: $version.err0.05 <br />
	$DBI::errstr <br />Failed to get encryption_type FROM $dbmail_users_table .";
        &DBMA_ConnectStatus;
    }
    while (my $rv = $criptGET->fetchrow_hashref())
    {
        my $encryption_type = $rv->{'encryption_type'};
        $encrypttype = $encryption_type;
        my $pwGET =
          $dbh->prepare(
            "SELECT passwd FROM $dbmail_users_table WHERE user_idnr = '$userID' LIMIT 1"
          );
        unless ($pwGET->execute())
        {
            $errormessage = "ErrorID: $version.err0.06 <br />
	$DBI::errstr <br />Failed SELECT passwd FROM $dbmail_users_table.";
            &DBMA_ConnectStatus;
        }
        while (my $rv = $pwGET->fetchrow_hashref())
        {
            my $passwd = $rv->{'passwd'};
            $password = $passwd;
            print <<"DBMA";
	<td><span class="gr">Password</span><br />
DBMA
            $passwd = "encrypted"
              if (   ($encryption_type =~ /md5sum/)
                  || ($encryption_type =~ /md5/)
                  || ($encryption_type =~ /crypt/));
            $passwd = "*PLAIN*" if $encryption_type =~ //;
            print "	<span style=\"font-size:9px\">$passwd</span></td>\n";
        }
        print <<"DBMA";
	<td><span class="gr">Crypt</span><br />
DBMA
        print "	<span class=\"out\">$encrypttype</span></td>\n";
    }

## -Get its last login.
    my $llGET =
      $dbh->prepare(
        "SELECT last_login FROM $dbmail_users_table WHERE user_idnr = '$userID' LIMIT 1"
      );
    unless ($llGET->execute())
    {
        $errormessage = "ErrorID: $version.err0.07 <br />
	$DBI::errstr <br />Failed SELECT last_login FROM $dbmail_users_table.";
        &DBMA_ConnectStatus;
    }
    while (my $rv = $llGET->fetchrow_hashref())
    {
        my $output2 = $rv->{'last_login'};
        print <<"DBMA";
	<td><span class="gr">Last Login</span><br />
DBMA
        print "	<span class=\"out\">$output2</span></td>\n";
    }

    if ($DBMail22Version eq "1")
    {
## -Get its cursieve_size. V22 Only
        my $sth =
          $dbh->prepare(
            "SELECT cursieve_size FROM $dbmail_users_table WHERE user_idnr = '$userID' LIMIT 1"
          );
        $sth->execute;
        while (my $rv = $sth->fetchrow_hashref())
        {
            my $output = $rv->{'cursieve_size'};
            print <<"DBMA";
	<td><span class="gr">Cur Sieve</span><br />
DBMA
            print "	<span class=\"out\">$output</span></td>\n";
        }
        $sth->finish;
        undef $output;
## -Get its maxsieve_size. V22 Only
        $sth =
          $dbh->prepare(
            "SELECT maxsieve_size FROM $dbmail_users_table WHERE user_idnr = '$userID' LIMIT 1"
          );
        $sth->execute;
        while (my $rv = $sth->fetchrow_hashref())
        {
            my $output = $rv->{'maxsieve_size'};
            print <<"DBMA";
	<td><span class="gr">Max Sieve</span><br />
DBMA
            print "	<span class=\"out\">$output</span></td>\n";
        }
        $sth->finish;
        undef $output;
    }
    unless ($DBMailOldVersion eq "1")
    {
## -How much mailbox used (older DBMail Db's don't have this so make it invisible if ne exist)
        my $mbGET =
          $dbh->prepare(
            "SELECT curmail_size FROM $dbmail_users_table WHERE user_idnr = '$userID' LIMIT 1"
          );
        unless ($mbGET->execute())
        {
            $errormessage = "ErrorID: $version.err0.08 <br />
	$DBI::errstr <br />Failed SELECT curmail_size FROM $dbmail_users_table.";
            &DBMA_ConnectStatus;
        }
        while (my $rv = $mbGET->fetchrow_hashref())
        {
            my $output3 = $rv->{'curmail_size'};
            print <<"DBMA";
	<td><span class="gr">Current_Mail</span><br /><span class="out">$output3</span></td>
DBMA
        }
    }
## - Mail quota?
    my $mballowedGET =
      $dbh->prepare(
        "SELECT maxmail_size FROM $dbmail_users_table WHERE user_idnr = '$userID' LIMIT 1"
      );
    unless ($mballowedGET->execute())
    {
        $errormessage = "ErrorID: $version.err0.09 <br />
	$DBI::errstr <br />Failed SELECT maxmail_size FROM $dbmail_users_table.";
        &DBMA_ConnectStatus;
    }
    while (my $rv = $mballowedGET->fetchrow_hashref())
    {
        $maxmail_size = $rv->{'maxmail_size'};
        $maxmailsize  = $maxmail_size;
        $maxmailsize =~ s/  / /g;
        print <<"DBMA";
	<td><span class="gr">Limit</span><br /><span class="out">$maxmail_size</span></td>
DBMA
    }
## - Get all its aliases; learn where they go; create search all mailboxes for mail
## - and report what IMAP mailboxes it has.
    print <<"DBMA";
	</tr></table></center></div>
	<div><center><table style="background-position: bottom right;background-attachment: fixed; background-image: url(images/bg.jpg);"><tr><td>
	<span class="gr">Aliases for $username</span></td>
	<td>
DBMA
    if (($allow_read_mail eq "1") || ($DBMail22Version eq "1"))
    {
        print <<"DBMA";
	<span class="gr"><b>$username\'s Mailboxes</b></span>
	<form method="post" action="$mythisscript">
	<input type="hidden" name="RQT" value="33a" /><input type="hidden" name="userID" value="$userID" />
	<input type="hidden" name="username" value="$username" /><input type="hidden" name="required" value="searchterms" />
	<input type="text" onmouseover="this.className='back2';" onmouseout="this.className='back';" name="searchterms" value="$searchterms" size="14" title="enter a string to search for" style="font-size: 9pt; font-family: sans-serif" />
	<input title="Search mail in all $username\'s Mailboxes" type="image" style="width:43px;height:17px;vertical-align:middle;" src="images/search_gr.gif" />
	<span style="font-size:10px;color:green">Headers only?</span><input title="Select to search headers only" type="radio" name="headers_only" value="1" /></form>
DBMA
    }
    print <<"DBMA";
	</td></tr>
	<tr><td><textarea class=\"alias\" name=\"alias\" rows=\"6\" cols=\"65\">
DBMA
    my $output4;
    $usernameDISPLAY = $username;
    if ($usernameDISPLAY eq "anyone")
    {
        $newRQT  = 49;
        $message = "UPDATE ACLs for ANYONE";
    }
    else
    {
        $newRQT  = 50;
        $message = "Add Shared Folder for $usernameDISPLAY from drop list";
    }

if ($sqltype =~ /pgsql/)
{
    my $aGET = $dbh->prepare(
        "SELECT alias, userid, deliver_to FROM $dbmail_aliases_table
    LEFT JOIN $dbmail_users_table ON CAST($dbmail_users_table.user_idnr AS text) = $dbmail_aliases_table.deliver_to
    WHERE LOWER(alias) LIKE LOWER('$username@%') or deliver_to = '$userID' ORDER BY alias"
                            );

    unless ($aGET->execute())
    {
        $errormessage = "ErrorID: $version.err0.10 <br />
          $DBI::errstr <br />Failed Compile query to get aliases";
        &DBMA_ConnectStatus;
    }
    while (($alias, $username, $deliver_to) = $aGET->fetchrow_array)
    {
        &filt($alias) if $alias;
        $alias =~ s/ //         if $alias;
        $alias =~ s/\@/\&#64;/g if $alias;
        my $to  = $deliver_to || "";
        my $who = $username   || "";
        $to =~ s/ //         if $to;
        $to =~ s/\@/\&#64;/g if $to;
        $output4 .= "$alias => $who ($to)\n" if $alias;
    }
    print $output4 if ($output4);
    print "</textarea>";
}

if ($sqltype =~ /mysql/)
{
    my $aGET = $dbh->prepare(
        "SELECT alias, userid, deliver_to from $dbmail_aliases_table
    LEFT JOIN $dbmail_users_table ON $dbmail_users_table.user_idnr=$dbmail_aliases_table.deliver_to
    WHERE LOWER(alias) LIKE LOWER('$username@%') or deliver_to = '$userID' ORDER BY alias"
                            );
    unless ($aGET->execute())
    {
        $errormessage = "ErrorID: $version.err0.10 <br />
          $DBI::errstr <br />Failed Compile query to get aliases";
        &DBMA_ConnectStatus;
    }
    while (($alias, $username, $deliver_to) = $aGET->fetchrow_array)
    {
        &filt($alias) if $alias;
        $alias =~ s/ //         if $alias;
        $alias =~ s/\@/\&#64;/g if $alias;
        my $to  = $deliver_to || "";
        my $who = $username   || "";
        $to =~ s/ //         if $to;
        $to =~ s/\@/\&#64;/g if $to;
        $output4 .= "$alias => $who ($to)\n" if $alias;
    }
    print $output4 if ($output4);
    print "</textarea>";
}

    print <<"DBMA";
	<form method="post" action="$mythisscript"><input type="hidden" name="RQT" value="11" /><input type="hidden" name="newuserID" value="$userID" />
	<input type="hidden" name="username" value="$userID" /><input type="hidden" name="GroupID" value="$GroupID" /><input type="hidden" name="mailboxsize" value="$maxmailsize" />
	<input type="hidden" name="password" value="$password" /><input type="hidden" name="encrypttype" value="$encrypttype" />
	<input type="submit" title="MODIFY $usernameDISPLAY\'s ($userID) Account" value="Modify $usernameDISPLAY\'s Account" onmouseover="this.className='letsgo';" onmouseout="this.className='c16';" class="c16" style="margin-bottom:10px;margin-top:10px" /><a target="_blank" onmouseover="self.status='Help';return true" onmouseout="self.status='DBMA';return true" href="DBMA_help.htm#user_account_window"><img class="q" src="images/q.gif" alt="Modify User Account Help" /></a></form>
	<form method="post" action="$mythisscript"><input type="hidden" name="userID" value="$userID" /><input type="hidden" name="RQT" value="4" /><input class="c15" type="submit" onclick="return confirm('DELETE $usernameDISPLAY: Are you sure?')" title="DELETE $usernameDISPLAY\'s ($userID) Account? Be sure!" onmouseover="this.className='caution';" onmouseout="this.className='c15';" value="Delete $usernameDISPLAY\'s Account" /></form><!--Copyright dbma.ca--></td>
	<td style="text-align:left;float:left; vertical-align:top;line-height:100%">
DBMA
    if (($allow_read_mail eq "1") || ($DBMail22Version eq "1"))
    {
        &get_mailbox_list;
    }
    if (($DBMailOldVersion eq "0") && ($ACL_ctrl eq "1"))
    {
        $sth =
          $dbh->prepare(
            "SELECT user_idnr FROM $dbmail_users_table WHERE LOWER(userid) = LOWER('__public__') LIMIT 1"
          );
        unless ($sth->execute)
        {
            $errormessage = "
	ErrorID: $version.err0.11 <br />$DBI::errstr <br />Failed PUBLIC Query";
            &DBMA_ConnectStatus;
        }
        if (($PUBLICuserID) = $sth->fetchrow_array)
        {
            &fetch_shared_folders($PUBLICuserID, $userID);
        }
    }

    print <<"DBMA";
	</td></tr></table></center></div>
DBMA
    if (($DBMailOldVersion eq "0") && ($ACL_ctrl eq "1"))
    {
        print <<"DBMA";
	<div><center><form method="post" action="$mythisscript"><table style="font-size:70%">
	<tr style="background: #ffffc4"><td colspan="2"><input type="hidden" name="RQT" value="$newRQT" />
DBMA
        print "	$message\n" if ($message);
        print <<"DBMA";
	<a target="_blank" onmouseover="self.status='ACL Help';return true" onmouseout="self.status='DBMA';return true" href="DBMA_help.htm#acl"><img class="q" src="images/q.gif" alt="ACL Help" /></a></td>
	<td title="lookup: mailbox is visible to LIST/LSUB commands ">lookup</td>
	<td title="read: SELECT the mailbox, perform CHECK, FETCH, PARTIAL SEARCH, COPY from mailbox ">read</td>
	<td title="seen: keep seen/unseen information across session ">seen</td>
	<td title="write: STORE flags other than SEEN and DELETED ">write</td>
	<td title="insert: perform APPEND, COPY into mailbox ">insert</td>
	<td title="post: send mail to submission address for mailbox ">post</td>
	<td title="create: CREATE new sub-mailboxes in any implementation defined hierarchy ">create</td>
	<td title="delete: STORE DELETED flag perform EXPUNGE ">delete</td>
	<td title="administer: perform SETACL ">administer</td></tr>
	<tr class="dl"><td style="background:#ffffc4" title="Share a folder."><input type="submit" value="Add ACL" onmouseover="this.className='clear';" onmouseout="this.className='letsgo';" class="letsgo" title="Share a folder."/>
	<input type="hidden" value="$userID" name="userID" /></td>
	<td style="background:#ffffc4" title="Select a Shared Public Folder you want
DBMA
        print "	$usernameDISPLAY\n" if ($usernameDISPLAY);
        print <<"DBMA";
	to have access on.">
	<select style="font-size:10px;color:navy" size="1" name="mailbox_idnr">
DBMA
        print "	$public_mailboxes\n"         if ($public_mailboxes);
        print "	$user_ACL_avail_mailboxes\n" if ($user_ACL_avail_mailboxes);
        my $struct = "type=\"text\" style=\"font-size:9px;cursor:help\"";
        print <<"DBMA";
	</select></td>
	<td style="background:#ffffc4"><input $struct name="lookup_flag" size="2" value="1" title="lookup: mailbox is visible to LIST/LSUB commands " /></td>
	<td style="background:#ffffc4"><input $struct name="read_flag" size="2" value="1" title="read: SELECT the mailbox, perform CHECK, FETCH, PARTIAL SEARCH, COPY from mailbox " /></td>
	<td style="background:#ffffc4"><input $struct name="seen_flag" size="2" value="1" title="seen: keep seen/unseen information across session " /></td>
	<td style="background:#ffffc4"><input $struct name="write_flag" size="2" value="1" title="write: STORE flags other than SEEN and DELETED " /></td>
	<td style="background:#ffffc4"><input $struct name="insert_flag" size="2" value="1" title="insert: perform APPEND, COPY into mailbox " /></td>
	<td style="background:#ffffc4"><input $struct name="post_flag" size="2" value="1" title="post: send mail to submission address for mailbox " /></td>
	<td style="background:#ffffc4"><input $struct name="create_flag" size="2" value="0" title="create: CREATE new sub-mailboxes in any implementation defined hierarchy " /></td>
	<td style="background:#ffffc4"><input $struct name="delete_flag" size="2" value="0" title="delete: STORE DELETED flag perform EXPUNGE " /></td>
	<td style="background:#ffffc4"><input $struct name="administer_flag" size="2" value="0" title="administer: perform SETACL " /></td></tr>
	</table></form></center></div>
DBMA
        &fetch_usr_acl_folders($userID);
        $user_mailboxes = $user_mailboxes || "none";
        $PUBLICuserID   = $PUBLICuserID   || "none";

        if ($user_mailboxes)
        {
            print <<"DBMA";
	<div><center><table><tr><td style="background:#ffffc4"><form method="post" action="$mythisscript">
	<span class="out">These are the shared folders of mail user "
DBMA
            print "	$usernameDISPLAY\n" if ($usernameDISPLAY);
            print <<"DBMA";
	":</span><select style="font-size:11px" name="mailbox_idnr">
DBMA
            print "	$user_mailboxes\n" if ($user_mailboxes);
            print <<"DBMA";
	</select><input type="hidden" name="RQT" value="47" />
	<input type="hidden" value="$userID" name="userID" /><input type="hidden" name="PUBLICuserID" value="$PUBLICuserID" /><input type="image" value ="submit" src="images/delete.gif" onmouseover="self.status='Delete Shared Folder';return true" onmouseout="self.status='DBMA';return true" style="width:37px;height:14px" title="Delete Folder" onclick="return confirm('DELETE Shared Folder: Are you sure?')" /><br /></form></td></tr>
	</table></center></div>
DBMA
        }

    }
    &auto_notifications($userID);
    &auto_replies($userID, $usernameDISPLAY);

    if ($DBMail22Version eq "1")
    {
        ($login, $sock_allow, $sock_deny, $usermap_userid) = 0;
        $sth->finish() if ($sth);
        $sth =
          $dbh->prepare(
            "SELECT login, sock_allow, sock_deny, userid FROM $dbmail_usermap_table where userid = '$usernameDISPLAY' OR login = '$usernameDISPLAY'"
          );
        $sth->execute();
        if (($login, $sock_allow, $sock_deny, $usermap_userid) =
            $sth->fetchrow_array)
        {
            $str .=
              "<div><center><table style=\"width:738px;background-color:#d6cfde\"><tr><td>
	<form method=\"post\" action=\"$mythisscript\" />
	<input title=\"Set UserMap Directives for $usernameDISPLAY\" type=\"submit\" value=\"User Maps\" onmouseover=\"this.className=\'clear\';\" onmouseout=\"this.className=\'letsgo\';\" class=\"letsgo\" />
	<a rel=\"external\" onmouseover=\"self.status=\'Help\';return true\" onmouseout=\"self.status=\'DBMA\';return true\" href=\"DBMA_help.htm#user_map\"><img class=\"q\" src=\"images/q.gif\" alt=\"Auto Reply Warning and Help File\" /></a>
	<input title=\"LOCK OUT this user ($usernameDISPLAY). Overrides all settings\" onmouseover=\"this.className=\'caution\';self.status=\'Lock Out User - Turn off this account\';return true\" onmouseout=\"this.className=\'c7\';self.status=\'DBMA\';return true\" type=\"radio\" name=\"deny_user_access\" value=\"DENY\" onclick=\"return alert(\'This will prevent $usernameDISPLAY from fetching mail on POP3 or IMAP.\')\" /><span style=\"color:red;background:#d6cfde;font-size:11px;font-weight:bold\"> LOCK </span>
	<input title=\"CLEAR all usermap settings (for $usernameDISPLAY)\" onmouseover=\"this.className=\'letsgo\';self.status=\'CLEAR all usermap settings for $usernameDISPLAY\';return true\" onmouseout=\"this.className=\'c7\';self.status=\'DBMA\';return true\" type=\"radio\" name=\"clear_user_mapping\" value=\"CLEAR\" /><span style=\"color:green;background:#d6cfde;font-size:11px;font-weight:bold\">CLEAR</span>
	<input type=\"hidden\" name =\"RQT\" value=\"65\" /><input type=\"hidden\" name=\"userID\" value=\"$usernameDISPLAY\" />
	<input type=\"text\" name=\"login\" title=\"login name\" style=\"font-family:arial;font-size:10px;background-image: url(images/usermap_login.jpg)\" size=\"12\" value=\"$login\" />
	<input type=\"text\" title=\"socket allow format is inet:xxx.xxx.xxx.xxx:port\" name=\"sock_allow\" value=\"$sock_allow\" style=\"font-family:arial;font-size:10px;background-image: url(images/usermap_allow.jpg)\" size=\"19\" />
	<input type=\"text\" title=\"socket deny format is inet:xxx.xxx.xxx.xxx:port\" name=\"sock_deny\" value=\"$sock_deny\" style=\"font-family:arial;font-size:10px;background-image: url(images/usermap_deny.jpg)\" size=\"19\" />
	<input type=\"text\" name=\"usermap_userid\" title=\"userid\" style=\"font-family:arial;font-size:10px;background-image: url(images/usermap_userid.jpg)\" value=\"$usermap_userid\" size=\"12\" />
	</form></td></tr></table></center></div>";
        }
        else
        {
            print <<"DBMA";
	<div><center><table style="width:738px;background-color:#d6cfde"><tr><td>
	<form method="post" action="$mythisscript" />
	<input title="Set UserMap Directives for $usernameDISPLAY" type="submit" value="User Maps" onmouseover="this.className='front';" onmouseout="this.className='letsgo';" class="letsgo" />
	<a target="_blank" onmouseover="self.status='Help';return true" onmouseout="self.status='DBMA';return true" href="DBMA_help.htm#user_map"><img class="q" src="images/q.gif" alt="Auto Reply Warning and Help File" /></a>
	<input title="LOCK OUT this user ($usernameDISPLAY). Overrides all settings" onmouseover="this.className='caution';self.status='LOCK OUT $usernameDISPLAY Turn off $usernameDISPLAY account';return true" onmouseout="this.className='c7';self.status='DBMA';return true" type="radio" name="deny_user_access" value="DENY" onclick="return alert('This will prevent $usernameDISPLAY from fetching mail on POP3 or IMAP.')" /><span style="color:red;background:#d6cfde;font-size:11px;font-weight:bold"> LOCK </span>
	<input title="CLEAR all usermap settings for $usernameDISPLAY" onmouseover="this.className='letsgo';self.status='CLEAR this accounts settings';return true" onmouseout="this.className='c7';self.status='DBMA';return true" type="radio" name="clear_user_mapping" value="CLEAR" /><span style="color:green;background:#d6cfde;font-size:11px;font-weight:bold">CLEAR</span>
	<input type="hidden" name ="RQT" value="66" /><input type="hidden" name="userID" value="$usernameDISPLAY" />
	<input type="text" name="login" title="login name" style="font-family:arial;font-size:10px;color:#6a6a6a;background-image: url(images/usermap_login.jpg)" size="12" value="$usernameDISPLAY" />
	<input type="text" title="socket allow format is inet:xxx.xxx.xxx.xxx:port" name="sock_allow" value="" style="font-family:arial;font-size:10px;background-image: url(images/usermap_allow.jpg)" size="19" />
	<input type="text" title="socket deny format is inet:xxx.xxx.xxx.xxx:port" name="sock_deny" value="" style="font-family:arial;font-size:10px;background-image: url(images/usermap_deny.jpg)" size="19" />
	<input type="text" name="usermap_userid" title="userid" style="font-family:arial;font-size:10px;color:#6a6a6a;background-image: url(images/usermap_userid.jpg)" value="$usernameDISPLAY" size="12" />
	</form></td></tr></table></center></div>
DBMA
            $dbh->disconnect() if ($dbh);
            &end_HTML;
        }
        print $str;
        undef $str;
    }
    &end_HTML;
}
############################################################## - sub Create_User_Account_MODIFY_Window RQT11
sub Create_User_Account_MODIFY_Window ($)
{
    my $userID     = $newuserID;
    my $deliver_to = "";
    &defaults;
    unless ($RESTRICTGroupID eq "any")
    {
        $placethisforRESTRICTGroupID =
          "<input type=\"hidden\" value=\"$RESTRICTGroupID\" name=\"GroupID\" />$RESTRICTGroupID";
        $title =
          "<title>$RESTRICTGroupIDName - DBMA Update User $username</title>";
    }
    else
    {
        $sth =
          $dbh->prepare(
            "SELECT client_idnr FROM $dbmail_users_table WHERE user_idnr = '$newuserID'"
          );
        $sth->execute();
        if (($GroupID) = $sth->fetchrow_array)
        {
            $title = "<title>DBMA Update User $username</title>";
            $placethisforRESTRICTGroupID =
              "<input type=\"text\" onmouseover=\"this.className=\'front\';\" onmouseout=\"this.className=\'back\';\" size=\"3\" value=\"$GroupID\" name=\"GroupID\" />";
        }
    }
    my $forwards;
    $sth =
      $dbh->prepare(
        "SELECT user_idnr, userid, passwd, client_idnr, maxmail_size, encryption_type, last_login FROM $dbmail_users_table WHERE user_idnr = '$newuserID'"
      );
    $sth->execute();
    while (
           (
            $userID,      $username,    $password, $myGroupID,
            $mailboxsize, $encrypttype, $last_login
           )
           = $sth->fetchrow_array
          )
    {
        $username =~ s/__public__/\#Public/;
        my $messagebody = "Dear $username:\n
Here is the updated information for your email account.
Your account name is $username 
Your mailbox capacity is $mailboxsize bytes.
Your password is everything between the brackets: ($password)\n\n
Yours truly,\n$admin_address";
        &meta;
        print $title;
        print "	</head><body>\n";
        print <<"DBMA";
	<div><center><table width="738px">
	<tr><td colspan="2" style="font-size:11px;color:#6a6a95;background:#F8F8FF;width:738px">$version on $server $date</td></tr></table></center></div><div><center><table class="c5" cellspacing="0" cellpadding="0" width="738px" border="0"><tbody>
	<tr><td class="c1" colspan="2"><h1>Modify User Account : $newuserID - $username</h1></td></tr>
	<tr><td style="text-align:right;width:100%;float:right" colspan="2" >[ <b><a href="$mythisscript?$newuserID">$username\'s Account</a></b> | <a href="$mythisscript"><b>Main</b></a> |
	<a target="_blank" href="DBMA_help.htm"  onclick="return confirm('_______________________Help_______________________\\n\\n\\nWith this tool:\\n\\nYou can modify the user name; change a password and encryption type;\\nadjust the mailbox size; add or remove aliases; add a new user to the group;\\nlist the entire group; and email a notification of any changes made to the user.\\n\\nCHANGE PASSWORD:\\n\\n1 - Type plain, md5sum, md5 or crypt for encryption type. \\n\\n2 - Enter the new password in the space provided, \\noverwriting the original and select the *Change Password* check box.\\n\\n3 - Press *Update...* to commit the changes to your database.\\n\\n Click *OK* for more help or *CANCEL* to close.')"><b> Help</b></a> ]</td></tr>
	<tr><td><form method="post" action="$mythisscript"><input type="hidden" name="RQT" value="2" />
	<input type="text" $mouseover title="Enter another user ID or name." value="$username" name="userID"
	size="19" /><input title="Search for another user" type="submit" onmouseover="this.className='clear';" onmouseout="this.className='letsgo';" class="letsgo" value="User Search" /></form></td><td>
	<form method="post" action="$mythisscript"><input type="hidden" name="RQT" value="21" /><input type="hidden" name="mailfrom" value="$admin_address" /><input type="hidden" name="mailto" value="$username" /><input type="hidden" name="subject" value="Your Email Account" />
	<input type="hidden" name="message" value="$messagebody" /><b>$message</b>
	<input style="margin-top:0px" class="c17" type="submit" onmouseover="this.className='c18';" onmouseout="this.className='c17';" value="Email $username" /></form></td></tr></tbody></table></center></div>
	<div><center><form action="$mythisscript" method="post"><table class="c5" cellspacing="0" cellpadding="0" width="738px" border="0"><tbody>
	<tr><td>User ID Number</td><td ><input type="hidden" name="RQT" value="12" /><input type="hidden" value="$newuserID" name="newuserID" />$newuserID</td><td ><!--future use--></td></tr>
	<tr><td>Name</td><td ><input type="text" $mouseover name="username" value="$username" size="64" style="font-size: 10px; font-family: Arial" /></td><td ><input type="hidden" name="required" value="GroupID,password,username" /></td></tr>
	<tr><td>Password</td><td ><input type="text" $mouseover name="password" size="64" value="$password" style="font-size: 10px; font-family: Arial" /></td><td ><!--future use--></td></tr>
	<tr><td>Group</td><td >$placethisforRESTRICTGroupID</td><td ><!--future use--></td></tr>
	<tr><td>Encrypt Type</td><td ><input type="text" $mouseover size="6" value="$encrypttype" name="encrypttype" /><small>Type plain, md5sum, md5 or crypt. Check "Change Password" at right.</small></td><td >Change Password<input type="checkbox" name="changepassword" value="pBq1XZ6StL9xpjFUrOlJ03cRws" />
	<a target="_blank" href="DBMA_help.htm"  onclick="return confirm('_______________________Help_______________________\\n\\n\\nWith this tool:\\n\\nYou can modify the user name; change a password and encryption type;\\nadjust the mailbox size; add or remove aliases; add a new user to the group;\\nlist the entire group; and email a notification of any changes made to the user.\\n\\nCHANGE PASSWORD:\\n\\n1 - Type plain, md5sum, md5 or crypt for encryption type. \\n\\n2 - Enter the new password in the space provided, \\noverwriting the original and select the *Change Password* check box.\\n\\n3 - Press *Update...* to commit the changes to your database.\\n\\n Click *OK* for more help or *CANCEL* to close.')">Help</a></td></tr>
	<tr><td>MailBox Quota</td><td ><input title="Enter zeroes or 10k, 10m, 1g etc." size="9" value="$mailboxsize" $mouseover type="text" name="mailboxsize" /></td><td ><!--future user--></td></tr>
	<tr><td><span style="float:right">Add an Email Alias here &gt;</span></td><td colspan="2"><input title="Add an email alias for $username" type="text" $mouseover name="newalias" size="42" /><br />
	<input class="c7" type="submit" title="update email account" onmouseover="this.className='letsgo';" onmouseout="this.className='c7';" value="Update $username" name="submit" /></td></tr>
	<tr><td style="font-size:10px"colspan="3">To create open aliases for LAN accounts, like '\@domain.int' you must Force Bypass RFC-Compliant Alias Check <input onmouseover="this.className='caution';self.status='This will force bypass alias checking.';return true" onmouseout="this.className='c11';self.status='DBMA';return true" style="height:20px" type="radio" value="1" name="bypass" />on<input type="radio" value="0" name="bypass" />off
	<br />DBMA will display these in "My Groups" panel as '* \@domain'. <span style="color:black">Note: Possible risks. Know what you are doing.</span></td></tr>
	<tr><td colspan="3"><hr style="color:#D6CFDE;height:2px" /></td></tr></tbody></table></form></center></div>
	<div><center><table class="c5" cellspacing="0" cellpadding="0" width="738px">
	<tr style="background:#FDF5E6"><td style="text-align: left"><form method="post" action="$mythisscript"><input type="hidden" name="RQT" value="3" />
	<input onmouseover="this.className='clearl';" onmouseout="this.className='grl';" class="grl" type="submit" value="Add Another User" /></form></td>
	<td style="text-align: Left"><form method="post" action="$mythisscript"><input type="hidden" name="RQT" />
	<input type="hidden" value="$newuserID" name="userID" /><input onmouseover="this.className='clearl';" onmouseout="this.className='grl';" class="grl" type="submit" title="$username Account" value="Open $username\'s Account Window"/></form></td>
	<td style="text-align: Left"><form method="post" action="$mythisscript"><input type="hidden" name="RQT" value="all_in_this_group" /><input onmouseover="this.className='clearl';" onmouseout="this.className='grl';"
	class="grl" title="All Users in Group $GroupID" type="submit" value="List All Group $GroupID" />
	<input type="hidden" name="GroupID" value="$myGroupID" /></form></td>
	<td style="text-align: Left"><form method="post" action="$mythisscript"><input onmouseover="this.className='clearl';" onmouseout="this.className='grl';" class="grl" type="submit" value="Main" /></form></td></tr></table></center></div>
	<div><center><table class="c5" cellspacing="2" cellpadding="0" width="738px"><tr><td colspan="4"><hr style="color:#D6CFDE;height:2px" /></td></tr>
	<tr><td colspan="4"><h3><br />Administer Aliases &amp; Forwards for $username</h3></td></tr>
DBMA
if ($sqltype =~ /pgsql/)
{
        $forwards =
          $dbh->prepare(
            "SELECT alias_idnr, alias, userid, deliver_to 
FROM $dbmail_aliases_table
LEFT JOIN $dbmail_users_table ON CAST($dbmail_users_table.user_idnr AS text) = $dbmail_aliases_table.deliver_to
WHERE LOWER(alias)
LIKE LOWER('$username@%')
OR LOWER(alias)
LIKE '%@%'
AND LOWER(deliver_to) = LOWER('$userID')
OR LOWER(alias) = LOWER('$username@%')
ORDER by alias");
}
if ($sqltype =~ /mysql/)
{
        $forwards =
          $dbh->prepare(
            "SELECT alias_idnr, alias, userid, deliver_to FROM $dbmail_aliases_table LEFT JOIN $dbmail_users_table ON $dbmail_users_table.user_idnr=$dbmail_aliases_table.deliver_to WHERE LOWER(alias) LIKE LOWER('$username@%') OR LOWER(alias) LIKE '%@%' AND LOWER(deliver_to) = LOWER('$userID') OR LOWER(alias) = LOWER('$username@%') ORDER by alias"
          );
}
        $forwards->execute();

        while (($alias_idnr, $alias, $username, $deliver_to) =
               $forwards->fetchrow_array)
        {
            $alias_idnr = $alias_idnr || "";
            $alias      = $alias      || "";
            $username   = $username   || $FORM{'username'} || "";
            $deliver_to = $deliver_to || "";
            our $deliver_from = $alias;
            $alias =~ s/ //         if $alias;
            $alias =~ s/\@/\&#64;/g if $alias;
            $str .= "	<tr title=\"$alias\" style=\"background:#FDF5E6\">
	<td style=\"text-align:left;width:142px\"><form action=\"$mythisscript\" method=\"post\">
	<input name=\"deliver_from\" value=\"$deliver_from\" type=\"hidden\" />
        <input type=\"hidden\" name=\"alias_idnr\" value=\"$alias_idnr\" />
        <input type=\"hidden\" name=\"userID\" value=\"$userID\" /><input type=\"hidden\" name=\"RQT\" value=\"13a\" />
	<input style=\"font-family:arial,sans-serif:font-size:9px\" type=\"submit\" title=\"Change delivery of $deliver_from to another E-Maill address or local user\" value=\"Forward or Edit\" onmouseover=\"this.className=\'clearl\';\" onmouseout=\"this.className=\'grl\';\" class=\"grl\" /></form></td>
	<td style=\"text-align:left\"><input type=\"text\" size=\"32\" name=\"alias\" value=\"$alias\" /><b>==></b> <a onmouseover=\"self.status=\'Open this account\';return true\" onmouseout=\"self.status=\'DBMA\';return true\" title=\"Open this account\" href=\"$mythisscript?$deliver_to\">$deliver_to</a> <em>Owner</em>: $username</td>
	<td style=\"text-align:right\"><form method=\"post\" action=\"$mythisscript\">
	<input type=\"hidden\" name=\"RQT\" value=\"41\" /><input type=\"hidden\" name=\"alias\" value=\"$alias\" />
	<input type=\"hidden\" name=\"alias_idnr\" value=\"$alias_idnr\" /><input type=\"hidden\" name=\"userID\" value=\"$userID\" /><input style=\"font-family:arial,sans-serif:font-size:9px\" type=\"submit\" title=\"delete $alias by alias_idnr $alias_idnr\" value =\"Delete\" class=\"nowarn\" onmouseover=\"this.className=\'warn\';\" onmouseout=\"this.className=\'nowarn\';\" onclick=\"return confirm(\'DELETE alias: $alias ?\')\" /></form></td><td  style=\"text-align:right\"></td></tr>\n";
        }
    }
    $sth->finish() if ($sth);
    print $str     if ($str);
    print <<"DBMA";
	<tr><td colspan="4"><hr style="background-color:#D6CFDE; color:#D6CFDE;height:20px" /></td></tr></table></center></div>
DBMA
    end_HTML;
    exit;
}
############################################################## - sub get_mailbox_list
sub get_mailbox_list
{
    $sth = $dbh->prepare(
        "SELECT userid, mailbox_idnr, name FROM $dbmail_mailboxes_table
LEFT JOIN $dbmail_users_table ON $dbmail_mailboxes_table.owner_idnr = $dbmail_users_table.user_idnr
WHERE owner_idnr = '$userID'
ORDER BY $dbmail_mailboxes_table.name"
                        );
    unless ($sth->execute())
    {
        print
          "<span class=\"er\">$DBI::errstr <br />Failed get_mailbox_list.</span>";
    }
    $numrows = $sth->rows;
    while (($username, $mailbox_idnr, $mailbox_name) = $sth->fetchrow_array)
    {
        $username =~ s/__public__/\#Public/;
        $str5 .=
          "	<form title=\"Click one of the $numrows mailbox icons to list messages in box or search all mailboxes.\" method=\"post\" action=\"$mythisscript\">
	<input type=\"hidden\" value=\"$userID\" name=\"userID\" /><input type=\"hidden\" value=\"$mailbox_idnr\" name=\"mailbox_idnr\" />
	<input type=\"hidden\" value=\"$mailbox_name\" name=\"mailbox_name\" /><input type=\"hidden\" value=\"$username\" name=\"username\" />
	<input title=\"Open $mailbox_name Mailbox\" type=\"image\" src=\"images/mailbox.gif\" value=\"$mailbox_name\" /><small>$mailbox_name</small></form>\n";
        $user_ACL_avail_mailboxes .=
          "	<option value=\"$mailbox_idnr\">$usernameDISPLAY\/$mailbox_name</option>\n";
    }
    print $str5    if ($str5);
    undef $str5    if ($str5);
    $sth->finish() if ($sth);
}
############################################################## - sub get_mail_list
sub get_mail_list
{
    &meta;
    $sth = $dbh->prepare(
        "SELECT message_idnr, $dbmail_physmessage_table.internal_date, $dbmail_messages_table.physmessage_id, unique_id, rfcsize, messagesize, seen_flag, answered_flag, deleted_flag, status 
FROM $dbmail_messages_table
LEFT JOIN $dbmail_physmessage_table ON $dbmail_messages_table.physmessage_id = $dbmail_physmessage_table.id
WHERE $dbmail_messages_table.mailbox_idnr = '$mailbox_idnr'
ORDER BY $dbmail_physmessage_table.internal_date desc"
                        );
    unless ($sth->execute())
    {
        print
          "<span class=\"er\">$DBI::errstr <br />Failed get_mail_list - This may not work in older versions.</span>";
    }
    $numrows = $sth->rows;
    while (
           (
            $messageID,    $internal_date, $physmessage_id, $unique_id,
            $rfcsize,      $messagesize,   $seen_flag,      $answered_flag,
            $deleted_flag, $status
           )
           = $sth->fetchrow_array
          )
    {
        $seen_flag     =~ s/1/YES/g;
        $seen_flag     =~ s/0/NO/g;
        $answered_flag =~ s/1/YES/g;
        $answered_flag =~ s/0/NO/g;
        $deleted_flag  =~ s/1/YES/g;
        $deleted_flag  =~ s/0/NO/g;
        $str10 .=
          "	<tr style=\"font-size:11px\"><td><form method=\"post\" action=\"$mythisscript\"><input type=\"hidden\" value=\"$userID\" name=\"userID\" /><input type=\"hidden\" value=\"$mailbox_name\" name=\"mailbox_name\" />
	<input type=\"hidden\" value=\"$username\" name=\"username\" /><input type=\"hidden\" name=\"physmessage_id\" value=\"$physmessage_id\" /><input type=\"hidden\" value=\"$messageID\" name=\"messageID\" /><input type=\"hidden\" value=\"$mailbox_name\" name=\"mailbox_name\" /><input type=\"hidden\" value=\"$deleted_flag\" name=\"deleted_flag\" /><input type=\"hidden\" value=\"$seen_flag\" name=\"seen_flag\" /><input title=\"Open id $physmessage_id having message_idnr $messageID\" type=\"image\" src=\"images/read_mail.gif\" onmouseover=\"this.className=\'letsgo\';\" onmouseout=\"this.className=\'notseen\';\" class=\"notseen\"/></form></td>
	<td>$messageID</td><td><b style=\"color:#6a6a95\"> $internal_date</b></td><td>$mailbox_name</td><td>$unique_id</td><td>$rfcsize</td><td>$messagesize</td></tr>
	<tr style=\"font-size:11px\"><td>Seen=<b>$seen_flag</b></td><td>Answered=<b>$answered_flag</b></td><td>Marked Delete = <b>$deleted_flag</b></td><td>Status = <b>$status</b></td>
	<td title=\"Mark this message for deletion by next dbmail-util run.\"><form method=\"post\" action=\"$mythisscript\"><input type=\"hidden\" value=\"31\" name =\"RQT\" />
	<input type=\"hidden\" value=\"$mailbox_name\" name =\"mailbox_name\" /><input type=\"hidden\" value=\"$messageID\" name =\"messageID\" /><input type=\"hidden\" value=\"$userID\" name=\"userID\" /><input type=\"hidden\" value=\"$username\"  name=\"username\" /><input type=\"image\" value =\"submit\" src=\"images/delete.gif\" onmouseover=\"self.status=\'Delete Mail\';return true\" onmouseout=\"self.status=\'DBMA\';return true\" style=\"width:37px;height:14px\" /></form></td>
	<td colspan=\"2\" title=\"UnDelete this message\"><form method=\"post\" action=\"$mythisscript\"><input type=\"hidden\" value=\"32\" name =\"RQT\" />
	<input type=\"hidden\" value=\"$mailbox_name\" name =\"mailbox_name\" /><input type=\"hidden\" value=\"$messageID\" name =\"messageID\" /><input type=\"hidden\" value=\"$userID\" name=\"userID\" /><input type=\"hidden\" value=\"$username\"  name=\"username\" />
	<input type=\"image\" value =\"submit\" src=\"images/undelete.gif\" onmouseover=\"self.status=\'UnDelete this Message\';return true\" onmouseout=\"self.status=\'DBMA\';return true\" style=\"width:49px;height:16px\" /></form></td></tr>
	<tr><td colspan=\"7\"><hr style=\"background-color:#D6CFDE; height:4px; color:#D6CFDE\" /></td></tr>\n";
    }
    print <<"DBMA";
	<title>DBMA Messages: $username $mailbox_name</title>
	</head>
	<body><div><center><table>
	<tr><td title="Mark all $numrows messages on this page ($username $mailbox_name $mailbox_idnr) for deletion by the next dbmail-util run.">
	<form method="post" action="$mythisscript">
	<input type="hidden" value="34" name ="RQT" />
	<input type="hidden" value="$mailbox_name" name ="mailbox_name" />
	<input type="hidden" value="$mailbox_idnr" name ="mailbox_idnr" />
	<input type="hidden" value="$userID" name="userID" />
	<input type="hidden" value="$username"  name="username" />
	<input onclick="return confirm('DELETE ALL MAIL? Are you very sure?')" onmouseover="this.className='warndm';" onmouseout="this.className='dm';" type="submit" class="dm" value="Delete $numrows $mailbox_name messages " name="Submit"></form></td>
	<td title="Undelete all the mail on this page. ($username $mailbox_name $mailbox_idnr)">
	<form method="post" action="$mythisscript">
	<input type="hidden" value="35" name ="RQT" />
	<input type="hidden" value="$mailbox_name" name ="mailbox_name" />
	<input type="hidden" value="$mailbox_idnr" name ="mailbox_idnr" />
	<input type="hidden" value="$userID" name="userID" />
	<input type="hidden" value="$username"  name="username" />
	<input onclick="return confirm('Are you sure you want to UNDELETE this mail?')" type="submit" onmouseover="this.className='un';" onmouseout="this.className='undm';" class="undm" value="Undelete $numrows $mailbox_name messages " name="Submit"></form></td></tr></table></center></div><div><center><table>
	<tr><td colspan="7"><h3><span style="font-family:arial,sans-serif;font-size:105%;background-color:#FFFFc4;font-weight:bold">$numrows messages in $username\/$mailbox_name</span> <a href="$mythisscript?$userID">$username\'s Account</a> | <a href="$mythisscript">Main Menu</a></h3></td></tr>
	<tr><td title="Looking for a particular message? Enter a search string. DBMA will return the most recent message matching your string" colspan="4"><form method="post" action="$mythisscript">
	<input type="hidden" name="RQT" value="33" />
	<input type="hidden" value="$mailbox_name" name ="mailbox_name" />
	<input type="hidden" value="$mailbox_idnr" name ="mailbox_idnr" />
	<input type="hidden" value="$userID" name="userID" />
	<input type="hidden" value="$username"  name="username" />
	<input type="hidden" name="required" value="searchterms" />
	<input type="text" $mouseover name="searchterms" size="20" style="font-size: 9pt; font-family: sans-serif" />
	<input type="submit" title="returns single best match" class="c7" onmouseover="this.className='letsgo';" onmouseout="this.className='clear';" value="Search $mailbox_name" name="Submit" /></form></td><td style="text-align:right" colspan="3">
DBMA
    $searchterms =~ s/\</\&\#60\;/g;
    $searchterms =~ s/\>/\&\#62\;/g;
    $searchterms =~ s/\@/\&\#64\;/g;
    $searchterms =~ s/\^/\&\#136\;/g;
    print <<"DBMA";
	<form method="post" action="$mythisscript">
	<input type="hidden" name="RQT" value="33a" /><input type="hidden" name="userID" value="$userID" />
	<input type="hidden" name="username" value="$username" /><input type="hidden" name="required" value="searchterms" />
	<input type="text" $mouseover name="searchterms" value="$searchterms" style="font-size:9pt;font-family: sans-serif" size="20" title="Enter your search terms. DBMA will search all mailboxes." /><!--&#67;&#111;&#112;&#121;&#114;&#105;&#103;&#104;&#116; &#77;&#105;&#107;&#101; &#97;&#116; &#109;&#111;&#98;&#114;&#105;&#101;&#110;&#46;&#99;&#111;&#109;-->
	<input title="Search mail in all $username\'s Mailboxes" class="c7" onmouseover="this.className='letsgo';" onmouseout="this.className='clear';" value="Search all folders" type="submit" />
	<br /><span style="font-size:12px;color:green">Search header fields only?</span><input title="Select to search headers only" type="radio" name="headers_only" value="1" /></form></td></tr>
	<tr><td><span class="gr">Read Message</span></td>
	<td><span class="gr">Message ID</span></td>
	<td><span class="gr">Date</span></td>
	<td><span class="gr">Mailbox</span></td>
	<td><span class="gr">Unique ID</span></td><td><span class="gr">RFCSize</span></td><td><span class="gr">Size</span></td></tr>
DBMA
    print $str10       if ($str10);
    $sth->finish()     if ($sth);
    $dbh->disconnect() if ($dbh);
    print "	</table></center></div>\n";
    end_HTML;
    exit;
}
############################################################## - sub get_message
sub get_message
{
## Problem PERL MODULE DBI::mysql 3.0002_4 is seriously broken for LONGBLOBS
## dbmail_messageblks.messageblk has changed to LONGBLOB binary in version 2.0.9
## so must functions in DBMA will fail due to memory constraints if they relate in any way to
## dbmail_messageblks.messageblk and DBI::mysql 3.0002_4 is installed
## FYI
## TINYTEXT and TINYBLOB - A TEXT/BLOB with max length of 255 characters.
## TEXT and BLOB - A TEXT/BLOB with max length of 65535 characters
## MEDIUMTEXT and MEDIUMBLOB - A TEXT/BLOB with max length of 16777216 characters.
## LONGTEXT and LONGBLOB - A TEXT/BLOB with max length of 4294967295 characters.

    if (($DBMail22Version eq "1") && ($allow_read_mail eq "0"))
    {
        &V22get_message;
    }
    &meta;
    print <<"DBMA";
<title>DBMA Message $messageID for $username</title>
</head><body>
DBMA
    $sth = $dbh->{LongReadLen} =
      $dbh->prepare(
        "SELECT messageblk, is_header from $dbmail_messageblks_table where id = $physmessage_id $order"
      );
    $sth->execute();
    while (($messageblk, $is_header) = $sth->fetchrow_array)
    {
        $messageblk =~ s/=([\da-fA-F]{2})/pack("C", hex($1))/ge;
        $messageblk =~ s/=\?iso-8859-1\?q\?([^?]*)\?=/pack("C", hex($1))/ge;
        $messageblk =~ s/\@/\&\#64\;/g;
        $messageblk =~ s/\</&#60\;/g;
        $messageblk =~ s/\>/&#62\;/g;
        $messageblk =~ s/=\n$//;
        $is_header  =~ s/1/Header/g;
        $is_header  =~ s/0/Message/g;

        if (grep(/Subject:/i, $messageblk) => 1)
        {
            $messageblk =~ s/Subject/\<b\>Subject:\<\/b\>/g;
            $messageblk =~ s/Reply\-To/\<b\>Reply\-To :\<\/b\>/g;
            $messageblk =~ s/To/\<b\>To:\<\/b\>/g;
            $messageblk =~ s/Received/\<b\>Received:\<\/b\>/g;
            $messageblk =~ s/From/\<b\>From:\<\/b\>/g;
            $messageblk =~ s/Date/\<b\>Date:\<\/b\>/g;
            $messageblk =~ s/Cc/\<b\>Cc:\<\/b\>/g;
            $messageblk =~ s/Content-Type/\<b\>Content-Type:\<\/b\>/g;
            $messageblk =~ s/thread-index/\<b\>thread-index:\<\/b\>/g;
            $messageblk =~
              s/X-DBMail-PhysMessage-ID/\<b\>X-DBMail-PhysMessage-ID:\<\/b\>/g;
            $messageblk =~ s/Return-Path/\<b\>Return-Path:\<\/b\>/g;
            $messageblk =~ s/Message-Id/\<b\>Message-Id:\<\/b\>/g;
            $messageblk =~ s/\n/\<br \/\>/g;
            $messageblk =~ s/=\<br \/\>/\<br \/\>/g;
        }
        $messageblk = $str .=
          "<tr><td class=\"ad\"><h3>$is_header</h3></td></tr>
          <tr><td style=\"width:738px;font-size:13px;font-family:san-serif\"><pre-wrap style=\"font-size:12px;font-family:arial,san-serif\">$messageblk</pre-wrap></td></tr>\n";
    }
    print <<"DBMA";
	<div><center><table style="width:738px">
	<tr><td colspan="3" style="width:738px"><span style="font-weight:600;font-size:105%">$username Account ~ $mailbox_name Folder</span></td></tr>
	<tr><td colspan="3"><h4>Message $messageID | <a href="$mythisscript?$userID">Back to $username Account</a> | <a href="$mythisscript">Main Menu | <a href="javascript: history.go(-1)">Back To List</a></h4></td></tr>
	<tr><td title="Delete this message."></td></tr>
	<tr><td><table style="width:738px;border-style:none;border-color:#D6CFDE;background-color:#D6CFDE">
	<tr><td class="dd c2 c15">Seen: <b>$seen_flag</b> Marked Delete: <b>$deleted_flag</b></td>
	<td class="dd c2"><form method="post" action="$mythisscript">
	<input type="hidden" value="31" name ="RQT" /><input type="hidden" value="$mailbox_name" name ="mailbox_name" /><input type="hidden" value="$messageID" name ="messageID" /><input type="hidden" value="$userID" name="userID" />
	<input type="hidden" value="$username"  name="username" /><input title="Delete $messageID" type="submit" value ="Delete $messageID" onclick="return confirm('Mark Message $messageID for immediate delete?')" onmouseover="this.className='warndm';" onmouseout="this.className='dm';" type="submit" class="dm" /></form></td>
	<td class="dd c2"><form method="post" action="$mythisscript"><input type="hidden" value="32" name ="RQT" /><input type="hidden" value="$mailbox_name" name ="mailbox_name" />
	<input type="hidden" value="$messageID" name ="messageID" /><input type="hidden" value="$userID" name="userID" />
	<input type="hidden" value="$username"  name="username" /><input title="UnDelete $messageID." type="submit" value ="UnDelete $messageID" onmouseover="this.className='un';" onmouseout="this.className='undm';" class="undm" /></form></td></tr>
	<tr><td colspan="3" style="text-align:left;background-color:#ffffc4">
DBMA
    &minisearchform;
    print <<"DBMA";
	</td></tr></table></td></tr>
	<tr><td><span style="font-family:sans-serif;font-size:12px;color:#6a6a95;background-color:#F8F8FF">(DBMA forced ASCII text format with filters. This tool disables links and scripts and is for admin purposes only.)</span></td></tr>
DBMA
    print $str if ($str);
    print "</table></center></div>\n";
    end_HTML;
    $dbh->disconnect() if ($dbh);
}
############################################################## - sub V22get_message
sub V22get_message
{
    our (
         $headername, $toname,      $toaddr,      $fromname, $fromaddr,
         $datefield,  $replytoname, $replytoaddr, $subject
        )
      = 0;
    &meta;
    print <<"DBMA";
<title>DBMA DBMailV22 Message $messageID for $username</title>
</head><body>
DBMA
    $sth = $dbh->{LongReadLen} = $dbh->prepare(
        "SELECT toname, toaddr, fromname, fromaddr, replytoname, replytoaddr, $dbmail_datefield_table.datefield, $dbmail_headername_table.headername, $dbmail_headervalue_table.headervalue, $dbmail_subjectfield_table.subjectfield  from $dbmail_headervalue_table
LEFT JOIN $dbmail_headername_table ON $dbmail_headername_table.id = $dbmail_headervalue_table.headername_id
LEFT JOIN $dbmail_fromfield_table on $dbmail_headervalue_table.physmessage_id = $dbmail_fromfield_table.physmessage_id
LEFT JOIN $dbmail_tofield_table on $dbmail_headervalue_table.physmessage_id = $dbmail_tofield_table.physmessage_id
LEFT JOIN $dbmail_datefield_table on $dbmail_headervalue_table.physmessage_id = $dbmail_datefield_table.physmessage_id
LEFT JOIN $dbmail_subjectfield_table on $dbmail_headervalue_table.physmessage_id = $dbmail_subjectfield_table.physmessage_id
LEFT JOIN $dbmail_replytofield_table on $dbmail_headervalue_table.physmessage_id = $dbmail_replytofield_table.physmessage_id
where $dbmail_headervalue_table.physmessage_id = $physmessage_id"
                                              );
    undef $physmessage_id;
    $sth->execute();
    while (
           (
            $toname,      $toaddr,    $fromname,   $fromaddr,    $replytoname,
            $replytoaddr, $datefield, $headername, $headervalue, $subject
           )
           = $sth->fetchrow_array
          )
    {
        $headername =~ s/Subject/\<b\>Subject:\<\/b\>/g;
        $headername =~ s/Reply\-To/\<b\>Reply\-To :\<\/b\>/g;
        $headername =~ s/To/\<b\>To:\<\/b\>/g;
        $headername =~ s/Received/\<b\>Received:\<\/b\>/g;
        $headername =~ s/From/\<b\>From:\<\/b\>/g;
        $headername =~ s/Date/\<b\>Date:\<\/b\>/g;
        $headername =~ s/Cc/\<b\>Cc:\<\/b\>/g;
        $headername =~ s/Content-Type/\<b\>Content-Type:\<\/b\>/g;
        $headername =~ s/thread-index/\<b\>thread-index:\<\/b\>/g;
        $headername =~
          s/X-DBMail-PhysMessage-ID/\<b\>X-DBMail-PhysMessage-ID:\<\/b\>/g;
        $headername =~ s/Return-Path/\<b\>Return-Path:\<\/b\>/g;
        $headername =~ s/Message-Id/\<b\>Message-Id:\<\/b\>/g;
        $headername =~ s/\n/\<br \/\>/g;
        $headername =~ s/=\<br \/\>/\<br \/\>/g;
        $str1 =
          "To: $toname &lt;$toaddr&gt;<br />From: $fromname &lt;$fromaddr&gt;<br />Reply to:$replytoname &lt$replytoaddr&gt;<br />Date: $datefield<br />Subject: $subject";
        $str .=
          "<tr><td style=\"width:738px;font-size:11px;font-family:san-serif\"><pre-wrap style=\"margin-left:20px;font-size:11px;font-family:arial,san-serif\">$headername $headervalue</pre-wrap><br />
	</td></tr>\n";

    }
    print <<"DBMA";
	<div><center><table style="width:738px">
	<tr><td colspan="3" style="width:738px"><span style="font-weight:600;font-size:105%">$username Account ~ $mailbox_name Folder</span></td></tr>
	<tr><td colspan="3"><h4>Message $messageID | <a href="$mythisscript?$userID">Back to $username Account</a> | <a href="$mythisscript">Main Menu | <a href="javascript: history.go(-1)">Back To List</a></a></h4></td></tr>
	<tr><td title="Delete this message."></td></tr>
	<tr><td><table style="width:738px;border-style:none;border-color:#D6CFDE;background-color:#D6CFDE">
	<tr><td class="dd c2 c15">Seen: <b>$seen_flag</b> Marked Delete: <b>$deleted_flag</b></td>
	<td class="dd c2"><form method="post" action="$mythisscript">
	<input type="hidden" value="31" name ="RQT" /><input type="hidden" value="$mailbox_name" name ="mailbox_name" /><input type="hidden" value="$messageID" name ="messageID" /><input type="hidden" value="$userID" name="userID" />
	<input type="hidden" value="$username"  name="username" /><input title="Delete $messageID" type="submit" value ="Delete $messageID" onclick="return confirm('Mark Message $messageID for immediate delete?')" onmouseover="this.className='warndm';" onmouseout="this.className='dm';" type="submit" class="dm" /></form></td>
	<td class="dd c2"><form method="post" action="$mythisscript"><input type="hidden" value="32" name ="RQT" /><input type="hidden" value="$mailbox_name" name ="mailbox_name" />
	<input type="hidden" value="$messageID" name ="messageID" /><input type="hidden" value="$userID" name="userID" />
	<input type="hidden" value="$username"  name="username" /><input title="UnDelete $messageID." type="submit" value ="UnDelete $messageID" onmouseover="this.className='un';" onmouseout="this.className='undm';" class="undm" /></form></td></tr>
	<tr><td colspan="3" style="text-align:left;background-color:#ffffc4">$str1</td></tr></table></td></tr>
DBMA
    print $str if ($str);
    undef $str1;
    undef $str;
    print "</table></center></div>\n";
    end_HTML;
    $dbh->disconnect() if ($dbh);

}
############################################################## - sub search_mail
sub search_mail
{
    &meta;
    $sth =
      $dbh->prepare(
        "SELECT name FROM $dbmail_mailboxes_table WHERE mailbox_idnr = '$mailbox_idnr'"
      );
    $sth->execute();
    while (($mailbox_name) = $sth->fetchrow_array)
    {
        $str2 .= "$mailbox_name";
        print <<"DBMA";
	<title>DBMA Mail Search for $searchterms</title>
	</head>
	<body><div><center><table>
	<tr><td colspan="7" style="background-color:#ffffc4">
DBMA
        &minisearchform;
        print <<"DBMA";
	</td></tr>
DBMA
        $sth = $dbh->{LongReadLen} = $dbh->prepare(
            "SELECT $dbmail_messageblks_table.physmessage_id FROM $dbmail_messageblks_table
LEFT JOIN $dbmail_messages_table ON $dbmail_messageblks_table.physmessage_id = $dbmail_messages_table.physmessage_id
WHERE headervalue LIKE '%$searchterms%' AND $dbmail_messages_table.mailbox_idnr = '$mailbox_idnr'
ORDER BY id desc LIMIT 1"
                                                  );
        $sth->execute();
        while (($physmessage_id) = $sth->fetchrow_array)
        {
            $str3 .= "$physmessage_id";
            $sth = $dbh->{LongReadLen} =
              $dbh->prepare(
                "SELECT headervalue from $dbmail_messageblks_table where id = '$physmessage_id' $order"
              );
            $sth->execute();
            while (($messageblk, $is_header) = $sth->fetchrow_array)
            {
                $messageblk =~
                  s/=\?iso-8859-1\?q\?([^?]*)\?=/pack("C", hex($1))/ge;
                $messageblk =~ s/=([\da-fA-F]{2})/pack("C", hex($1))/ge;
                $messageblk =~ s/\@/\&\#64\;/g;
                $messageblk =~ s/\</&#60\;/g;
                $messageblk =~ s/\>/&#62\;/g;
                $messageblk =~ s/=\n$//;
                $is_header  =~ s/1/Header/g;
                $is_header  =~ s/0/Message/g;
                $str1 .=
                  "	<tr><td><small>Block Type=$is_header</small></td></tr>\n
	<tr><td title=\"DBMA will block HTML, URI links, and IFRAMES from executing.\" style=\"width:738px\">\n
	<textarea cols=\"70\" rows=\"11\" style=\"border-style:solid;border-color:#F8F8FF;width:738px;font-size:11px;font-family:arial,verdana,san-serif;scrollbar-arrow-color:green;scrollbar-face-color:#f5f3f8;scrollbar-shadow-color:#BDB6CE; scrollbar-track-color:#F8F8FF\">\n$messageblk\n</textarea></td>\n</tr>\n";
            }
            $sth = $dbh->prepare(
                "SELECT message_idnr, $dbmail_physmessage_table.internal_date, $dbmail_messages_table.physmessage_id, unique_id, rfcsize, messagesize, seen_flag, answered_flag, deleted_flag, status 
FROM $dbmail_messages_table
LEFT JOIN $dbmail_physmessage_table ON $dbmail_messages_table.physmessage_id = $dbmail_physmessage_table.id
WHERE $dbmail_messages_table.physmessage_id = '$physmessage_id' LIMIT 1"
                                );
            unless ($sth->execute())
            {
                print
                  "<span class=\"er\">$DBI::errstr <br />Failed message search</span>";
            }
            while (
                   (
                    $messageID, $internal_date, $physmessage_id,
                    $unique_id, $rfcsize,       $messagesize,
                    $seen_flag, $answered_flag, $deleted_flag,
                    $status
                   )
                   = $sth->fetchrow_array
                  )
            {
                $seen_flag     =~ s/1/\<b\>YES\<\/b\>/g;
                $seen_flag     =~ s/0/\<b\>NO\<\/b\>/g;
                $answered_flag =~ s/1/\<b\>YES\<\/b\>/g;
                $answered_flag =~ s/0/\<b\>NO\<\/b\>/g;
                $deleted_flag  =~ s/1/\<b\>YES\<\/b\>/g;
                $deleted_flag  =~ s/0/\<b\>NO\<\/b\>/g;
                $str .= "	<tr style=\"font-size:11px\">
	<td>$internal_date</td><td>$mailbox_name</td><td>$unique_id</td><td>$rfcsize</td><td>$messagesize</td></tr>
	</table></center></div><div><center><table><tr style=\"font-size:11px\"><td class=\"ad\">Seen = $seen_flag</td><td class=\"ad\">Answered = $answered_flag</td><td class=\"ad\">Marked For Delete = $deleted_flag</td><td class=\"ad\">Status = <b>$status</b></td>
	<td class=\"ad\" colspan=\"2\" title=\"Mark this message for deletion by next dbmail-util run.\"><form method=\"post\" action=\"$mythisscript\"><input type=\"hidden\" value=\"31\" name =\"RQT\" />
	<input type=\"hidden\" value=\"$mailbox_name\" name =\"mailbox_name\" /><input type=\"hidden\" value=\"$messageID\" name =\"messageID\" /><input type=\"hidden\" value=\"$userID\" name=\"userID\" /><input type=\"hidden\" value=\"$username\"  name=\"username\" /><input type=\"image\" value =\"submit\" src=\"images/delete.gif\" onmouseover=\"self.status=\'Delete Mail\';return true\" onmouseout=\"self.status=\'DBMA\';return true\" style=\"width:37px;height:14px\" /></form></td>
	<td class=\"ad\" colspan=\"2\" title=\"UnDelete this message\"><form method=\"post\" action=\"$mythisscript\"><input type=\"hidden\" value=\"32\" name =\"RQT\" />
	<input type=\"hidden\" value=\"$mailbox_name\" name =\"mailbox_name\" /><input type=\"hidden\" value=\"$messageID\" name =\"messageID\" /><input type=\"hidden\" value=\"$userID\" name=\"userID\" /><input type=\"hidden\" value=\"$username\"  name=\"username\" />
	<input type=\"image\" value =\"submit\" src=\"images/undelete.gif\" onmouseover=\"self.status=\'UnDelete this Message\';return true\" onmouseout=\"self.status=\'DBMA\';return true\" style=\"width:49px;height:16px\" /></form></td></tr>\n";
                last;
            }
            last;
        }
        last;
    }
    if (defined $str3 > 0)
    {
        print <<"DBMA";
	<tr><td colspan="7"><h3><a href="$mythisscript?$userID">Back to $username Account</a> | <a href="$mythisscript">Main Menu</a></h3></td></tr>
	<tr><td>Delete or undelete this message, or do an extended search above if this is not what you seek.</td></tr>
	<tr><td colspan="6" style="color:#000090;border-style:solid;border-color:#D6CFDE;font-size:9pt">
	NOTE: DBMA has returned the raw content of the most recent message containing your search string in a safe environment wherein html links, images or malicious code will not execute. You searched for <i><b>$searchterms</b></i> in $username\'s
	$str2 ($mailbox_idnr). Message content displays in two text areas: Block Type=Header, and Block Type=Message. This relies on the "dbmail_messageblks.is_header" flag. Some DBMail versions do not insert the "is_header" flag.</td></tr>
	<tr><td colspan="6"><h2>Message $messageID</h2></td></tr></table></center></div>
	<div><center><table width="738px">
	<tr><td><span class="gr">Date</span></td>
	<td><span class="gr">Mailbox</span></td>
	<td><span class="gr">Unique ID</span></td><td><span class="gr">RFCSize</span></td><td><span class="gr">Size</span></td></tr>
DBMA
        print $str if ($str);
        print <<"DBMA";
	</table></center></div><div><center><table width="738px">
DBMA
        print <<"DBMA";
	<tr><td colspan="6"><hr style="background-color:#D6CFDE; height:4px; color:#D6CFDE" /></td></tr>
DBMA
        print $str1 if ($str1);
    }
    elsif (defined $str3 < 1)
    {
        print <<"DBMA";
	<tr><td colspan="6"><hr style="background-color:#D6CFDE; height:4px; color:#D6CFDE" /></td></tr>
	<tr><td><b>Nothing found for $searchterms</b>. Please try again with different search terms.</td></tr>
DBMA
    }
    print "</table></center></div>\n";
    end_HTML;
    $sth->finish()     if ($sth);
    $dbh->disconnect() if ($dbh);
    exit;
}
############################################################## - sub search_mail_extended
sub search_mail_extended
{
    &meta;
    $headers_results  = "";
    $headers_only_sql = "";
    $headers_only     = $FORM{'headers_only'} || "0";
    if ($headers_only == 1)
    {
        $headers_results  = "<em>(in headers only)</em>";
        $headers_only_sql =
          " AND " . $dbmail_messageblks_table . ".is_header=1 ";
    }
    $starttime = time();
    $sth = $dbh->{LongReadLen} = $dbh->prepare(
        "SELECT message_idnr, $dbmail_physmessage_table.internal_date, $dbmail_messages_table.physmessage_id, unique_id, rfcsize, messagesize, $dbmail_messages_table.seen_flag, $dbmail_messages_table.answered_flag, $dbmail_messages_table.deleted_flag, $dbmail_messages_table.status, $dbmail_mailboxes_table.name
FROM $dbmail_messages_table
LEFT JOIN $dbmail_mailboxes_table ON $dbmail_mailboxes_table.mailbox_idnr = $dbmail_messages_table.mailbox_idnr
LEFT JOIN $dbmail_physmessage_table ON $dbmail_messages_table.physmessage_id = $dbmail_physmessage_table.id
LEFT JOIN $dbmail_messageblks_table ON $dbmail_messages_table.physmessage_id = $dbmail_messageblks_table.physmessage_id
WHERE $dbmail_messageblks_table.messageblk LIKE '%$searchterms%' AND $dbmail_mailboxes_table.owner_idnr = '$userID' $headers_only_sql
ORDER BY $dbmail_physmessage_table.internal_date desc"
                                              );
    unless ($sth->execute())
    {
        print
          "<span class=\"er\">$DBI::errstr <br />Sorry. Search failed for mail in this users mailboxes using your searchterms.</span>";
    }
    $numrows = $sth->rows;
    while (
           (
            $messageID,    $internal_date, $physmessage_id, $unique_id,
            $rfcsize,      $messagesize,   $seen_flag,      $answered_flag,
            $deleted_flag, $status,        $mailbox_name
           )
           = $sth->fetchrow_array
          )
    {
        $seen_flag     =~ s/1/YES/g;
        $seen_flag     =~ s/0/NO/g;
        $answered_flag =~ s/1/YES/g;
        $answered_flag =~ s/0/NO/g;
        $deleted_flag  =~ s/1/YES/g;
        $deleted_flag  =~ s/0/NO/g;
        $str .=
          "	<tr><td title=\"$username\'s $mailbox_name\"><span style=\"background:#f5f3f8\"><b>$mailbox_name</b></span></td>
	<td><span class=\"gr\">Message ID</span></td>
	<td><span class=\"gr\">$mailbox_name Date</span></td>
	<td><span class=\"gr\">Unique ID</span></td><td><span class=\"gr\">RFCSize</span></td><td><span class=\"gr\">Size</span></td></tr>
	<tr style=\"font-size:11px\"><td><form method=\"post\" action=\"$mythisscript\"><input type=\"hidden\" value=\"$messageID\" name=\"messageID\" /> <input type=\"hidden\" value=\"$userID\" name=\"userID\" /><input type=\"hidden\" value=\"$searchterms\" name=\"searchterms\" /><input type=\"hidden\" value=\"$mailbox_name\" name=\"mailbox_name\" /><input type=\"hidden\" value=\"$deleted_flag\" name=\"deleted_flag\" /><input type=\"hidden\" value=\"$seen_flag\" name=\"seen_flag\" />
	<input type=\"hidden\" value=\"$messageID\" name=\"messageID\" />
	<input type=\"hidden\" value=\"$username\" name=\"username\" /><input type=\"hidden\" name=\"physmessage_id\" value=\"$physmessage_id\" /><input title=\"Open id $physmessage_id having message_idnr $messageID\" type=\"image\" src=\"images/read_mail.gif\" onmouseover=\"this.className=\'letsgo\';\" onmouseout=\"this.className=\'notseen\';\" class=\"notseen\" /></form></td>
	<td>$messageID</td><td><b style=\"color:#6a6a95\"> $internal_date</b></td><td>$unique_id</td><td>$rfcsize</td><td>$messagesize</td></tr>
	<tr style=\"font-size:11px\"><td>Seen=<b>$seen_flag</b></td><td>Answered=<b>$answered_flag</b></td><td>Marked Delete = <b>$deleted_flag</b></td><td>Status = <b>$status</b></td>
	<td title=\"Mark this message for deletion by next dbmail-util run.\"><form method=\"post\" action=\"$mythisscript\"><input type=\"hidden\" value=\"31\" name =\"RQT\" />
	<input type=\"hidden\" value=\"$mailbox_name\" name =\"mailbox_name\" /><input type=\"hidden\" value=\"$messageID\" name =\"messageID\" /><input type=\"hidden\" value=\"$userID\" name=\"userID\" /><input type=\"hidden\" value=\"$username\"  name=\"username\" /><input type=\"image\" value =\"submit\" src=\"images/delete.gif\" onmouseover=\"self.status=\'Delete Mail\';return true\" onmouseout=\"self.status=\'DBMA\';return true\" style=\"width:37px;height:14px\" /></form></td>
	<td title=\"UnDelete this message\"><form method=\"post\" action=\"$mythisscript\"><input type=\"hidden\" value=\"32\" name =\"RQT\" />
	<input type=\"hidden\" value=\"$mailbox_name\" name =\"mailbox_name\" /><input type=\"hidden\" value=\"$messageID\" name =\"messageID\" /><input type=\"hidden\" value=\"$userID\" name=\"userID\" /><input type=\"hidden\" value=\"$username\"  name=\"username\" />
	<input type=\"image\" value =\"submit\" src=\"images/undelete.gif\" onmouseover=\"self.status=\'UnDelete this Message\';return true\" onmouseout=\"self.status=\'DBMA\';return true\" style=\"width:49px;height:16px\" /></form></td></tr>
	<tr><td colspan=\"7\"><hr style=\"background-color:#D6CFDE; height:4px; color:#D6CFDE\" /></td></tr>\n";
    }
    $endtime      = time;
    $DBSearchTime = $endtime - $starttime;
    print <<"DBMA";
	<title>DBMA: Message Search in $username\'s Mailboxes</title>
	</head>
	<body><div><center><table>
	<tr><td colspan="7"><h2>Searching $username Mailboxes</h2</td></tr>
	<tr><td style="background:#D6CFDE" colspan="7"><span style="font-family:arial,sans-serif;font-size:105%;font-weight:bold"><a href="$mythisscript?$userID">Open $username\'s Account Window</a> | <a href="$mythisscript">Main Menu</a></span></td></tr>
	<tr><td colspan="7" style="background-color:#ffffc4">
DBMA
    &minisearchform;
    print <<"DBMA";
	</td></tr>
	<tr><td colspan="7" style="background-color:#D0F4D2;font-size:90%"><b>$numrows Messages</b> have string matches to your search terms $headers_results order by date. <b>$DBSearchTime Secs</b></td></tr>
	<tr><td colspan="7">Results:</td></tr>
DBMA
    print $str         if ($str);
    $sth->finish()     if ($sth);
    $dbh->disconnect() if ($dbh);
    print "</table></center></div>\n";
    end_HTML;
    exit;
}
#############################  End User Account Window Section
############################################################## - sub List_Group_Users RQT29
sub List_Group_Users
{
    &checkrequired;
    &header;
    &numusers;
    if (   ($FORM{'GroupID'} eq "0")
        || ($FORM{'GroupID'} eq " ")
        || ($FORM{'GroupID'} eq "00"))
    {
        $GroupID =~ /\0/;
    }
    if ($DBMailOldVersion eq "0")
    {
        $sth =
          $dbh->prepare(
            "SELECT user_idnr, userid, passwd, client_idnr, maxmail_size, curmail_size, encryption_type, last_login FROM $dbmail_users_table WHERE client_idnr ='$GroupID' ORDER BY $orderby $LIMIT"
          );
        unless ($sth->execute())
        {
            $errormessage = "
	ErrorID: $version.err0.12 <br />$DBI::errstr <br />Failed List_Group_Users function";
            &DBMA_ConnectStatus;
        }
        print <<"DBMA";
	<div><center><table><tr><td><form method="post" action="$mythisscript"><input type="hidden" name ="orderby" value="user_idnr" />
	<input type="hidden" name ="RQT" value="all_in_this_group" /><input type="hidden" value="$GroupID" name="GroupID" />
	<input type="image" src="images/id.gif" style="width:19px;height:14px" title="Sort by User ID Number" /></form></td>
	<td><form method="post" action="$mythisscript"><input type="hidden" name ="orderby" value="userid" /><input type="hidden" name ="RQT" value="all_in_this_group" /><input type="hidden" value="$GroupID" name="GroupID" /><input type="image" src="images/user.gif" style="width:32px;height:14px" title="Sort by User Name" /></form></td>
	<td><span style="color:#B5924A;font-weight:675">Modify</span></td><td><span style="color:red;font-weight:675">Delete</span></td>
	<td><span style="color:#009A31">Alias</span></td><td><span style="color:blue;font-weight:675">Notify</span></td>
	<td><span style="color:navy;font-weight:675">Password</span></td><td><span style="color:navy;font-weight:675">Group</span></td>
	<td><span style="color:navy;font-weight:675">Mail Quota</span></td><td><form method="post" action="$mythisscript"><input type="hidden" name ="orderby" value="curmail_size desc" /><input type="hidden" name ="RQT" value="all_in_this_group" /><input type="hidden" value="$GroupID" name="GroupID" />
	<input type="image" src="images/curmail.gif" style="width:70px;height:14px" title="Sort by Volume of Current Mail" /></form></td>
	<td><form method="post" action="$mythisscript"><input type="hidden" name ="orderby" value="last_login desc" /><input type="hidden" name ="RQT" value="all_in_this_group" /><input type="hidden" value="$GroupID" name="GroupID" />
	<input type="image" src="images/lastlogin.gif" style="width:63px;height:14px" title="Sort by date of last login" /></form></td></tr>
DBMA
        while (
               (
                $userID,       $username,     $passwd,          $GroupID,
                $maxmail_size, $curmail_size, $encryption_type, $last_login
               )
               = $sth->fetchrow_array
              )
        {
            $username =~
              s/__\@\!internal_delivery_user\!\@__/LocalDeliveryAgent/;
            $username =~ s/__public__/\#Public/;
            $passwd = "encrypted"
              if (   ($encryption_type =~ /md5sum/)
                  || ($encryption_type =~ /md5/)
                  || ($encryption_type =~ /crypt/));
            $passwd = "*plain*" if $encryption_type =~ //;
            $str .= "	<tr>
	<td class=\"ad c0\">$userID</td>
	<td class=\"ad c0\"><a title=\"Open $username\'s Account Window\" href=\"$mythisscript\?$userID\" onmouseover=\"self.status=\'Open this users account.\';return true\" onmouseout=\"self.status=\'DBMA\';return true\" /><img alt=\"User\" src=\"images/usericon.gif\" style=\"width:12px;height:17px\" /> $username</a></td>
	<td class=\"ad\" title=\"MODIFY user $username\"><form method=\"post\" action=\"$mythisscript\">
	<input type=\"hidden\" name=\"RQT\" value=\"11\" /><input type=\"hidden\" name=\"newuserID\" value=\"$userID\" /><input type=\"hidden\" name=\"username\" value=\"$username\" /><input type=\"hidden\" name=\"GroupID\" value=\"$GroupID\" />
	<input type=\"hidden\" name=\"mailboxsize\" value=\"$maxmail_size\" />
	<input type=\"hidden\" name=\"password\" value=\"$passwd\" /><input type=\"hidden\" name=\"encrypttype\" value=\"$encryption_type\" /><input type=\"image\" src=\"images/modify.gif\" title=\"MODIFY $username Account\" width=\"33\" height=\"13\" /></form></td>
	<td class=\"ad\" title=\"DELETE user $username\"><form method=\"post\" action=\"$mythisscript\">
	<input type=\"hidden\" name=\"RQT\" value=\"5\" /><input type=\"hidden\" name=\"userID\" value=\"$userID\" />
	<input type=\"hidden\" name=\"displayusername\" value=\"$username\" />
	<input type=\"image\" value =\"submit\" src=\"images/delete.gif\" onmouseover=\"self.status=\'Go to a Delete-User Window For This User\';return true\" onmouseout=\"self.status=\'DBMA\';return true\" style=\"width:37px;height:14px\" /></form></td>
	<td class=\"ad\" title=\"Add an Alias for user $username\">
	<form name=\"alias\" method=\"post\" action=\"$mythisscript\"><input type=\"hidden\" name=\"RQT\" value=\"7\" />
	<input type=\"hidden\" name=\"userID\" value=\"$userID\" /><input type=\"hidden\" name=\"GroupID\" value=\"$GroupID\" /><input type=\"hidden\" name=\"displayusername\" value=\"$username\" />
	<input type=\"image\" value =\"submit\" src=\"images/add-alias.gif\" onmouseover=\"self.status=\'Add an Alias\';return true\" onmouseout=\"self.status=\'DBMA\';return true\" style=\"width:28px;height:14px\" /></form></td>
	<td class=\"ad\" title=\"Notify someone when $username gets mail\"><form method=\"post\" action=\"$mythisscript\">
	<input type=\"hidden\" name=\"RQT\" value=\"16\" /><input type=\"hidden\" name=\"userID\" value=\"$userID\" />
	<input type=\"hidden\" name=\"GroupID\" value=\"$GroupID\" /><input type=\"hidden\" name=\"displayusername\" value=\"$username\" />
	<input type=\"image\" value =\"submit\" src=\"images/notify.gif\" onmouseover=\"self.status=\'Notify someone when this account gets mail.\';return true\" onmouseout=\"self.status=\'DBMA\';return true\" style=\"width:33px;height:14px\" /></form></td>
	<td class=\"ad\">$passwd</td><td class=\"ad\">$GroupID</td><td class=\"ad\">$maxmail_size</td><td class=\"ad\">$curmail_size</td><td class=\"ad\">$last_login</td></tr>\n";
        }
        print $str if ($str);
        print "	</table></center></div>\n";
        end_HTML;
        $dbh->disconnect() if ($dbh);
        exit;
    }
    if ($DBMailOldVersion eq "1")
    {
        $sth =
          $dbh->prepare(
            "SELECT user_idnr,  userid,  passwd,  client_idnr,  maxmail_size, encryption_type, $cmailsize last_login  FROM $dbmail_users_table WHERE client_idnr ='$GroupID' ORDER BY $orderby $LIMIT"
          );
        unless ($sth->execute())
        {
            $errormessage = "
	ErrorID: $version.err0.13 <br />$DBI::errstr <br />Failed $sth";
            &DBMA_ConnectStatus;
        }
        print <<"DBMA";
	<div><center><table><tr>
	<td><form method="post" action="$mythisscript">
	<input type="hidden" name ="orderby" value="user_idnr" />
	<input type="hidden" name ="RQT" value="all_in_this_group" /><input type="hidden" value="$GroupID" name="GroupID" />
	<input type="image" src="images/id.gif" style="width:19px;height:14px" title="Sort by User ID Number" /></form></td>
	<td><form method="post" action="$mythisscript">
	<input type="hidden" name ="orderby" value="userid" />
	<input type="hidden" name ="RQT" value="all_in_this_group" />
	<input type="hidden" value="$GroupID" name="GroupID" />
	<input type="image" src="images/user.gif" style="width:32px;height:14px" title="Sort by User Name" /></form></td>
	<td><span style="color:red;font-weight:675">Delete</span></td>
	<td><span class="gr">Alias</span></td>
	<td><span style="color:blue;font-weight:675">Notify</span></td>
	<td><span style="color:navy;font-weight:675">Password</span></td>
	<td><span style="color:navy;font-weight:675">Group</span></td>
	<td><span style="color:navy;font-weight:675">Mail Quota</span></td>
	<td><form method="post" action="$mythisscript">
	<input type="hidden" name ="orderby" value="last_login desc" />
	<input type="hidden" name ="RQT" value="all_in_this_group" /><input type="hidden" value="$GroupID" name="GroupID" />
	<input type="image" src="images/lastlogin.gif" style="width:63px;height:14px" title="Sort by date of last login" />
	</form></td></tr>
DBMA
        while (
               (
                $userID,       $username,        $passwd,       $GroupID,
                $maxmail_size, $encryption_type, $curmail_size, $last_login
               )
               = $sth->fetchrow_array
              )
        {
            $username =~
              s/__\@\!internal_delivery_user\!\@__/LocalDeliveryAgent/;
            $username =~ s/__public__/\#Public/;
            $passwd = "encrypted"
              if (   ($encryption_type =~ /md5sum/)
                  || ($encryption_type =~ /md5/)
                  || ($encryption_type =~ /crypt/));
            $passwd = "*plain*"
              if (   ($encryption_type =~ /^md5sum/)
                  && ($encryption_type =~ /^md5/)
                  && ($encryption_type =~ /^crypt/)
                  || ($encryption_type eq " ")
                  || ($encryption_type eq "plain"));
            $str .= "	<tr>
	<td class=\"ad c0\">$userID</td>
	<td class=\"ad c0\"><a title=\"Open $username\'s Account Window\" href=\"$mythisscript\?$userID\" onmouseover=\"self.status=\'Open this users account.\';return true\" onmouseout=\"self.status=\'DBMA\';return true\" /><img alt=\"User\" src=\"images/usericon.gif\" style=\"width:12px;height:17px\" /> $username</a></td>
	<td class=\"ad\" title=\"DELETE user $username\"><form method=\"post\" action=\"$mythisscript\">
	<input type=\"hidden\" name=\"RQT\" value=\"5\" /><input type=\"hidden\" name=\"userID\" value=\"$userID\" />
	<input type=\"hidden\" name=\"displayusername\" value=\"$username\" />
	<input type=\"image\" value =\"submit\" src=\"images/delete.gif\" onmouseover=\"self.status=\'Go to a Delete-User Window For This User\';return true\" onmouseout=\"self.status=\'DBMA\';return true\" style=\"width:37px;height:14px\" /></form></td>
	<td class=\"ad\" title=\"Add an Alias for user $username\"><form name=\"alias\" method=\"post\" action=\"$mythisscript\"><input type=\"hidden\" name=\"RQT\" value=\"7\" /><input type=\"hidden\" name=\"userID\" value=\"$userID\" /><input type=\"hidden\" name=\"GroupID\" value=\"$GroupID\" />
	<input type=\"hidden\" name=\"displayusername\" value=\"$username\" /><input type=\"image\" value =\"submit\" src=\"images/add-alias.gif\" onmouseover=\"self.status=\'Add an Alias\';return true\" onmouseout=\"self.status=\'DBMA\';return true\" style=\"width:28px;height:14px\" /></form></td>
	<td class=\"ad\" title=\"Notify someone when $username gets mail\"><form method=\"post\" action=\"$mythisscript\">
	<input type=\"hidden\" name=\"RQT\" value=\"16\" /><input type=\"hidden\" name=\"userID\" value=\"$userID\" /><input type=\"hidden\" name=\"GroupID\" value=\"$GroupID\" /><input type=\"hidden\" name=\"displayusername\" value=\"$username\" />
	<input type=\"image\" value =\"submit\" src=\"images/notify.gif\" onmouseover=\"self.status=\'Notify someone when this account gets mail.\';return true\" onmouseout=\"self.status=\'DBMA\';return true\" style=\"width:33px;height:14px\" /></form></td>
	<td class=\"ad\">$passwd</td><td class=\"ad\">$GroupID</td><td class=\"ad\">$maxmail_size</td><td class=\"ad\">$curmail_size</td>\n<td class=\"ad\">$last_login</td>\n</tr>\n";
        }
        print $str if ($str);
        print "	</table></center></div>\n";
        end_HTML;
        $dbh->disconnect() if ($dbh);
        exit;
    }
}
############################################################## - sub List_Global_Users RQTany
sub List_Global_Users
{
    if (($RESTRICTGroupID =~ m/[0-9]/i) && (defined $FORM{'userID'} eq "any"))
    {
        &fail;
    }
    &checkrequired;
    &header;
    &numusers;
    if ($DBMailOldVersion eq "0")
    {
        print <<"DBMA";
	<div><center><table><tr>
	<td><form method="post" action="$mythisscript"><input type="hidden" name ="orderby" value="user_idnr" /><input type="hidden" name="limit" value="$limit" />
	<input type="hidden" name ="userID" value="any" /><input type="image" src="images/id.gif" style="width:19px;height:14px" title="Sort by User ID Number" /></form></td>
	<td><form method="post" action="$mythisscript"><input type="hidden" name ="orderby" value="userid" /><input type="hidden" name="limit" value="$limit" /><input type="hidden" name ="userID" value="any" /><input type="image" src="images/user.gif" style="width:32px;height:14px" title="Sort by User Name" /></form></td>
	<td><form method="post" action="$mythisscript"><input type="hidden" name ="orderby" value="client_idnr desc" /><input type="hidden" name="limit" value="$limit" />
	<input type="hidden" name ="userID" value="any" /><input type="image" src="images/groupID.gif" style="width:40px;height:14px" title="Sort by Group Number" /></form></td>
	<td><span class="gr">Password</span></td>
	<td><form method="post" action="$mythisscript"><input type="hidden" name ="orderby" value="maxmail_size desc" /><input type="hidden" name="limit" value="$limit" /><input type="hidden" name ="userID" value="any" />
	<input type="image" src="images/mailquota.gif" style="width:63px;height:14px" title="Sort by Mail Quota Size" /></form></td>
	<td><form method="post" action="$mythisscript"><input type="hidden" name ="orderby" value="curmail_size desc" /><input type="hidden" name="limit" value="$limit" /><input type="hidden" name ="userID" value="any" />
	<input type="image" src="images/curmail.gif" style="width:70px;height:14px" title="Sort by Volume of Current Mail" /></form></td>
	<td><form method="post" action="$mythisscript"><input type="hidden" name ="orderby" value="last_login desc" /><input type="hidden" name="limit" value="$limit" /><input type="hidden" name ="userID" value="any" />
	<input type="image" src="images/lastlogin.gif" style="width:63px;height:14px" title="Sort by date of last login" /></form></td></tr>
DBMA
        $sth =
          $dbh->prepare(
            "SELECT user_idnr, userid, passwd, client_idnr, maxmail_size, curmail_size, encryption_type, last_login FROM $dbmail_users_table ORDER BY $orderby $LIMIT"
          );
        unless ($sth->execute())
        {
            $errormessage = "ErrorID: $version.err0.14 <br />
	$DBI::errstr <br />Failed SELECT data FROM $dbmail_users_table.";
            &DBMA_ConnectStatus;
        }
        while (
               (
                $userID,       $username,     $passwd,          $GroupID,
                $maxmail_size, $curmail_size, $encryption_type, $last_login
               )
               = $sth->fetchrow_array
              )
        {
            $username =~
              s/__\@\!internal_delivery_user\!\@__/LocalDeliveryAgent/;
            $username =~ s/__public__/\#Public/;
            &filt($passwd);
            $passwd = "encrypted"
              if (   ($encryption_type =~ /md5sum/)
                  || ($encryption_type =~ /md5/)
                  || ($encryption_type =~ /crypt/));
            $passwd = "*plain*" if $encryption_type =~ //;
            $str .=
              "	<tr onmouseover=\"this.className=\'hl\';\" onmouseout=\"this.className=\'dl\';\">
	<td>$userID</td><td class=\"c0\"><a title=\"Open $username\'s Account Window\" href=\"$mythisscript\?$userID\"><img alt=\"User\" src=\"images/usericon-small.jpg\" /> $username</a></td>
	<td><form method=\"post\" action=\"$mythisscript\"><input type=\"hidden\" name=\"RQT\" value=\"all_in_this_group\" />
	<input type=\"hidden\" value=\"$GroupID\" name=\"GroupID\" /><input type=\"hidden\" name=\"required\" value=\"GroupID\" />$GroupID<input title=\"Open Group $GroupID\" type=\"image\" name=\"submit\" style=\"width:17px;height:7px\" src=\"images/gr.gif\" onmouseout=\"self.status=\'DBMA\';return true\" onmouseover=\"self.status=\'Open Group $GroupID\';return true\" /></form></td>
	<td>$passwd</td><td>$maxmail_size</td><td>$curmail_size</td><td>$last_login</td></tr>\n";
        }
        print $str if ($str);
        print <<"DBMA";
	<tr><td colspan="7"><hr style="background-color:#D6CFDE; color:#D6CFDE;height:20px" /></td></tr></table></center></div>
DBMA
        end_HTML;
        $dbh->disconnect() if ($dbh);
        exit;
    }
    if ($DBMailOldVersion eq "1")
    {
        print <<"DBMA";
	<div><center><table><tr>
	<td><form method="post" action="$mythisscript">
	<input type="hidden" name ="orderby" value="user_idnr" /><input type="hidden" name="limit" value="$limit" />
	<input type="hidden" name ="userID" value="any" />
	<input type="image" src="images/id.gif" style="width:19px;height:14px" title="Sort by User ID Number" /></form></td>
	<td><form method="post" action="$mythisscript">
	<input type="hidden" name ="orderby" value="userid" /><input type="hidden" name="limit" value="$limit" />
	<input type="hidden" name ="userID" value="any" />
	<input type="image" src="images/user.gif" style="width:32px;height:14px" title="Sort by User Name" /></form></td>
	<td><span class="gr">Password	</span></td>
	<td><form method="post" action="$mythisscript">
	<input type="hidden" name ="orderby" value="client_idnr desc" /><input type="hidden" name="limit" value="$limit" />
	<input type="hidden" name ="userID" value="any" />
	<input type="image" src="images/groupID.gif" style="width:40px;height:14px" title="Sort by Group Number" /></form></td>
	<td><form method="post" action="$mythisscript">
	<input type="hidden" name ="orderby" value="maxmail_size desc" /><input type="hidden" name="limit" value="$limit" />
	<input type="hidden" name ="userID" value="any" />
	<input type="image" src="images/mailquota.gif" style="width:63px;height:14px" title="Sort by Mail Quota Size" /></form></td>
	<td><form method="post" action="$mythisscript">
	<input type="hidden" name ="orderby" value="last_login desc" /><input type="hidden" name="limit" value="$limit" />
	<input type="hidden" name ="userID" value="any" />
	<input type="image" src="images/lastlogin.gif" style="width:63px;height:14px" title="Sort by date of last login" /></form></td></tr>
DBMA
        $sth =
          $dbh->prepare(
            "SELECT user_idnr,  userid,  passwd,  client_idnr,  maxmail_size, encryption_type, $cmailsize last_login FROM $dbmail_users_table ORDER BY $orderby $LIMIT"
          );
        unless ($sth->execute())
        {
            $errormessage = "
	ErrorID: $version.err0.15 <br />
	$DBI::errstr <br />Failed SELECT data FROM $dbmail_users_table.";
            &DBMA_ConnectStatus;
        }
        while (
               (
                $userID,       $username,        $passwd,       $GroupID,
                $maxmail_size, $encryption_type, $curmail_size, $last_login
               )
               = $sth->fetchrow_array
              )
        {
            $username =~
              s/__\@\!internal_delivery_user\!\@__/LocalDeliveryAgent/;
            $username =~ s/__public__/\#Public/;
            &filt($passwd);
            $passwd = "encrypted"
              if (   ($encryption_type =~ /md5sum/)
                  || ($encryption_type =~ /md5/)
                  || ($encryption_type =~ /crypt/));
            $passwd = "*plain*" if $encryption_type =~ //;
            $str .=
              "	<tr onmouseover=\"this.className=\'hl\';\" onmouseout=\"this.className=\'dl\';\">
	<td>$userID</td>
	<td class=\"c0\"><a title=\"Open $username\'s Account Window\" href=\"$mythisscript\?$userID\">
	<img alt=\"User\" src=\"images/usericon-small.jpg\" /> $username</a></td>
	<td>$passwd</td>
	<td>$GroupID</td>
	<td>$maxmail_size</td>
	<td>$curmail_size</td>
	<td>$last_login</td></tr>\n";
        }
        print $str if ($str);
        print <<"DBMA";
	</table></center></div>
DBMA
        end_HTML;
        $dbh->disconnect() if ($dbh);
        exit;
    }
}
############################################################## - sub List_Group_Aliases
sub List_Group_Aliases ($)
{

    # Check that the aliases and users groups match so that RESTRICTGroupID (Single Group)
    # Admins are not able to accidentally redirect mail from another group.

if ($sqltype =~ /pgsql/)
{
    $dbh->do("
UPDATE $dbmail_aliases_table
JOIN $dbmail_users_table
ON $dbmail_aliases_table.deliver_to = CAST($dbmail_users_table.user_idnr AS text)
SET $dbmail_aliases_table.client_idnr = $dbmail_users_table.client_idnr
WHERE $dbmail_aliases_table.deliver_to = CAST($dbmail_users_table.user_idnr AS text)"
    );
}
if ($sqltype =~ /mysql/)
{
    $dbh->do("
UPDATE $dbmail_aliases_table
JOIN $dbmail_users_table
ON $dbmail_aliases_table.deliver_to = $dbmail_users_table.user_idnr
SET $dbmail_aliases_table.client_idnr = $dbmail_users_table.client_idnr
WHERE $dbmail_aliases_table.deliver_to = $dbmail_users_table.user_idnr"
    );
}

    $dbh->commit();

    &checkrequired;
    &header;
    print <<"DBMA";
	<div><center><table style="font-size:13px;width:738px;text-align:left">
	<tr><td colspan="4"><h1>Regular Aliases</h1></td></tr>
	<td style="width:45px"><span class="gr">Group $GroupID</span></td>
	<td><span class="gr">Aliases in alpha sort</span></td>
	<td style="width:45px"><span class="gr">ID</span></td>
	<td><span class="gr">User Name</span></td>
	<td><span class="gr">Current Mail</span></td>
	<td><span class="gr">Last Login</span></td>
	<td></td>
	</tr>
DBMA

if ($sqltype =~ /pgsql/)
{
    $sth =
      $dbh->prepare(
        "SELECT $dbmail_users_table.client_idnr, alias_idnr, userid, alias, deliver_to, $cmailsize last_login FROM $dbmail_aliases_table  JOIN $dbmail_users_table ON $dbmail_aliases_table.deliver_to = CAST($dbmail_users_table.user_idnr as text) WHERE $dbmail_users_table.client_idnr = $GroupID ORDER by alias"
      );
}
if ($sqltype =~ /mysql/)
{
    $sth =
      $dbh->prepare(
        "SELECT $dbmail_users_table.client_idnr, alias_idnr, userid, alias, deliver_to, $cmailsize last_login FROM $dbmail_aliases_table  JOIN $dbmail_users_table ON $dbmail_aliases_table.deliver_to=$dbmail_users_table.user_idnr WHERE $dbmail_users_table.client_idnr = $GroupID ORDER by alias"
      );
}

    unless ($sth->execute())
    {
        $errormessage = "
	ErrorID: $version.err0.16 <br />$DBI::errstr <br />Failed To select data.";
        &DBMA_ConnectStatus;
    }
    while (
           (
            $GroupID, $alias_idnr,   $username, $alias,
            $userID,  $cur_mailsize, $last_login
           )
           = $sth->fetchrow_array
          )
    {
        &filt($alias);
        $alias =~ s/\@/\&#64;/g if $alias;
        $str .=
          "	<tr onmouseover=\"this.className=\'hl\';\" onmouseout=\"this.className=\'dl\';\">
	<td><form method=\"post\" action=\"$mythisscript\"><input type=\"hidden\" name=\"RQT\" value=\"all_in_this_group\" />
	<input type=\"hidden\" value=\"$GroupID\" name=\"GroupID\" /><input type=\"hidden\" name=\"required\" value=\"GroupID\" /><input title=\"Open Group $GroupID\" type=\"image\" name=\"submit\" style=\"width:17px;height:7px\" src=\"images/gr.gif\" onmouseout=\"self.status=\'DBMA\';return true\" onmouseover=\"self.status=\'Open Group $GroupID\';return true\" /></form></td>
	<td class=\"c0\"><a title=\"Find this account\" href=\"$mythisscript\?$userID\" onmouseover=\"self.status=\'DBMA\';return true\" /><img alt=\"User\" src=\"images/usericon-small.jpg\" /> $alias</a></td>
	<td class=\"c0\"><a title=\"Open $username\'s account\?\" href=\"$mythisscript\?$userID\">$userID</a></td><td class=\"c0\"><a title=\"Open $username\'s account\?\" href=\"$mythisscript\?$userID\"><img alt=\"User\" src=\"images/usericon-small.jpg\" /> $username</a></td><td>$cur_mailsize</td><td>$last_login</td>
	<td><form method=\"post\" action=\"$mythisscript\"><input type=\"hidden\" name=\"RQT\" value=\"41\"><input type=\"hidden\" name=\"alias_idnr\" value=\"$alias_idnr\"><input type=\"hidden\" name=\"alias\" value=\"$alias\"><input type=\"hidden\" name=\"GroupID\" value=\"$GroupID\">
	<input type=\"image\" title=\"Delete by alias_idnr $alias_idnr : $alias\?\" value =\"submit\" onclick=\"return confirm(\'DELETE $alias : Are you sure?\')\" src=\"images/delete.gif\" onmouseover=\"self.status=\'Delete alias_idnr $alias_idnr $alias\';return true\" onmouseout=\"self.status=\'DBMA\';return true\" style=\"width:37px;height:14px\" /></form></td></tr>\n";
    }
    print $str if ($str);
    print "</table></center></div>\n</body>\n</html>\n";
    $dbh->disconnect() if ($dbh);
    exit;
}
############################################################## - sub List_Global_Aliases
sub List_Global_Aliases
{
    &header;
    &numusers;
    $alias = "";

if ($sqltype =~ /pgsql/)
{
    $sth = $dbh->prepare("
SELECT userid, alias_idnr, alias, deliver_to, $dbmail_aliases_table.client_idnr, $cmailsize last_login 
FROM $dbmail_aliases_table
JOIN $dbmail_users_table
ON $dbmail_aliases_table.deliver_to = CAST($dbmail_users_table.user_idnr AS text)
ORDER by alias $LIMIT"
    );
}
if ($sqltype =~ /mysql/)
{
    $sth = $dbh->prepare("
SELECT userid, alias_idnr, alias, deliver_to, $dbmail_aliases_table.client_idnr, $cmailsize last_login 
FROM $dbmail_aliases_table
JOIN $dbmail_users_table
ON $dbmail_aliases_table.deliver_to=$dbmail_users_table.user_idnr
ORDER by alias $LIMIT"
    );
}
    unless ($sth->execute())
    {
        $errormessage = "
	ErrorID: $version.err0.18 <br />$DBI::errstr <br />Failed to find every alias.";
        &DBMA_ConnectStatus;
    }
    while (
           (
            $username, $alias_idnr,   $alias, $userID,
            $GroupID,  $cur_mailsize, $last_login
           )
           = $sth->fetchrow_array
          )
    {
        $alias =~ s/ //         if $alias;
        $alias =~ s/\@/\&#64;/g if $alias;

        $str .=
          "	<tr onmouseover=\"this.className=\'hl\';\" onmouseout=\"this.className=\'dl\';\">
	<td><form method=\"post\" action=\"$mythisscript\"><input type=\"hidden\" name=\"RQT\" value=\"all_in_this_group\" />
	<input type=\"hidden\" value=\"$GroupID\" name=\"GroupID\" /><input type=\"hidden\" name=\"required\" value=\"GroupID\" /><input title=\"Open Group $GroupID\" type=\"image\" name=\"submit\" style=\"width:17px;height:7px\" src=\"images/gr.gif\" onmouseout=\"self.status=\'DBMA\';return true\" onmouseover=\"self.status=\'Open Group $GroupID\';return true\" />$GroupID</form></td>
	<td class=\"c0\"><a title = \"Open user account window for $username\" href=\"$mythisscript\?$userID\" onmouseover=\"self.status=\'DBMA: Open user account window for $username\';return true\"><img alt=\"User\" src=\"images/usericon-small.jpg\" /> $alias</a></td>
	<td class=\"c0\"><a title = \"Open user account window for $username\" href=\"$mythisscript\?$userID\" onmouseover=\"self.status=\'DBMA: Open User Account Window for $username\';return true\">$userID</a></td>
	<td class=\"c0\"><a title=\"Open $username\'s account\?\" href=\"$mythisscript\?$userID\" onmouseover=\"self.status=\'DBMA: Open User Account Window for $username\';return true\"><img alt=\"User\" src=\"images/usericon-small.jpg\" /> $username</a></td>
	<td>$cur_mailsize</td><td>$last_login</td><td><form method=\"post\" action=\"$mythisscript\">
	<input type=\"hidden\" name=\"RQT\" value=\"42\" />
	<input type=\"hidden\" name=\"alias_idnr\" value=\"$alias_idnr\" />
	<input type=\"hidden\" name=\"alias\" value=\"$alias\" />
	<input type=\"image\" title=\"Delete by alias_idnr $alias_idnr : $alias\?\" value =\"submit\" onclick=\"return confirm(\'DELETE $alias : Are you sure?\')\" src=\"images/delete.gif\" onmouseover=\"self.status=\'Delete alias_idnr $alias_idnr $alias\';return true\" onmouseout=\"self.status=\'DBMA\';return true\" style=\"width:37px;height:14px\" /></form></td></tr>\n";
    }

    $sth->finish() if ($sth);

    $username     = "";
    $alias_idnr   = "";
    $alias        = "";
    $userID       = "";
    $cur_mailsize = "";
    $last_login   = "";
    $GroupID      = "";

    $sth = $dbh->prepare("
SELECT DISTINCT $dbmail_aliases_table.alias_idnr, $dbmail_aliases_table.alias, $dbmail_aliases_table.deliver_to, $dbmail_aliases_table.client_idnr
FROM $dbmail_aliases_table
WHERE $dbmail_aliases_table.deliver_to like '%\@%'
GROUP by $dbmail_aliases_table.alias_idnr, $dbmail_aliases_table.deliver_to, $dbmail_aliases_table.alias, $dbmail_aliases_table.deliver_to, $dbmail_aliases_table.client_idnr
$LIMIT");
    unless ($sth->execute())
    {
        $errormessage = "$DBI::errstr <br />Failed to find orphans.";
        &DBMA_ConnectStatus;
    }

    while (($alias_idnr, $alias, $deliver_to, $GroupID) = $sth->fetchrow_array)
    {
        $alias =~ s/ //         if $alias;
        $alias =~ s/\@/\&#64;/g if $alias;
        $username = " mail forward" if ($deliver_to =~ m/\@/i);

        $str2 .=
          "	<tr onmouseover=\"this.className=\'hl\';\" onmouseout=\"this.className=\'dl\';\">
	<td><form method=\"post\" action=\"$mythisscript\"><input type=\"hidden\" name=\"RQT\" value=\"all_in_this_group\" />
	<input type=\"hidden\" value=\"$GroupID\" name=\"GroupID\" /><input type=\"hidden\" name=\"required\" value=\"GroupID\" /><input title=\"Open Group $GroupID\" type=\"image\" name=\"submit\" style=\"width:17px;height:7px\" src=\"images/gr.gif\" onmouseout=\"self.status=\'DBMA\';return true\" onmouseover=\"self.status=\'Open Group $GroupID\';return true\" />$GroupID</form></td>
	<td class=\"c0\"><img alt=\"User\" src=\"images/usericon-small.jpg\" /> $alias</td>
	<td colspan=\"2\" class=\"c0\">$deliver_to</td>
	<td colspan=\"1\" class=\"c0\">$username</td>
	<td><form method=\"post\" action=\"$mythisscript\">
	<input type=\"hidden\" name=\"RQT\" value=\"14\" />
	<input type=\"hidden\" name=\"alias_idnr\" value=\"$alias_idnr\" />
	<input type=\"hidden\" name=\"GroupID\" value=\"$GroupID\" />
	<input type=\"hidden\" name=\"deliver_to\" value=\"$deliver_to\" />
	<input type=\"hidden\" name=\"deliver_from\" value=\"$alias\" />
	<input type=\"image\" value =\"submit\" alt=\"Open an Editor for this forward\" src=\"images/edit.gif\" onmouseover=\"self.status=\'Edit Mail Forward\';return true\" onmouseout=\"self.status=\'DBMA\';return true\" style=\"width:22px;height:14px\" /> <span style=\"vertical-align:top\" class=\"gr\">Forward</span></form></td>
	<td><form method=\"post\" action=\"$mythisscript\">
	<input type=\"hidden\" name=\"RQT\" value=\"42\" />
	<input type=\"hidden\" name=\"alias_idnr\" value=\"$alias_idnr\" />
	<input type=\"hidden\" name=\"alias\" value=\"$alias\" />
	<input type=\"image\" title=\"Delete by alias_idnr $alias_idnr : $alias\?\" value =\"submit\" onclick=\"return confirm(\'DELETE $alias : Are you sure?\')\" src=\"images/delete.gif\" onmouseover=\"self.status=\'Delete alias_idnr $alias_idnr $alias\';return true\" onmouseout=\"self.status=\'DBMA\';return true\" style=\"width:37px;height:14px\" /></form></td></tr>\n";
    }
############################## find orphans
    $username     = "";
    $alias_idnr   = "";
    $alias        = "";
    $userID       = "";
    $cur_mailsize = "";
    $last_login   = "";
    $GroupID      = "";

if ($sqltype =~ /pgsql/)
{
    $sth = $dbh->prepare("
SELECT DISTINCT $dbmail_aliases_table.alias_idnr, $dbmail_aliases_table.alias, $dbmail_aliases_table.deliver_to, $dbmail_aliases_table.client_idnr
FROM $dbmail_aliases_table
LEFT JOIN $dbmail_users_table ON $dbmail_aliases_table.deliver_to = CAST($dbmail_users_table.user_idnr AS text)
WHERE $dbmail_users_table.user_idnr IS NULL AND $dbmail_aliases_table.deliver_to NOT LIKE '%\@%'
GROUP by $dbmail_aliases_table.alias_idnr, $dbmail_aliases_table.deliver_to, $dbmail_aliases_table.alias, $dbmail_aliases_table.deliver_to, $dbmail_aliases_table.client_idnr
$LIMIT");
}
if ($sqltype =~ /mysql/)
{
    $sth = $dbh->prepare("
SELECT DISTINCT $dbmail_aliases_table.alias_idnr, $dbmail_aliases_table.alias, $dbmail_aliases_table.deliver_to, $dbmail_aliases_table.client_idnr
FROM $dbmail_aliases_table
WHERE $dbmail_aliases_table.deliver_to like '%\@%'
GROUP by $dbmail_aliases_table.alias_idnr, $dbmail_aliases_table.deliver_to, $dbmail_aliases_table.alias, $dbmail_aliases_table.deliver_to, $dbmail_aliases_table.client_idnr
$LIMIT");
}
    unless ($sth->execute())
    {
        $errormessage = "$DBI::errstr <br />Failed to find orphans.";
        &DBMA_ConnectStatus;
    }

    while (($alias_idnr, $alias, $deliver_to, $GroupID) = $sth->fetchrow_array)
    {
        $alias =~ s/ //         if $alias;
        $alias =~ s/\@/\&#64;/g if $alias;
        if ($deliver_to =~ m/\@/i) { $username = " mail forward" }
        else { $username = "<em>Orphan</em>"; }

        $str3 .=
          "	<tr title=\"Orphan?\" style=\"background:#FFE8E9;\" onmouseover=\"this.className=\'hl\';\" onmouseout=\"this.className=\'dl\';\">
	<td><form style=\"margin-bottom:5px\" method=\"post\" action=\"$mythisscript\"><input type=\"hidden\" name=\"RQT\" value=\"all_in_this_group\" />
	<input type=\"hidden\" value=\"$GroupID\" name=\"GroupID\" /><input type=\"hidden\" name=\"required\" value=\"GroupID\" /><input title=\"Open Group $GroupID\" type=\"image\" name=\"submit\" style=\"width:17px;height:7px\" src=\"images/gr.gif\" onmouseout=\"self.status=\'DBMA\';return true\" onmouseover=\"self.status=\'Open Group $GroupID\';return true\" />$GroupID</form></td>
	<td class=\"c0\"><img alt=\"User\" src=\"images/usericon-small.jpg\" /> $alias</td>
	<td colspan=\"2\" class=\"c0\"><a title=\"No such user ID number.\" href=\"$mythisscript\?$deliver_to\">$deliver_to</a></td>
	<td colspan=\"1\" class=\"c0\">$username</a></td>
	<td><form method=\"post\" action=\"$mythisscript\">
	<input type=\"hidden\" name=\"RQT\" value=\"14\" />
	<input type=\"hidden\" name=\"alias_idnr\" value=\"$alias_idnr\" />
	<input type=\"hidden\" name=\"GroupID\" value=\"$GroupID\" />
	<input type=\"hidden\" name=\"deliver_to\" value=\"$deliver_to\" />
	<input type=\"hidden\" name=\"deliver_from\" value=\"$alias\" />
	<input type=\"image\" value =\"submit\" alt=\"Edit and fix this orphan\" src=\"images/edit.gif\" onmouseover=\"self.status=\'Edit Mail Forward\';return true\" onmouseout=\"self.status=\'DBMA\';return true\" style=\"width:22px;height:14px\" /> <span style=\"vertical-align:top\" class=\"gr\">Orphan</span></form></td>
	<td><form method=\"post\" action=\"$mythisscript\">
	<input type=\"hidden\" name=\"RQT\" value=\"42\" />
	<input type=\"hidden\" name=\"alias_idnr\" value=\"$alias_idnr\" />
	<input type=\"hidden\" name=\"alias\" value=\"$alias\" />
	<input type=\"image\" title=\"Delete by alias_idnr $alias_idnr : $alias\?\" value =\"submit\" onclick=\"return confirm(\'DELETE $alias : Are you sure?\')\" src=\"images/delete.gif\" onmouseover=\"self.status=\'Delete alias_idnr $alias_idnr $alias\';return true\" onmouseout=\"self.status=\'DBMA\';return true\" style=\"width:37px;height:14px\" /></form></td></tr>\n";
    }
###### print the contents of the page
    print <<"DBMA";
	<div><center><table><tr><td colspan="4"><h3>All Aliases Found in $dbmail_aliases_table.</h3></td></tr>
	<tr>
	<td><span class="gr">Group</span></td>
	<td><span class="gr">Alias</span></td>
	<td><span class="gr">Account</span></td>
	<td><span class="gr">Local Recipient</span></td>
	<td><span class="gr">Cur Mail</span></td>
	<td><span class="gr">Last Login</span></td>
	<td style="width:37px">Delete<span class="gr"></span></td></tr>
DBMA

    print $str3 if ($str3);
    print $str  if ($str);
    print $str2 if ($str2);

    print <<"DBMA";
	<tr><td colspan="7"><hr style="background-color:#D6CFDE; color:#D6CFDE;height:20px" /></td></tr></table></center></div>
DBMA
    end_HTML;
}
############################################################## - sub List_all_Forwards RQT20
sub List_all_Forwards
{
    my $deliver_to;
    &header;
    &numusers;
    print <<"DBMA";
	<div><center><table style="font-size:13px;width:738px;text-align:left">
	<tr><td><h3>Forwards</h3></td></tr>
	<tr><td style="width:50px"><span class="gr">Group</span></td>
	<td><span class="gr">Forward From:</span></td>
	<td><span class="gr">To: </span></td>
	<td><span class="gr">             </span></td>
	<td><span class="gr">             </span></td>
	</tr>
DBMA

    if ($RESTRICTGroupID =~ m/[1-9]/i)
    {
        $sth = $dbh->prepare(
            "SELECT alias_idnr, alias, deliver_to, client_idnr FROM $dbmail_aliases_table
WHERE $dbmail_aliases_table.deliver_to LIKE '%@%' AND client_idnr = $RESTRICTGroupID
ORDER BY deliver_to $LIMIT"
                            );
    }
    elsif ($RESTRICTGroupID eq "any")
    {
        $sth = $dbh->prepare(
            "SELECT alias_idnr, alias, deliver_to, client_idnr FROM $dbmail_aliases_table
WHERE $dbmail_aliases_table.deliver_to LIKE '%@%'
ORDER BY deliver_to $LIMIT"
                            );
    }
    unless ($sth->execute())
    {
        $errormessage = "
	ErrorID: $version.err0.17 <br />$DBI::errstr <br />Failed to get forwards.";
        &DBMA_ConnectStatus;
    }
    while (($alias_idnr, $alias, $deliver_to, $GroupID) = $sth->fetchrow_array)
    {
        $alias =~ s/ //         if $alias;
        $alias =~ s/\@/\&#64;/g if $alias;
        $str2 .=
          "	<tr onmouseover=\"this.className=\'hl\';\" onmouseout=\"this.className=\'dl\';\">
	<td><form method=\"post\" action=\"$mythisscript\">
	<input type=\"hidden\" name=\"RQT\" value=\"all_in_this_group\" />
	<input type=\"hidden\" value=\"$GroupID\" name=\"GroupID\" />
	<input type=\"hidden\" name=\"required\" value=\"GroupID\" />$GroupID
	<input title=\"Open Group $GroupID\" type=\"image\" name=\"submit\" style=\"width:17px;height:7px\" src=\"images/gr.gif\" onmouseout=\"self.status=\'DBMA\';return true\" onmouseover=\"self.status=\'Open Group $GroupID\';return true\" /></form></td>
	<td class=\"c0\"><a title=\"$alias forwards to $deliver_to Click to open User $deliver_to\" href=\"$mythisscript\?$alias\"><img alt=\"User\" src=\"images/usericon-small.jpg\" /> $alias</a></td>
	<td class=\"c0\"><a title=\"$alias forwards to $deliver_to Click to open User $deliver_to\" href=\"$mythisscript\?$deliver_to\"><img alt=\"User\" src=\"images/usericon-small.jpg\" /> $deliver_to</a></td>
	<td><form method=\"post\" action=\"$mythisscript\">
	<input type=\"hidden\" name=\"RQT\" value=\"14\" />
	<input type=\"hidden\" name=\"alias_idnr\" value=\"$alias_idnr\" />
	<input type=\"hidden\" name=\"GroupID\" value=\"$GroupID\" />
	<input type=\"hidden\" name=\"deliver_to\" value=\"$deliver_to\" />
	<input type=\"hidden\" name=\"deliver_from\" value=\"$alias\" />
	<input type=\"image\" value =\"submit\" alt=\"Edit and change this forward\" src=\"images/edit.gif\" onmouseover=\"self.status=\'Edit Mail Forward\';return true\" onmouseout=\"self.status=\'DBMA\';return true\" style=\"width:22px;height:14px\" /></form></td>
	<td><form method=\"post\" action=\"$mythisscript\">
	<input type=\"hidden\" name=\"RQT\" value=\"9\" />
	<input type=\"hidden\" name=\"alias_idnr\" value=\"$alias_idnr\" />
	<input type=\"hidden\" name=\"alias\" value=\"$alias\" />
	<input type=\"image\" value =\"submit\" src=\"images/delete.gif\" onmouseover=\"self.status=\'Delete Mail Forward\';return true\" onmouseout=\"self.status=\'DBMA\';return true\" alt=\"Delete This forward\" style=\"width:37px;height:14px\" onclick=\"return confirm(\'DELETE $alias : Are you sure?\')\" /></form></td></tr>\n";
    }
    $dbh->disconnect() if ($dbh);
    print $str2        if ($str2);
    print <<"DBMA";
        <tr><td colspan="5"><hr style="background-color:#D6CFDE; color:#D6CFDE;height:20px" /></td></tr></table></center></div>
        </body></html>
DBMA
    exit;
}
############################################################## - sub List_auto_notifications  RQT22
sub List_auto_notifications
{
    $sth =
      $dbh->prepare(
        "SELECT userid, $dbmail_auto_notifications_table.user_idnr, notify_address from $dbmail_auto_notifications_table LEFT JOIN $dbmail_users_table ON $dbmail_users_table.user_idnr = $dbmail_auto_notifications_table.user_idnr where $dbmail_auto_notifications_table.notify_address LIKE '%@%' ORDER BY notify_address $LIMIT"
      );
    unless ($sth->execute())
    {
        $errormessage =
          "<span class=\"stats\">Is this an Older version of DBMail WITHOUT the Auto Notifications feature? If so, that explains why your database does not contain auto_notifications? If you need this feature, visit http://www.dbmail.org to upgrade to a more recent version.<br />You attempted to SELECT userid, user_idnr and notify_address from $dbmail_auto_notifications_table.</span><br />$DBI::errstr ";
        &DBMA_ConnectStatus;
    }
    while (($username, $userID, $notify_address) = $sth->fetchrow_array)
    {
        $notify_address =~ s/ //         if $alias;
        $notify_address =~ s/\@/\&#64;/g if $alias;
        $str .=
          "	<tr onmouseover=\"this.className=\'hl\';\" onmouseout=\"this.className=\'dl\';\">
	<td class=\"c0\"><a title=\"User Account Window for $username\" href=\"$mythisscript?$userID\"><img alt=\"User\" src=\"images/usericon-small.jpg\" />$username ($userID)</a></td>
	<td class=\"c0\">a notice is sent to:</td><td class=\"c0\"><a title=\"click here only if $notify_address is local\" href=\"$mythisscript?$notify_address\"><img alt=\"User\" src=\"images/usericon-small.jpg\" />$notify_address</a></td>
	<td><form method=\"post\" action=\"$mythisscript\"><input type=\"hidden\" name=\"userID\" value=\"$userID\" /><input type=\"hidden\" name=\"RQT\" value=\"56\" /><input type=\"image\" value =\"submit\" src=\"images/delete.gif\" onmouseover=\"self.status='Delete Auto Notification';return true\" onmouseout=\"self.status='DBMA';return true\" style=\"vertical-align:bottom;width:37px;height:14px\" title=\"Delete Auto Notification\" onclick=\"return confirm('DELETE Auto Notify')\" /></form></td></tr>\n";
    }
    &header;
    print <<"DBMA";
	<div><center><table style="font-size:90%;width:738px">
	<tr><td colspan="4"><h3>Auto Notifications</h3></td></tr>
	<tr><td><span class="gr">When User</span></td><td><span class="gr">Gets Mail</span></td>
	<td><span class="gr">Notify Address</span></td><td><span class="rd">Delete</span></td></tr>
DBMA
    print $str if ($str);
    print "</table></center></div>\n";
    end_HTML;
    $dbh->disconnect() if ($dbh);
    exit;
}
############################################################## - sub showrecentlogins RQT23
sub showrecentlogins
{
    if ($DBMailOldVersion eq "1") { &make_form; }
    &header;
    print <<"DBMA";
	<div><center><table style="font-size:13px;margin-right:150px;width:560px;text-align:left">
	<tr><td colspan="3"><b>Recent Logins Pop Before SMTP</b></td></tr>
	<tr><td style="width:150px"><span class="gr">ID Number	</span></td>
	<td style="width:150px"><span class="gr">IP Address 	</span></td>
	<td><span class="gr">Date</span></td></tr>
DBMA
    my ($since, $ipnumber, $str, $idnr);
    if ($sqltype =~ /mysql/)
    {
        $sth =
          $dbh->prepare(
            "SELECT idnr, since, ipnumber from $dbmail_pbsp_table WHERE DATE_SUB(NOW(), INTERVAL $loginterval HOUR) <= since ORDER BY  since"
          );
        $sth->execute();
        while (($idnr, $ipnumber, $since) = $sth->fetchrow_array)
        {
            $str1 .=
              "	<tr onmouseover=\"this.className=\'hl\';\" onmouseout=\"this.className=\'dl\';\"><td style=\"width:150px\">$idnr</td><td style=\"width:150px\">$since</td><td>$ipnumber</td></tr>\n";
        }
        print $str1 if ($str1);
        print "	</table></center></div>\n";
        $sth->finish() if ($sth);
    }
    elsif ($sqltype =~ /pgsql/)
    {
        $sth =
          $dbh->prepare(
            "SELECT idnr, since, ipnumber from $dbmail_pbsp_table WHERE since > CURRENT_TIMESTAMP -INTERVAL '$loginterval hours' ORDER BY since LIMIT 500"
          );
        $sth->execute();
        while (($idnr, $ipnumber, $since) = $sth->fetchrow_array)
        {
            $str1 .=
              "	<tr onmouseover=\"this.className=\'hl\';\" onmouseout=\"this.className=\'dl\';\"><td style=\"width:150px\">$idnr</td><td style=\"width:150px\">$since</td><td>$ipnumber</td></tr>\n";
        }
        print $str1 if ($str1);
        print "	</table></center></div>\n";
        $sth->finish() if ($sth);
    }
    print <<"DBMA";
	<div><center><table style="font-size:13px;margin-right:150px;width:560px;text-align:left">
	<tr><td colspan="3"><b>Last $loginterval hrs Logins By User Name</b></td></tr>
	<tr>
	<td style="width:150px"><span class="gr">User  	</span></td>
	<td style="width:150px"><span class="gr">Current Mailbox</span></td>
	<td><span class="gr">Date</span></td>
	</tr>
DBMA
    if ($sqltype =~ /mysql/)
    {
        $sth =
          $dbh->prepare(
            "SELECT userid, $cmailsize last_login from $dbmail_users_table WHERE DATE_SUB(NOW(), INTERVAL $loginterval HOUR) <= last_login ORDER BY last_login"
          );
        unless ($sth->execute())
        {
            $errormessage = "
	ErrorID: $version.err0.20 <br />
	$DBI::errstr <br />Failed SELECT userid, $cmailsize last_login from $dbmail_users_table.";
            &DBMA_ConnectStatus;
        }
        while (($username, $curmail_size, $last_login) = $sth->fetchrow_array)
        {
            $str .=
              "	<tr onmouseover=\"this.className=\'hl\';\" onmouseout=\"this.className=\'dl\';\"><td style=\"width:150px\"><a href=\"$mythisscript?$username\">$username</a></td><td style=\"width:150px\">$curmail_size</td><td>$last_login</td></tr>\n";
        }
        print $str     if ($str);
        $sth->finish() if ($sth);
        print <<"DBMA";
	</table></center></div>
	
DBMA
        end_HTML;
    }
    elsif ($sqltype =~ /pgsql/)
    {
        $sth =
          $dbh->prepare(
            "SELECT userid, $cmailsize last_login from $dbmail_users_table WHERE last_login > CURRENT_TIMESTAMP -INTERVAL '$loginterval hours' ORDER BY last_login LIMIT 500"
          );
        unless ($sth->execute())
        {
            $errormessage = "
	ErrorID: $version.err0.21 <br />
	$DBI::errstr <br />Failed SELECT userid, $cmailsize last_login from $dbmail_users_table.";
            &DBMA_ConnectStatus;
        }
        while (($username, $curmail_size, $last_login) = $sth->fetchrow_array)
        {
            $str .=
              "	<tr onmouseover=\"this.className=\'hl\';\" onmouseout=\"this.className=\'dl\';\"><td style=\"width:150px\"><a href=\"$mythisscript?$username\">$username</a></td><td style=\"width:150px\">$curmail_size</td><td>$last_login</td></tr>\n";
        }
        print $str     if ($str);
        $sth->finish() if ($sth);
        print <<"DBMA";
	</table></center></div>
	
DBMA
        end_HTML;
    }
    $dbh->disconnect() if ($dbh);
    exit;
}
############################################################## - sub numusers
sub numusers
{
    $addtext     = "";
    $andgroup    = "";
    $andmoretext = "";
    my $numusers = "";
    my $userstr  = "";
    if ($FORM{'GroupID'})
    {
        $andgroup = "WHERE client_idnr = " . $GroupID;
        $addtext  = "in Group " . $GroupID;
    }
    else
    {
        $andgroup = " ";
        $addtext  = "Total";
    }
    if ($FORM{'limit'}) { $andmoretext = "(Display $LIMIT)" || ""; }
    $sth = $dbh->prepare("SELECT COUNT(*) FROM $dbmail_users_table $andgroup");
    $sth->execute();
    while (($numusers) = $sth->fetchrow_array)
    {
        $userstr .=
          "	<div><form action=\"$mythisscript\" method=\"post\"><center><table><tr><td style=\"background-color:#ffffc4; color:#4602A0\"><span style=\"font-family:sans-serif;font-size:95%\"><b>$numusers Email Accounts $addtext $andmoretext</b>.
	Click <img src=\"images/dn.gif\" alt=\"Click this below to sort list\" style=\"width:7px;height:9px\" /> to resort by category.</span>
	<input type=\"hidden\" value=\"2\" name=\"RQT\" /><input type=\"text\" title=\"Please enter the user ID or name.\" size=\"10\" style=\"font-family:arial;font-size:9px\" onmouseover=\"this.className=\'back2\';\" onmouseout=\"this.className=\'front\';\" class=\"front\" name=\"userID\" />
	<input title=\"Search for user\" type=\"image\" style=\"vertical-align:top;width:100px;height:18px;\" src=\"images/search_user.gif\" />
	</td></tr></table></center></form></div>";
        last;
    }
    print $userstr;
    $sth->finish() if ($sth);
}
## - TOOLS WHICH CHANGE THE DATABASE
############################################################## - sub MODIFY_User_SQL
sub MODIFY_User_SQL
{
    &checkrequired;
    &check_if_RFC_alias($newalias)
      if (($FORM{'newalias'}) || ($newalias =~ /0-9a-zA-Z/));
    $sql =
      "UPDATE $dbmail_users_table SET userid = '$username' where user_idnr = '$newuserID'";
    $sth = $dbh->prepare($sql);
    $sth->execute();
    $sth->finish() if ($sth);
    unless ($dbh->commit)
    {
        $errormessage = "
	ErrorID: $version.err0.22 <br />$DBI::errstr <br />Error: commit FAIL for user update";
        &DBMA_ConnectStatus;
    }
    if (   ($FORM{'encrypttype'} eq "plain")
        || ($FORM{'encrypttype'} eq "clear")
        || ($FORM{'encrypttype'} eq "on")
        || ($FORM{'encrypttype'} eq "off")
        || ($FORM{'encrypttype'} eq "blank")
        || ($FORM{'encrypttype'} eq "ascii")
        || ($FORM{'encrypttype'} eq "cleartext")
        || ($FORM{'encrypttype'} eq "plaintext")
        || ($FORM{'encrypttype'} eq "none")
        || ($FORM{'encrypttype'} eq "")
        || ($FORM{'encrypttype'} eq " ")
        && ($FORM{'encrypttype'} ne "md5sum")
        && ($FORM{'encrypttype'} ne "crypt")
        && ($FORM{'encrypttype'} ne "md5")
        && ($FORM{'encrypttype'} ne "MD5"))
    {
        $encrypttype = "";
    }
    else
    {
        $encrypttype = $FORM{'encrypttype'};
        $encrypttype =~ s/md5-hash/md5sum/g
          ;    # fixes an error in dbmail where md5-hash is interpreted as "md5"
    }
    $sql =
      "UPDATE $dbmail_users_table SET encryption_type = '$encrypttype' where user_idnr = '$newuserID'";
    $sth = $dbh->prepare($sql);
    unless ($sth->execute())
    {
        $errormessage = "
	ErrorID: $version.err0.23 <br />
	$DBI::errstr <br />Failed UPDATE $dbmail_users_table SET encryption_type";
        &DBMA_ConnectStatus;
    }
    $sth->finish() if ($sth);
########## - changepassword
    $FORM{'encrypttype'} =~ s/md5-hash/md5sum/g;
    $encrypttype         =~ s/md5-hash/md5sum/g;
    if (   ($FORM{'changepassword'})
        && ($changepassword =~ /pBq1XZ6StL9xpjFUrOlJ03cRws/))
    {
        if (($sqltype =~ /mysql/) && ($encrypttype =~ /md5sum/))
        {

            $password = &MD5_hash($FORM{'password'});
            $sql      =
              "UPDATE $dbmail_users_table SET passwd = '$password' where user_idnr = '$newuserID'";
            $sth = $dbh->prepare($sql);
            unless ($sth->execute())
            {
                $errormessage =
                  "ErrorID: $version.err0.25 $DBI::errstr Failed SET new passwd.";
                &DBMA_ConnectStatus;
            }
            $dbh->commit();

        }
        elsif (   ($encrypttype eq "md5")
               || ($encrypttype eq "MD5")
               && ($encrypttype ne "md5sum")
               && ($encrypttype ne "plain")
               && ($encrypttype ne "clear")
               && ($encrypttype ne "crypt")
               && ($encrypttype ne "cleartext")
               && ($encrypttype ne " "))
        {
            $results = &MD5_Encrypt($FORM{'password'});
            $sql     =
              "UPDATE $dbmail_users_table SET passwd = '$results' where user_idnr = '$newuserID'";
            $sth = $dbh->prepare($sql);
            unless ($sth->execute())
            {
                $errormessage = "
	ErrorID: $version.err0.26 <br />$DBI::errstr <br />Failed to set password";
                &DBMA_ConnectStatus;
            }
            $sth->finish() if ($sth);
        }
        elsif (   ($encrypttype eq "crypt")
               && ($encrypttype ne "md5sum")
               && ($encrypttype ne "plain")
               && ($encrypttype ne "clear")
               && ($encrypttype ne "cleartext")
               && ($encrypttype ne " "))
        {
            $results = &perl_crypt($FORM{'password'});
            $sql     =
              "UPDATE $dbmail_users_table SET passwd = '$results' where user_idnr = '$newuserID'";
            $sth = $dbh->prepare($sql);
            unless ($sth->execute())
            {
                $errormessage = "
	ErrorID: $version.err0.27 <br />$DBI::errstr <br />Failed to set password";
                &DBMA_ConnectStatus;
            }
            $sth->finish() if ($sth);
        }
        elsif ($encrypttype eq (("md5sum") || ("md5-hash")))
        {
            $password = &MD5_hash($FORM{'password'});
            $sql      =
              "UPDATE $dbmail_users_table SET passwd = '$password' where user_idnr = '$newuserID'";
            $sth = $dbh->prepare($sql);
            unless ($sth->execute())
            {
                $errormessage = "
	ErrorID: $version.err0.28 <br />$DBI::errstr <br />Failed operation";
                &DBMA_ConnectStatus;
            }
            $sth->finish() if ($sth);
        }
        elsif ($FORM{'encrypttype'} eq "plain")
        {
            $password = $FORM{'password'};
            $sql      =
              "UPDATE $dbmail_users_table SET passwd = '$password' where user_idnr = '$newuserID'";
            $sth = $dbh->prepare($sql);
            unless ($sth->execute())
            {
                $errormessage = "
	ErrorID: $version.err0.29 <br />$DBI::errstr <br />Failed operation";
                &DBMA_ConnectStatus;
            }
            $sth->finish() if ($sth);
        }
        elsif ($FORM{'encrypttype'} eq " ")
        {
            $password = $FORM{'password'};
            $sql      =
              "UPDATE $dbmail_users_table SET passwd = '$password' where user_idnr = '$newuserID'";
            $sth = $dbh->prepare($sql);
            unless ($sth->execute())
            {
                $errormessage = "
	ErrorID: $version.err0.30 <br />$DBI::errstr <br />Failed operation";
                &DBMA_ConnectStatus;
            }
            $sth->finish() if ($sth);
        }
    }
########## - End condition and action changepassword
    $sql =
      "UPDATE $dbmail_users_table SET client_idnr = '$GroupID' where user_idnr = '$newuserID'";
    $sth = $dbh->prepare($sql);
    unless ($sth->execute())
    {
        $errormessage = "
	ErrorID: $version.err0.31 <br />$DBI::errstr <br />Failed operation";
        &DBMA_ConnectStatus;
    }
    $sth->finish() if ($sth);

    # in case the client_idnr has been changed the aliases of the same ilk must also be changed
    $sql =
      "UPDATE $dbmail_aliases_table SET client_idnr = '$GroupID' where deliver_to = '$newuserID'";
    $sth = $dbh->prepare($sql);
    unless ($sth->execute())
    {
        $errormessage = "
	ErrorID: $version.err0.31 <br />$DBI::errstr <br />Failed to update Group on alias";
        &DBMA_ConnectStatus;
    }
    $sth->finish() if ($sth);

    $sql =
      "UPDATE $dbmail_users_table SET maxmail_size = '$mailboxsize' where user_idnr = '$newuserID'";
    $sth = $dbh->prepare($sql);
    unless ($sth->execute())
    {
        $errormessage = "
	ErrorID: $version.err0.32 <br />$DBI::errstr <br />Failed operation";
        &DBMA_ConnectStatus;
    }
    $sth->finish() if ($sth);
## add the alias but first check if alias first_part is a user
    if ($auto_create_user eq "1")
    {
        my $check_for_this_user;
        $newalias           = $FORM{'newalias'};
        @is_it_new_output   = &split($newalias);
        $is_it_new_username = $is_it_new_output[0];
        $sth                =
          $dbh->prepare(
            "SELECT DISTINCT userid FROM $dbmail_users_table WHERE LOWER(userid) = LOWER('$is_it_new_username') LIMIT 1"
          );
        $sth->execute();
        unless (($check_for_this_user) = $sth->fetchrow_array)
        {
            $message =
              "You added alias $newalias but no account existed for $is_it_new_username. DBMA created account <a href=\"$mythisscript?$is_it_new_username\">$is_it_new_username</a>\n";
            my $it_is_new_pwd = &MD5_hash_salt_key("DBMANOACCESS");
            $insertnewuser =
              "INSERT INTO $dbmail_users_table (userid, passwd, client_idnr, maxmail_size, encryption_type, last_login)
    	VALUES ('$is_it_new_username', '$it_is_new_pwd', '$GroupID', '$mailboxsize', 'md5', CURRENT_DATE)";
            $sth = $dbh->prepare($insertnewuser);
            $sth->execute;
            $sth->finish;
            $sth =
              $dbh->prepare(
                "SELECT user_idnr FROM $dbmail_users_table WHERE LOWER(userid) = LOWER('$is_it_new_username') LIMIT 1"
              );

            unless ($sth->execute())
            {
                $errormessage =
                  "$DBI::errstr <br />Failed to get user_idnr for $is_it_new_username.";
                &DBMA_ConnectStatus;
            }
            while (my $rv = $sth->fetchrow_hashref())
            {
                my $is_it_new_userID = $rv->{'user_idnr'};
                &filt($is_it_new_userID);
            }
            $sth = $dbh->prepare(
                "INSERT INTO $dbmail_mailboxes_table (owner_idnr, name, seen_flag, answered_flag, deleted_flag, flagged_flag, recent_flag, draft_flag, no_inferiors, no_select, permission)
    	VALUES ('$is_it_new_userID', 'INBOX', '1', '1', '1', '1', '1', '1', '0', '0', '2')"
                                );
            $sth->execute();
            unless ($dbh->commit)
            {
                $errormessage = "
	ErrorID: $version.err0.40 <br />$DBI::errstr <br />Error: commit FAIL for add mailbox for $is_it_new_userID";
                &DBMA_ConnectStatus;
            }
        }
    }
    $newalias =~ tr/[A-Z]/[a-z]/;
    $addnewaliases =
      "INSERT INTO $dbmail_aliases_table (alias, deliver_to, client_idnr) VALUES ('$newalias', '$newuserID', '$GroupID')"
      if ($FORM{'newalias'});
    $sth = $dbh->prepare($addnewaliases) if ($FORM{'newalias'});
    $sth->execute() if ($FORM{'newalias'});
    unless ($dbh->commit)
    {
        $errormessage = "
	ErrorID: $version.err0.33 <br />
	$DBI::errstr <br />Error: commit FAIL for $username update";
        &DBMA_ConnectStatus;
    }
    $password = $FORM{'password'};
    &Create_User_Account_MODIFY_Window($message);
}
############################################################## - sub add_user_sql RQT1
sub add_user_sql($)
{

    $FORM{'encrypttype'} =~ s/md5-hash/md5sum/g;
    $encrypttype         =~ s/md5-hash/md5sum/g;

    $encrypttype = &char_filt($FORM{'encrypttype'});

    $sth =
      $dbh->prepare(
        "SELECT user_idnr, client_idnr from $dbmail_users_table WHERE LOWER(userid) = LOWER('$username')"
      );
    unless ($sth->execute())
    {
        push(@ERROR, $DBI::errstr);
        &error('Failed check if User Exists', @ERROR);
    }

    if (($userID, $GroupID) = $sth->fetchrow_array)
    {
        push(@ERROR,
             "User: " . $username,
             "User number: " . $userID,
             "Group: " . $GroupID);
        &error(
            'This user exists already. Open the User Account Window for this user by pressing "User Search" then select "Modify..." to make changes.',
            @ERROR
        );
    }

    if ($RESTRICTGroupID =~ m/[1-9]/) { $GroupID = $RESTRICTGroupID }
    else { $GroupID = $FORM{'GroupID'} }

    if (($count_users_per_group eq "1") && ($GroupID))
    {

        $sth =
          $dbh->prepare(
            "SELECT user_idnr FROM $dbmail_users_table WHERE client_idnr = '$GroupID'"
          );
        $sth->execute;
        $numrows = $sth->rows;
        if ($numrows > $group_limit)
        {
            push(@ERROR,
                 "User: " . $username,
                 "Group Limit " . $group_limit,
                 "Current Users " . $numrows,
                 "Group: " . $GroupID);
            &error(
                'This user could not be added. <br />You have reached the configured Group Limit. <br />Please consult your System Administrator.',
                @ERROR
            );
            exit;
        }
    }
    undef $numrows;
    $sth->finish() if ($sth);
    &checkrequired;

    if ($CFP eq "1")
    {
        $encrypttype = " ";
    }
    else
    {
        $encrypttype = $FORM{'encrypttype'};
    }
    if (   ($FORM{'encrypttype'} eq "plain")
        || ($FORM{'encrypttype'} eq "on")
        || ($FORM{'encrypttype'} eq "off")
        || ($FORM{'encrypttype'} eq "clear")
        || ($FORM{'encrypttype'} eq "ascii")
        || ($FORM{'encrypttype'} eq "cleartext")
        || ($FORM{'encrypttype'} eq "plaintext")
        || ($FORM{'encrypttype'} eq "none")
        || ($FORM{'encrypttype'} eq "")
        || ($FORM{'encrypttype'} eq " ")
        && ($FORM{'encrypttype'} ne "md5sum")
        && ($FORM{'encrypttype'} ne "crypt")
        && ($FORM{'encrypttype'} ne "md5")
        && ($FORM{'encrypttype'} ne "MD5"))
    {
        $encrypttype = "";
    }
    else
    {
        my $encrypttype = $FORM{'encrypttype'};
        $encrypttype =~ s/md5-hash/md5sum/g;
    }

    $insertnewuser =
      "INSERT INTO $dbmail_users_table (userid, passwd, client_idnr, maxmail_size, encryption_type, last_login)
    	VALUES ('$username', '$password', '$GroupID', '$mailboxsize', '$encrypttype', CURRENT_DATE)";
    $sth = $dbh->prepare($insertnewuser);
    $sth->execute;

    if (   ($encrypttype eq "md5")
        || ($encrypttype eq "MD5")
        || ($encrypttype =~ /Md5/))
    {
        $password = &MD5_Encrypt($FORM{'password'});
        $sql      =
          "UPDATE $dbmail_users_table SET passwd = '$password' WHERE LOWER(userid) = LOWER('$username')";
        $sth = $dbh->prepare($sql);
        unless ($sth->execute())
        {
            $errormessage = "
	ErrorID: $version.err0.34 <br />
	$DBI::errstr <br />Failed to set password encryption - is it installed?";
            &DBMA_ConnectStatus;
        }
        $sth->finish() if ($sth);
        unless ($dbh->commit)
        {
            $errormessage = "
	ErrorID: $version.err0.35 <br />
	$DBI::errstr <br />Error: commit FAIL for add user";
            &DBMA_ConnectStatus;
        }
    }
    elsif (   ($encrypttype eq "crypt")
           || ($encrypttype eq "CRYPT")
           || ($encrypttype =~ /unix/))
    {
        $results = &perl_crypt($FORM{'password'});
        $sql     =
          "UPDATE $dbmail_users_table SET passwd = '$results' WHERE LOWER(userid) = LOWER('$username')";
        $sth = $dbh->prepare($sql);
        unless ($sth->execute())
        {
            $errormessage = "
	ErrorID: $version.err0.36 <br />
	DBI::errstr <br />Failed to set password using PERL Crypt - is it installed?";
            &DBMA_ConnectStatus;
        }
        $sth->finish() if ($sth);
        unless ($dbh->commit)
        {
            $errormessage = "
	ErrorID: $version.err0.37 <br />
	DBI::errstr <br />Error: commit FAIL for add user";
            &DBMA_ConnectStatus;
        }
    }
    elsif (($sqltype =~ /mysql/) && ($encrypttype =~ /md5sum/))
    {

        $password = &MD5_hash($FORM{'password'});

        $sql =
          "UPDATE $dbmail_users_table SET passwd = '$password' WHERE LOWER(userid) = LOWER('$username')";
        $sth = $dbh->prepare($sql);
        unless ($sth->execute)
        {
            $errormessage = "
	ErrorID: $version.err0.38 <br />$DBI::errstr <br />$DBI::errstr <br />Failed UPDATE $dbmail_users_table SET passwd.";
            &DBMA_ConnectStatus;
        }

    }
    unless ($dbh->commit)
    {
        $errormessage = "
	ErrorID: $version.err0.39 <br />$DBI::errstr <br />Error: commit FAIL for add user";
        &DBMA_ConnectStatus;
    }
    elsif (($sqltype =~ /pgsql/) && ($encrypttype =~ /md5sum/))
    {
        $password = &MD5_hash($FORM{'password'});
        $sql      =
          "UPDATE $dbmail_users_table SET passwd = '$password' WHERE LOWER(userid) = LOWER('$username')";
        $sth = $dbh->prepare($sql);
        unless ($sth->execute())
        {
            $errormessage =
              "$DBI::errstr <br />Failed to set password using PERL Digest::MD5 - is it installed?";
            &DBMA_ConnectStatus;
        }
        $sth->finish() if ($sth);
        unless ($dbh->commit)
        {
            $errormessage =
              "$DBI::errstr <br />Error: commit FAIL for add user";
            &DBMA_ConnectStatus;
        }
    }
    if ($create_first_alias eq "1")
    {

        my $username = $FORM{'username'} || $username || $userID || "";
        my $AutoNewAlias = "$FORM{'username'}\@$defaultdomain";
        $AutoNewAlias =~ tr/[A-Z]/[a-z]/;

        &check_if_RFC_alias($AutoNewAlias);
        my $sth =
          $dbh->prepare(
            "SELECT user_idnr FROM $dbmail_users_table WHERE LOWER(userid) = LOWER('$username')"
          );
        $sth->execute();

        while ($rv = $sth->fetchrow_hashref())
        {
            my $myuserID = $rv->{'user_idnr'};
            &filt($myuserID);
            $newuserID = $myuserID;
        }
        $addnewaliases =
          "INSERT INTO $dbmail_aliases_table (alias, deliver_to, client_idnr) VALUES ('$AutoNewAlias', '$newuserID', '$GroupID')";
        $sth = $dbh->prepare($addnewaliases);
        unless ($sth->execute())
        {
            $errormessage =
              "$DBI::errstr <br />Failed INSERT INTO $dbmail_aliases_table.";
            &DBMA_ConnectStatus;
        }
        $sth = $dbh->prepare(
            "INSERT INTO $dbmail_mailboxes_table (owner_idnr, name, seen_flag, answered_flag, deleted_flag, flagged_flag, recent_flag, draft_flag, no_inferiors, no_select, permission)
    	VALUES ('$newuserID', 'INBOX', '1', '1', '1', '1', '1', '1', '0', '0', '2')"
                            );
        $sth->execute();
        unless ($dbh->commit)
        {
            $errormessage =
              "$DBI::errstr <br />Error: commit FAIL for add alias and mailbox";
            &DBMA_ConnectStatus;
        }

        &add_user_form_sql;
        exit;
    }
    else
    {
        my $newalias = $FORM{'newalias'};
        &add_alias_sql
          if ($FORM{'newalias'})
          ;    # handled only in a subroutine in case not creating an alias
    }

    &add_mailbox_sql;
}

#                                                   ########## - sub add_alias_sql part of RQT1
sub add_alias_sql ($)
{    # part of the add_user process but built as a sub to bypass a form NULL
    &defaults;
    my $bypass = $FORM{'bypass'} || "0";
    my $newalias = $FORM{'newalias'} || $newalias || $alias;
    $newalias =~ tr/[A-Z]/[a-z]/;
    my $username = $FORM{'username'} || $username || $userID || "";
    &check_if_RFC_alias($newalias) unless ($bypass eq "1");
    my $sth =
      $dbh->prepare(
        "SELECT user_idnr FROM $dbmail_users_table WHERE LOWER(userid) = LOWER('$username')"
      );
    $sth->execute();

    while ($rv = $sth->fetchrow_hashref())
    {
        my $myuserID = $rv->{'user_idnr'};
        &filt($myuserID);
        $newuserID = $myuserID;
    }
    $addnewaliases =
      "INSERT INTO $dbmail_aliases_table (alias, deliver_to, client_idnr) VALUES ('$newalias', '$newuserID', '$GroupID')";
    $sth = $dbh->prepare($addnewaliases);
    unless ($sth->execute())
    {
        $errormessage =
          "$DBI::errstr <br />Failed INSERT INTO $dbmail_aliases_table.";
        &DBMA_ConnectStatus;
    }
    $sth = $dbh->prepare(
        "INSERT INTO $dbmail_mailboxes_table (owner_idnr, name, seen_flag, answered_flag, deleted_flag, flagged_flag, recent_flag, draft_flag, no_inferiors, no_select, permission)
    	VALUES ('$newuserID', 'INBOX', '1', '1', '1', '1', '1', '1', '0', '0', '2')"
                        );
    $sth->execute();
    unless ($dbh->commit)
    {
        $errormessage =
          "$DBI::errstr <br />Error: commit FAIL for add alias and mailbox";
        &DBMA_ConnectStatus;
    }
    if ($create_first_alias eq "1")
    {
        &add_user_form_sql;
        exit;
    }
    else
    {
        &Create_User_Account_MODIFY_Window;
    }
}

#                                                   ########## - sub add_mailbox_sql part of RQT1
sub add_mailbox_sql
{
    $sth =
      $dbh->prepare(
        "SELECT user_idnr FROM $dbmail_users_table WHERE LOWER(userid) = LOWER('$username')"
      );
    unless ($sth->execute())
    {
        $errormessage =
          "$DBI::errstr <br />Failed to get user_idnr from $dbmail_users_table.";
        &DBMA_ConnectStatus;
    }
    while (my $rv = $sth->fetchrow_hashref())
    {
        my $myuserID = $rv->{'user_idnr'};
        &filt($myuserID);
        $newuserID = $myuserID;
    }
    $sth = $dbh->prepare(
        "INSERT INTO $dbmail_mailboxes_table (owner_idnr, name, seen_flag, answered_flag, deleted_flag, flagged_flag, recent_flag, draft_flag, no_inferiors, no_select, permission)
    	VALUES ('$newuserID', 'INBOX', '1', '1', '1', '1', '1', '1', '0', '0', '2')"
                        );
    $sth->execute();
    unless ($dbh->commit)
    {
        $errormessage = "
	ErrorID: $version.err0.40 <br />$DBI::errstr <br />Error: commit FAIL for add mailbox";
        &DBMA_ConnectStatus;
    }
    sleep 1;
    &Create_User_Account_MODIFY_Window;
}
############################################################## - sub create_alias_sql RQT6
sub create_alias_sql
{
    $newalias =~ tr/[A-Z]/[a-z]/;
    &checkrequired;
    &check_if_RFC_alias($newalias);
    &prepare_input;
    $addnewaliases =
      "INSERT INTO $dbmail_aliases_table (alias, deliver_to, client_idnr) VALUES ('$newalias', '$userID', '$GroupID')";
    $sth = $dbh->prepare($addnewaliases);
    $sth->execute() if ($FORM{'newalias'});
    $sth->finish()  if ($sth);

    unless ($dbh->commit)
    {
        $errormessage =
          "$DBI::errstr <br />Error: commit FAIL for create alias";
        &DBMA_ConnectStatus;
    }
    &make_form($userID);
}
############################################################## - sub create_group_alias_sql RQT6a

sub create_group_alias_sql
{
    unless ($RESTRICTGroupID eq "any")
    {
        make_form;
    }

    &connect unless ($dbh);
    $newalias = "";
    my $lastpart = $FORM{'newalias'};
    my $GroupID = $FORM{'GroupID'} || $GroupID;
    $lastpart =~ tr/[A-Z]/[a-z]/;
    &checkrequired;

    my $sql =
      "SELECT userid, user_idnr, client_idnr from $dbmail_users_table where client_idnr = $GroupID";
    my $sth = $dbh->prepare($sql);
    $sth->execute();
    $sth->bind_columns(\$username, \$userID, \$GroupID);
    while ($sth->fetch())
    {

        @output   = &split($username);
        $username = $output[0];

        $dbh->do(
            "INSERT INTO $dbmail_aliases_table (alias, deliver_to, client_idnr) VALUES ('$username\@$lastpart', '$userID', '$GroupID\')"
        );
    }
    unless ($dbh->commit)
    {
        $errormessage =
          "$DBI::errstr <br />Error: commit FAIL for create alias";
        &DBMA_ConnectStatus;
    }

    $sth->finish() if ($sth);
    &List_Group_Aliases($GroupID);
}

############################################################## - sub add_notify_sql RQT15
sub add_notify_sql ()
{
    &checkrequired;
    our $userID = $FORM{'userID'} || $userID || "";
    &prepare_input;
    $addnotify =
      "INSERT INTO $dbmail_auto_notifications_table (user_idnr, notify_address) VALUES ('$userID', '$notify_address')";
    unless ($sth = $dbh->prepare($addnotify))
    {
        $errormessage =
          "Error: Unable to Execute Addition of auto notify for $userID $sth->errstr";
        &DBMA_ConnectStatus;
    }
    unless ($sth->execute)
    {
        $errormessage =
          "Error: Unable to Execute Addition of auto notify for $userID";
        &DBMA_ConnectStatus;
    }
    unless ($dbh->commit)
    {
        $errormessage = "
	ErrorID: $version.err0.41 <br />$DBI::errstr <br />Error: commit FAIL for add notify";
        &DBMA_ConnectStatus;
    }
    &Create_User_Account_Window($userID);
}
############################################################## - sub delete_notify_sql RQT17
sub delete_notify_sql
{
    &checkrequired;
    &prepare_input;
    $sth =
      $dbh->prepare(
        "DELETE FROM $dbmail_auto_notifications_table WHERE user_idnr = '$userID'"
      );
    unless ($sth->execute)
    {
        $errormessage =
          "Error: Unable to delete Auto Notify for $userID. Check that there is one. Did you enter the correct UserID number?";
        &DBMA_ConnectStatus;
    }
    unless ($dbh->commit)
    {
        $errormessage =
          "$DBI::errstr <br />Error: commit FAIL for delete notify";
        &DBMA_ConnectStatus;
    }
    &make_form($userID);
}
############################################################## - sub fix_deleted RQT36 aka fix_deletes as standalone
sub fix_deleted
{

    # First DBMA will connect aliases to usrs and fix client_idnrs where the alias has the wrong client_idnr

if ($sqltype =~ /pgsql/)
{
    $dbh->do("
UPDATE $dbmail_aliases_table
JOIN $dbmail_users_table
ON $dbmail_aliases_table.deliver_to = CAST($dbmail_users_table.user_idnr AS text)
SET $dbmail_aliases_table.client_idnr = $dbmail_users_table.client_idnr
WHERE $dbmail_aliases_table.deliver_to = CAST($dbmail_users_table.user_idnr AS text)"
    );
}
if ($sqltype =~ /mysql/)
{
    $dbh->do("
UPDATE $dbmail_aliases_table
JOIN $dbmail_users_table
ON $dbmail_aliases_table.deliver_to = $dbmail_users_table.user_idnr
SET $dbmail_aliases_table.client_idnr = $dbmail_users_table.client_idnr
WHERE $dbmail_aliases_table.deliver_to = $dbmail_users_table.user_idnr"
    );
}
    $dbh->commit();

    # Then we are going to set the status flag to 003 for messages the client has marked for deletion.

    $sth =
      $dbh->prepare(
        "UPDATE $dbmail_messages_table SET status = '003' where  deleted_flag = '1' OR status >0"
      );
    unless ($sth->execute())
    {
        print
          "$DBI::errstr <br />Failed in updating deleted status on messages client has marked delete.";
    }
    unless ($dbh->commit)
    {
        $errormessage =
          "$DBI::errstr <br />Failed in updating deleted status on messages client has marked delete. This is a strange thing. Check your configurations.";
        &DBMA_ConnectStatus;
    }
    $sth->finish() if ($sth);

    # Now we are going to search for messages which have no owner. Orphaned messages.
    $sth = $dbh->prepare(
        "SELECT message_idnr from $dbmail_messages_table
JOIN $dbmail_mailboxes_table ON $dbmail_messages_table.mailbox_idnr = $dbmail_mailboxes_table.mailbox_idnr
LEFT JOIN $dbmail_users_table ON $dbmail_users_table.user_idnr = $dbmail_mailboxes_table.owner_idnr
WHERE $dbmail_users_table.user_idnr IS NULL"
                        );
    unless ($sth->execute())
    {
        print
          "$DBI::errstr <br />Failed in updating deleted status for non-existant users.";
    }

    # And now if we found some orphaned messages we will set their status to 001.
    # If you hit the "Update Delete Status" any orphaned messages that we have found here will be escalated to 003
    # and deleted from the database on the next Utility/Maintenance run.
    # Look for changes in the MAIN MENU statistics column: "Number of deletes pending"
    while (($message_idnr) = $sth->fetchrow_array)
    {
        $sth =
          $dbh->prepare(
            "UPDATE $dbmail_messages_table SET status = '002', deleted_flag = '1' where  message_idnr = '$message_idnr'"
          );
        $sth->execute();
        unless ($dbh->commit)
        {
            $errormessage =
              "$DBI::errstr <br />Failed in updating deleted status for non-existant users.";
            &DBMA_ConnectStatus;
        }
    }
    $sth->finish() if ($sth);

    # Delete messages mailboxes owned by no user.
    unless ($sqltype =~ /pgsql/)
    {
        $sth = $dbh->prepare(
            "UPDATE $dbmail_messages_table
LEFT JOIN $dbmail_mailboxes_table ON $dbmail_messages_table.mailbox_idnr = $dbmail_mailboxes_table.mailbox_idnr
SET $dbmail_messages_table.deleted_flag = '1', status = '002' WHERE $dbmail_mailboxes_table.mailbox_idnr IS NULL"
                            );
        unless ($sth->execute())
        {
            print
              "$DBI::errstr <br />Failed in updating deleted status where mailboxes to messages relationship is broken.";
        }
        unless ($dbh->commit)
        {
            $errormessage =
              "$DBI::errstr <br />Failed in updating deleted status where mailboxes to messages relationship is broken.";
            &DBMA_ConnectStatus;
        }
        $sth->finish() if ($sth);
    }

    # Check for and delete orphaned messages which are found in dbmail_messageblks and dbmail_physmessage
    # but not attached to an existing mailbox or usr_idnr. You would have a pretty messy database to need this
    unless ($DBMailOldVersion eq "1")
    {
        $sth = $dbh->prepare("select id from $dbmail_physmessage_table");
        $sth->execute();
        my $ref = $sth->fetchall_arrayref();
        $sth->finish() if ($sth);
        foreach (@$ref)
        {
            my $sth1 = $dbh->prepare("
SELECT COUNT(*) FROM $dbmail_messages_table, $dbmail_users_table, $dbmail_mailboxes_table
WHERE $dbmail_messages_table.mailbox_idnr=$dbmail_mailboxes_table.mailbox_idnr 
AND $dbmail_users_table.user_idnr = $dbmail_mailboxes_table.owner_idnr 
AND $dbmail_messages_table.physmessage_id = ?"
            );
            $sth1->execute($messageID);
            my $var = $sth1->fetchrow_array();
            $sth1->finish() if ($sth1);
            if (!$var)
            {
                $dbh->do(
                    "delete from $dbmail_messages_table where id = ?",
                    undef, $messageID
                );
                $dbh->do("delete from $dbmail_physmessage_table where id = ?",
                         undef, $messageID);
                $dbh->do(
                    "delete from $dbmail_messageblks_table where id = ?",
                    undef, $messageID
                );
            }
        }
    }

    # Defragging
    # If there are random insertions or deletions in the indexes of a table, the indexes may become fragmented
    # where the physical ordering of the index pages on the disk is not close to the
    # alphabetical ordering of the records on the pages, or that there are many unused pages in the 64-page
    # blocks which were allocated to the index.
    # Defragmentation can be done by performing a 'null' alter table operation.

    if ($sqltype =~ /mysql/)
    {
        $dbh->prepare("SHOW TABLE STATUS LIKE '$dbmail_acl_table'");
        $sth->execute();
        while ((my @line) = $sth->fetchrow_array)
        {
            foreach $line (@line)
            {
                if ($line =~ m/InnoDB free/i) { $InnoDB = 1; }
            }
        }
        $sth->finish() if ($sth);
        if ($InnoDB == 1)
        {
            $dbh->do("ALTER TABLE $dbmail_aliases_table TYPE=InnoDB");
            $dbh->do("ALTER TABLE $dbmail_users_table TYPE=InnoDB");
            $dbh->do("ALTER TABLE $dbmail_mailboxes_table TYPE=InnoDB");
            $dbh->do("ALTER TABLE $dbmail_messages_table TYPE=InnoDB");
            $dbh->do("ALTER TABLE $dbmail_messageblks_table TYPE=InnoDB");
            $dbh->do("ALTER TABLE $dbmail_physmessage_table TYPE=InnoDB");
            $dbh->do("ALTER TABLE $dbmail_subscription_table TYPE=InnoDB")
              unless ($DBMailOldVersion eq "1");
            $dbh->do("ALTER TABLE $dbmail_headervalue_table TYPE=InnoDB")
              if ($DBMail22Version eq "1");

        }
    }

    &make_form;
    exit;
}
############################################################## - sub delete_mail RQT31
sub delete_mail
{
    $sth =
      $dbh->prepare(
        "UPDATE $dbmail_messages_table SET deleted_flag ='1' WHERE message_idnr = '$messageID'"
      );
    unless ($sth->execute)
    {
        $errormessage = "
	ErrorID: $version.err0.42 <br />$DBI::errstr <br />Error: Unable to delete mail for $userID.";
        &DBMA_ConnectStatus;
    }
    unless ($dbh->commit)
    {
        $errormessage =
          "$DBI::errstr <br />Error: delete mail for $userID WHERE message_idnr  = '$messageID'";
        &DBMA_ConnectStatus;
    }
    $sth =
      $dbh->prepare(
        "UPDATE $dbmail_messages_table SET status ='003' WHERE message_idnr = '$messageID'"
      );
    unless ($sth->execute)
    {
        $errormessage = "
	ErrorID: $version.err0.43 <br />$DBI::errstr <br />Error: Unable to delete mail for $userID.";
        &DBMA_ConnectStatus;
    }
    unless ($dbh->commit)
    {
        $errormessage =
          "$DBI::errstr <br />Error: delete mail for $userID WHERE message_idnr  = '$messageID'";
        &DBMA_ConnectStatus;
    }
    &Create_User_Account_Window($userID);
}
############################################################## - sub delete_all_mail RQT34
sub delete_all_mail
{
    $sth =
      $dbh->prepare(
        "UPDATE $dbmail_messages_table SET deleted_flag ='1' WHERE mailbox_idnr = '$mailbox_idnr'"
      );
    unless ($sth->execute)
    {
        $errormessage = "
	ErrorID: $version.err0.44 <br />$DBI::errstr <br />Error: Unable to delete mail for $username.";
        &DBMA_ConnectStatus;
    }
    unless ($dbh->commit)
    {
        $errormessage =
          "$DBI::errstr <br />Error: delete mail for $username WHERE mailbox_idnr  = '$mailbox_idnr'";
        &DBMA_ConnectStatus;
    }
    $sth =
      $dbh->prepare(
        "UPDATE $dbmail_messages_table SET status ='003' WHERE mailbox_idnr = '$mailbox_idnr'"
      );
    unless ($sth->execute)
    {
        $errormessage = "
	ErrorID: $version.err0.45 <br />$DBI::errstr <br />Error: Unable to delete all mail for $userID.";
        &DBMA_ConnectStatus;
    }
    unless ($dbh->commit)
    {
        $errormessage =
          "$DBI::errstr <br />Error: delete all mail for $username WHERE mailbox_idnr  = $mailbox_idnr";
        &DBMA_ConnectStatus;
    }
    &Create_User_Account_Window($userID);
}
############################################################## - sub undelete_mail RQT35
sub undelete_mail
{
    $sth =
      $dbh->prepare(
        "UPDATE $dbmail_messages_table SET deleted_flag ='0' WHERE message_idnr  = '$messageID'"
      );
    unless ($sth->execute)
    {
        $errormessage =
          "Error: Unable to UNDELETE mail (set deleted_flag = 0) for $username.";
        &DBMA_ConnectStatus;
    }
    unless ($dbh->commit)
    {
        $errormessage =
          "$DBI::errstr <br />Error: FAILED to undelete mail for $username WHERE message_idnr = $messageID";
        &DBMA_ConnectStatus;
    }
    $sth =
      $dbh->prepare(
        "UPDATE $dbmail_messages_table SET status ='000' WHERE message_idnr = '$messageID'"
      );
    unless ($sth->execute)
    {
        $errormessage = "
	ErrorID: $version.err0.46 <br />$DBI::errstr <br />Error: Unable to undelete mail for $username.";
        &DBMA_ConnectStatus;
    }
    unless ($dbh->commit)
    {
        $errormessage =
          "$DBI::errstr <br />Error: Failed reset delete status for $username 's Mail WHERE message_idnr = '$messageID'";
        &DBMA_ConnectStatus;
    }
    &Create_User_Account_Window($userID);
}
############################################################## - sub undelete_all_mail RQT35
sub undelete_all_mail
{
    $sth =
      $dbh->prepare(
        "UPDATE $dbmail_messages_table SET deleted_flag ='0' WHERE mailbox_idnr  = '$mailbox_idnr'"
      );
    unless ($sth->execute)
    {
        $errormessage = "
	ErrorID: $version.err0.47 <br />$DBI::errstr <br />Error: Unable to undelete mail for $userID.";
        &DBMA_ConnectStatus;
    }
    unless ($dbh->commit)
    {
        $errormessage =
          "$DBI::errstr <br />Error: undelete mail for $userID WHERE mailbox_idnr = '$mailbox_idnr'";
        &DBMA_ConnectStatus;
    }
    $sth =
      $dbh->prepare(
        "UPDATE $dbmail_messages_table SET status ='000' WHERE mailbox_idnr  = '$mailbox_idnr'"
      );
    unless ($sth->execute)
    {
        $errormessage = "
	ErrorID: $version.err0.48 <br />$DBI::errstr <br />Error: Unable to undelete mail for $userID.";
        &DBMA_ConnectStatus;
    }
    unless ($dbh->commit)
    {
        $errormessage =
          "$DBI::errstr <br />Error: undelete mail for $userID WHERE mailbox_idnr = '$mailbox_idnr'";
        &DBMA_ConnectStatus;
    }
    &Create_User_Account_Window($userID);
}
############################################################## - sub delete_user RQT4
sub delete_user
{
    &protect_sys_accounts($userID);
    my $userID = $FORM{'userID'} if $FORM{'userID'};
    unless ($RESTRICTGroupID =~ m/[0-9]/i)
    {
        &prepare_input;
        $deleteuser =
          "DELETE FROM $dbmail_users_table WHERE user_idnr = '$userID'";
        $sth = $dbh->prepare($deleteuser);
        unless ($sth->execute)
        {
            $errormessage =
              "Error: Unable to delete User Check that this user exists.";
            &DBMA_ConnectStatus;
        }
        unless ($dbh->commit)
        {
            $errormessage =
              "$DBI::errstr <br />Error: commit FAIL for delete user";
            &DBMA_ConnectStatus;
        }
## - delete dbmail_acl.user_id
        $sth =
          $dbh->prepare(
                     "DELETE FROM $dbmail_acl_table where user_id = '$userID'");
        unless ($sth->execute)
        {
            $errormessage = "$DBI::errstr DELETE ACL Failed";
            &DBMA_ConnectStatus;
        }
        unless ($dbh->commit)
        {
            $errormessage =
              "$DBI::errstr <br />Error: Could not delete Public ACL for $userID";
            &DBMA_ConnectStatus;
        }
## - delete dbmail_auto_replies.user_idnr
        $sth =
          $dbh->prepare(
            "DELETE from $dbmail_auto_replies_table WHERE user_idnr='$userID'");
        unless ($sth->execute)
        {
            $errormessage = "
	ErrorID: $version.err0.49 <br />$DBI::errstr <br />DELETE AutoReply Failed for $userID";
            &DBMA_ConnectStatus;
        }
        unless ($dbh->commit)
        {
            $errormessage = "
	ErrorID: $version.err0.50 <br />$DBI::errstr <br />Error:  DELETE AutoReply Failed for $userID";
            &DBMA_ConnectStatus;
        }
        $sth->finish() if ($sth);
## - go get aliases and forwards, mail should be deleted on cascade dbmail_users.user_idnr
        &delete_alias_sql($userID);
    }
    else
    {
        &delete_user_restricted($userID);
    }
}
############################################################## - sub delete_alias_sql RQT10
sub delete_alias_sql ($)
{
    my $userID = $FORM{'userID'} if $FORM{'userID'};
    my $username = ($username) || $FORM{'username'} || "";

    # DBMA: Delete Multiple Aliases and Forwards By User
    &checkrequired;
    &prepare_input;
    $sth =
      $dbh->prepare(
              "DELETE FROM $dbmail_aliases_table WHERE deliver_to = '$userID'");
    unless ($sth->execute)
    {
        $errormessage =
          "Error: Unable to delete aliases for $userID. Check that they exist.";
        &DBMA_ConnectStatus;
    }
    $sth->finish() if ($sth);
    $sth =
      $dbh->prepare(
        "DELETE FROM $dbmail_auto_notifications_table where user_idnr = '$userID'"
      );
    unless ($sth->execute)
    {
        $errormessage =
          "Error: Unable to delete Auto Notification for $userID.";
        &DBMA_ConnectStatus;
    }
    $sth->finish() if ($sth);
    unless ($dbh->commit)
    {
        $errormessage =
          "$DBI::errstr <br />Error: commit FAIL for Delete Alias";
        &DBMA_ConnectStatus;
    }

    push(@ERROR, "User number: " . $userID . $username . " is gone.");
    &error('Success! Deleted.', @ERROR);
}
############################################################## - sub delete_user_restricted RQT39
sub delete_user_restricted
{
## Extra security for RESTRICTGroupID
    my $userID = $FORM{'userID'} if $FORM{'userID'};
    &protect_sys_accounts($userID);
    &prepare_input;
    $deleteuser =
      "DELETE FROM $dbmail_users_table WHERE user_idnr = '$userID' AND client_idnr ='$RESTRICTGroupID'";
    $sth = $dbh->prepare($deleteuser);
    unless ($sth->execute)
    {
        $errormessage =
          "Error: Unable to delete $userID Check that $userID exists or that you are authorized to administer this group.";
        &DBMA_ConnectStatus;
    }
    unless ($dbh->commit)
    {
        $errormessage = "
	ErrorID: $version.err0.51 <br />$DBI::errstr <br />Error: commit FAIL for delete user";
        &DBMA_ConnectStatus;
    }
    &delete_alias_sql($userID);
}
############################################################## - sub delete_group RQT40
sub delete_group
{
    if (($deletegroup > 0) && ($RESTRICTGroupID eq "any"))
    {
        $deleteuser =
          "DELETE FROM $dbmail_users_table WHERE client_idnr = '$deletegroup'";
        $sth = $dbh->prepare($deleteuser);
        unless ($sth->execute)
        {
            $errormessage =
              "Error: Unable to delete Group $deletegroup Check that Group $deletegroup exists.";
            &DBMA_ConnectStatus;
        }
        unless ($dbh->commit)
        {
            $errormessage =
              "$DBI::errstr <br />Error: commit FAIL for delete Group $deletegroup";
            &DBMA_ConnectStatus;
        }
        &checkrequired;
        &prepare_input;
        $sth =
          $dbh->prepare(
            "DELETE FROM $dbmail_aliases_table WHERE client_idnr = '$deletegroup'"
          );
        unless ($sth->execute)
        {
            $errormessage =
              "Error: Unable to delete aliases for $deletegroup. Check that they exist.";
            &DBMA_ConnectStatus;
        }
        $sth->finish() if ($sth);
        $sth =
          $dbh->prepare(
            "DELETE FROM $dbmail_auto_notifications_table where client_idnr = '$deletegroup'"
          );
        $sth->execute;
        $sth->finish() if ($sth);
        $dbh->commit;
        &make_form($userID);
    }
    elsif ($deletegroup > 0)
    {
        $errormessage =
          "Group &quot;0&quot; is restricted to system use. Please contact your Supervisor.";
        &protect_group_Zero;
    }
    else
    {
        $errormessage =
          "You are outside your administrative authority. Please contact your Supervisor.";
        &protect_group_Zero;
    }
    exit;
}
############################################################## - sub delete_specific_forwards_sql RQT9
sub delete_specific_forwards_sql
{
    unless ($FORM{'alias_idnr'})
    {
        $sth =
          $dbh->prepare(
            "SELECT alias_idnr, client_idnr FROM $dbmail_aliases_table WHERE LOWER(alias) = LOWER('$alias')"
          );
        unless ($sth->execute)
        {
            &error('DBMA Cannot find alias $alias');
        }
        while (($alias_idnr, $GroupID) = $sth->fetchrow_array)
        {
            if (   ($RESTRICTGroupID =~ m/[0-9]/i)
                && ($GroupID == $RESTRICTGroupID))
            {
                &error(
                      'Part of this operation is outside your assigned group.');
            }
            $sth =
              $dbh->prepare(
                "DELETE FROM $dbmail_aliases_table WHERE LOWER(alias) = LOWER('$alias') AND alias_idnr = '$alias_idnr'"
              );
            unless ($sth->execute)
            {
                $errormessage =
                  "ErrorID: $version.err0.52 <br />$DBI::errstr<br />Error: Unable to delete aliases $alias - Check that it exists.";
                &DBMA_ConnectStatus;
            }
            unless ($dbh->commit)
            {
                $errormessage =
                  "ErrorID: $version.err0.53 <br />$DBI::errstr<br />$DBI::errstr <br />Error: commit FAIL for delete specific alias";
                &DBMA_ConnectStatus;
            }
        }
        &List_all_Forwards;
    }
    else
    {
        $sth =
          $dbh->prepare(
            "DELETE FROM $dbmail_aliases_table WHERE LOWER(alias) = LOWER('$alias') AND alias_idnr = '$alias_idnr'"
          );
        unless ($sth->execute)
        {
            $errormessage =
              "Error: Unable to delete aliases $alias - Check that it exists.";
            &DBMA_ConnectStatus;
        }
        unless ($dbh->commit)
        {
            $errormessage =
              "$DBI::errstr <br />Error: commit FAIL for delete specific alias";
            &DBMA_ConnectStatus;
        }
        &List_all_Forwards;
    }
}
############################################################## - sub delete_from_aliases_sql RQT41
sub delete_from_aliases_sql
{
    $sth =
      $dbh->prepare(
        "DELETE FROM $dbmail_aliases_table WHERE LOWER(alias) = LOWER('$alias') AND alias_idnr = '$alias_idnr'"
      );
    unless ($sth->execute)
    {
        $errormessage =
          "Error: Unable to delete aliases $alias - Check that it exists.";
        &DBMA_ConnectStatus;
    }
    unless ($dbh->commit)
    {
        $errormessage =
          "$DBI::errstr <br />Error: commit FAIL for delete specific alias";
        &DBMA_ConnectStatus;
    }
    if (($GroupID > 0) && (!$userID)) { &List_Group_Aliases($GroupID); }
    elsif ($userID > 0) { &Create_User_Account_MODIFY_Window($userID); }
    else { &make_form($userID); }
}
############################################################## - sub delete_from_aliases_global_admin
sub delete_from_aliases_global_admin
{
    $sth =
      $dbh->prepare(
        "DELETE FROM $dbmail_aliases_table WHERE LOWER(alias) = LOWER('$alias') AND alias_idnr = '$alias_idnr'"
      );
    unless ($sth->execute)
    {
        $errormessage =
          "Error: Unable to delete aliases $alias - Check that it exists.";
        &DBMA_ConnectStatus;
    }
    unless ($dbh->commit)
    {
        $errormessage =
          "$DBI::errstr <br />Error: commit FAIL for delete specific alias";
        &DBMA_ConnectStatus;
    }
    &List_Global_Aliases;
}
############################################################## - sub mydelete_specific_alias
sub mydelete_specific_alias
{
    $sth =
      $dbh->prepare(
          "DELETE FROM $dbmail_aliases_table WHERE alias_idnr = '$alias_idnr'");
    unless ($sth->execute())
    {
        $errormessage =
          "$DBI::errstr <br />Failed DELETE FROM $dbmail_aliases_table.";
        &DBMA_ConnectStatus;
    }
    unless ($dbh->commit)
    {
        $errormessage =
          "$DBI::errstr <br />Error: commit FAIL for delete specific alias";
        &DBMA_ConnectStatus;
    }
    &Create_User_Account_Window($userID);
}
############################################################## - sub auto_replies
sub auto_replies ($)
{
    &connect unless ($dbh);
    &defaults;
    $sth =
      $dbh->prepare(
        "SELECT reply_body FROM $dbmail_auto_replies_table WHERE user_idnr='$userID'"
      );
    $sth->execute;
    if (($reply_body) = $sth->fetchrow_array)
    {
        print <<"DBMA";
	<div><center><form method="post" action="$mythisscript" style="margin-bottom: 0px; margin-top: 0px">
        <table style="width:738px;background-color:#d6cfde">
	<tr><td><input title="Update AutoReply" onclick="return confirm('Is Auto reply configured in dbmail.conf? \\nAuto reply has risks including mail looping and can expose your system to DoS attacks. \\nClick CANCEL unless you truly know what you are doing.')" type="submit"
	value="AutoReply" onmouseover="this.className='clear';" onmouseout="this.className='letsgo';" class="letsgo" /></td>
	<td style="text-align:left;width:100%"><input type="hidden" name="userID" value="$userID" /><input type="hidden" name="RQT" value="53" /><a target="_blank" onmouseover="self.status='Help';return true" onmouseout="self.status='DBMA';return true" href="DBMA_help.htm#auto_replies"><img class="q" src="images/q.gif" alt="Auto Reply Warning and Help File" /></a>
	<textarea title="Update AutoReply" name="reply_body" class="stats" cols="110" rows="2">$reply_body</textarea></td></tr>
DBMA
        if ($DBMail22Version eq "1")
        {
            $sth =
              $dbh->prepare(
                "SELECT start_date, stop_date FROM $dbmail_auto_replies_table WHERE user_idnr='$userID'"
              );
            $sth->execute;
            while (($start_date, $stop_date) = $sth->fetchrow_array)
            {

                print <<"DBMA";
	<tr><td></td><td style="text-align:left;width:100%"><span class="out">Start date:</span><input style="font-size:11px" size="17" $mouseover type="text" name ="start_date" value="$start_date" /><span class="out">Stop date:</span><input style="font-size:11px" size="17" $mouseover type="text" name ="stop_date" value="$stop_date" /></td></tr>

DBMA
            }
        }

        print <<"DBMA";
	</table></form></center></div>
	<div><center><form method="post" action="$mythisscript"><table><tr><td><input type="hidden" name="userID" value="$userID"><input type="hidden" name="RQT" value="52" /><input type="image" value ="submit" src="images/delete.gif" onmouseover="self.status='Delete Auto Reply';return true" onmouseout="self.status='DBMA';return true" style="vertical-align:bottom;width:37px;height:14px" title="Delete Auto Reply" onclick="return confirm('DELETE Auto Reply.')" />
	<span style="font-size:10px"> Auto Reply</span></td></tr></table></form></center></div>
DBMA
    }
    else
    {
        print <<"DBMA";
	<div><center><form method="post" action="$mythisscript" style="margin-bottom: 0px; margin-top: 0px">
        <table style="width:738px;background-color:#d6cfde">
	<tr><td style="text-align:left;width:100%"><input title="Set AutoReply ... Please read Help!" onclick="return confirm('Is Auto reply configured in dbmail.conf? \\n\\nAuto reply has risks inluding mail looping. Check for pseudo-accounts and forwards on this account first. \\n\\nClick CANCEL if you would like to double check.\\n\\nClick OK to proceed.')" type="submit" value="AutoReply" onmouseover="this.className='front';" onmouseout="this.className='letsgo';" class="letsgo" />
	<input type="hidden" name="userID" value="$userID" /><input type="hidden" name="RQT" value="51" />
	<a target="_blank" onmouseover="self.status='Help';return true" onmouseout="self.status='DBMA';return true" href="DBMA_help.htm#auto_replies"><img class="q" src="images/q.gif" alt="Auto Reply Warning and Help File" /></a>
	<textarea name="reply_body" class="stats" cols="110" rows="2">Auto Reply not set. Erase this text and type your message.
DBMA

        if ($DBMail22Version eq "1")
        {
            print
              "Enter a start date and finish date below and press \"AutoReply\" at left. See HELP for more info.</textarea></td></tr>\n";
        }
        else
        {
            print
              "Then press \"AutoReply\" at left. WARNING: Auto Reply has risks attached. See HELP</textarea></td></tr>\n";
        }

        if ($DBMail22Version eq "1")
        {
            &mysql_date;
            print <<"DBMA";
	<tr><td style="text-align:center;width:100%"><span class="out">AutoReply Start Date :</span><input style="font-size:11px" size="17" $mouseover type="text" name ="start_date" value="$mysqldate" /><span class="out">   Set the "Stop Date" into the future:</span><input style="font-size:11px" size="17" $mouseover type="text" name ="stop_date" value="$mysqldate" /></td></tr>
DBMA
        }
        print <<"DBMA";
	</table></form></center></div>
DBMA
    }
}
############################################################## - sub add_AutoReply
sub add_AutoReply
{

    $reply_body =~ s/\'/\\'/g;

    $reply_body =~ s/\*/\\*/g;
    $reply_body =~ s/\+/\\+/g;
    $reply_body =~ s/\-/\\-/g;
    $reply_body =~ s/\~/\\~/g;
    if ($DBMail22Version eq "1")
    {

        &filt($reply_body);
        if ($reply_body =~ /Auto Reply not set/)
        {
            push(@ERROR, $reply_body);
            &error(
                'Please delete the help text and enter your own Auto Reply Message ',
                @ERROR
            );
        }
        else
        {
            $sth =
              $dbh->prepare(
                "INSERT INTO $dbmail_auto_replies_table (user_idnr, reply_body, start_date, stop_date) VALUES ('$userID', '$reply_body', '$start_date', '$stop_date' )"
              );
            unless ($sth->execute)
            {
                $errormessage =
                  "$DBI::errstr ADD AutoReply Failed <br /> $userID";
                &DBMA_ConnectStatus;
            }
            unless ($dbh->commit)
            {
                $errormessage =
                  "$DBI::errstr <br />Error: ADD AutoReply Failed for $userID";
                &DBMA_ConnectStatus;
            }
            $sth->finish() if ($sth);
            &Create_User_Account_Window($userID);
            exit;
        }
    }
    else
    {

        &filt($reply_body);
        if ($reply_body =~ /Auto Reply not set/)
        {
            push(@ERROR, $reply_body);
            &error(
                'Please delete the help text and enter your own Auto Reply Message ',
                @ERROR
            );
        }
        else
        {
            $sth =
              $dbh->prepare(
                "INSERT INTO $dbmail_auto_replies_table (user_idnr, reply_body) VALUES ('$userID', '$reply_body')"
              );
            unless ($sth->execute)
            {
                $errormessage =
                  "$DBI::errstr ADD AutoReply Failed <br /> $userID";
                &DBMA_ConnectStatus;
            }
            unless ($dbh->commit)
            {
                $errormessage =
                  "$DBI::errstr <br />Error: ADD AutoReply Failed for $userID";
                &DBMA_ConnectStatus;
            }
            $sth->finish() if ($sth);
            &Create_User_Account_Window($userID);
            exit;
        }
    }
}
############################################################## - sub delete_AutoReply
sub delete_AutoReply
{
    &filt($reply_body);
    $sth =
      $dbh->prepare(
            "DELETE from $dbmail_auto_replies_table WHERE user_idnr='$userID'");
    unless ($sth->execute)
    {
        $errormessage = "
	ErrorID: $version.err0.54 <br />$DBI::errstr <br />DELETE AutoReply Failed for $userID";
        &DBMA_ConnectStatus;
    }
    unless ($dbh->commit)
    {
        $errormessage = "
	ErrorID: $version.err0.55 <br />$DBI::errstr <br />Error:  DELETE AutoReply Failed for $userID";
        &DBMA_ConnectStatus;
    }
    $sth->finish() if ($sth);
    &Create_User_Account_Window($userID);
    exit;
}
############################################################## - sub update_AutoReply
sub update_AutoReply ($)
{
    &filt($reply_body);

    if ($DBMail22Version eq "1")
    {
        $sth =
          $dbh->prepare(
            "UPDATE $dbmail_auto_replies_table SET reply_body='$reply_body', start_date='$start_date', stop_date='$stop_date' WHERE user_idnr='$userID'"
          );
    }
    else
    {
        $sth =
          $dbh->prepare(
            "UPDATE $dbmail_auto_replies_table SET reply_body='$reply_body' WHERE user_idnr='$userID'"
          );
    }
    unless ($sth->execute)
    {
        $errormessage = "
	ErrorID: $version.err0.56 <br />$DBI::errstr <br />AutoReply Failed for $userID";
        &DBMA_ConnectStatus;
    }
    unless ($dbh->commit)
    {
        $errormessage =
          "$DBI::errstr <br />Error:  AutoReply Failed for $userID";
        &DBMA_ConnectStatus;
    }
    $sth->finish() if ($sth);
    &Create_User_Account_Window($userID);
    exit;
}
############################################################## - sub delete_auto_notify
sub delete_auto_notify ($)
{
    $sth =
      $dbh->prepare(
        "DELETE from $dbmail_auto_notifications_table WHERE user_idnr='$userID'"
      );
    unless ($sth->execute)
    {
        $errormessage = "
	ErrorID: $version.err0.57 <br />$DBI::errstr <br />DELETE AutoNotify Failed for $userID";
        &DBMA_ConnectStatus;
    }
    unless ($dbh->commit)
    {
        $errormessage = "
	ErrorID: $version.err0.58 <br />$DBI::errstr <br />Error:  DELETE AutoNotify Failed for $userID";
        &DBMA_ConnectStatus;
    }
    $sth->finish() if ($sth);
    &Create_User_Account_Window($userID);
    exit;
}
############################################################## - sub update_auto_notify
sub update_auto_notify ($)
{
    &check_if_RFC_alias($notify_address);
    $sth =
      $dbh->prepare(
        "UPDATE $dbmail_auto_notifications_table SET notify_address ='$notify_address' WHERE user_idnr='$userID'"
      );
    unless ($sth->execute)
    {
        $errormessage = "
	ErrorID: $version.err0.59 <br />$DBI::errstr <br />Update AutoNotify Failed for $userID";
        &DBMA_ConnectStatus;
    }
    unless ($dbh->commit)
    {
        $errormessage =
          "$DBI::errstr <br />Error: Update AutoNotify Failed for $userID";
        &DBMA_ConnectStatus;
    }
    $sth->finish() if ($sth);
    &Create_User_Account_Window($userID);
    exit;
}
############################################################## - sub auto_notifications
sub auto_notifications ($)
{
    $sth =
      $dbh->prepare(
        "SELECT notify_address FROM $dbmail_auto_notifications_table WHERE user_idnr='$userID'"
      );
    $sth->execute;
    if (($notify_address) = $sth->fetchrow_array)
    {
        print <<"DBMA";
	<div><center><form method="post" action="$mythisscript" style="margin-bottom: 0px; margin-top: 0px">
        <table style="background-color:#d6cfde;width:738px"><tr>
	<td><input title="Update Auto Notification" onclick="return confirm('Have you checked your input carefully?\\nIs Auto Notify configured in dbmail.conf?')" type="submit" value="AutoNotify" onmouseover="this.className='clear';" onmouseout="this.className='letsgo';" class="letsgo" /></td>
	<td style="width:100%"><input type="hidden" name="userID" value="$userID" /><input type="hidden" name="RQT" value="57" /><a target="_blank" onmouseover="self.status='Help';return true" onmouseout="self.status='DBMA';return true" href="DBMA_help.htm#add_auto_notify"><img class="q" src="images/q.gif" alt="Auto Notify Help" /></a>
	<input title="You can change the email address to which NEW MAIL NOTICES should be sent." type="text"  size="36" value="$notify_address" name="notify_address" $mouseover $changecase><span class="out">Type your change of email address to be notified.</span></td></tr></table></form></center></div>
	<div><center><form method="post" action="$mythisscript"><table><tr><td><input type="hidden" name="userID" value="$userID" /><input type="hidden" name="RQT" value="56" /><input type="image" value ="submit" src="images/delete.gif" onmouseover="self.status='Delete Auto Notification';return true" onmouseout="self.status='DBMA';return true" style="vertical-align:bottom;width:37px;height:14px" title="Delete Auto Notification" onclick="return confirm('DELETE Auto Notify')" />
	<span style="font-size:10px"> Auto Notify</span></td></tr></table></form></center></div>
DBMA
    }
    else
    {
        print <<"DBMA";
	<div><center><form method="post" action="$mythisscript" style="margin-bottom: 0px; margin-top: 0px"><table style="background-color:#d6cfde"><tr>
	<td><input title="Add Auto Notification" onclick="return confirm('Reminder: is Auto Notify configured in dbmail.conf? \\nClick OK to proceed now and create Auto Notification?')" type="submit" value="AutoNotify" onmouseover="this.className='front';" onmouseout="this.className='letsgo';" class="letsgo" /></td>
	<td style="width:100%;text-align:left"><input type="hidden" name="userID" value="$userID" /><input type="hidden" name="RQT" value="15" /><a target="_blank" onmouseover="self.status='Help';return true" onmouseout="self.status='DBMA';return true" href="DBMA_help.htm#add_auto_notify"><img class="q" src="images/q.gif" alt="Auto Notify Help File" /></a><input title="Type email address to send auto notification." type="text" size="36" name="notify_address" $mouseover $changecase />
	<span class="out">Type address to be notified when $usernameDISPLAY gets mail.</span></td></tr></table></form></center></div>
DBMA
    }
}
############################################################## - sub Update_UserMap RQT65
sub Update_UserMap
{
    if (($DBMail22Version eq "1") && ($deny_user_access eq "DENY") && ($userID))
    {
        &deny_user_access;
    }
    elsif (   ($DBMail22Version eq "1")
           && ($clear_user_mapping eq "CLEAR")
           && ($userID))
    {
        &clear_user_mapping;
    }
    elsif (($DBMail22Version eq "1") && ($userID))
    {
        my $sql =
          "UPDATE $dbmail_usermap_table SET login='$login', sock_allow='$sock_allow', sock_deny='$sock_deny', userid='$usermap_userid' WHERE userid = '$userID' OR login = '$userID'";
        $sth = $dbh->prepare($sql);
        $sth->execute();
        $sth->finish() if ($sth);
        $dbh->commit();
        &Create_User_Account_Window($userID);
    }
    else { &make_menu; }

}

############################################################## - sub Create_UserMap RQT66
sub Create_UserMap
{
    if (($DBMail22Version eq "1") && ($deny_user_access eq "DENY") && ($userID))
    {
        my $sql =
          "INSERT INTO $dbmail_usermap_table (login, sock_allow, sock_deny, userid) VALUES ('$userID', '', 'inet:0.0.0.0:0', '$userID')";
        $sth = $dbh->prepare($sql);
        $sth->execute();
        $sth->finish() if ($sth);
        $dbh->commit();
        &Create_User_Account_Window($userID);
    }
    elsif (   ($DBMail22Version eq "1")
           && ($clear_user_mapping eq "CLEAR")
           && ($userID))
    {
        &clear_user_mapping;
    }
    elsif (($DBMail22Version eq "1") && ($userID))
    {
        my $sql =
          "INSERT INTO $dbmail_usermap_table (login, sock_allow, sock_deny, userid) VALUES ('$login', '$sock_allow', '$sock_deny', '$usermap_userid')";
        $sth = $dbh->prepare($sql);
        $sth->execute();
        $sth->finish() if ($sth);
        $dbh->commit();
        &Create_User_Account_Window($userID);
    }
    else { &make_menu; }

}
############################################################## - clear_user_mapping
sub clear_user_mapping
{

## Clear the usermap settings doesn't actually clear them. It only clears the action directives allow and deny
## presently I am setting login and userid to dbmail_users.userid which is the account name thus it is a 1to1 mapping to itself
## this is the default mapping when nothing is set so essentially we have reserved a usermap row for this user
## I do this for a number of reasons, one of which is to lock a mapping row for the user so it cannot be entered by mistake later
## and another is to save work later
## It is slightly possible this could create a contradiction in furture MTA virtual settings so Let's watch it.

    if (   ($DBMail22Version eq "1")
        && ($clear_user_mapping eq "CLEAR")
        && ($userID))
    {
        my $sql =
          "UPDATE $dbmail_usermap_table SET login='$userID', sock_allow='', sock_deny='', userid='$userID' WHERE userid = '$userID' OR login = '$userID'";
        $sth = $dbh->prepare($sql);
        $sth->execute();
        $sth->finish() if ($sth);
        $dbh->commit();
        &Create_User_Account_Window($userID);
    }
    else { &make_menu; }

}

############################################################## - sub deny_user_access
sub deny_user_access
{
    if (($DBMail22Version eq "1") && ($userID))
    {
        my $sql =
          "UPDATE $dbmail_usermap_table SET login='$userID', sock_allow='', sock_deny='inet:0.0.0.0:0', userid='$userID' WHERE userid = '$userID' OR login = '$userID'";
        $sth = $dbh->prepare($sql);
        $sth->execute();
        $sth->finish() if ($sth);
        $dbh->commit();
        &Create_User_Account_Window($userID);
    }
    else { &make_menu; }

}
############################################################## - sub prepare_input
sub prepare_input ($)
{
    &connect unless ($dbh);
    &LIST_Global if ($userID eq "any");
    $userID =~ s/ //g;
    if ($RESTRICTGroupID =~ m/[0-9]/i)
    {
        $GroupControl = " AND client_idnr = \'$RESTRICTGroupID\'";
    }
    else
    {
        $GroupControl = "";
    }

    if ($userID =~ /^[^@]+@([-\w]+\.)+[A-Za-z]{2,4}$/)
    {
        $sth =
          $dbh->prepare(
            "SELECT user_idnr FROM $dbmail_users_table WHERE LOWER(userid) = LOWER('$userID')$GroupControl"
          );
        $sth->execute();
        while (($user_idnr) = $sth->fetchrow_array)
        {
            $userID       = $user_idnr;
            $myUserIDdata = $userID;
        }

        unless ($myUserIDdata)
        {

if ($sqltype =~ /pgsql/)
{
            $sth = $dbh->prepare(
                "SELECT deliver_to
FROM $dbmail_aliases_table
LEFT JOIN $dbmail_users_table on CAST($dbmail_users_table.user_idnr AS text) = $dbmail_aliases_table.deliver_to
WHERE LOWER(alias) = LOWER('$userID')$GroupControl"
                                );
}
if ($sqltype =~ /mysql/)
{
            $sth = $dbh->prepare(
                "SELECT deliver_to
FROM $dbmail_aliases_table
LEFT JOIN $dbmail_users_table on $dbmail_users_table.user_idnr = $dbmail_aliases_table.deliver_to
WHERE LOWER(alias) = LOWER('$userID')$GroupControl"
                                );
}
            $sth->execute();
            while (($user_idnr) = $sth->fetchrow_array)
            {
                $userID       = $user_idnr;
                $myUserIDdata = $userID;
            }
        }

        $sth->finish() if ($sth);
    }
    elsif ($userID =~ /[A-Za-z0-9\!\#\$\%\&\'\*\+\-\/\=\?\^\_\'\`\{\|\+\~]/)
    {
        $sth =
          $dbh->prepare(
            "SELECT user_idnr FROM $dbmail_users_table WHERE LOWER(userid) LIKE LOWER('$userID')$GroupControl"
          );
        $sth->execute();
        while (($user_idnr) = $sth->fetchrow_array)
        {
            $userID       = $user_idnr;
            $myUserIDdata = $userID;
        }
        $sth->finish() if ($sth);
    }
    else
    {
        $userID = $FORM{'userID'};
    }
    my (@output, $thename);
    @output = &split($userID);
    my $myUserIDdata = $output[0];
    $myUserIDdata =~ s/[^\w]//g;    #security
    if ($myUserIDdata =~ /([^0-9])/)
    {
        $sth =
          $dbh->prepare(
            "SELECT user_idnr FROM $dbmail_users_table WHERE LOWER(userid) like LOWER('$myUserIDdata')"
          );
        $sth->execute();
        while (($user_idnr) = $sth->fetchrow_array)
        {
            $userID       = $user_idnr;
            $myUserIDdata = $userID;
        }
    }
    $userID =~ s/[^0-9]//g;
    $sth =
      $dbh->prepare(
        "SELECT client_idnr FROM $dbmail_users_table WHERE user_idnr = '$userID'"
      );
    $sth->execute();
    while (my $rv = $sth->fetchrow_hashref())
    {
        $myClientID = $rv->{'client_idnr'};
        $myGroupID  = $myClientID;
        $GroupID    = $myGroupID;
    }
    if (($RESTRICTGroupID =~ m/[0-9]/i) && ($myClientID > 0))
    {
        unless ($RESTRICTGroupID == $myGroupID)
        {
            $errormessage = "Please select another user name.";
            &exist_in_another_Group;
        }
    }
}
############################################################## - sub DBI_drivers
sub DBI_drivers
{
    my ($driver, @drivers, $perlVersionString);
    print "	<h4>PERL DBI drivers on $ENV{'SERVER_NAME'}</h4><ul>";
    @drivers = DBI->available_drivers('quiet');
    foreach $driver (@drivers)
    {
        print "	<li>$driver</li>";
    }
    $perlVersionString = `perl -v`;
    chop($perlVersionString);
    print
      "	</ul><strong>Perl Version</strong>:<small>$perlVersionString</small>";
}
############################################################## - sub checkrequired
sub checkrequired
{
    unless ($FORM{'required'})
    {
        return 0;
    }
    if ($RESTRICTGroupID eq "any")
    {
        $GroupID = $FORM{'GroupID'} || ($GroupID) || shift || $_;
    }

    elsif ($RESTRICTGroupID =~ m/[1-9]/i) { $GroupID = $RESTRICTGroupID; }

    if ($GroupID =~ m/[a-z]|[A-Z]/i)
    {
        &error('A group ID may not be an alpha character');
    }
    if (defined $FORM{'GroupID'} eq "0")
    {
        &error('Group 0 (zero) is intended for internal system use only');
    }
    @required = split(/,/, $FORM{'required'});
    foreach $require (@required)
    {
        if (!($FORM{$require}) || $FORM{$require} eq ' ')
        {
            push(@ERROR, $require);
        }
    }
    if (@ERROR)
    {
        &error('Please enter additional information to proceed: ', @ERROR);
    }
}
############################################################## - sub make_sixty_four
sub make_sixty_four
{
    my $salt_range =
      "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    my ($v, $n) = @_;
    my $ret = '';
    while (--$n >= 0)
    {
        $ret .= substr($salt_range, $v & 0x3f, 1);
        $v >>= 6;
    }
    $ret;
}
############################################################## - sub split
sub split
{
    my ($emailstring) = shift(@_);
    @components = split('@', $emailstring);
    return @components;
}
############################################################## - sub check_if_RFC_alias
sub check_if_RFC_alias ($)
{
    if ($bypass eq "1")
    {
        return 1;
    }
    $text         = qr/[\x01-\x09\x0b\x0c\x0e-\x7f]/;
    $notwsctlchar = qr/[\x01-\x08\x0b\x0c\x0e-\x1f\x7f]/;
    my ($string) = @_;
    my $dtext = qr/[\x21-\x5a\x5e-\x7e\x01-\x08\x0b\x0c\x0e-\x1f\x7f]/;
    $quotedpair = qr/\\$text/;
    my $dcontent              = qr/($dtext|$quotedpair)/;
    my $domain_literal        = qr/\[(${dcontent})*\]/;
    my $myalpha_plus_RFC_char =
      qr/[A-Za-z0-9\!\#\$\%\&\'\*\+\-\/\=\?\^\_\`\{\|\+\~]/;
    my $myquerytext_char = qr/([\x21\x23-\x5b\x5d-\x7e]|$notwsctlchar)/;
    my $myquerytext      = qr/($myquerytext_char|\\$text)*/;
    my $partition     = qr/$myalpha_plus_RFC_char+(\.$myalpha_plus_RFC_char+)*/;
    my $quoted_string = qr/"$myquerytext"/;

    if ($string =~
        /^($partition|$quoted_string)\@($partition|$domain_literal)$/)
    {
        return 1;
    }
    else
    {
        push(@ERROR, $string);
        &error('RFC-Illegal email address for: ', @ERROR);
    }
}
############################################################## - sub perl_crypt
sub perl_crypt
{
    my ($string) = @_;
    my $salt = join "", (0 .. 9, "A" .. "Z", "a" .. "z")[rand 63, rand 63];
    return crypt($string, $salt);
}
############################################################## - sub MD5_hash
sub MD5_hash
{
    my ($string) = @_;
    require Digest::MD5;
    $md5 = Digest::MD5->new;
    $md5->add($string);
    $digest = $md5->hexdigest;
    return $digest;
}
############################################################## - sub MD5_Encrypt
sub MD5_Encrypt
{
    my ($pl);
    use Digest::MD5;
    my ($string) = @_;
    my $salt = join "", (0 .. 9, "A" .. "Z", "a" .. "z", ".", "/")
      [rand 64, rand 64, rand 64, rand 64, rand 64, rand 64, rand 64, rand 64];
    my $salt_delineate = q/$1$/;
    my $password;
    my $ctx = new Digest::MD5;
    $ctx->add($string);
    $ctx->add($salt_delineate);
    $ctx->add($salt);
    my ($crypt_result) = new Digest::MD5;
    $crypt_result->add($string);
    $crypt_result->add($salt);
    $crypt_result->add($string);
    $crypt_result = $crypt_result->digest;

    for ($pl = length($string) ; $pl > 0 ; $pl -= 16)
    {
        $ctx->add(substr($crypt_result, 0, $pl > 16 ? 16 : $pl));
    }
    for ($i = length($string) ; $i ; $i >>= 1)
    {
        if ($i & 1) { $ctx->add(pack("C", 0)); }
        else { $ctx->add(substr($string, 0, 1)); }
    }
    $crypt_result = $ctx->digest;
    for ($i = 0 ; $i < 1000 ; $i++)
    {
        my $ctx1 = new Digest::MD5;
        if ($i & 1) { $ctx1->add($string); }
        else { $ctx1->add(substr($crypt_result, 0, 16)); }
        if ($i % 3) { $ctx1->add($salt); }
        if ($i % 7) { $ctx1->add($string); }
        if ($i & 1) { $ctx1->add(substr($crypt_result, 0, 16)); }
        else { $ctx1->add($string); }
        $crypt_result = $ctx1->digest;
    }
    $password = '';
    $password .=
      make_sixty_four(
                      int(unpack("C",   (substr($crypt_result, 0,  1))) << 16) |
                        int(unpack("C", (substr($crypt_result, 6,  1))) << 8) |
                        int(unpack("C", (substr($crypt_result, 12, 1)))),
                      4
                     );
    $password .=
      make_sixty_four(
                      int(unpack("C",   (substr($crypt_result, 1,  1))) << 16) |
                        int(unpack("C", (substr($crypt_result, 7,  1))) << 8) |
                        int(unpack("C", (substr($crypt_result, 13, 1)))),
                      4
                     );
    $password .=
      make_sixty_four(
                      int(unpack("C",   (substr($crypt_result, 2,  1))) << 16) |
                        int(unpack("C", (substr($crypt_result, 8,  1))) << 8) |
                        int(unpack("C", (substr($crypt_result, 14, 1)))),
                      4
                     );
    $password .=
      make_sixty_four(
                      int(unpack("C",   (substr($crypt_result, 3,  1))) << 16) |
                        int(unpack("C", (substr($crypt_result, 9,  1))) << 8) |
                        int(unpack("C", (substr($crypt_result, 15, 1)))),
                      4
                     );
    $password .=
      make_sixty_four(
                      int(unpack("C",   (substr($crypt_result, 4,  1))) << 16) |
                        int(unpack("C", (substr($crypt_result, 10, 1))) << 8) |
                        int(unpack("C", (substr($crypt_result, 5,  1)))),
                      4
                     );
    $password .=
      make_sixty_four(int(unpack("C", substr($crypt_result, 11, 1))), 2);
    $crypt_result = '';
    $digest       = ($salt_delineate . $salt . q/$/ . $password);
    return $digest;
}
############################################################## - sub MD5_hash_salt_key
sub MD5_hash_salt_key
{
    my ($string) = @_;
    use Digest::MD5 qw(md5_base64);
    $key = "$string";
    my $DBMA_RAND_SALT = join "", (0 .. 9, "A" .. "Z", "a" .. "z", ".", "/")
      [rand 62, rand 62, rand 62, rand 62, rand 62, rand 62, rand 62, rand 62];
    my $digest = '$1$'
      . $DBMA_RAND_SALT . '$'
      . md5_base64("$DBMA_RAND_SALT/$string/$key");
    return "$digest";
}
############################################################## - sub compare
sub compare(\$\$)
{
    my ($a, $b) = @_;
    return 0 unless @$a == @$b;
    for (my $i = 0 ; $i < @$a ; $i++)
    {
        return 0 if $a->[$i] != $b->[$i];
    }
    return 1;
}
############################################################## - sub char_filt
sub char_filt
{
    $_[0] =~ s/\'/\\\'/g;
    $_[0] =~ s/[^\w]//g;
    $_[0] =~ s/ //g;
    return $_[0];
}
############################################################## - sub filt
sub filt
{
    $_[0] =~ s/^\s+//;
    $_[0] =~ s/\s+$//;
    return $_[0];
}
############################################################## - sub password_tools
sub password_tools
{
    &defaults;
    &meta;
    &menu;
    my $operator = $operator || "";
    my $results  = $results  || "";
    my $encrypttype = $FORM{'encrypttype'} || $encrypttype || "";
    print <<"DBMA";
	<div><center><form method="post" action="$mythisscript"><table width="738px" cellspacing="0" cellpadding="6">
	<tr><td colspan="3" style="font-size: 12px">The effect of this test tool is visual. It shows what various encrypt methods <em>should look like</em>. You choose your default encryption method not here but from the &quot;Configuration Window&quot;. Examples:
	<br /><br /> &#149; <b>MD5</b> = <span style="color:#6a6a95;background:#F8F8FF">\&#36;1\&#36;s0yfoqOn\&#36;i6Nr5nPSAhuqxbk.h.EJn/</span> In this MD5 password string, the characters between the 2nd and 3rd &quot;\$&quot; are the 8-chars (maximum) of 'Salt' used to create the RSA password which follows the 3rd &quot;\$&quot;.
	<br /> &#149; <b>md5sum</b> = <span style="color:#6a6a95;background:#F8F8FF">9cd234f150c500d196fbad63d2877bb2</span> or <b>md5 hash</b> is a one-way hash algorithm defined by RFC1321. On the command line type &quot;md5 -s encrypthelp&quot; for identical 128 bit digital signature of the password string.
	<br /> &#149; <b>crypt</b> = <span style="color:#6a6a95;background:#F8F8FF">MBQF2l2BTiTbM</span> or UNIX crypt is based on a DES algorithm with a standard 2-char &quot;salt&quot;. The first two chars define the salt which perturbs the algorithm in one of 4096 different ways.<p>DBMail uses "crypt", "md5" and "md5sum" in addition to clear text (plain). Hopefully this helps you decide your password policies. (For future admin use, SHA1 and MD5hash_key (using salt/string/key) are shown here.)</p></td></tr>
	<tr><td>Password</td><td style="font-size: 10px"><input type="radio" name="encrypttype" value="crypt" />crypt<input type="radio" name="encrypttype" value="md5" />md5<input type="radio" value="md5sum" name="encrypttype" />md5sum<br /><input type="radio" name="encrypttype" value="SHA1" />*<span class="notseen">SHA1</span><input type="radio" name="encrypttype" value="MD5_hash_salt_key" />*<span class="notseen">MD5hash_key</span></td>
	<td>$message Results $operator</td></tr>
	<tr><td><p><input type="text" $mouseover value="$password" name="password" size="12" /></p><input type="hidden" name="RQT" value="27" /></td><td><input class="c7" type="submit" value="Encrypt" name="submit" /></td><td><input type="text" $mouseover value="$results" size="42" style="bgcolor:#f0f0f0" /></td></tr>
	<tr><td colspan="3"><br />* <small>DBMA internal use</small></td></tr>
	<tr><td colspan="4"><hr style="background-color:#D6CFDE; color:#D6CFDE;height:20px" /></td></tr>
	</table></form></center></div>
DBMA
    exit;
}
############################################################## - sub password_encrypt
sub password_encrypt
{
    my $password = ((&char_filt($FORM{'password'})) || ("encrypthelp"));
    my $encrypttype = $FORM{'encrypttype'} || $encrypttype || "";
    my $results     = $results             || "NULL";
    my $operator    = "";
    my $message     = "";
    if ($encrypttype =~ /md5sum/)
    {
        $results = &MD5_hash($FORM{'password'});
        $message = "MD5 hash";
    }
    elsif ($encrypttype =~ /MD5_hash_salt_key/)
    {
        $results = &MD5_hash_salt_key($FORM{'password'});
        $message = "md5_base64:salt/pass/key";
    }
    elsif ($encrypttype =~ /md5/)
    {
        $results = &MD5_Encrypt($FORM{'password'});
        $message = "MD5 8Chars salt";
    }
    elsif ($encrypttype =~ /crypt/)
    {
        $results = &perl_crypt($FORM{'password'});
        $message = "crypt";
    }
    elsif ($encrypttype =~ /SHA1/)
    {
        $operator = "SHA1";
        $sth      = $dbh->prepare("SELECT $operator('$password');");
        unless ($sth->execute())
        {
            $errormessage = "
	ErrorID: $version.err0.70 <br />$DBI::errstr <br />SHA1 Is unavailable";
            &password_tools;
        }
        while (($output) = $sth->fetchrow_array)
        {
            $results = $output;
        }
    }
    elsif (($sqltype =~ /mysql/) && ($encrypttype =~ /md5sum/))
    {
        $operator    = "MD5";
        $message     = "MySQL";
        $encrypttype = "md5sum";
        $sth         = $dbh->prepare("SELECT $operator('$password');");
        unless ($sth->execute())
        {
            $errormessage = "
	ErrorID: $version.err0.71 <br />$DBI::errstr <br />Failed SELECT password.";
            &DBMA_ConnectStatus;
        }
        while (($output) = $sth->fetchrow_array)
        {
            $results = $output;
        }
    }
    else
    {
        $results = &MD5_hash($FORM{'password'});
        $message = "MD5 hash";
    }
    &meta;
    &menu;
    print <<"DBMA";
	<div><center><form method="post" action="$mythisscript"><table width="738px" cellspacing="0" cellpadding="6">
	<tr><td colspan="3" style="font-size: 12px">The effect of this test tool is visual. It shows what various encrypt methods <em>should look like</em>. Choose a default encryption method from the &quot;Configurations Window&quot;. Look at the encrypted string "encrypthelp".
	<br /><br /> &#149; <b>MD5</b> = <span style="color:#6a6a95;background:#F8F8FF">\&#36;1\&#36;s0yfoqOn\&#36;i6Nr5nPSAhuqxbk.h.EJn/</span> In this MD5 password string, the characters between the 2nd and 3rd &quot;\&#36;&quot; are the 8-chars (maximum) of 'Salt' used to create the RSA password which follows the 3rd &quot;\&#36;&quot;.
	<br /> &#149; <b>md5sum</b> = <span style="color:#6a6a95;background:#F8F8FF">9cd234f150c500d196fbad63d2877bb2</span> or <b>md5 hash</b> is a one-way hash algorithm defined by RFC1321. On the command line type &quot;md5 -s encrypthelp&quot; for identical 128 bit digital signature of the password string.
	<br /> &#149; <b>crypt</b> = <span style="color:#6a6a95;background:#F8F8FF">MBQF2l2BTiTbM</span> or UNIX crypt is based on a DES algorithm with a standard 2-char &quot;salt&quot;. The first two chars define the salt which perturbs the algorithm in one of 4096 different ways.<p>DBMail uses "crypt", "md5" and "md5sum" in addition to clear text (plain). Hopefully this helps you decide your password policies. (For future admin use, SHA1 and MD5hash_key (using salt/string/key) are shown here.)</p></td></tr>
	<tr><td>Password</td><td style="font-size: 10px"><input type="radio" name="encrypttype" value="crypt" />crypt<input type="radio" name="encrypttype" value="md5" />md5<input type="radio" value="md5sum" name="encrypttype" />md5sum<br /><input type="radio" name="encrypttype" value="SHA1" />*<span class="notseen">SHA1</span><input type="radio" name="encrypttype" value="MD5_hash_salt_key" />*<span class="notseen">MD5hash_key</span></td>
	<td>$message Results $operator</td></tr>
	<tr><td><p><input type="text" $mouseover value="$password" name="password" size="12" /></p><input type="hidden" name="RQT" value="27" /></td><td><input class="c7" type="submit" value="Encrypt" name="submit" /></td><td><input type="text" $mouseover value="
DBMA
    print $results if $results;
    print <<"DBMA";
" size="42" style="bgcolor:#f0f0f0" /></td></tr>
	<tr><td colspan="3"><br />* <small>DBMA internal use</small></td></tr>
	<tr><td colspan="4"><hr style="background-color:#D6CFDE; color:#D6CFDE;height:20px" /></td></tr>
	</table></form></center></div>
DBMA
    exit;
}
############################################################## - sub password_generator
sub password_generator
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
        $password .= $char;
    }
    return $password;
}

# - Forms Errors Warnings and Reports
############################################################## - sub minisearchform
sub minisearchform
{
    $searchterms =~ s/\</\&\#60\;/g;
    $searchterms =~ s/\>/\&\#62\;/g;
    $searchterms =~ s/\@/\&\#64\;/g;
    $searchterms =~ s/\^/\&\#136\;/g;
    print <<"DBMA";
	<form method="post" action="$mythisscript">
	<input type="hidden" name="RQT" value="33a" /><input type="hidden" name="userID" value="$userID" /><input type="hidden" name="username" value="$username" /><input type="hidden" name="required" value="searchterms" />
	<span style="font-size:10px;color:green">Search header fields only?</span><input type="radio" name="headers_only" value="1" />
	<input type="text" $mouseover name="searchterms" value="$searchterms" style="font-size:11px;background-color:#ffffc4" size="30" title="Enter your search terms. DBMA will search all mailboxes." />
	<input title="Search mail in all $username\'s Mailboxes" type="image" style="vertical-align:top;width:85px;height:18px;vertical-align:top;" src="images/search.gif" />
</form>
DBMA
}
############################################################## - sub DBMA_Advisor
sub DBMA_Advisor
{
    my ($noinput, $my_insert);
    my ($message, @message_fields) = @_;
    my $missing_field;
    &meta;
    &menu;
    print <<"DBMA";
    	<div><center><table><tr><td>$message<blockquote>
DBMA
    foreach $missing_field (@message_fields)
    {
        print
          "<span style=\"font-weight:600;background:#F8F8FF;color:#800000\">$missing_field</span><br />\n";
    }
    if (   ($message eq "Success! Deleted.")
        || ($message =~ /Congratulations. This step completed successfully/))
    {
        $my_insert = "<small>$version $date</small>\n";
    }
    else
    {
        $my_insert =
          "<span style=\"color:#6a6a95\"><<< </span><a title=\"return to form\" href=\"javascript:history.go(-1)\" onmouseover=\"self.status=\'Back to form\';return true\" onmouseout=\"self.status=\'DBMA\';return true\" />Back</a>\n";
    }
    print <<"DBMA";
	<br />$my_insert</blockquote></td></tr></table></center></div>
DBMA
    end_HTML;
    exit;
}
############################################################## - sub error
sub error
{
    my ($noinput, $my_insert);
    my ($error, @error_fields) = @_;
    my $missing_field;
    &meta;
    &menu;
    &check_permissions;
    print
      "	<div><center><table><tr><td><h5 style=\"color:red\">$perm_error</h5></td></tr></table></center></div>\n"
      if ($perm_error);

    print <<"DBMA";
    	<div><center><table><tr><td><h3>$error</h3><blockquote>
DBMA
    foreach $missing_field (@error_fields)
    {
        print
          "<span style=\"font-weight:600;background:#F8F8FF;color:#800000\">$missing_field</span><br />\n";
    }
    if (   ($error eq "Success! Deleted.")
        || ($error =~ /Congratulations. This step completed successfully/))
    {
        $my_insert = "<small>$version $date</small>\n";
    }
    else
    {
        $my_insert =
          "<span style=\"color:#6a6a95\"><<< </span><a title=\"return to form\" href=\"javascript:history.go(-1)\" onmouseover=\"self.status=\'Back to form\';return true\" onmouseout=\"self.status=\'DBMA\';return true\" />Back</a>\n";
    }
    print <<"DBMA";
	<br />$my_insert</blockquote></td></tr></table></center></div>
DBMA
    end_HTML;
    exit;
}
############################################################## sub check_permissions
sub check_permissions
{
    my $user = `whoami`;
    my $daemon = $ENV{'SERVER_SOFTWARE'} if ($ENV{'SERVER_SOFTWARE'});
    unless (-W $ALIAS_AND_SQL_MATCH)
    {
        $colortellsastory = "#F0F0F0";
        $perm_error       =
          "<br />ALERT: DBMA cannot write to $ALIAS_AND_SQL_MATCH. Please fix permissions.";
    }
    unless (-W $DBMA_DATA)
    {
        $colortellsastory = "#F0F0F0";
        $perm_error       =
          "<br />ALERT: DBMA cannot write to $DBMA_DATA . Please fix permissions.";
    }
    unless (-W $DBMA_GROUP_DATA)
    {
        $colortellsastory = "#F0F0F0";
        $perm_error       =
          "<br />ALERT: DBMA cannot write to $DBMA_GROUP_DATA . Please fix permissions.";
    }
    unless (-W $DBMA_TIMESTAMP)
    {
        $colortellsastory = "#F0F0F0";
        $perm_error       =
          "<br />ALERT: DBMA cannot write to $DBMA_TIMESTAMP . Please fix permissions.";
    }
    unless (-W $myDBMA_OPTIONS)
    {
        $colortellsastory = "#F0F0F0";
        $perm_error       =
          "<br />ALERT: DBMA cannot write to $myDBMA_OPTIONS .  Please fix /dbmailadministrator permissions for  $user  real user and group the HTTPD runs as ($daemon).";
    }
    unless (-W $DBMA_STATS)
    {
        $colortellsastory = "#F0F0F0";
        $perm_error       =
          "<br />ALERT: DBMA cannot write to $DBMA_STATS . Please fix permissions.";
    }
    unless (-W $myDBMA_CONFIG)
    {
        $colortellsastory = "#F0F0F0";
        $perm_error       =
          "<br />ALERT: DBMA cannot write to $myDBMA_CONFIG . Please fix /dbmailadministrator permissions for  $user  real user and group the HTTPD runs as ($daemon).";
    }
    unless (-W $DBMA_DATA_MTA_TEMP)
    {
        $colortellsastory = "#F0F0F0";
        $perm_error       =
          "<br /><u>Caution: DBMA_DATA_MTA_TEMP out of sync.</u><br />Have you created the DBMA MTA domains yet? If not and --Use MTA Domains-- has just now been set to YES, please create the tables by pressing the button down below: \"Create DBMA MTA Tables\". This message also appears on version upgrades where tables exist and DBMA\'s drop (temp) files are not yet written. If this is an upgrade or change, and the DBMA MTA tables do in fact exist, select \"Menu\" above then press \'Go!\' twice on the main menu to make certain all flat DBs are initiated. If you are in doubt, test your configs by going to the main menu."
          if ($use_DBMA_MTA_Domains eq "1");
    }
    unless (-W $DBMA_SQL_MTA)
    {
        $colortellsastory = "#F0F0F0";
        $perm_error       =
          "<br />ALERT: DBMA cannot write to $DBMA_SQL_MTA . Please fix permissions.";
    }
    unless (-W $Missing_In_SQL_MTA)
    {
        $colortellsastory = "#F0F0F0";
        $perm_error       =
          "<br />ALERT: DBMA cannot write to $Missing_In_SQL_MTA . Please fix /dbmailadministrator permissions for  $user  real user and group the HTTPD runs as ($daemon)."
          if ($use_DBMA_MTA_Domains eq "1");
    }
    unless (-W $Not_Found_In_Aliases)
    {
        $colortellsastory = "#F0F0F0";
        $perm_error       =
          "<br />ALERT: DBMA cannot write to $Not_Found_In_Aliases . Please fix permissions.";
    }
}
############################################################## - sub fail
sub fail
{
    $value = $userID || $FORM{'userID'} || "";
    $errormessage = $errormessage || "";
    &meta;
    &menu;
    print <<"DBMA";
	<div><center><table><tr><td colspan="6" ><h1 style="color:red">User: $value does not exist.</h1><br />$errormessage<h3>Press the button below to add an account for $FORM{'userID'}.</h3></td></tr></table></center></div>
	<div><center><form method="post" action="$mythisscript"><table><tr><td><input type="hidden" name ="RQT" value="3" /><input type="hidden" name ="username" value="$FORM{'userID'}" /><input style="background-color: #D6CFDE; color: #5204A5;" type="submit" value="Add User $FORM{'userID'}" name="submit" />
	</td></tr></table></form></center></div>
DBMA
    end_HTML;
    exit;
}
############################################################## - sub exist_in_another_Group
sub exist_in_another_Group ($)
{
    my $userID = $FORM{'userID'} || '';
    &meta;
    &menu;
    print <<"DBMA";
	<div><center><table><tr><td colspan="6" ><h1 style="color:red">Wrong Group: $userID</h1><br />$errormessage<h3>&nbsp;</h3></td></tr></table></center></div>
DBMA
    end_HTML;
    exit;
}
############################################################## - sub protect_sys_accounts
sub protect_sys_accounts
{
    $PROTECTED_SYS_ACCOUNTS =
      $dbh->prepare(
        "SELECT userid, client_idnr FROM $dbmail_users_table WHERE user_idnr = '$userID'"
      );
    $PROTECTED_SYS_ACCOUNTS->execute();
    while (($username, $GroupID) = $PROTECTED_SYS_ACCOUNTS->fetchrow_array)
    {
        unless (($username eq "__public__") || ($username eq "anyone"))
        {
            if (   $username eq "LocalDeliveryAgent"
                || $GroupID == 0
                || $username eq "__\@!internal_delivery_user!\@__"
                || $username eq "_PROTECTED_")
            {
                $PROTECTED_SYS_ACCOUNTS->finish();

                &error(
                    '<span style="font-size:120%;color:red">You may not delete a system account.</span>'
                );
                $username =~ s/__\@\!internal_delivery_user\!\@__/_PROTECTED_/;
                $username =~ s/LocalDeliveryAgent/_PROTECTED_/;
                exit;
            }
        }
    }
}
############################################################## - sub protect_group_Zero
sub protect_group_Zero
{
    &meta;
    &menu;
    print <<"DBMA";
	<div><center><table><tr><td colspan="6" ><h1 style="color:red">Administrative limits exceeded.</h1><br />$errormessage<h3>&nbsp;</h3></td></tr></table></center></div>
DBMA
    end_HTML;
    exit;
}
############################################################## - sub mymailform
sub mymailform
{
    &defaults;
    &meta;
    if ($FORM{'mailto'})
    {
        $mymessage =
          "	<b>Go back to account window for <a title=\"Open an account window for $mailto\" href=\"$mythisscript?$mailto\">$mailto</a></b\n";
    }
    print <<"DBMA";
<title>DBMA - DBMail Administrator Sending Email Message</title>
<script type="text/JavaScript">
	<!-- //Copyright 1993-2008 Mike O'Brien Mouse House Creative Technologies
    					function verify() {
    	var subject = document.mail1.subject.value;
    	var mailto = document.mail1.mailto.value;
    	var mailfrom = document.mail1.mailfrom.value;
    	var message = document.mail1.message.value;
    	if (subject.length < 2)
    	alert('Your message should have a subject.');
    	else if (mailfrom.length < 2)
    	alert('To who? A username is fine if your MTA will pass it to DBMail. A full address is better.');
    	else if (mailfrom.length < 3)
    	alert('Who is the message from?');	
    	else if (message.length < 2)
    	alert('Your message is blank. If you wanted that, just enter three characters to avoid this nag.');	
    	else	document.mail1.submit();
    	}
// -->
</script>
</head><body>  
	<div align="center"><form name="mail1" method="post" action="$mythisscript"><center><table>
	<tr><td class="c1" style="width:738px" colspan="2" >Location of the MTA for your DBMail is configured as <b> $SMTP_ServerName </b>. Is that correct?</td></tr>
	<tr><td colspan="2" style="width:738px"><b><a href="$mythisscript">DBMail Administrator (DBMA)</a></b></td></tr>
	<tr><td class="c1" style="width:100%" align="right" colspan="2"><small>NOTE: A 'mail to' username alone is fine if your MTA will pass it to DBMail. Otherwise please enter a domain name.</small></td></tr>
	<tr><td colspan="3" style="width:100%">$mymessage</td></tr>
	<tr><td style="width:100" align="right">Mail to:<input type="hidden" value="28" name="RQT" /> </td><td style="width:600px;text-align:left" align="left">
	<input type="text" $mouseover $changecase size="45" name="mailto" value="$mailto" /></td></tr>
	<tr><td width="100px" align="right">Mail from:</td><td style="width:600px;text-align:left" align="left">
	<input type="text" $mouseover $changecase size="45" name="mailfrom" value ="$mailfrom" /></td></tr>
	<tr><td style="width:100" align="right">Subject:</td><td style="width:600;text-align:left" align="left">
	<input type="text" $mouseover size="45" name="subject" value="$subject" /></td></tr>
	<tr><td style="width:100px" align="right">Message:</td><td style="width:100px;text-align:left"><textarea class="list" cols="60" rows="14" name="message">$message</textarea><a onmouseover="self.status='Sending out an email';return true" onmouseout="self.status='Typing and checking an email';return true" href="javascript:verify();">
	<img alt="Send" border="0" src="images/dbma_send.jpg" width="44px" height="23px" /></a></td></tr>
	<tr><td colspan="2"><small>You can edit this message in any manner you wish.<br />Caution: Check that you are not sending an unusable encrypted password in this message.<br />Do you have an alternate 'mail-to' address for this user? Important if you have changed a password.</small></td></tr></table></center></form></div>
DBMA
    end_HTML;
    exit;
}
############################################################## - sub send_mail
sub send_mail
{
    use Net::SMTP;
    &defaults;
    $smtp = Net::SMTP->new($SMTP_ServerName);
    die "Couldn't connect to server" unless $smtp;
    $smtp->mail($mailfrom);
    $smtp->to($mailto);
    $smtp->data();
    $smtp->datasend("To: $mailto\n");
    $smtp->datasend("From: $mailfrom\n");
    $smtp->datasend("Subject: $subject\n");
    $smtp->datasend("\n");
    $smtp->datasend("$onlytime - $version\n\n$message\n");
    $smtp->dataend();
    $smtp->quit();
    &meta;
    print <<"DBMA";
<title>DBMail Administrator (DBMA) Sending Email Message </title>
<script type="text/JavaScript">
<!-- //Copyright 1993-2008 Mike O'Brien
    					function verify() {
    	var subject = document.mail1.subject.value;
    	var mailto = document.mail1.mailto.value;
    	var mailfrom = document.mail1.mailfrom.value;
    	var message = document.mail1.message.value;
	if (subject.length < 2)
    	alert('Your message should have a subject.');
    	else if (mailfrom.length < 2)
    	alert('To who? A username is fine if your MTA will pass it to DBMail. A full address is better.');
    	else if (mailfrom.length < 3)
    	alert('Who is the message from?');	
    	else if (message.length < 2)
    	alert('Your message is blank. If you wanted that, just enter three characters to avoid this nag.');	
    	else	document.mail1.submit();
    	}
// -->
</script></head>
	<body><div align="center"><form name="mail1" method="post" action="$mythisscript"><center>
	<table border="0" style="font-family: Trebuchet MS,arial,sans-serif; font-size: 12pt; text-align: Center; margin-left: 5px" cellspacing="0" cellpadding="0" width="738px"><tr><td class="c1" style="width:738px" colspan="2" >Message Sent</td></tr>
	<tr><td class="c1" style="text-align: left;" colspan="2" width="738px"><a title="Go Back to DBMA" href="$mythisscript"><h4>Back to DBMail Administrator (DBMA)</h4></a></td></tr>
	<tr><td style="text-align: left;" colspan="2" width="738px"> <span style="color:#008000;font-weight:bold">OK Your Mail to <a title="Open an account window for $mailto" href="$mythisscript?$mailto">$mailto</a> was sent</span></td></tr>
	<tr><td style="text-align: left" colspan="2" width="738px"><br />$date</td></tr>
	<tr><td style="text-align: left" colspan="2" width="738px"><b>Send Another Email | Go to account window for <a title="Open an account window for $mailto" href="$mythisscript?$mailto">$mailto</a></b></td></tr>
	<tr><td width="100px" align="right">Mail to:</td><td width="600px" style="text-align:left" align="left">
	<input type="text" $mouseover $changecase name="mailto" size="45" /></td></tr>
	<tr><td width="100px" align="right">Mail from:</td><td width="600px" style="text-align:left" align="left">
	<input type="text" $mouseover $changecase name="mailfrom" size="45" value="$mailfrom" /></td></tr>
	<tr><td width="100px" align="right">Subject:</td><td width="600px" style="text-align:left" align="left">
	<input type="text" $mouseover name="subject" size="45" value="$subject" /></td></tr>
	<tr><td width="100px" align="right" valign="top">Message:</td><td width="600px" style="text-align:left" align="left"><textarea rows="4" name="message" cols="44">$message</textarea><a onmouseover="self.status='Sending out an email';return true" onmouseout="self.status='Typing and checking an email';return true" href="javascript:verify();">
	<img alt="Send" border="0" src="images/dbma_send.jpg" width="44" height="23" /></td></tr></table></center></form></div>
DBMA
    end_HTML;
    exit;
}
############################################################## - sub add_user_form_sql RQT3
sub add_user_form_sql
{
    $password = "";
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
        if ($CFP eq "1")
        {
            $password .= $char;
            $onoffplain = "checked=\"checked\"";
        }
    }
    if (($CFP eq "0") && ($DBMAencrypt =~ /md5sum/))
    {
        $onoffmd5sum = "checked=\"checked\"";
        $encrypttype = "md5sum";
    }
    elsif (($CFP eq "0") && ($DBMAencrypt =~ /crypt/))
    {
        $onoffcrypt  = "checked=\"checked\"";
        $encrypttype = "crypt";
    }
    elsif (($CFP eq "0") && ($DBMAencrypt =~ /md5hash/))
    {
        $onoffhash   = "checked=\"checked\"";
        $encrypttype = "md5";
    }
    elsif ($DBMAencrypt =~ /plain/)
    {
        $onoffplain  = "checked=\"checked\"";
        $encrypttype = " ";
    }
    else
    {
        $onoffplain  = "checked=\"checked\"";
        $encrypttype = " ";
    }
    $| = 1;
    if ($create_first_alias eq "1")
    {
        $firstalias = "	First alias is (above name)\@$defaultdomain\n";
    }
    else
    {
        $firstalias =
          "	<input type=\"text\" onmouseover=\"this.className=\'front\';\" onmouseout=\"this.className=\'back\';\" name=\"newalias\" size=\"40\" \/>";
    }
    $message =
      "Note:<small>DBMA will automatically encrypt ('md5sum', 'md5', 'crypt') passwords.</small>";
    &meta;
    &menu;
    if (($create_first_alias eq "1") && ($RESTRICTGroupID =~ m/[1-9]/i))
    {
        $GroupID = $RESTRICTGroupID;
        print <<"DBMA";
	<div><center><form action="$mythisscript" method="post"><center><table class="c5" cellspacing="0" cellpadding="0" width="738px" border="0">
	<tr><td colspan="3"><h1>DBMA: Create (Add) User</h1></td></tr>
	<tr><td class="c2 c2">User Name</td><td class="c2 c2"><input type="hidden" name="RQT" value="1" /><input type="text" $mouseover $changecase name="username" value="" size="20" /></td>
	<td class="c2 c2" rowspan="3">$message</td></tr>
	<tr><td class="c2 c2">Password</td><td class="c2 c2"><input name="password" size="20" value="$password" type="text" $mouseover/><input type="hidden" name="required" value="GroupID,password,username,mailboxsize" /></td></tr>
	<tr><td class="c2 c2">Client (Group) ID</td><td class="c2 c2"><input size="4" value="$RESTRICTGroupID" name="GroupID" type="hidden" />$RESTRICTGroupID</td></tr>
	<tr><td class="c2 c2">Encryption Type</td>
	<td class="c2" colspan="2"><input type="radio" value="md5sum" name="encrypttype" $onoffmd5sum />md5sum<input type="radio" name="encrypttype" $onoffplain />Plain<input type="radio" $onoffcrypt value="crypt" name="encrypttype" />crypt<input type="radio" value="md5" name="encrypttype" $onoffhash />md5</td></tr>
	<tr><td class="c2 c2">MailBox Size</td><td class="c2 c2" colspan="2"><input type="text" size="9" $mouseover name="mailboxsize" value="$defaultmailboxsize"  /></td></tr>
	<tr><td class="c2 c2">Email Address</td><td class="c2 c2" colspan="2">
DBMA
    }
    elsif ($RESTRICTGroupID =~ m/[1-9]/i)
    {
        $GroupID = $RESTRICTGroupID;
        print <<"DBMA";
	<div><center><form action="$mythisscript" method="post"><center><table class="c5" cellspacing="0" cellpadding="0" width="738px" border="0">
	<tr><td colspan="3"><h1>DBMA: Create (Add) User</h1></td></tr>
	<tr><td class="c2 c2">User Name</td><td class="c2 c2"><input type="hidden" name="RQT" value="1" /><input type="text" $mouseover $changecase name="username" value="$username" size="20" /></td>
	<td class="c2 c2" rowspan="3">$message</td></tr>
	<tr><td class="c2 c2">Password</td><td class="c2 c2"><input name="password" size="20" value="$password" type="text" $mouseover/><input type="hidden" name="required" value="GroupID,password,username,mailboxsize" /></td></tr>
	<tr><td class="c2 c2">Client (Group) ID</td><td class="c2 c2"><input size="4" value="$RESTRICTGroupID" name="GroupID" type="hidden" />$RESTRICTGroupID</td></tr>
	<tr><td class="c2 c2">Encryption Type</td>
	<td class="c2" colspan="2"><input type="radio" value="md5sum" name="encrypttype" $onoffmd5sum />md5sum<input type="radio" name="encrypttype" $onoffplain />Plain<input type="radio" $onoffcrypt value="crypt" name="encrypttype" />crypt<input type="radio" value="md5" name="encrypttype" $onoffhash />md5</td></tr>
	<tr><td class="c2 c2">MailBox Size</td><td class="c2 c2" colspan="2"><input type="text" $mouseover size="9" name="mailboxsize" value="$defaultmailboxsize"  /></td></tr>
	<tr><td class="c2 c2">Email Address</td><td class="c2 c2" colspan="2">
DBMA
    }
    elsif ($create_first_alias eq "1")
    {
        print <<"DBMA";
	<div><center><form action="$mythisscript" method="post"><center><table class="c5" cellspacing="0" cellpadding="0" width="738px" border="0">
	<tr><td colspan="3"><h1>DBMA: Create (Add) User</h1></td></tr>
	<tr><td class="c2 c2">User Name</td><td class="c2 c2"><input type="hidden" name="RQT" value="1" /><input type="text" $mouseover $changecase name="username" value="" size="20" /></td>
	<td class="c2 c2" rowspan="3">$message</td></tr>
	<tr><td class="c2 c2">Password</td><td class="c2 c2"><input name="password" size="20" value="$password" type="text" $mouseover/><input type="hidden" name="required" value="GroupID,password,username,mailboxsize" /></td></tr>
	<tr><td class="c2 c2">Client (Group) ID</td><td class="c2 c2"><input size="4" value="$GroupID" name="GroupID" type="text" $mouseover /></td></tr>
	<tr><td class="c2 c2">Encryption Type</td>
	<td class="c2" colspan="2"><input type="radio" value="md5sum" name="encrypttype" $onoffmd5sum />md5sum<input type="radio" name="encrypttype" $onoffplain />Plain<input type="radio" $onoffcrypt value="crypt" name="encrypttype" />crypt<input type="radio" value="md5" name="encrypttype" $onoffhash />md5</td></tr>
	<tr><td class="c2 c2">MailBox Size</td><td class="c2 c2" colspan="2"><input type="text" size="9" $mouseover name="mailboxsize" value="$defaultmailboxsize"  /></td></tr>
	<tr><td class="c2 c2">Email Address</td><td class="c2 c2" colspan="2">
DBMA
    }
    else
    {
        &defaults;
        print <<"DBMA";
	<div><center><form action="$mythisscript" method="post"><center><table class="c5" cellspacing="0" cellpadding="0" width="738px" border="0">
	<tr><td colspan="3"><h1>DBMA: Create (Add) User</h1></td></tr>
	<tr><td class="c2 c2">User Name</td><td class="c2 c2"><input type="hidden" name="RQT" value="1" /><input type="text" $mouseover $changecase name="username" value="$username" size="20" /></td>
	<td class="c2 c2" rowspan="3">$message</td></tr>
	<tr><td class="c2 c2">Password</td><td class="c2 c2"><input name="password" size="20" value="$password" type="text" $mouseover/><input type="hidden" name="required" value="GroupID,password,username,mailboxsize" /></td></tr>
	<tr><td class="c2 c2">Client (Group) ID</td><td class="c2 c2"><input size="4" value="$defaultGroup_ID" name="GroupID" type="text" $mouseover /></td></tr>
	<tr><td class="c2 c2">Encryption Type</td>
	<td class="c2" colspan="2"><input type="radio" value="md5sum" name="encrypttype" $onoffmd5sum />md5sum<input type="radio" name="encrypttype" $onoffplain />Plain<input type="radio" $onoffcrypt value="crypt" name="encrypttype" />crypt<input type="radio" value="md5" name="encrypttype" $onoffhash />md5</td></tr>
	<tr><td class="c2 c2">MailBox Size</td><td class="c2 c2" colspan="2"><input type="text" $mouseover size="9" name="mailboxsize" value="$defaultmailboxsize"  /></td></tr>
	<tr><td class="c2 c2">Email Address</td><td class="c2 c2" colspan="2">
DBMA
    }
    print $firstalias;
    print <<"DBMA";
    	
	<input title="Create" onmouseover="this.className='clear';" onmouseout="this.className='letsgo';" class="letsgo"  type="submit" value="Add New User" name="submit" /></td></tr>
	<tr><td colspan="3"><hr style="background-color:#D6CFDE; color:#D6CFDE;height:20px" /></td></tr>
DBMA
    if ($RESTRICTGroupID eq "any")
    {
        print <<"DBMA";
	<tr><td style="font-size:10px"colspan="3">To create open aliases for LAN accounts, like '\@domain.int' you must Force Bypass RFC-Compliant Alias Check <input onmouseover="this.className='caution';self.status='This will force bypass alias checking.';return true" onmouseout="this.className='c11';self.status='DBMA';return true" style="height:20px" type="radio" value="1" name="bypass" />on<input type="radio" value="0" name="bypass" />off
<br />DBMA will display these with Group info in "My Groups" panel as '* \@domain'. <span style="color:black">Note: Possible risks. Know what you are doing.</span></td></tr>
	<tr><td colspan="4"><hr style="background-color:#D6CFDE; color:#D6CFDE;height:1px" /></td></tr>
DBMA
    }
    print <<"DBMA";
	</table></center></form></center></div>
DBMA
    if (($stats_on eq "1") && ($RESTRICTGroupID eq "any"))
    {
        print <<"DBMA";
<div><center><table><tr><td>
DBMA
        &user_form_helper;
        print <<"DBMA";
	</td><td><small><b>System Domains: </b>To the left is a list of all the domains in this system. In the 'Configurations' windows the Administrator may have asked DBMA to auto-create the alias above using a preset default domain. In the alternative you can cut and paste from here to reduce key presses.</small></td></tr></table></center></div>
DBMA
        end_HTML;
    }
    else
    {
        end_HTML;
    }
    exit;
}

#                                               ############# - sub user_form_helper
sub user_form_helper
{
    print "	<textarea class=\"list\" rows=\"5\" cols=\"40\">";
    open(DOMAINDATA, "$DBMA_DATA_MTA_TEMP");
    @data = <DOMAINDATA>;
    foreach $add_user_form_helper (sort @data)
    {
        print $add_user_form_helper;
    }
    undef $encrypttype;
    close(DOMAINDATA);
    print "</textarea>";
}
############################################################## - sub create_alias_form_sql RQT7
sub create_alias_form_sql
{
    &meta;
    &menu;
    $RQT = "";
    &defaults;
    my $displayusername = $FORM{'displayusername'} || $username || "";
    print <<"DBMA";
	<div><center><form action="$mythisscript" method="post">
	<table class="c5" cellspacing="0" cellpadding="0" width="738px" border="0">
	<tr><td colspan="3"><h1>DBMA: Insert (Add) Single Alias</h1></td></tr>
	<tr><td class="c2 c2">User Number or Name</td><td class="c2 c2"><input type="hidden" name="RQT" value="6" />
	<input type="hidden" name="required" value="userID,newalias" />
	<input name="userID" value="$userID" size="20" type="text" $mouseover $changecase />$displayusername</td></tr>
	<tr><td class="c2 c2">Alias</td><td class="c2 c2"><input type="text" $mouseover $changecase name="newalias" size="40" /></td>
	<td class="c2 c2"><input class="c7" type="submit" value="Add Alias" name="submit" onmouseover="this.className='letsgo';" onmouseout="this.className='clear';" /></td></tr></table></form></center></div>
DBMA
    if ($RESTRICTGroupID eq "any")
    {
        print <<"DBMA";
	<div><center><form action="$mythisscript" method="post">
	<table class="c5" cellspacing="0" cellpadding="0" width="738px" border="0">
	<tr><td colspan="3"><h1><br />DBMA: Add Domain Alias for Each User in an Entire Group</h1></td></tr>
	<tr><td colspan="3">Note: This tool assumes you are adding a domain on which you wish all users in a group to 
	receive mail. If any user already has an alias for the domain you enter, a new alias will be created and they will
	receive an additional copy of each message addressed to that alias.
	A listing of group aliases will appear after this function completes.
	Check for duplicates and delete those you do not want.<p><br /></p></td></tr>
	<tr><td class="c2 c2">Group Number</td><td class="c2 c2"><input type="hidden" name="RQT" value="6a" />
	<input type="hidden" name="required" value="newalias,GroupID" />
	<input name="GroupID" value="" size="4" type="text" $mouseover $changecase /></td></tr>
	<tr><td class="c2 c2">Domain</td><td class="c2 c2"><input type="text" $mouseover $changecase name="newalias" size="40" /></td>
	<td class="c2 c2"><input class="c7" type="submit" value="Add Alias to Group" name="submit" onmouseover="this.className='letsgo';" onmouseout="this.className='clear';" onclick="return confirm('Give every user in this Group a new alias? : Are you sure?')" /></td></tr>
	<tr><td colspan="3"><hr style="background-color:#D6CFDE; color:#D6CFDE;height:20px" /></td></tr></table></form></center></div>
DBMA
    }
    end_HTML;
    exit;
}
############################################################## - sub add_forward_form_sql RQT14
sub add_forward_form_sql
{

    my $alias_idnr = $FORM{'alias_idnr'} || "";
    $deliver_to = $FORM{'deliver_to'} || "";
    my $userID = $FORM{'userID'} || "";
    $deliver_from = $FORM{'deliver_from'} || "";
    @output = split('@', $deliver_from);

    $username = $FORM{'username'} || $output[0];
    &meta;
    &menu;
    print <<"DBMA";
	<div><form action="$mythisscript" method="post"><center>
	<table class="c5" cellspacing="0" cellpadding="0" width="738" border="0">
	<tbody><tr><td colspan="3" style="width:728px"><h1>DBMA: Directing E-Mail Delivery</h1></td></tr>
	<tr><td style="width:113px" colspan="2"><h3>Forward From:</h3></td><td style="width:613px"><input type="hidden" name="RQT" value="13a" /><input type="hidden" name="required" value="deliver_to" /><input type="hidden" name="GroupID" value="$GroupID" /><input type="hidden" name="alias_idnr" value="$alias_idnr" />
	<input name="deliver_from" value="$deliver_from" type="text" $mouseover $changecase size="40" />&nbsp;</td></tr>
	<tr><td style="width:57px"><h3>To:</h3></td><td style="width:56px"></td><td style=" width:613px" colspan="2"><input name="deliver_to" value="$deliver_to" size="40" type="text" $mouseover $changecase /></td></tr>
	<tr><td colspan="3" style="width:728px">The "From" email address can be forwarded or converted to an ordinary alias for local delivery. Enter an email address, a User ID number or a user name as a "To:" destination.
	Press "Verify" and DBMA will check if the "Forward From" exists on the system as well as checking local
	delivery availablity for User Number or User Name in the "To:" box.</td></tr>
	<tr><td style="width:113px" colspan="2"><td style="width:613px"><input class="c7" type="submit" value="Verify" onmouseover="this.className='letsgo';" onmouseout="this.className='clear';" /></td></tr>
	<tr><td colspan="3" style="width:728px"><hr style="background-color:#D6CFDE; color:#D6CFDE;height:20px" /></td></tr></form></body></html>
DBMA
    exit;

}
############################################################## - sub edit_forward_form_sql RQT13a
sub edit_forward_form_sql
{
    &defaults;
    my $alias_idnr    = $FORM{'alias_idnr'};
    my $alias_GroupID = '';
    my $userID        = $FORM{'userID'} || $userID;
    my $username      = $FORM{'username'} || "";
    $deliver_to = $FORM{'deliver_to'} || "";
    my $deliver_from        = $FORM{'deliver_from'} || $deliver_from || "";
    my @is_it_new_output1   = &split($deliver_from);
    my $is_it_new_username1 = $is_it_new_output1[0];
    &filt($deliver_from);
    &filt($deliver_to);

    if ($deliver_from eq "$deliver_to")
    {
        &error(
            'LOOP!<br />Both "From:" and "To:" email addresses are the same or blank. If you wish to redirect the alias to its user name, simply type the destination user name or number as a "To:" destination.'
        );
    }
    &checkrequired;
    unless (($deliver_from) && ($deliver_to))
    {
        &add_forward_form_sql;
    }
    &check_if_RFC_alias($deliver_to) if $deliver_to =~ m/\@/i;
    if ($deliver_from)
    {
        &check_if_RFC_alias($deliver_from);
        my $sth =
          $dbh->prepare(
            "SELECT alias_idnr, alias, deliver_to, client_idnr from $dbmail_aliases_table WHERE LOWER(alias) = LOWER('$deliver_from')"
          );
        unless ($sth->execute()) { print $DBI::errstr; }
        unless (($alias_idnr, $alias, $deliver_from, $alias_GroupID) =
                $sth->fetchrow_array())
        {
            push(@MESSAGE, "This alias does not currently exist.");
            &DBMA_Advisor(
                'No such alias exists or you have a misspelled mail address. Please enter a valid, existing email address to forward. Or perhaps you intended to create an alias. In that case go to the User Account WIndow and select "MODIFY..."',
                @ERROR
            );
        }
        $sth->finish() if ($sth);
        &meta;
        &menu;
        $alias_GroupID = '';
        $sth           = $dbh->prepare("
SELECT alias_idnr, alias, client_idnr
FROM $dbmail_aliases_table
WHERE $dbmail_aliases_table.alias_idnr = '$alias_idnr'");
        $sth->execute() if ($alias_idnr);
        while (($alias_idnr, $deliver_from, $alias_GroupID) =
               $sth->fetchrow_array)
        {

            print <<"DBMA";
	<div><form action="$mythisscript" method="post"><center>
	<table class="c5" cellspacing="0" cellpadding="0" width="738" border="0"><tbody><tr><td colspan="4" style="width:728px"><h1>DBMA: Confirm <b>$deliver_from</b> Mail Forward</h1></td></tr>
        <tr><td colspan="4">Press "Commit" and $deliver_from\'s mail will be delivered to the new destination below instead of its current delivery destination.<p><br /></p></td></tr>
	<tr><td style="width:126"><h3>From</h3> </td><td title="alias_idnr: $alias_idnr" style="width:226"><h3>$deliver_from  <small>(Group: $alias_GroupID Alias id: $alias_idnr)</small> </h3></td><td></td><td></td></tr>
DBMA

            if ($deliver_to =~ m/\@/i)
            {
                print <<"DBMA";
	<tr><td style="width:126"><h3>To Address:</h3></td><td style="width:226"><h3>$deliver_to</h3></td>
DBMA
                print
                  "	<tr><td colspan=\"4\">If this is not what you intended you can go <a title=\"return to form\" href=\"javascript:history.go(-1)\" onmouseover=\"self.status=\'Back to form\';return true\" onmouseout=\"self.status=\'DBMA\';return true\" /><b>Back</b></a> and edit your addresses.</td></tr>\n";
                print <<"DBMA";
	<td style="width:226"></td><td style="width:146"></td></tr>
	<tr><td style="width:126"><td style="width:226"></td><td style="width:226"></td><td style="width:146">
	<input class="c7" type="submit" value="Commit" onmouseover="this.className='letsgo';" onmouseout="this.className='clear';" />
	<input type="hidden" value="$deliver_from" name="deliver_from">
	<input type="hidden" value="$deliver_to" name="deliver_to">
	<input type="hidden" value="$alias_GroupID" name="GroupID">
	<input type="hidden" value="$alias_idnr" name="alias_idnr">
	<input type="hidden" name="RQT" value="13b" />
	</td></tr>
	<tr><td colspan="4" style="width:728px"><hr style="background-color:#D6CFDE; color:#D6CFDE;height:20px" /></td></tr></tbody></table></center></form></div></body></html>
DBMA
            }

            elsif ($FORM{'deliver_to'})
            {
                my $deliver_to = $FORM{'deliver_to'};

                $sth =
                  $dbh->prepare(
                    "SELECT userid, user_idnr FROM $dbmail_users_table WHERE LOWER(userid)=LOWER('$deliver_to') OR user_idnr='$deliver_to' LIMIT 1"
                  );

                unless ($sth->execute()) { print $DBI::errstr; }
                if (($username, $userID) = $sth->fetchrow_array)
                {
                    if ($deliver_to eq $username)
                    {
                        print
                          "	<tr><td style=\"width:126\"><h3>To</h3> </td><td style=\"width:226\"><h3>$username</h3></td>\n";
                        print
                          "	<tr><td colspan=\"4\"><p><br /><span class=\"nowarn\">You used a user name instead of a \"Deliver To\" email address.</span></td></tr>\n";
                        print
                          "	<tr><td colspan=\"4\"><span class=\"nowarn\">If you continue, this \'forward\' will become an \'alias\' of user: <a href=\"$mythisscript\?$username\">$username</a></p></span></td></tr>\n";
                        print
                          "	<tr><td colspan=\"4\">If this is not what you intended you can go <a title=\"return to form\" href=\"javascript:history.go(-1)\" onmouseover=\"self.status=\'Back to form\';return true\" onmouseout=\"self.status=\'DBMA\';return true\" /><b>Back</b></a> and edit your addresses.</td></tr>\n";

                        print <<"DBMA";
	<td style="width:226"></td><td style="width:146"></td></tr>
	<tr><td style="width:126"><td style="width:226"></td><td style="width:226"></td><td style="width:146">
	<input class="c7" type="submit" value="Commit" onmouseover="this.className='letsgo';" onmouseout="this.className='clear';" />
	<input type="hidden" value="$deliver_from" name="deliver_from">
	<input type="hidden" value="$userID" name="deliver_to">
	<input type="hidden" value="$alias_GroupID" name="GroupID">
	<input type="hidden" value="$alias_idnr" name="alias_idnr">
	<input type="hidden" name="RQT" value="13b" />
	</td></tr>
	<tr><td colspan="4" style="width:728px"><hr style="background-color:#D6CFDE; color:#D6CFDE;height:20px" /></td></tr></tbody></table></center></form></div></body></html>
DBMA

                    }
                    elsif ($deliver_to eq $userID)
                    {
                        print
                          "	<tr><td style=\"width:126\"><h3>To</h3> </td><td style=\"width:226\"><h3>$username</h3></td>\n";
                        print
                          "	<tr><td colspan=\"4\"><p><br /><span class=\"nowarn\">You used a user number instead of a \"Deliver To\" email address.</span></td></tr>\n";
                        print
                          "	<tr><td colspan=\"4\"><span class=\"nowarn\">If you continue, this \'forward\' will become an \'alias\' of user: <a href=\"$mythisscript\?$username\">$username</a></p></span></td></tr>\n";
                        print
                          "	<tr><td colspan=\"4\">If this is not what you intended you can go <a title=\"return to form\" href=\"javascript:history.go(-1)\" onmouseover=\"self.status=\'Back to form\';return true\" onmouseout=\"self.status=\'DBMA\';return true\" /><b>Back</b></a> and edit your addresses.</td></tr>\n";
                        print <<"DBMA";
	<td style="width:226"></td><td style="width:146"></td></tr>
	<tr><td style="width:126"><td style="width:226"></td><td style="width:226"></td><td style="width:146">
	<input class="c7" type="submit" value="Commit" onmouseover="this.className='letsgo';" onmouseout="this.className='clear';" />
	<input type="hidden" value="$deliver_from" name="deliver_from">
	<input type="hidden" value="$userID" name="deliver_to">
	<input type="hidden" value="$alias_GroupID" name="GroupID">
	<input type="hidden" value="$alias_idnr" name="alias_idnr">
	<input type="hidden" name="RQT" value="13b" />
	</td></tr>
	<tr><td colspan="4" style="width:728px"><hr style="background-color:#D6CFDE; color:#D6CFDE;height:20px" /></td></tr></tbody></table></center></form></div></body></html>
DBMA

                    }
                    $sth->finish if ($sth);
                }

                elsif ($deliver_to)
                {
                    $sth =
                      $dbh->prepare(
                        "SELECT userid, user_idnr FROM $dbmail_users_table WHERE LOWER(userid)=LOWER('$is_it_new_username1') LIMIT 1"
                      );

                    unless ($sth->execute())
                    {
                        $errormessage = "$DBI::errstr";
                        &DBMA_ConnectStatus;
                    }
                    if (($username, $userID) = $sth->fetchrow_array)
                    {
                        if ($is_it_new_username1 eq $username)
                        {
                            print
                              "	<tr><td style=\"width:126\"><h3>To INBOX of</h3> </td><td style=\"width:226\"><h3>$username</h3></td>\n";
                            print
                              "	<tr><td colspan=\"4\"><p><br /><span class=\"nowarn\"><p>You did not enter a \"Deliver To\" email address.</span></td></tr>\n";
                            print
                              "	<tr><td colspan=\"4\">If you continue, this \'forward\' will now revert to being an \'alias\' of user: <b>$username</b> and mail addressed to $deliver_from will be stored in $username\'s INBOX</p></td></tr>\n";
                            print
                              "	<tr><td colspan=\"4\">If this is not what you intended you can go <a title=\"return to form\" href=\"javascript:history.go(-1)\" onmouseover=\"self.status=\'Back to form\';return true\" onmouseout=\"self.status=\'DBMA\';return true\" />Back</a> and edit your addresses.</td></tr>\n";

                            print <<"DBMA";
	<td style="width:226"></td><td style="width:146"></td></tr>
	<tr><td style="width:126"><td style="width:226"></td><td style="width:226"></td><td style="width:146">
	<input class="c7" type="submit" value="Commit" onmouseover="this.className='letsgo';" onmouseout="this.className='clear';" />
	<input type="hidden" value="$deliver_from" name="deliver_from">
	<input type="hidden" value="$userID" name="deliver_to">
	<input type="hidden" value="$alias_GroupID" name="GroupID">
	<input type="hidden" value="$alias_idnr" name="alias_idnr">
	<input type="hidden" name="RQT" value="13b" />
	</td></tr>
	<tr><td colspan="4" style="width:728px"><hr style="background-color:#D6CFDE; color:#D6CFDE;height:20px" /></td></tr></tbody></table></center></form></div></body></html>
DBMA
                        }

                    }

                }

            }
        }
        $sth->finish() if ($sth);
        @is_it_new_output1   = "";
        $is_it_new_username1 = "";
        undef $deliver_to;
        undef $alias_idnr;
        undef $deliver_from;

        exit;
    }
    else
    {
        &add_forward_form_sql;
    }
}
############################################################## - sub Forwards_SQL RQT13 and RQT13b
sub Forwards_SQL ($)
{
    my $deliver_to   = $FORM{'deliver_to'};
    my $deliver_from = $FORM{'deliver_from'};
    my $alias_idnr   = $FORM{'alias_idnr'};
    if (   ($RESTRICTGroupID =~ m/[0-9]/i)
        && ($RESTRICTGroupID != $FORM{'GroupID'}))
    {
        $errormessage =
          "$deliver_from belongs to a user in another Group.<br />Please contact your system administrator.";
        &exist_in_another_Group($deliver_from);
    }
    &check_if_RFC_alias($deliver_to) if $deliver_to =~ m/\@/i;
    &check_if_RFC_alias($deliver_from);

    # if edit requested do UPDATE
    if ($alias_idnr > 0)
    {

        # We would like to pass the GroupID to the database but there are
        # some circumstances as in an alias 'edit' where we do not know the GroupID.
        # This could be ignored for MySQL but not PostgreSQL.
        # A no-value integer is actually bad SQL and later pgsql versions will not forgive it.
        # The following 5 lines avoid the problem which popped up (rarely) in DBMA V2.3.

        my $addgroup = ", client_idnr=\'$GroupID\'" if ($GroupID);

        $sql =
          "UPDATE $dbmail_aliases_table SET deliver_to = '$deliver_to'$addgroup WHERE alias_idnr = '$alias_idnr' AND alias = '$deliver_from'";
        unless ($sth = $dbh->prepare($sql))
        {
            push(@ERROR, $sql);
            &error('Prepare failed for', @ERROR);
        }
        unless ($sth->execute())
        {
            push(@ERROR, $DBI::errstr);
            &error('Execute failed', @ERROR);
        }
        unless ($dbh->commit)
        {
            $errormessage = "
	ErrorID: $version.err0.77 <br />$DBI::errstr <br />Error: commit FAIL for FORWARD update";
            &DBMA_ConnectStatus;
        }
        $sth->finish;
        &List_all_Forwards;
        exit;
    }
    else
    {
        $addnewaliases =
          "INSERT INTO $dbmail_aliases_table (alias, deliver_to, client_idnr) VALUES ('$deliver_from', '$deliver_to', '$GroupID')";
        unless ($sth = $dbh->prepare($addnewaliases))
        {
            $errormessage =
              "Error: Unable to Execute Addition of forwards for $deliver_from $sth->errstr";
            &DBMA_ConnectStatus;
        }
        unless ($sth->execute)
        {
            $errormessage =
              "Error: Unable to Execute Addition of forwards for $deliver_from";
            &DBMA_ConnectStatus;
        }
        unless ($dbh->commit)
        {
            $errormessage =
              "$DBI::errstr <br />Error: commit FAIL for add $deliver_from forward";
            &DBMA_ConnectStatus;
        }
        &List_all_Forwards;
    }
}
############################################################## - sub add_notify_form_sql RQT16
sub add_notify_form_sql ()
{
    $notify_address = $notify_address || "";
    my $displayusername = $FORM{'displayusername'} || "";
    my $userID = $userID || $FORM{'userID'} || "";
    &meta;
    &menu;
    print <<"DBMA";
	<div><form action="$mythisscript" method="post"><center>
	<table class="c5" cellspacing="0" cellpadding="0" width="738px" border="0"><tr><td colspan="3"><h1>DBMA: Insert Auto Notify</h1></td></tr>
	<tr><td class="c2 c2">When UserID <small>(name or number)</small></td><td colspan="2">
	<input type="text" $mouseover $changecase
        name="userID" value="$userID" size="25" />$displayusername gets a message</td></tr>
	<tr><td class="c2 c2">Notify</td><td class="c2 c2"><input type="hidden" name="required" value="userID,notify_address" /><input type="hidden" name="RQT" value="15" /><input name="notify_address" value="$notify_address" size="40" type="text" $mouseover $changecase /></td>
	<td class="c2 c2"><input class="c7" type="submit" value="Insert AutoNotify" name="submit" onmouseover="this.className='front';" onmouseout="this.className='letsgo';" class="letsgo" /></td></tr>
	<tr><td colspan="3"><hr style="background-color:#D6CFDE; color:#D6CFDE;height:20px" /></td></tr></table></center></form></div>
DBMA
    end_HTML;
    exit;
}
############################################################## - sub delete_notify_form_sql
sub delete_notify_form_sql ($)
{
    $view_userID = $userID || $FORM{'userID'} || "";
    &meta;
    &menu;
    print <<"DBMA";
	<div><center><form action="$mythisscript" method="post"><table class="c5" cellspacing="0" cellpadding="0" width="738px" border="0">
	<tr><td colspan="3"><h1>DBMA: Delete Auto Notify</h1></td></tr>
	<tr><td class="c2 c2">User ID Name or Number</td><td class="c2 c2"><input type="hidden" name="RQT" value="17" /><input name="userID" value="$view_userID" size="20" type="text" $mouseover $changecase /></td><td class="c2 c2"><input class="c7" type="submit" value="Delete Auto Notification" name="submit" onclick="return confirm('DELETE Notification : Are you sure?')" /><input type="hidden" name="required" value="userID" /></td></tr>
	<tr><td colspan="3"><hr style="background-color:#D6CFDE; color:#D6CFDE;height:20px" /></td></tr></table></form></center></div>
DBMA
    end_HTML;
    exit;
}
############################################################## - sub delete_alias_form_sql
sub delete_alias_form_sql
{
    $view_userID = $userID || $FORM{'userID'} || "";
    &meta;
    &menu;
    print <<"DBMA";
	<body><div><center><form action="$mythisscript" method="post">
	<table class="c5" cellspacing="0" cellpadding="0" width="738px" border="0">
	<tbody>
	<tr><td class="c1" colspan="3"><h1>DBMA: Delete Single Alias or Forward</h1></td></tr>
	<tr><td class="c2 c2">Enter the full, exact alias.</td>
	<td class="c2 c2"><input type="hidden" name="RQT" value="9" /><input type="text" $mouseover $changecase name="alias" size="40" /></td><td class="c2 c2"><input onclick="return confirm('DELETE : Are you sure?')" type="submit" value="Delete" name="submit" onmouseover="this.className='clear';" onmouseout="this.className='letsgo';" class="letsgo" /></td></tr>
	<tr><td colspan="3"><br /><br /><b>Important:</b><br />The best method for deleting FORWARDS or ALIASES from the "Modify User Account Window".</td></tr></tbody></table></form></center></div><br /><br />
	<div><center><form action="$mythisscript" method="post"><table class="c5" cellspacing="0" cellpadding="0" width="738px" border="0"><tbody><tr><td class="c1" colspan="3">
	<h1>DBMA: Delete All of a User's Aliases</h1></td></tr>
	<tr><td class="c2 c2">Enter the User Name or ID.</td>
	<td class="c2 c2"><input type="text" $mouseover $changecase name="userID" value="$view_userID" size="4" /><input type="hidden" name="RQT" value="10" /></td>
	<td class="c2 c2"><input type="submit" onclick="return confirm('DELETE Every alias for this user: Are you sure?')" value="Delete All Aliases" name="submit" onmouseover="this.className='warn';" onmouseout="this.className='letsgo';" class="letsgo" title="Delete every alias for this user"/>
	</td></tr>
	<tr><td colspan="3"><br /><br /><b>Important:</b> By typing the User's ID number or Name above and
    	pressing "Delete All Aliases" you do a brute force deletion of every "Regular" alias assigned to that account. This does not include forwards if there are any for the named user.</td></tr>
	<tr><td colspan="4"><hr style="background-color:#D6CFDE; color:#D6CFDE;height:20px" /></td></tr></td></tr></tbody></table></form></center></div>
DBMA
    end_HTML;
    exit;
}
############################################################## - sub delete_user_form_sql RQT5
sub delete_user_form_sql
{
    if ($RESTRICTGroupID =~ m/[0-9]/i)
    {
        &meta;
        &menu;
        my $displayusername = $FORM{'displayusername'} || "";
        $view_userID = $userID || $FORM{'userID'} || "";
        print <<"DBMA";
	<div><center><form action="$mythisscript" method="post"><table class="c5" cellspacing="0" cellpadding="0" width="738px" border="0"><tr><td colspan="3"><h1>DBMA: Delete User</h1></td></tr>
	<tr><td>User ID Number or Name</td><td class="c2 c2"><input type="hidden" name="RQT" value="39" /><input type="text" $mouseover $changecase name="userID" value="$view_userID" size="20" />$displayusername</td>
	<td class="c2 c2"><input class="c7" onclick="return confirm('DELETE User : Are you sure?')" type="submit" value="Delete User $displayusername" name="submit" /></td></tr>
	<tr><td colspan="3"><hr style="background-color:#D6CFDE; color:#D6CFDE;height:20px" /></td></tr></table></form></center></div>
DBMA
        end_HTML;
        exit;
    }
    else
    {
        &meta;
        &menu;
        my $displayusername = $FORM{'displayusername'} || "";
        $view_userID = $userID  || $FORM{'userID'}  || "";
        $deletegroup = $GroupID || $FORM{'GroupID'} || "";
        print <<"DBMA";
	<div><center><form action="$mythisscript" method="post"><table class="c5" cellspacing="0" cellpadding="0" width="738px" border="0"><tr><td colspan="3"><h1>DBMA: Delete User</h1></td></tr>
	<tr><td>User ID Number or Name</td><td class="c2 c2"><input type="hidden" name="RQT" value="4" /><input type="text" onmouseover="this.className='front';self.status='Delete User';return true" onmouseout="this.className='back';self.status='DBMA';return true" name="userID" value="$view_userID" size="20" />$displayusername</td>
	<td class="c2 c2"><input class="c7" onmouseover="this.className='nowarn';" onmouseout="this.className='c7';" title="Delete User $displayusername - $view_userID " onclick="return confirm('DELETE User : Are you sure?')" type="submit" value="Delete User $displayusername" name="submit" /></td></tr>
	<tr><td colspan="3"><hr style="background-color:#D6CFDE; color:#D6CFDE;height:20px" /></td></tr></table></form></center></div>
	<div><center><form action="$mythisscript" method="post"><table class="c5" cellspacing="0" cellpadding="0" width="738px" border="0"><tr><td colspan="3"><h1>DBMA: Delete Entire Group of Users</h1></td></tr>
	<tr><td title="Delete Entire Group of users. Be careful.">Enter Group Number</td><td class="c2 c2"><input type="hidden" name="RQT" value="40" /><input type="text" onmouseover="this.className='ohoh';self.status='Delete Entire Group Of Users';return true" onmouseout="this.className='back';self.status='DBMA';return true" name="deletegroup" value="$deletegroup" size="20" /></td>
	<td class="c2 c2"><input title="Delete entire group." class="c7" onmouseover="this.className='warn';" onmouseout="this.className='c7';" onclick="return confirm('DELETE The Entire Group of Users? : Are you sure? This is permanent.')" type="submit" value="Delete Entire Group" name="submit" /></td></tr>
	<tr><td colspan="3"><hr style="background-color:#D6CFDE; color:#D6CFDE;height:20px" /></td></tr></table></form></center></div>
DBMA
        end_HTML;
        exit;
    }
}
############################################################## - sub stats
sub stats
{
    if ($stats_on eq "1")
    {
        print <<"DBMA";
    <div><center>
    <table width="738px" style="font-size:85%; width:738px;border-style:solid;border-color:#d6cfde" cellspacing="0" cellpadding="0">
    <tr><td style="width:200px"><small>My Mail System:</small><br/><span class="stats" style="font-size:80%;line-height:130%">Host:$sqlhost<br />$mysqldate<br />Database:$sqldb</span><br />
    <span class="stats" style="font-size:80%;line-height:130%">
DBMA
        my (
            $db,          $table,  $status_line, $strV,
            $str1,        $str2,   $str2a,       $str2b1,
            $str2b2,      $str2b,  $str2c,       $str2d,
            $str2e,       $str2e2, $str2f,       $str3,
            $table_count, $table_list
           );
        print "$sqltype ";
        $sth = $dbh->prepare("SELECT VERSION()");
        unless ($sth->execute())
        {
            $errormessage =
              "$DBI::errstr Failed on a configuration error.  Have you entered the correct DBMail version? -stats1";
        }
        while (($table) = $sth->fetchrow_array)
        {
            $strV .= "$table\n";
        }
        unless ($sqltype eq "pgsql") { print $strV if ($strV); }
        $sth->finish() if ($sth);
        print "	<br />\n";

        if ($sqltype =~ /mysql/)
        {
## -STATS:  InnoDB Free
            my ($line, @line);
            $sth =
              $dbh->prepare(
                   "SHOW TABLE STATUS LIKE '$dbmail_auto_notifications_table'");
            $sth->execute();
            if ((@line) = $sth->fetchrow_array)
            {
                foreach $line (@line)
                {
                    $InnoDB_Free = $line
                      if (($line) && ($line =~ m/InnoDB free/i));
                }
                $InnoDB = 1;
            }
            $InnoDB_Free =~ s/[^kB]*$//g;
            print $InnoDB_Free;
            $sth->finish() if ($sth);
            undef $line;
        }
        print "	<br />\n" if ($InnoDB_Free);
## -STATS:  Table Details
        $sth = $dbh->prepare("SELECT COUNT(*) FROM $dbmail_users_table");
        unless ($sth->execute())
        {
            $errormessage =
              "$DBI::errstr Failed on a configuration error.  Have you entered the correct DBMail version? -stats2";
        }
        while (($table) = $sth->fetchrow_array)
        {
            $str2a .= "Email Users: $table\n";
        }
        print $str2a if ($str2a);
        $num_users = $str2a if ($str2a);
        $sth->finish() if ($sth);
        print "	<br />\n";

## -STATS:  Number of aliases
        $sth = $dbh->prepare("SELECT COUNT(*) FROM $dbmail_aliases_table");
        unless ($sth->execute())
        {
            $errormessage =
              "$DBI::errstr Failed on a configuration error.  Have you entered the correct DBMail version? -stats3";
        }
        while (($table) = $sth->fetchrow_array)
        {
            $str2b .= "Email Aliases: $table\n";
        }
        print $str2b   if ($str2b);
        $sth->finish() if ($sth);
        print "	<br />\n";

## -STATS:  Auto Replies
        $sth = $dbh->prepare("SELECT COUNT(*) FROM $dbmail_auto_replies_table");
        unless ($sth->execute())
        {
            $errormessage =
              "$DBI::errstr Failed on a configuration error.  Have you entered the correct DBMail version? -stats4";
        }
        while (($table) = $sth->fetchrow_array)
        {
            $str2b1 .= "Auto Replies: $table\n";
        }
        print $str2b1  if ($str2b1);
        $sth->finish() if ($sth);
        print "	<br />\n";
## -STATS:   Auto Notifications
        $sth =
          $dbh->prepare(
                       "SELECT COUNT(*) FROM $dbmail_auto_notifications_table");
        $sth->execute();
        while (($table) = $sth->fetchrow_array)
        {
            $str2b2 .= "Auto Notifies: $table\n";
        }
        print $str2b2  if ($str2b2);
        $sth->finish() if ($sth);
        print "	<br />\n";

        unless ($DBMailOldVersion eq "1")
        {
## -STATS:  Recent logins
            $sth = $dbh->prepare("SELECT COUNT(*) FROM $dbmail_pbsp_table");
            $sth->execute();
            while (($table) = $sth->fetchrow_array)
            {
                $str2f .= "Recent Logins: $table\n";
            }
            print $str2f   if ($str2f);
            $sth->finish() if ($sth);
            print "	<br />\n";

## -STATS:  How Many Deletes Pending?
            $sth =
              $dbh->prepare(
                "SELECT COUNT(*) FROM $dbmail_messages_table WHERE deleted_flag='1' OR status >0"
              );
            unless ($sth->execute())
            {
                $errormessage =
                  "$DBI::errstr Failed on a configuration error. I looked for the number of deletes pending. Have you entered the correct DBMail version? -stats2";
            }
            while (($table) = $sth->fetchrow_array)
            {
                $str .= "Deletes Pending: $table\n";
            }
            print $str     if ($str);
            $sth->finish() if ($sth);
            print "	<br />\n";

## -STATS:  Mailboxes
            $sth =
              $dbh->prepare("SELECT COUNT(*) FROM $dbmail_mailboxes_table");
            $sth->execute();
            while (($table) = $sth->fetchrow_array)
            {
                $str2d .= "Total Mailboxes: $table\n";
            }
            print $str2d   if ($str2d);
            $sth->finish() if ($sth);
            print "	<br />\n";
## -STATS:  Messages
            undef $table;
            $sth = $dbh->prepare("SELECT COUNT(*) FROM $dbmail_messages_table");
            unless ($sth->execute())
            {
                $errormessage = "
	ErrorID: $version.err0.74 <br />$DBI::errstr <br />
$DBI::errstr Failed on a configuration error.  Have you entered the correct DBMail version? -stats5";
            }
            while (($table) = $sth->fetchrow_array)
            {
                $str2c .= "Mail Messages: $table\n";
            }
            print $str2c   if ($str2c);
            $sth->finish() if ($sth);

            print "	<br />\n";
## -STATS:  Physical Messages
            $sth =
              $dbh->prepare("SELECT COUNT(*) FROM $dbmail_physmessage_table");
            $sth->execute();
            while (($table) = $sth->fetchrow_array)
            {
                $str2e2 .= "Physical Msgs: $table\n";
            }
            print $str2e2  if ($str2e2);
            $sth->finish() if ($sth);
            print "	<br />\n";
        }
## -STATS:  Message Blocks
        if ($DBMailOldVersion eq "0")
        {
            $sth =
              $dbh->prepare("SELECT COUNT(*) FROM $dbmail_messageblks_table");
            unless ($sth->execute())
            {
                $errormessage = "
	ErrorID: $version.err0.75 <br />$DBI::errstr <br />
	$DBI::errstr Failed on a configuration error.  Have you entered the correct DBMail version? -stats6";
            }
            while (($table) = $sth->fetchrow_array)
            {
                $str2e .= "Message Blks: $table\n";
            }
            print $str2e   if ($str2e);
            $sth->finish() if ($sth);
            print "	</span></td>\n";
        }
        else
        {
            print "	</td>";
        }
        &Groups_and_Domains;
        &showstatus;
        print "	</tr>
	<tr><td colspan=\"3\"><span style=\"font-size:10px\">\n";
        print $errormessage if $errormessage;

        $check_secs = (stat($DBMA_DATA))[9];
        $write_secs = (stat($DBMA_TIMESTAMP))[9];
        print " DBMail V3.2.x or newer." if ($DBMail22Version eq "1");
        print " Note: DBMail V1.2.11 or older. Consider upgrade to 2.x"
          if ($DBMailOldVersion eq "1");
        print " DBMail V2.0.x Legacy"
          if (($DBMailOldVersion eq "0") && ($DBMail22Version eq "0"));
        print " Data last updated "        if ($sqltype =~ /mysql/);
        print " Domain data last updated " if ($sqltype =~ /pgsql/);
        $value = ($write_secs - $check_secs);
        print($value);
        print " seconds ago.";
        print "\n	</span></td></tr></table></center></div>\n";
        end_HTML;

        $sth->finish()     if ($sth);
        $dbh->disconnect() if ($dbh);
    }
    else
    {
        print "	</span></td></tr>\n";
        end_HTML;
        $dbh->disconnect() if ($dbh);
    }
}
############################################################## - sub Groups_and_Domains
sub Groups_and_Domains
{
    &connect unless ($dbh);
## -Fetch domains
    $str = "";
    if (($fetch_domains == "1") || ($use_DBMA_MTA_Domains eq "1"))
    {
        $check_secs = (stat($DBMA_DATA))[9];
        $write_secs = (stat($DBMA_TIMESTAMP))[9];
        open(TIMESTAMP, ">$DBMA_TIMESTAMP")
          or die(
            "Please check permissions. chmod 777 $path_determined 
Can't create DBMA_TIMESTAMP file"
                );
        print TIMESTAMP "$date\n";
        close(TIMESTAMP);
        if (($write_secs - $check_secs) > $refresh_rate)
        {
            $sth =
              $dbh->prepare(
                "SELECT alias from $dbmail_aliases_table ORDER by client_idnr");
            unless ($sth->execute()) { print "Configuration Problem."; }
            while (($alias) = $sth->fetchrow_array)
            {
                &filt($alias);
                $alias =~ s/[0-9a-zA-Z\.\-\_\!\#\$\%\&\'\*\+\/\=\?\^]+\@//g;
                $alias =~ s/\@//g;
                $str7 .= "$alias\n";
                open(DOMAINDATA, "> $DBMA_DATA")
                  or die(
                    "Please check permissions. chmod 777 $path_determined
Can't create DBMA_DATA.DB file?"
                        );
                print DOMAINDATA "$str7";
            }
            close(DOMAINDATA);
        }
        unlink $DBMA_DATA_MTA_TEMP;
        open(DOMAINDATA, "$DBMA_DATA");
        @data = <DOMAINDATA>;
        foreach $line (sort @data)
        {
            foreach ($line)
            {
                $count++ unless $seen{$_}++;
            }
        }
        $value = $count + 0;
## - Start building My Domains panel
        print "	<td style=\"flush:right\"><small>My Domains:</small><br />
	<textarea onmouseover=\"this.className=\'statsover\';self.status=\'Total $value Domains\';return true\" onmouseout=\"this.className=\'stats\';self.status=\'DBMA\';return true\" title=\"$sqlhost has aliases on $value domains\" 
	class=\"stats\" rows=\"16\" cols=\"28\">\n";
        print "Alias Domains:($value)\n";
        foreach $line (sort @data)
        {
            foreach ($line)
            {
                next if /^(\s)*$/;
                my $uniquedomain .= $line unless ($line{$_}++);
                print $uniquedomain if $uniquedomain;
                open(TEMPDATA, ">>$DBMA_DATA_MTA_TEMP")
                  or die("Can't open DBMA_DATA_MTA_TEMP file");
                print TEMPDATA "$uniquedomain" if $uniquedomain;
            }
        }
        print "--------------------\n";
        close(TEMPDATA);
        close(DOMAINDATA);
        if ($use_DBMA_MTA_Domains eq "1")
        {
            &MTA_Compare_Alias_and_SQL;
        }
## - MTA Domains only
        $transport = $FORM{'transport'} || "dbmail-lmtp:127.0.0.1:24";
        unless (-z $Missing_In_SQL_MTA)
        {
            if ($use_DBMA_MTA_Domains eq "1")
            {
                &MTA_Compare_Alias_and_SQL;
                open(UPDATEDATA, "$Missing_In_SQL_MTA")
                  or die("Can't open SQL_MTA Update file");
                @sqldata = <UPDATEDATA>;
                foreach $line (@sqldata)
                {
                    my $sqldata .= &filt($line);
                    $sth =
                      $dbh->prepare(
                        "INSERT INTO DBMA_MTA (mydestination, transport) VALUES ('$sqldata', '$transport')"
                      );
                    $sth->execute();
                    unless ($dbh->commit())
                    {
                        print "Configuration error.";
                    }
                }
                close(UPDATEDATA);
            }
        }
## - MTA Domains only
        if ($use_DBMA_MTA_Domains eq "1")
        {
            $sth =
              $dbh->prepare(
                "SELECT mydestination FROM DBMA_MTA ORDER BY DBMA_MTA.mydestination"
              );
            unless ($sth->execute())
            {
                print
                  "You are not fully configured yet. Try pressing \"Go!\" twice to re-initiate data files. \n";
            }
            $numrows = $sth->rows;
            while ((my $mydestination) = $sth->fetchrow_array)
            {
                $str8 .= "$mydestination\n";
            }
            print "\nMTA Domains:($numrows)\n";
            print $str8    if ($str8);
            $sth->finish() if ($sth);
            if (-z $Missing_In_SQL_MTA)
            {
                print "--------------------\nMTA Domains up to date";
            }
            open(SQLDATA, "> $DBMA_SQL_MTA");
            print SQLDATA "$str8" if ($str8);
            close(SQLDATA);
        }
        print "</textarea></td>\n";
## - GroupGet and analysis
        my $GroupID_data;
        $sth =
          $dbh->prepare(
            "SELECT DISTINCT client_idnr from $dbmail_users_table ORDER by client_idnr"
          );
        unless ($sth->execute()) { print $DBI::errstr; }
        $numrows = $sth->rows;
        print "	<td style=\"flush:right\"><small>My Groups:</small><br />
	<textarea onmouseover=\"this.className=\'statsover\';self.status=\'Total $numrows User Groups\';return true\" onmouseout=\"this.className=\'stats\';self.status=\'DBMA\';return true\" title=\"$sqlhost has $numrows Groups incl Group 0 for system use\" 
	class=\"stats\" rows=\"16\" cols=\"28\">\n";
        print "Total $numrows Groups\n(";

        while (($GroupID_data) = $sth->fetchrow_array)
        {
            if ($GroupID_data > 0) { $GroupID_data = ",$GroupID_data"; }
            if ($GroupID_data eq "0") { $GroupID_data =~ s/0/\&#48;/g; }
            print $GroupID_data if ($GroupID_data);
        }
        print ")";

        print "\n----------------------\n";

        if (($write_secs - $check_secs) > $refresh_rate)
        {
            my $sth =
              $dbh->prepare(
                "SELECT DISTINCT alias, client_idnr from $dbmail_aliases_table ORDER by client_idnr"
              );
            unless ($sth->execute())
            {
                print $DBI::errstr;
            }
            while (($alias, $GroupID) = $sth->fetchrow_array)
            {
                &filt($alias);
                $alias =~ s/^&+//;
                $alias =~ s/[0-9a-zA-Z\.\-\_\!\#\$\%\&\'\*\+\/\=\?\^]+\@//g;
                $str9 .= "\(Group $GroupID\)\|$alias\n";
                open(DATA, "> $DBMA_GROUP_DATA")
                  or die(
                    "Please check permissions. chmod 777 $path_determined 
Can't create DBMA_GROUP_DATA.DB file?"
                        );
                print DATA "$str9\n";
                close(DATA);
            }
        }
        $sth->finish() if ($sth);

## clean up
        my %data = ();
        %data = &make_a_hash($DBMA_GROUP_DATA);
        if (%data)
        {
            open(DATA, "> $DBMA_GROUP_DATA");
            for $key (sort keys(%data))
            {
                foreach ($key)
                {
                    delete $data{$key} if ($key{$_}++);
                    print DATA "$key\n";
                }
            }
            close(DATA);
        }
        if (($count_users_per_group == 1) && ($fetch_domains == 1))
        {
## make a who's who of domains per group

            open(PARSE, "$DBMA_GROUP_DATA")
              or die(
                "Please check permissions. chmod 777 $path_determined 
 Can't open DBMA_GROUP_DATA.DB file?"
                    );
            my @parse = <PARSE>;
            my $parse = '';
            my %parse = ();
            $_ = '';

            foreach $line (sort @parse)
            {
                chomp $line  if $line;
                &filt($line) if $line;
                $line =~ s/[\n]+//gm;
                our ($grp, $dom) = split(/\|/, $line) if $line;
                $stripped_group = $grp if $grp;
                $stripped_group =~ s/\(Group//g if $grp;
                $stripped_group =~ s/\)//g      if $grp;
                $stripped_group =~ s/ //g       if $grp;

                if ($dom) { ($parse{$grp}) = split [/\|/, %parse] if $grp; }

                for (keys(%parse))
                {
                    foreach ($grp)
                    {
                        $sth = $dbh->prepare("
SELECT COUNT(*) FROM $dbmail_users_table
WHERE client_idnr = '$stripped_group'"
                        );
                        $sth->execute;
                        $output = $sth->fetchrow_array;
                        $dom =~ s/\@/Warn.Open alias:\n*\&#64;/g;
                        print "\n$grp - $output users\n" unless ($grp{$_}++);
                        print "$dom\n" unless ($parse{$grp, $dom}++);

                    }
                }

            }
            $num_users =~ s/Email U/U/g;
            print "\nTotals:\n"
              . $num_users
              . "Groups:"
              . $numrows . "\n"
              ; ### brought back in June 2, 2006 V2.4.9 - a little redundant but helpful for large systems
            close(DATA);
        }

        else
        {
## make a who's who of domains per group

            open(PARSE, "$DBMA_GROUP_DATA")
              or die(
                "Please check permissions. chmod 777 $path_determined 
 Can't open DBMA_GROUP_DATA.DB file?"
                    );
            my @parse = <PARSE>;
            my $parse = '';
            my %parse = ();
            $_ = '';

            foreach $line (sort @parse)
            {
                chomp $line  if $line;
                &filt($line) if $line;
                $line =~ s/[\n]+//gm;
                our ($grp, $dom) = split(/\|/, $line) if $line;

                if ($dom) { ($parse{$grp}) = split [/\|/, %parse] if $grp; }

                for (keys(%parse))
                {
                    foreach ($grp)
                    {
                        $dom =~ s/\@/Warn.Open alias:\n*\&#64;/g;
                        print "\n$grp\n" unless ($grp{$_}++);
                        print "$dom\n" unless ($parse{$grp, $dom}++);
                    }
                }

            }

            close(DATA);
        }
        print "</textarea></td>\n";
        undef $line;
        undef $num_users;
    }
}
############################################################## - sub showstatus
sub showstatus
{
    $str3 = "";
    $str4 = "";
    undef @row;
    $check_secs = (stat($DBMA_STATS))[9];
    $write_secs = (stat($DBMA_TIMESTAMP))[9];
## -STATS:  Status and connections
    if ($sqltype eq "pgsql")
    {
        print "	<td style=\"width:1%\">";
    }
    elsif (   ($sqltype eq "mysql")
           && (($write_secs - $check_secs) > $refresh_rate))
    {
        print <<"DBMA";
	<td style="flush:right"><small>My RDBMS:</small><br />
	<textarea title="My RDBMS tables and connections" cols="30" rows="16" class="stats" onmouseover="this.className='statsover';self.status='$sqlhost DBMS Statistics and Processlist';return true" onmouseout="this.className='stats';self.status='DBMA';return true">
DBMA

        $sth = $dbh->prepare("SHOW TABLES");
        unless ($sth->execute())
        {
            $errormessage =
              "$DBI::errstr Failed on a configuration error.  Have you entered the correct DBMail version? -stats7";
        }
        while ((@row) = $sth->fetchrow_array)
        {
            $str3 .= "@row\n";
        }
        $sth->finish() if ($sth);
## Add PROCESSLIST
        my $sth = $dbh->prepare(qq{ SHOW PROCESSLIST })
          or die $errormessage =
          "couldn't prepare show process list: " . $dbh->errstr;
        unless ($sth->execute())
        {
            $errormessage =
              "ErrorID: $version.err0.76 <br />$DBI::errstr Failed on a configuration error.  Have you entered the correct DBMail version? -stats8";
        }
        while (my $process = $sth->fetchrow_hashref)
        {
            $str4 .= $process->{Host} . "\n";
        }
        open(STATS, "> $DBMA_STATS")
          or die(
            "Please check permissions. chmod 777 $path_determined 
Can't create DBMA_STATS file"
                );
        print STATS "$str3";
        print STATS "\nCONNECTIONS\n";
        print STATS "$str4" if ($str4);
        close(STATS);
        print $str3 if ($str3);
        print "\nCONNECTIONS\n";
        print $str4 if ($str4);
        $value = ($write_secs - $check_secs);
        print 'Updated ' . $value . ' secs ago';
        print "\n";
        print "	</textarea></td>\n";
    }
    elsif (   ($sqltype eq "mysql")
           && (($write_secs - $check_secs) <= $refresh_rate))
    {
        print "	<td style=\"flush:right\"><small>My RDBMS</small><br />
	<textarea cols=\"30\" rows=\"12\" class=\"stats\" onmouseover=\"this.className=\'statsover\';self.status=\'$sqlhost DBMS Statistics and Processlist\';return true\" onmouseout=\"this.className=\'stats\';self.status=\'DBMA\';return true\" />\n";
        {
            local *INPUT;
            open(INPUT, "$DBMA_STATS")
              or warn "$DBMA_STATS not found" && return;
            +print while (<INPUT>);
            close INPUT;
        }
        $value = ($write_secs - $check_secs);
        print 'Updated ' . $value . ' secs ago';
        print "</textarea></td>\n";
    }
}
############################################################## - sub MTA_Compare_Alias_and_SQL
sub MTA_Compare_Alias_and_SQL
{
    $^W = 0;

    {
        no warnings 'redefine';
        my $filehash1             = "";
        my $filehash2             = "";
        my $key                   = "";
        my $Not_In_Aliases        = "";
        my $Not_In_SQL            = "";
        my $SQL_and_Aliases_Match = "";
        my %filehash1             = &make_a_hash($DBMA_DATA_MTA_TEMP);
        my %filehash2             = &make_a_hash($DBMA_SQL_MTA);
        open(ALIASANDSQL, "> $ALIAS_AND_SQL_MATCH")
          || die "Could not open file $ALIAS_AND_SQL_MATCH : $!";
        open(UPDATEDATA, "> $Missing_In_SQL_MTA")
          || die "Could not open file $Missing_In_SQL_MTA : $!";
        open(NOTINALIASES, "> $Not_Found_In_Aliases")
          || die "Could not open file $Not_Found_In_Aliases : $!";

        for $key (keys %filehash1)
        {
            if ($filehash2{$key} == 1)
            {
                print ALIASANDSQL "$key\n" if $key;
                $SQL_and_Aliases_Match++;
            }
            else
            {
                print UPDATEDATA "$key\n" if $key;
                $Not_In_SQL++;
            }
        }
        for $key (keys %filehash2)
        {
            unless ($filehash1{$key} == 1)
            {
                print NOTINALIASES "$key\n" if $key;
                $Not_In_Aliases++;
            }
        }
        close(ALIASANDSQL);
        close(UPDATEDATA);
        close(NOTINALIASES);
    }
}
############################################################## - path_determined
sub path_determined
{

## for MOD_PERL we must get the exact *real* path so try to automate that config from the environment keys
    if ($ENV{'DOCUMENT_ROOT'})
    {
        $path_determined = ($ENV{'DOCUMENT_ROOT'} . $ENV{'SCRIPT_NAME'});
        $path_determined =~ s/DBMA.cgi//g;
        $path_determined =~ s/dev.cgi//g;
        $path_determined =~ s/dbma.cgi//g;
        $path_determined =~ s/DBMA.dbma//g;
    }

    else
    {
        $path_determined = "./";
    }

    return $path_determined;
}
############################################################## - mysql_date
sub mysql_date
{
    $peopledate = "" . scalar localtime(time) . "";
    my ($sec, $min, $hour, $mday, $mon, $year) = localtime(time);
    my $actualtime = sprintf("%0.2d:%0.2d:%0.2d", $hour, $min, $sec);
    my $actualday = sprintf("%0.4d-%0.2d-%0.2d", $year + 1900, ++$mon, $mday);
    $date = "$actualday $actualtime";

    if ($dbh)
    {
        $sth = $dbh->prepare("SELECT CURRENT_TIMESTAMP;");
        $sth->execute();
        while ($mysqldate = $sth->fetchrow_array)
        {
            return $mysqldate;
        }

        $sth->finish() if ($sth);
    }

    unless ($mysqldate
      ) # on initial configure we won't stop clock because we cannot yet connect to RDBMS :o)
    {
        $mysqldate == $date;
    }

}
############################################################## - sub make_a_hash
sub make_a_hash ($)
{
    $filehash = '';
    $dir      = shift || @_ || '';
    %filehash = () if %filehash;
    open(STUFFFORHASH, "<$dir") || die $!;
    while (<STUFFFORHASH>)
    {
        chomp $_;
        s/^ *//;
        s/ *$//;
        $filehash{$_} = 1;
    }
    return %filehash;
}
############################################################## - sub DBMA_ConnectStatus
sub DBMA_ConnectStatus ($)
{    # (does some troubleshooting)
    my ($color, $title);
    if ($RQT eq "24")
    {
        $errormessage =
          "DBMA configuration, options &amp; system info: scroll page to check all. ";
        $color            = "#008000";
        $colortellsastory = "#E7FAE8";
        $title            =
          "<title>CONFIGURATION DETAILS -  (DBMA) DBMail Administrator Connected to $sqlhost from $server</title>";
    }
    elsif ($RQT eq "29")
    {
        $errormessage =
          "Primary Configuration Changes Made <form title=\"When your configuration is complete, go to the main menu and press Go twice to initiate db flat files.\" method=\"post\" action=\"$mythisscript\">\n<input class=\"c7\" type=\"submit\" value=\"Try the Database Connection Now?\" /></form>\n";
        $title            = "<title>DBMA Configuration Changes Made</title>";
        $colortellsastory = "#E7FAE8";
        $color            = "#008000";
    }
    elsif ($RQT eq "30")
    {
        $title        = "<title>DBMA OPTIONS Changes Made</title>";
        $errormessage =
          "OPTIONS changes completed.\n <form title=\"When your configuration is complete, go to the main menu and press Go twice to initiate db flat files.\" method=\"post\" action=\"$mythisscript\">\n<input class=\"c7\" type=\"submit\" value=\"Go to the Main Menu now?\" /></form>";
        $colortellsastory = "#E7FAE8";
        $color            = "#008000";
    }
    else
    {
        $title =
          "<title>CONNECTION ERROR (DBMA) DBMail Administrator Connected to $sqlhost from $server</title>";
        $colortellsastory = "#F0F0F0";
        $color            = "#ff0000";
    }
    &meta;
    print "$title";
    &defaults;
    $perm_error = "";
    &read_configs;
    print <<"DBMA";
	</head><body><div><center><table border="0" cellspacing="0" cellpadding="0" width="738px">
	<tr><td class="c2" colspan="2">$version ($sqltype $sqlhost) from $server [<a  target="_blank" title="Start reading the manual" href="DBMA_installation_configuration.htm"><b>Help</b></a>] <span class="c6" style="font-weight:bold"> <a title="Back to tthe main menu" href="$mythisscript">Menu </a></span></td></tr></table></center></div>
	<div><center><table cellspacing="0" cellpadding="0">
	<tr><td style="color:$color;line-height:120%;font-size:110%;font-weight:bold">$errormessage</td></tr>
	<tr><td style="color:#ff0000;line-height:120%;font-size:110%;font-weight:bold">
DBMA
    print $perm_error if ($perm_error);
    my $none_db_type = "style\=\"background:red\"" if ($sqltype =~ /none/);
    print <<"DBMA";
        </td></tr></table></center></div>
	<div class="c6"><center><form method="post" action="$mythisscript"><table width="700" style="font-family: Arial, sans-serif; font-size: 10pt; color: #000080; background-color: $colortellsastory">
	<tr><td style="background:white;color:green; font-family:arial,sans-serif;font-size:11px" colspan="2">Once your configuration is complete, go to the main menu and press "Go!" twice to initiate all of DBMAs db flat files.</td></tr>
	<tr><td class="c14"><h3>Primary Configuration</h3></td><td><input type="hidden" name="RQT" value="29" /><input type="submit" title="check your configuration" value="Commit DBMA Reconfiguration" name="submit" style="float:right;border-style:solid;background-color:#FFd9d9; color:#6C0000; font-family:arial, sans-serif; font-size:11px; font-weight:normal" /></td></tr>
        <tr><td style="text-align:left;font-size:12px;color:black" colspan="2">DBMail version 3.2.x or greater.</td></tr>
	<tr><td class="c14"><input type="hidden" $mouseover name="DBMailOldVersion" size="3" value="0" />DBMail Version 1.x No</td><td><a href="http://dbma.ca/DBMA_SQL_V2.tar.gz">Download DBMA v2.5.4</a></td></tr>
	<tr><td class="c14"><input type="hidden" $mouseover name="DBMail21Version" size="3" value="1" />DBMail Version 2.2&gt; No</td><td><a href="http://dbma.ca/DBMA_SQL_V2.tar.gz">Download DBMA v2.5.4</a></td></tr>
	<tr><td class="c14">DBMail Version 3.2&gt; Yes</td><td>DBMail 3.2 Version or greater? (Database differs)</td></tr>
	<tr><td $none_db_type class="c14"><input type="text" $mouseover $changecase value="$sqltype" name="sqltype" size="12" />mysql or pgsql</td><td>RDBMS type 'mysql' or 'pgsql'</td></tr>
	<tr><td class="c14"><input type="text" $mouseover value="$sqluser" name="sqluser" size="12" />Database User</td><td>Name of database user able to log into your DBMail database</td></tr>
	<tr><td class="c14"><input type="text" $mouseover value="$DBMAcode" name="DBMAcode" size="12" />Database Password</td><td>Database login password</td></tr>
	<tr><td class="c14"><input type="text" $mouseover value="$sqldb" name="sqldb" size="12" />Name of Database</td><td>The name of your DBMail database</td></tr>
	<tr><td class="c14"><input type="text" $mouseover value="$sqlhost" name="sqlhost" size="19" />Host Name</td><td>IP address or resolveable host name of database server</td></tr>
	<tr><td class="c14"><input type="text" $mouseover value="$sql_odd_port" name="sql_odd_port" size="5" /> Port? Blank for default.</td><td>Leave port number blank if standard. Change for non-standard or proxy.</td></tr></table></form></center></div>	
	<div class="c6"><center><form method="post" action="$mythisscript"><table border="0" width="738px" style="font-family: Arial, sans-serif; font-size: 10pt; color: #000080; background-color: $colortellsastory">
	<tr><td class="c14"><h3>Preset Options</h3></td><td><input type="hidden" name="RQT" value="30" /> <input type="submit" title="check your OPTIONS configuration before submitting" value="Commit DBMA OPTIONS" name="submit" style="float:right;border-style:solid;background-color:#FFd9d9; color:#6C0000; font-family:arial, sans-serif; font-size:11px; font-weight:normal" /></td></tr>
	<tr><td class="c14"><input type="text" $mouseover $changecase value="$SMTP_ServerName" name="SMTP_ServerName" size="15" />SMTP Server</td><td>Your DBMail MTA SMTP IP or resolveable host name.</td></tr>
	<tr><td class="c14"><input type="text" $mouseover $changecase value="$admin_address" name="admin_address" size="30" /></td><td>The administrator's email address for user notification mail.</td></tr>
	<tr><td class="c14"><input type="text" $mouseover value="$defaultmailboxsize" name="defaultmailboxsize" size="12" />Mailbox Size</td><td>Max for Restricted Group Admin and default for global mode.</td></tr>
	<tr><td class="c14"><input type="text" $mouseover value="$defaultGroup_ID" name="defaultGroup_ID" size="4" />Default Group ID</td><td>Default GroupID where you work most. A starting point. (client_idnr)</td></tr>
	<tr><td class="c14"><input type="text" $mouseover value="$group_limit" name="group_limit" SIZE="4" />Group Size Limit</td><td>Limit the number of users per group</td></tr>
	<tr><td class="c14"><input type="text" $mouseover value="$count_users_per_group" name="count_users_per_group" SIZE="3" />Count Users Per Group</td><td>Show the count of users in each group. (Slows Main Stats on large systems.)</td></tr>
	<tr><td class="c14"><input type="text" $mouseover value="$CFP" name="CFP" size="3" />Generate Password? 1=YES 0=NO</td><td>Do you want DBMA to auto-generate alphanumeric passwords?</td></tr>
	<tr><td class="c14"><input type="text" $mouseover value="$stats_on" name="stats_on" size="3" />Stats On? 1=YES 0=NO</td><td>DBMA Statistics on or off? (On recommended.)</td></tr>
	<tr><td class="c14"><input type="text" $mouseover value="$fetch_domains" name="fetch_domains" size="3" />Domain &amp; Group data? 1=YES 0=NO</td><td>Off for large systems or slow CPUs. Off is partly ignored if MTA Admin=1</td></tr>
	<tr><td class="c14"><input type="text" $mouseover value="$refresh_rate" name="refresh_rate" size="3" />Statistics refresh rate in seconds</td><td>Minimize database hits if stats on. Enter seconds (i.e.: 0,300,600)</td></tr>
	<tr><td class="c14"><input type="text" $mouseover value="$DBMAencrypt" name="DBMAencrypt" size="9" />Default encryption</td><td>Options: 'md5sum', 'crypt', 'md5' or 'plain text.</td></tr>
	<tr><td class="c14"><input type="text" $mouseover $changecase value="$defaultdomain" name="defaultdomain" size="16" />Default Domain</td><td>Default domain for new accounts. (Recommended. Please enter.)</td></tr>
	<tr><td class="c14"><input type="text" $mouseover value="$create_first_alias" name="create_first_alias" size="3" />Create First Alias? 1=YES, 0=NO</td><td>Do you want DBMA to create the first alias using the above domain?</td></tr>
	<tr><td class="c14"><input type="text" $mouseover value="$ACL_ctrl" name="ACL_ctrl" size="3" />Allow ACLs 1=YES, 0=NO</td><td>Provide Administration of ACLs</td></tr>
	<tr><td class="c14"><input type="hidden" $mouseover name="allow_read_mail" value="1" size="3" />Allow Read Mail OFF </td><td>Allow Administrator to Read Mail = OFF</td></tr>
	<tr><td class="c14"><input type="text" $mouseover value="$auto_create_user" name="auto_create_user" size="3" />Auto Create User for New Alias</td><td>If added alias has no user, DBMA creates user with No Access passwd.<a target="_blank" href="DBMA_help.htm#auto_create_user">Help</a></td></tr>
	<tr><td class="c14"><input type="text" $mouseover value="$use_DBMA_MTA_Domains" name="use_DBMA_MTA_Domains" size="3" />Use DBMA MTA Admin 1=YES, 0=NO</td><td>Store MTA domains, transports and access in $sqltype. Read <a target="_blank" href="DBMA_help.htm#use_DBMA_MTA_Domains">Help</a></td></tr>
	<tr><td class="c14"></td><td><input type="hidden" name="RQT" value="30" /> <input type="submit" title="check your OPTIONS configuration before submitting" value="Commit DBMA OPTIONS" name="submit" style="float:right;border-style:solid;background-color:#FFd9d9; color:#6C0000; font-family:arial, sans-serif; font-size:11px; font-weight:normal" /></td></tr>
	</table></form></center></div>
	<div><center><table border="0" cellspacing="0" cellpadding="0" width="738px">
DBMA

    if (($use_DBMA_MTA_Domains eq "1") && ($RQT eq "24"))
    {
        $sth = $dbh->prepare("SELECT * FROM $dbmail_users_table LIMIT 1");

        unless ($sth->execute())
        {
            print
              "<tr><td style=\"color:$color;line-height:120%;font-size:110%;font-weight:bold\" colspan=\"2\">$sqltype DBMA believes Database Connection has Gone Away!</td></tr>\n";
        }
        if (($_) = $sth->fetchrow_array)
        {
            if ($DBMailOldVersion eq "1") { $use_DBMA_MTA_Domains = 0 }
            if ($use_DBMA_MTA_Domains eq "1")
            {
                print
                  "	<tr><td style=\"color:$color;line-height:120%;font-size:110%;font-weight:bold\" colspan=\"2\">DBMA MTA Admin is turned ON \(\"Use DBMA MTA = $use_DBMA_MTA_Domains\"\)</td></tr>\n";

                &edit_MTA_Domains if $use_DBMA_MTA_Domains eq "1";
            }
        }
    }
    elsif (($use_DBMA_MTA_Domains eq "0") && ($RQT eq "29" || "30"))

    {
        print
          "	<tr><td style=\"color:orange;line-height:120%;font-size:110%;font-weight:bold\" colspan=\"2\">DBMA MTA Admin is OFF \(\"Use DBMA MTA = $use_DBMA_MTA_Domains\"\)</td></tr>\n";
        print <<"DBMA";
	<tr><td style="font-family: Arial, sans-serif; font-size: 10pt; color: #000080; background-color: $colortellsastory">
	<span style="color:#005A9C;font-size:110%;font-weight:600">MTA Domains and Transports</span></td>
	<td style="font-family: Arial, sans-serif; font-size: 10pt; color: #000080; background-color: $colortellsastory">
	<form method="post" action="$mythisscript"><input type="hidden" value="55" name ="RQT" />
	<input title="Create MTA Domains Tables." type="submit" value="Create DBMA_MTA Tables" style="float:right;border-style:solid;background-color:#FFd9d9; color:#6C0000; font-family:arial, sans-serif; font-size:11px; font-weight:normal" onclick="return confirm('_____________________TURNED OFF_____________________\\n\\n\\n1. DBMA MTA Admin IS OFF\\n2. Only current information will be entered into the database.\\n3. Automatic updates are OFF.\\n4. You will only be able to access this function from the Configuration Window\\n\\n Even though you have Use DBMA MTA Admin turned off this will immediately create MTA database tables for your MTA destination domains, mail transports, and MTA Access. \\n\\nIMPORTANT NOTE\\nIf you have already created MTA_Domains and have entered custom transports and domains for your MTA, they will all be returned to default values after this process has completed. Existing Access data will not be touched. Transports can easily be edited. The default domains are those within your alias fields. The default transport is the DBMail LMTPD on port 24.\\n\\nSelect CANCEL to go back and turn on DBMA MTA ADMIN\\n\\nDo you wish to proceed?')" /></form></td></tr>
DBMA
    }
    elsif (($use_DBMA_MTA_Domains eq "1") && ($RQT eq "29" || "30"))

    {
        print
          "	<tr><td style=\"color:$color;line-height:120%;font-size:110%;font-weight:bold\" colspan=\"2\">DBMA MTA Admin is turned ON \(\"Use DBMA MTA = $use_DBMA_MTA_Domains\"\)</td></tr>\n";
        print <<"DBMA";
	<tr><td style="font-family: Arial, sans-serif; font-size: 10pt; color: #000080; background-color: $colortellsastory">
	<span style="color:#005A9C;font-size:110%;font-weight:600">MTA Domains and Transports</span></td>
	<td style="font-family: Arial, sans-serif; font-size: 10pt; color: #000080; background-color: $colortellsastory">
	<form method="post" action="$mythisscript"><input type="hidden" value="55" name ="RQT" />
	<input title="Create MTA Domains Table." type="submit" value="Create DBMA_MTA Tables" style="float:right;border-style:solid;background-color:#FFd9d9; color:#6C0000; font-family:arial, sans-serif; font-size:11px; font-weight:normal" onclick="return confirm('This will immediately create MTA database tables for your MTA destination domains, mail transports, and MTA Access. \\n\\nIMPORTANT NOTICE\\n\\nEVERYTHING will be Re-Written\\n\\nIf you have already created MTA_Domains and have entered custom transports and domains for your MTA, they will all be returned to default values after this process has completed. Existing Access data will not be touched. This can be easily edited. The default domains are those within your alias fields. The default transport is the DBMail LMTPD on port 24.\\n\\nDo you wish to proceed?')" /></form></td></tr>
DBMA
    }

    print "	<tr><td style=\"width:600px\" colspan=\"2\">\n";
    &DBI_drivers;

    # Print Environment
    print
      "<h4>System Environment</h4><textarea rows=\"45\" cols=\"100\" style=\"margin-left:2px;background-color:#f5f3f8;color:#005B00;line-height:160%;font-family:arial, sans-serif;font-size:11px;border-style:none;scrollbar-arrow-color:#000090;scrollbar-face-color:#f5f3f8;scrollbar-shadow-color:#f5f3f8; scrollbar-track-color:#f5f3f8\">\n";
    @keys   = keys %ENV;
    @values = values %ENV;
    while (@keys)
    {
        print pop(@keys), ' = ', pop(@values), "\n";
    }
    print "</textarea>\n";

    &path_determined;

    print <<"DBMA";
	<tr><td colspan="2"><h4>Installation Name Space</h4><small>This is where DBMA writes its temp files so make sure this is writeable by the HTTPD user|group :</small><br />$path_determined<p><br /></p></td></tr>
DBMA

    # Show what values were present if called by error

    if (   ($RQT ne "24")
        && ($RQT ne "29")
        && ($RQT ne "30"))
    {
        print <<"DBMA";
	<br />The following is what, if anything, you submitted.<br />
	<textarea class=\"list\" rows="4" cols="50">
userID   : $userID
username : $username
Group    : $GroupID
$newalias</textarea>
DBMA
    }
    my $d1 = $ENV{'SERVER_SOFTWARE'};
    my $d2 = $ENV{'SERVER_PORT'};
    my $d3 = `whoami`;
    print "	</td></tr>\n";
    print <<"DBMA";
	<tr><td colspan="2"><h4>Server Environment</h4></td></tr>
	<tr><td colspan="2"><ul><li>Host: $server</li><li>$d1</li>
	<li>Port: $d2</li><li>HTTPD User: $d3</li></ul></td></tr>
DBMA
    if ($RQT eq "24")
    {
        print <<"DBMA";
<tr><td><h3>Is this a new installation? Do you wish to make some Test users?</h3></td></tr>
<tr><td><a href="extra/DBMA_maketestuser.cgi">If DBMA is running on a DBMail host, make some test users (beta).</a><p><br /></p></td></tr></table></center></div>
DBMA
        print
          "	<div class=\"c6\"><center><table><tr><td class=\"gr\"><p><br /></p><p><br /></p><small>&#67;&#111;&#112;&#121;&#114;&#105;&#103;&#104;&#116; &#77;&#105;&#107;&#101; &#97;&#116; &#109;&#111;&#98;&#114;&#105;&#101;&#110;&#46;&#99;&#111;&#109;</small></td></tr></table></center></div>\n";
    }
    else
    {
        print
          "	<div class=\"c6\"><center><table><tr><td class=\"gr\"><p><br /></p><p><br /></p><small>&#67;&#111;&#112;&#121;&#114;&#105;&#103;&#104;&#116; &#77;&#105;&#107;&#101; &#97;&#116; &#109;&#111;&#98;&#114;&#105;&#101;&#110;&#46;&#99;&#111;&#109;</small></td></tr></table></center></div>\n";
        end_HTML;
    }
    exit;
}
############################################################## - sub create_myDBMA_CONFIG
sub create_myDBMA_CONFIG
{
    $DBMailOldVersion = $FORM{'DBMailOldVersion'};
    $DBMail22Version  = $FORM{'DBMail21Version'};
    $sqltype          = $FORM{'sqltype'};
    $sqluser          = $FORM{'sqluser'};
    $DBMAcode         = $FORM{'DBMAcode'};
    $sqldb            = $FORM{'sqldb'};
    $sqlhost          = $FORM{'sqlhost'};
    $sql_odd_port     = $FORM{'sql_odd_port'};
    open(CONFIG, "> $myDBMA_CONFIG")
      || die "DBMA Please check permissions. chmod 777 $path_determined 
Can't create $myDBMA_CONFIG\n";
    print CONFIG
      "$DBMailOldVersion|$DBMail22Version|$sqltype|$sqluser|$DBMAcode|$sqldb|$sqlhost|$sql_odd_port\n";
    close(CONFIG);
    &DBMA_ConnectStatus;
}
############################################################## - sub create_myDBMA_OPTIONS
sub create_myDBMA_OPTIONS
{
    $create_first_alias    = $FORM{'create_first_alias'};
    $CFP                   = $FORM{'CFP'};
    $defaultdomain         = $FORM{'defaultdomain'};
    $defaultmailboxsize    = $FORM{'defaultmailboxsize'};
    $defaultGroup_ID       = $FORM{'defaultGroup_ID'};
    $DBMAencrypt           = $FORM{'DBMAencrypt'};
    $SMTP_ServerName       = $FORM{'SMTP_ServerName'};
    $admin_address         = $FORM{'admin_address'};
    $DBMAencrypt           = $FORM{'DBMAencrypt'};
    $stats_on              = $FORM{'stats_on'};
    $fetch_domains         = $FORM{'fetch_domains'};
    $refresh_rate          = $FORM{'refresh_rate'};
    $ACL_ctrl              = $FORM{'ACL_ctrl'};
    $allow_read_mail       = $FORM{'allow_read_mail'};
    $auto_create_user      = $FORM{'auto_create_user'};
    $use_DBMA_MTA_Domains  = $FORM{'use_DBMA_MTA_Domains'};
    $group_limit           = $FORM{'group_limit'};
    $count_users_per_group = $FORM{'count_users_per_group'};

    open(OPTIONS, "> $myDBMA_OPTIONS")
      || die "DBMA can't create $myDBMA_OPTIONS\n";
    print OPTIONS
      "$SMTP_ServerName|$admin_address|$defaultmailboxsize|$defaultGroup_ID|$CFP|$DBMAencrypt|$defaultdomain|$create_first_alias|$stats_on|$fetch_domains|$refresh_rate|$ACL_ctrl|$allow_read_mail|$auto_create_user|$use_DBMA_MTA_Domains|$group_limit|$count_users_per_group\n";
    close(OPTIONS);
    &DBMA_ConnectStatus;
}
############################################################## - sub ACL_create RQT45
sub ACL_create
{
    $anyone       = $FORM{'anyone'}       || "";
    $PUBLICuserID = $FORM{'PUBLICuserID'} || "";
    &connect unless ($dbh);
    $password = &MD5_hash_salt_key('MYdbma2006');
    unless ($FORM{'anyone'})
    {
        $insertnewuser =
          "INSERT INTO $dbmail_users_table (userid, passwd, encryption_type)
    	VALUES ('anyone', '$password', 'md5')";
        $sth = $dbh->prepare($insertnewuser);
        unless ($sth->execute)
        {
            $errormessage = "$DBI::errstr ADD MISSING anyone ACCOUNT FAIL at 1";
            &DBMA_ConnectStatus;
        }
        unless ($dbh->commit)
        {
            $errormessage =
              "$DBI::errstr <br />Error: failed to add user anyone";
            &DBMA_ConnectStatus;
        }
    }
### Check up on anyone if exists and confirm idnr
    $sth =
      $dbh->prepare(
        "SELECT user_idnr FROM $dbmail_users_table WHERE LOWER(userid) = LOWER('anyone')"
      );
    unless ($sth->execute)
    {
        $errormessage = "
	ErrorID: $version.err0.60 <br />$DBI::errstr <br />Error: Could not find user anyone";
        &DBMA_ConnectStatus;
    }
    while (($anyone) = $sth->fetchrow_array)
    {
### Find __public__ && Does PUBLIC Account Exist
        $sth =
          $dbh->prepare(
            "SELECT user_idnr FROM $dbmail_users_table WHERE LOWER(userid) = LOWER('__public__')"
          );
        unless ($sth->execute)
        {
            $errormessage = " ErrorID: $version.err0.61 $DBI::errstr";
            &DBMA_ConnectStatus;
        }
        if (($PUBLICuserID) = $sth->fetchrow_array)
        {
### make the shared folder
            {
                $dbh->do(
                    "INSERT INTO $dbmail_mailboxes_table (owner_idnr, name, seen_flag, answered_flag, deleted_flag, flagged_flag, recent_flag, draft_flag, no_inferiors, no_select, permission) VALUES ('$PUBLICuserID', '$shared_mailbox', '1', '1', '1', '1', '1', '1', '0', '0', '2')"
                );
                unless ($dbh->commit)
                {
                    $errormessage =
                      "$DBI::errstr <br />Failed to create shared folder";
                    &DBMA_ConnectStatus;
                }
            }
### Add anyone to ACL
            $sth =
              $dbh->prepare(
                "SELECT mailbox_idnr FROM $dbmail_mailboxes_table WHERE owner_idnr='$PUBLICuserID' AND name='$shared_mailbox'"
              );
            unless ($sth->execute)
            {
                $errormessage = "
	ErrorID: $version.err0.62 <br />$DBI::errstr <br />Error: Could not create Public Account 6";
                &DBMA_ConnectStatus;
            }
            if (($mailbox_idnr) = $sth->fetchrow_array)
            {
                $dbh->do(
                    "INSERT INTO $dbmail_acl_table VALUES ( '$anyone', '$mailbox_idnr', '1', '1', '1', '1', '1', '1', '0', '0', '0' )"
                );
            }
        }
    }
    $dbh->commit();
    $sth->finish() if ($sth);
    &ACL_FORM;
    exit;
}
############################################################## - sub create_PUBLIC_Account_and_ACL RQT46
sub create_PUBLIC_Account_and_ACL
{
    &connect unless ($dbh);
    $password = &MD5_hash_salt_key('MYdbma2006');
    unless ($FORM{'anyone'})
    {
        $insertnewuser =
          "INSERT INTO $dbmail_users_table (userid, passwd, encryption_type)
    	VALUES ('anyone', '$password', 'md5')";
        $sth = $dbh->prepare($insertnewuser);
        unless ($sth->execute)
        {
            $errormessage = "$DBI::errstr ADD MISSING anyone FAIL ed at 6184";
            &DBMA_ConnectStatus;
        }
        unless ($dbh->commit)
        {
            $errormessage =
              "$DBI::errstr <br />Error: failed to add user anyone";
            &DBMA_ConnectStatus;
        }
    }
### Get anyone
    $sth =
      $dbh->prepare(
           "SELECT user_idnr FROM $dbmail_users_table WHERE userid = 'anyone'");
    unless ($sth->execute)
    {
        $errormessage = "$DBI::errstr Error: Could not find anyone";
        &DBMA_ConnectStatus;
    }
    while (($anyone) = $sth->fetchrow_array)
    {
### Create __public__
        $insertnewuser =
          "INSERT INTO $dbmail_users_table (userid, passwd, encryption_type)
    	VALUES ('__public__', '$password', 'md5')";
        $sth = $dbh->prepare($insertnewuser);
        unless ($sth->execute)
        {
            $errormessage = "
	ErrorID: $version.err0.64 <br />$DBI::errstr <br />ADD MISSING PUBLIC ACCOUNT FAIL at 1";
            &DBMA_ConnectStatus;
        }
        unless ($dbh->commit)
        {
            $errormessage =
              "DBMail Older Versions need to be modified or upgraded to use ACLs"
              if ($DBMailOldVersion eq "1");
            $errormessage =
              "$DBI::errstr <br />Error: $DBI::errstr commit FAIL for add PUBLIC user";
            &DBMA_ConnectStatus;
        }
### Get PUBLIC Account ID
        $sth =
          $dbh->prepare(
            "SELECT user_idnr FROM $dbmail_users_table WHERE LOWER(userid) = LOWER('__public__')"
          );
        unless ($sth->execute)
        {
            $errormessage =
              "DBMail Older Versions need to be modified or upgraded to use ACLs"
              if ($DBMailOldVersion eq "1");
            $errormessage =
              "Error: $DBI::errstr Could not create Public Account 1";
            &DBMA_ConnectStatus;
        }
        while (($PUBLICuserID) = $sth->fetchrow_array)
        {
### make the shared folder
            {
                $sth = $dbh->prepare(
                    "INSERT INTO $dbmail_mailboxes_table (owner_idnr, name, seen_flag, answered_flag, deleted_flag, flagged_flag, recent_flag, draft_flag, no_inferiors, no_select, permission)
    	VALUES ('$PUBLICuserID', '$shared_mailbox', '1', '1', '1', '1', '1', '1', '0', '0', '2')"
                                    );
                $sth->execute();
                unless ($dbh->commit)
                {
                    $errormessage =
                      "$DBI::errstr <br />$DBI::errstr Error: Could not create Public Account 5";
                    &DBMA_ConnectStatus;
                }
            }
## Get the mailbox_idnr and Add anyone to share folder
            $sth =
              $dbh->prepare(
                "SELECT mailbox_idnr FROM $dbmail_mailboxes_table WHERE owner_idnr='$PUBLICuserID' AND name='$shared_mailbox'"
              );
            unless ($sth->execute)
            {
                $errormessage = "
	ErrorID: $version.err0.65 <br />$DBI::errstr<br />DBMail Older Versions need to be modified or upgraded to use ACLs"
                  if ($DBMailOldVersion eq "1");
                $errormessage = "
	ErrorID: $version.err0.66 <br />$DBI::errstr<br />Error: $DBI::errstr Could not create Public Account 6";
                &DBMA_ConnectStatus;
            }
            while (($mailbox_idnr) = $sth->fetchrow_array)
            {
                $sth =
                  $dbh->prepare(
                    "INSERT INTO $dbmail_acl_table VALUES ( '$anyone', '$mailbox_idnr', '1', '1', '1', '1', '1', '1', '0', '0', '0' )"
                  );
                unless ($sth->execute)
                {
                    $errormessage =
                      "DBMail Older Versions need to be modified or upgraded to use ACLs"
                      if ($DBMailOldVersion eq "1");
                    $errormessage = "
	ErrorID: $version.err0.67 <br />$DBI::errstr <br />Error: Could not create Public Account 7";
                    &DBMA_ConnectStatus;
                }
                unless ($dbh->commit)
                {
                    $errormessage =
                      "$DBI::errstr <br />Error: Could not create Public Account 8";
                    &DBMA_ConnectStatus;
                }
            }
        }
    }
    $sth->finish() if ($sth);
    &ACL_FORM;
    exit;
}
############################################################## - sub add_ACL_user RQT50
sub add_ACL_user
{
    &prepare_input($userID);
## We are not going to add it if it exists. Check first. Then if exist do update not insert.
## mysql and pgsql need different approaches for different versions. DBMA will embrace all with cute redundancy
    $sth =
      $dbh->prepare(
        "select user_id, mailbox_id from $dbmail_acl_table where user_id ='$userID' AND mailbox_id = '$mailbox_idnr'"
      );
    $sth->execute;
    if (($user_id, $mailbox_id) = $sth->fetchrow_array)
    {
        &update_ACL_user
          if (   ($user_id = $FORM{'userID'})
              && ($mailbox_id = $FORM{'mailbox_idnr'}));
    }
    else
    {
        $sth->finish() if ($sth);
        $sth = $dbh->prepare(
            "INSERT INTO $dbmail_acl_table 
VALUES (
'$userID',
'$mailbox_idnr',
'$lookup_flag',
'$read_flag',
'$seen_flag',
'$write_flag',
'$insert_flag',
'$post_flag',
'$create_flag',
'$delete_flag',
'$administer_flag')"
                            );
        unless ($sth->execute)
        {
            $errormessage = "$DBI::errstr ADD ACL Failed <br /> $sth";
            &DBMA_ConnectStatus;
        }
        unless ($dbh->commit)
        {
            $errormessage =
              "$DBI::errstr <br />Error: Could not create Public ACL for $userID";
            &DBMA_ConnectStatus;
        }
        $sth->finish() if ($sth);
        &Create_User_Account_Window($userID);
        exit;
    }
}
############################################################## - sub update_ACL_user RQT49
sub update_ACL_user ()
{
    $lookup_flag     = $FORM{'lookup_flag'}     || ($lookup_flag);
    $read_flag       = $FORM{'read_flag'}       || ($read_flag);
    $seen_flag       = $FORM{'seen_flag'}       || ($seen_flag);
    $write_flag      = $FORM{'write_flag'}      || ($write_flag);
    $insert_flag     = $FORM{'insert_flag'}     || ($insert_flag);
    $post_flag       = $FORM{'post_flag'}       || ($post_flag);
    $create_flag     = $FORM{'create_flag'}     || ($create_flag);
    $delete_flag     = $FORM{'delete_flag'}     || ($delete_flag);
    $administer_flag = $FORM{'administer_flag'} || ($administer_flag);
    $anyone          = $FORM{'anyone'}          || "";
    $userID          = $FORM{'userID'}          || "";
    $mailbox_idnr    = $FORM{'mailbox_idnr'}    || "";
    &connect unless ($dbh);

    if (($DBMailOldVersion eq "1") || ($ACL_ctrl eq "0"))
    {
        &error('This feature is not available in your version of DBMail')
          if ($DBMailOldVersion eq "1");
        &error('This feature has been turned off in the main configuration.')
          if ($ACL_ctrl eq "0");
    }
    &prepare_input($userID);
    $sth = $dbh->prepare(
        "UPDATE $dbmail_acl_table 
SET lookup_flag='$lookup_flag',
read_flag='$read_flag',
seen_flag='$seen_flag',
write_flag='$write_flag',
insert_flag='$insert_flag',
post_flag='$post_flag',
create_flag='$create_flag',
delete_flag='$delete_flag',
administer_flag='$administer_flag'
WHERE user_id = '$userID'
AND mailbox_id = '$mailbox_idnr'
                       "
                        );
    unless ($sth->execute)
    {
        $errormessage =
          "$DBI::errstr ERROR Could not update User: $userID mailbox: $mailbox_idnr ";
        &DBMA_ConnectStatus;
    }
    unless ($dbh->commit)
    {
        $errormessage = "
	ErrorID: $version.err0.68 <br />$DBI::errstr <br />Error: Commit ERROR Public Account err0.68";
        &DBMA_ConnectStatus;
    }
    &Create_User_Account_Window($userID);
    exit;
}
############################################################## - sub delete_ACL_user RQT47
sub delete_ACL_user ($)
{
    &connect unless ($dbh);
    $mailbox_idnr = $FORM{'mailbox_idnr'} || "";
    $userID       = $FORM{'userID'}       || "";
    if (($DBMailOldVersion eq "1") || ($ACL_ctrl eq "0"))
    {
        &error('This feature is not available in your version of DBMail')
          if ($DBMailOldVersion eq "1");
        &error('This feature has been turned off in the main configuration.')
          if ($ACL_ctrl eq "0");
    }
    &prepare_input($userID);
    $sth =
      $dbh->prepare(
        "DELETE FROM $dbmail_acl_table where user_id = '$userID' AND mailbox_id = '$mailbox_idnr'"
      );
    unless ($sth->execute)
    {
        $errormessage = "$DBI::errstr DELETE ACL Failed";
        &DBMA_ConnectStatus;
    }
    unless ($dbh->commit)
    {
        $errormessage =
          "$DBI::errstr <br />Error: Could not delete Public ACL for $userID";
        &DBMA_ConnectStatus;
    }
    &Create_User_Account_Window($userID);
    exit;
}
############################################################## - sub delete_ACL_folder RQT48
sub delete_ACL_folder ($)
{
    &connect unless ($dbh);
    $mailbox_idnr = $FORM{'mailbox_idnr'} || "";
    $userID       = $FORM{'userID'}       || "";
    $PUBLICuserID = ($PUBLICuserID) || $FORM{'PUBLICuserID'} || "";

    if (($DBMailOldVersion eq "1") || ($ACL_ctrl eq "0"))
    {
        &error('This feature is not available in your version of DBMail')
          if ($DBMailOldVersion eq "1");
        &error('This feature has been turned off in the main configuration.')
          if ($ACL_ctrl eq "0");
    }

### delete the ACLs attached to this mailbox first
    $sth =
      $dbh->prepare(
            "DELETE FROM $dbmail_acl_table where mailbox_id = '$mailbox_idnr'");
    $sth->execute();
    unless ($dbh->commit)
    {
        $errormessage =
          "$DBI::errstr <br />Error: Could not delete Public ACL for mailbox $mailbox_idnr";
        &DBMA_ConnectStatus;
    }

### now delete the mailbox
    $sth =
      $dbh->prepare(
        "DELETE FROM $dbmail_mailboxes_table WHERE mailbox_idnr = '$mailbox_idnr'"
      );
    unless ($sth->execute)
    {
        $errormessage =
          "$DBI::errstr DELETE ACL Failed for mailbox_idnr = '$mailbox_idnr <br />";
        &DBMA_ConnectStatus;
    }
    unless ($dbh->commit)
    {
        $errormessage =
          "$DBI::errstr <br />Error: Could not delete Public ACL for $userID";
        &DBMA_ConnectStatus;
    }
    &ACL_FORM;
    exit;
}

############################################################## - sub ACL_FORM RQT44
sub ACL_FORM ($)
{
    &defaults;
    $public_mailboxes = "";
    if (($DBMailOldVersion eq "1") || ($ACL_ctrl eq "0"))
    {
        &error('This feature is not available in your version of DBMail')
          if ($DBMailOldVersion eq "1");
        &error('This feature has been turned off in the main configuration.')
          if ($ACL_ctrl eq "0");
    }
    &meta;
    &menu;
    $sth =
      $dbh->prepare(
        "SELECT user_idnr FROM $dbmail_users_table WHERE LOWER(userid) = LOWER('anyone') LIMIT 1"
      );
    unless ($sth->execute)
    {
        $errormessage = "
	ErrorID: $version.err0.72 <br />$DBI::errstr <br />Failed PUBLIC Query";
        &DBMA_ConnectStatus;
    }
    if (($anyone) = $sth->fetchrow_array)
    {
        $str1 .=
          "	<input type=\"hidden\" name=\"anyone\" value=\"$anyone\" />\n";
        $message2 =
          "<span class=\"gr\">the user \"anyone\" does exist. Good.</span>";
    }
    else
    {
        $message2 =
          "	<span class=\"rd\">DBMA must create the user \"anyone\".</span>";
    }
    $sth =
      $dbh->prepare(
        "SELECT user_idnr FROM $dbmail_users_table WHERE LOWER(userid) = LOWER('__public__') LIMIT 1"
      );
    unless ($sth->execute)
    {
        $errormessage = "
	ErrorID: $version.err0.73 <br />$DBI::errstr <br />Failed __public__ Query";
        &DBMA_ConnectStatus;
    }
    if (($PUBLICuserID) = $sth->fetchrow_array)
    {
        $newRQT  = "45";
        $message =
          "<span class=\"gr\">#Public already exists. That's good.</span>";
        $str3 .=
          "	<input type=\"hidden\" name=\"PUBLICuserID\" value=\"$PUBLICuserID\" />\n";
        &fetch_shared_folders($PUBLICuserID);
    }
    else
    {
        $newRQT  = "46";
        $message =
          "	<span class=\"rd\">No \#Public. DBMA will fix that.</span>";
    }
    print <<"DBMA";
	<div><center><form action="$mythisscript" method="post"><table class="c5" cellspacing="0" cellpadding="0" width="738px" border="0">
DBMA
    &fetch_all_usr_acl_folders;
    print $str if ($str);
    print <<"DBMA";
	<tr><td colspan="3"><h1>DBMA: Access Control List Tools <a target="_blank" onmouseover="self.status='ACL Help';return true" onmouseout="self.status='DBMA';return true" href="DBMA_help.htm#acl"><img style="vertical-align:top;width:18;height:18" src="images/menu_help.jpg" alt="Auto Notify Help File"></a></h1></td></tr>
	<tr><td colspan="3">IMAP4 ACLs provide the option to share IMAP
	folders. If you have no shared folders, this is your tool to create them.<br /><i>System check:</i>
	$message and $message2<br />DBMA assigns
	limited user access rights to &quot;anyone&quot;
	(userID $anyone). User access rights are controlled from the User Account Window. You can
	permit users to have higher priviledged access rights or even administration rights.
	Read <a target="_blank" href="DBMA_help.htm#acl">help.</a>
	<input type="hidden" name="RQT" value="$newRQT" />
DBMA
    my $struct = "type=\"text\" style=\"font-size:9px;cursor:help\"";
    print $str1 if ($str1);
    print $str3 if ($str3);
    print <<"DBMA";
        </td></tr>
	<tr><td><h2><b>Create a Shared Folder:</b><input type="text" name="shared_mailbox" value="$shared_mailbox" size="20" /><input type="submit" value="Create Shared Folder" onmouseover="this.className='clear';" onmouseout="this.className='letsgo';" class="letsgo" onclick="return confirm('CREATE Shared IMAP Folders?')" /></h2></td></tr>
	<tr><td colspan="3"><hr style="background-color:#D6CFDE; color:#D6CFDE;height:8px" /></td></tr></table></form></center></div>
	<div><center><form method="post" action="$mythisscript"><table style="font-size:70%">
	<tr><td colspan="11"><b>Globally Manage Folders</b>: Update or add user access rights. Enter UserID or User's Name below the 'Commit' button. Note: the default $anyone user is <em>anyone</em> on thiis system; and the values (o and 1) below are defaults, not actual permissions. To see permissions select "ACList".</td></tr>
	<tr>
	<td colspan="11"><b>Shared Folder Rights:</b> Updating User<input type="radio" name="RQT" value="49" checked="checked" />  Adding New User<input type="radio" name="RQT" value="50" /></td></tr><tr style="background: #ffffc4">
	<td><input type="submit" value="Commit" onmouseover="this.className='clear';" onmouseout="this.className='letsgo';" class="letsgo" /></td>
	<td>All Shared Folders<br />#Users & #Public</td>
	<td title="lookup: mailbox is visible to LIST/LSUB commands ">lookup</td>
	<td title="read: SELECT the mailbox, perform CHECK, FETCH, PARTIAL SEARCH, COPY from mailbox ">read</td>
	<td title="seen: keep seen/unseen information across session ">seen</td>
	<td title="write: STORE flags other than SEEN and DELETED ">write</td>
	<td title="insert: perform APPEND, COPY into mailbox ">insert</td>
	<td title="post: send mail to submission address for mailbox ">post</td>
	<td title="create: CREATE new sub-mailboxes in any implementation defined hierarchy ">create</td>
	<td title="delete: STORE DELETED flag perform EXPUNGE ">delete</td>
	<td title="administer: perform SETACL ">administer</td></tr>
	<tr class="dl"><td title="User ID"><input type="text" value="$anyone" name="userID" size="4" /></td>
	<td title="Shared Public Folders"><select size="1" name="mailbox_idnr">
	<!-- DBMA public AND individual users shared mailboxes -->
DBMA
    print "	$user_mailboxes" if ($user_mailboxes);
    print <<"DBMA";
	</select></td>
	<td style="background:#ffffc4"><input $struct name="lookup_flag" size="2" value="1" title="lookup: mailbox is visible to LIST/LSUB commands " /></td>
	<td style="background:#ffffc4"><input $struct name="read_flag" size="2" value="1" title="read: SELECT the mailbox, perform CHECK, FETCH, PARTIAL SEARCH, COPY from mailbox " /></td>
	<td style="background:#ffffc4"><input $struct name="seen_flag" size="2" value="1" title="seen: keep seen/unseen information across session " /></td>
	<td style="background:#ffffc4"><input $struct name="write_flag" size="2" value="1" title="write: STORE flags other than SEEN and DELETED " /></td>
	<td style="background:#ffffc4"><input $struct name="insert_flag" size="2" value="1" title="insert: perform APPEND, COPY into mailbox " /></td>
	<td style="background:#ffffc4"><input $struct name="post_flag" size="2" value="1" title="post: send mail to submission address for mailbox " /></td>
	<td style="background:#ffffc4"><input $struct name="create_flag" size="2" value="0" title="create: CREATE new sub-mailboxes in any implementation defined hierarchy " /></td>
	<td style="background:#ffffc4"><input $struct name="delete_flag" size="2" value="0" title="delete: STORE DELETED flag perform EXPUNGE " /></td>
	<td style="background:#ffffc4"><input $struct name="administer_flag" size="2" value="0" title="administer: perform SETACL " /></td></tr>
	<tr><td colspan="11"><hr style="color: #d6cfde; HEIGHT: 8px; background: #d6cfde" /></td></tr></table></form></center></div>
	<div><center><table><tr><td><form method="post" action="$mythisscript"><span class="out"><b>Delete Public shared folders:</b></span>
	<select style="font-size:10px" name="mailbox_idnr">
	<!-- DBMA public shared mailboxes -->
DBMA
    print "	$public_mailboxes" if ($public_mailboxes);
    print <<"DBMA";
	</select><input type="hidden" name="RQT" value="48" />
	<input type="image" value ="submit" src="images/delete.gif" onmouseover="self.status='Delete Shared Folder';return true" onmouseout="self.status='DBMA';return true" style="vertical-align:bottom;width:37px;height:14px" title="Delete Folder" onclick="return confirm('DELETE Shared Folder: Are you sure?')" /><span class="out"> To delete a #Users/folder, go to the User's Account Window</span></form></td></tr>
	<tr><td colspan="6"><hr style="background-color:#D6CFDE; color:#D6CFDE;height:20px" /></td></tr></table></center></div>
DBMA
    end_HTML;
    exit;
}

# - DBMA Tools
############################################################## - sub ACL_LIST RQT43
sub ACL_LIST
{
    if (($DBMailOldVersion eq "1") || ($ACL_ctrl eq "0"))
    {
        &error('This feature is not available in your version of DBMail')
          if ($DBMailOldVersion eq "1");
        &error('This feature has been turned off in the main configuration.')
          if ($ACL_ctrl eq "0");
    }

    &meta;
    &menu;
    my $pubcheck =
      $dbh->prepare(
        "SELECT user_idnr FROM $dbmail_users_table WHERE LOWER(userid) = LOWER('__public__') LIMIT 1"
      );
    $pubcheck->execute;
    if (($PUBLICuserID) = $pubcheck->fetchrow_array)
    {
        $sth = $dbh->prepare("
SELECT $dbmail_users_table.userid,
name,
user_id,
owner_idnr,
mailbox_id,
lookup_flag,
read_flag,
$dbmail_acl_table.seen_flag,
write_flag,
insert_flag,
post_flag,
create_flag,
delete_flag,
administer_flag 
FROM $dbmail_acl_table 
JOIN $dbmail_users_table ON $dbmail_users_table.user_idnr = $dbmail_acl_table.user_id
JOIN $dbmail_mailboxes_table on $dbmail_mailboxes_table.mailbox_idnr = $dbmail_acl_table.mailbox_id  
ORDER BY $dbmail_users_table.userid");
        $sth->execute();
        while (
               (
                $username,    $name,        $user_id,   $owner_idnr,
                $mailbox_id,  $lookup_flag, $read_flag, $seen_flag,
                $write_flag,  $insert_flag, $post_flag, $create_flag,
                $delete_flag, $administer_flag
               )
               = $sth->fetchrow_array
              )
        {
            $owner_idnr =~ s/$PUBLICuserID/\#Public/g;
            $owner_idnr =~ s/$user_id/$username/g;
            $str .=
              "<tr onmouseover=\"this.className=\'hl\';\" onmouseout=\"this.className=\'dl\';\">
	<td title=\"User ID $user_id\">$username</td>
	<td title=\"Mailbox $mailbox_id\">$owner_idnr\/$name</td><td>$lookup_flag</td><td>$read_flag</td><td>$seen_flag</td><td>$write_flag</td><td>$insert_flag</td><td>$post_flag</td><td>$create_flag</td><td>$delete_flag</td><td>$administer_flag</td></tr>\n";
        }
    }
    print <<"DBMA";
	<div><center><table style="width:740px;color:#000090;font-size:70%"><tbody><tr><td colspan="11"><h1><b>DBMA: Access Control List</b><a target="_blank" onmouseover="self.status='ACL Help';return true" onmouseout="self.status='DBMA';return true" href="DBMA_help.htm#acl"><img style="vertical-align:top;width:18;height:18" src="images/menu_help.jpg" alt="ACL Help" /></a></h1></td></tr>
	<tr><td colspan="11">IMAP4 Access Control Lists (ACL's) provide the option to share IMAP folders. The following shows each of the shared folders on your system, to which users have access rights, and what those access rights are. The user 'anyone' applies to everyone on the system. You may see a folder beside 'anyone' and also beside another user's name. This could be done in order to assign a different set of Access Rights (i.e.: Admin SETACL rights allowing remote rights management of the folder) to the single user.
	You may also see a user name and unique folder which indicates that one of the user's own folders has been shared.
	That user will need SETACL rights in order to share access rights with other users. Please see "help"</td></tr>
	<tr><td colspan="11"><hr style="background-color:#D6CFDE; color:#D6CFDE;height:5px" /></td></tr>
	<tr style="background:#ffffc4"><td>User</td><td>Shared Mailbox</td>
	<td title="lookup: mailbox is visible to LIST/LSUB commands ">lookup</td>
	<td title="read: SELECT the mailbox, perform CHECK, FETCH, PARTIAL SEARCH, COPY from mailbox ">read</td>
	<td title="seen: keep seen/unseen information across session ">seen</td>
	<td title="write: STORE flags other than SEEN and DELETED ">write</td>
	<td title="insert: perform APPEND, COPY into mailbox ">insert</td>
	<td title="post: send mail to submission address for mailbox ">post</td>
	<td title="create: CREATE new sub-mailboxes in any implementation defined hierarchy ">create</td>
	<td title="delete: STORE DELETED flag perform EXPUNGE ">delete</td>
	<td title="administer: perform SETACL ">administer</td></tr>
DBMA
    print $str if ($str);
    print <<"DBMA";
	<tr><td colspan="11"><hr style="background-color:#D6CFDE; color:#D6CFDE;height:20px" /></td></tr></tbody></table></center></div>
DBMA
    end_HTML;
    exit;
}
############################################################## - sub fetch_shared_folders
sub fetch_shared_folders ($)
{
    ($public_mailboxes, $mailbox_name, $public_mailboxes, $mailbox_idnr) = "";
    &connect unless ($dbh);
    $sth =
      $dbh->prepare(
        "SELECT mailbox_idnr, name FROM $dbmail_mailboxes_table WHERE owner_idnr='$PUBLICuserID'"
      );
    $sth->execute;
    while (($mailbox_idnr, $mailbox_name) = $sth->fetchrow_array)
    {
        $public_mailboxes .=
          "	<option value=\"$mailbox_idnr\">\#Public\/$mailbox_name</option>\n";
    }

}
############################################################## - sub fetch_usr_acl_folders
sub fetch_usr_acl_folders ($)
{
    $sth = $dbh->prepare(
        "SELECT userid, mailbox_id, name FROM $dbmail_acl_table 
JOIN $dbmail_mailboxes_table ON $dbmail_acl_table.mailbox_id = $dbmail_mailboxes_table.mailbox_idnr 
JOIN $dbmail_users_table ON $dbmail_mailboxes_table.owner_idnr = $dbmail_users_table.user_idnr 
WHERE user_id ='$userID'"
                        );
    unless ($sth->execute)
    {
        $errormessage = "
	ErrorID: $version.err0.69 <br />$DBI::errstr <br />Error: Could not get Public mailboxes";
        &DBMA_ConnectStatus;
    }
    while (($username, $mailbox_idnr, $mailbox_name) = $sth->fetchrow_array)
    {
        $username     = $username     || "DNA";
        $mailbox_idnr = $mailbox_idnr || "none";
        $mailbox_name = $mailbox_name || "none";
        $username =~ s/__public__/\#Public/;
        $user_mailboxes .=
          "<option value=\"$mailbox_idnr\">$username\/$mailbox_name</option>\n";
        $user_mailboxes =~ s/[ \t]+/ /g;
    }
}
############################################################## - sub fetch_all_usr_acl_folders
sub fetch_all_usr_acl_folders
{
    ($user_mailboxes, $username, $mailbox_idnr, $mailbox_name) = "";
    $sth = $dbh->prepare(
        "SELECT userid, mailbox_id, name FROM $dbmail_acl_table 
JOIN $dbmail_mailboxes_table ON $dbmail_acl_table.mailbox_id = $dbmail_mailboxes_table.mailbox_idnr 
JOIN $dbmail_users_table ON $dbmail_mailboxes_table.owner_idnr = $dbmail_users_table.user_idnr
GROUP BY $dbmail_users_table.userid, $dbmail_acl_table.mailbox_id, $dbmail_mailboxes_table.mailbox_idnr, $dbmail_mailboxes_table.name"
                        );
    unless ($sth->execute)
    {
        $errormessage = "
	ErrorID: $version.err0.69 <br />$DBI::errstr <br />Error: Could not get Public mailboxes";
        &DBMA_ConnectStatus;
    }
    while (($username, $mailbox_idnr, $mailbox_name) = $sth->fetchrow_array)
    {
        $username =~ s/__public__/\#Public/;
        $user_mailboxes .=
          "	<option value=\"$mailbox_idnr\">$username\/$mailbox_name</option>\n";
    }
}
############################################################## - sub create_DBMA_MTA_Table
sub create_DBMA_MTA_Table
{
    {
        no warnings 'redefine';
        &defaults;
        &connect unless ($dbh);
        &drop_MTA_Table;

### start MySQL unique

        if ($sqltype =~ /mysql/)
        {
            $sth =
              $dbh->prepare(
                "CREATE TABLE DBMA_MTA (mydestination varchar(35) NOT NULL default '', transport varchar(128) NOT NULL default '', UNIQUE KEY mydestination (mydestination))"
              );
            unless ($sth->execute())
            {
                push(@ERROR, $DBI::errstr);
                &error(
                    'Unable to create DBMA_MTA table. You cannot use this feature unless this is fixed.',
                    @ERROR
                );
            }
            unless ($dbh->commit())
            {
                push(@ERROR, $DBI::errstr);
                &error(
                    'Unable to create DBMA_MTA table. You cannot use this feature unless this is fixed.',
                    @ERROR
                );
            }
            $sth->finish() if ($sth);

            $sth = $dbh->prepare("SELECT sender FROM DBMA_MTA_ACCESS LIMIT 1");
            unless ($sth->execute())
            {
                $sth->finish() if ($sth);
                $sth =
                  $dbh->prepare(
                    "CREATE TABLE DBMA_MTA_ACCESS (myid int(5) NOT NULL auto_increment, sender  varchar(128) NOT NULL default '', action  varchar(25) NOT NULL default 'REJECT', PRIMARY KEY  ( myid ),  UNIQUE KEY  sender  ( sender )) COMMENT='DBMA MTA access table for white or blacklisting senders' AUTO_INCREMENT=1"
                  );
                unless ($sth->execute())
                {
                    push(@ERROR, $DBI::errstr);
                    &error(
                        'Unable to create DBMA_MTA_ACCESS You cannot use this feature unless this is fixed.',
                        @ERROR
                    );
                }
                unless ($dbh->commit())
                {
                    push(@ERROR, $DBI::errstr);
                    &error(
                        'Unable to create DBMA_MTA_ACCESS You cannot use this feature unless this is fixed.',
                        @ERROR
                    );
                }
            }
            $sth->finish() if ($sth);
        }

### start PostgreSQL unique

        if ($sqltype =~ /pgsql/)
        {
            $sth =
              $dbh->prepare(
                "CREATE TABLE DBMA_MTA (mydestination varchar (35) NOT NULL, transport varchar (128) NOT NULL)"
              );
            unless ($sth->execute())
            {
                push(@ERROR, $DBI::errstr);
                &error(
                    'ERROR 4321-6 Unable to create PgSQL DBMA_MTA table. You cannot use this feature unless this is fixed.',
                    @ERROR
                );
            }
            unless ($dbh->commit())
            {
                push(@ERROR, $DBI::errstr);
                &error(
                    'ERROR 4321-7 Unable to create PgSQL DBMA_MTA table. You cannot use this feature unless this is fixed.',
                    @ERROR
                );
            }
            $sth->finish() if ($sth);
            $sth =
              $dbh->prepare(
                "CREATE UNIQUE INDEX mydestination_DBMA_MTA_ukey ON DBMA_MTA(mydestination)"
              );
            unless ($sth->execute())
            {
                push(@ERROR, $DBI::errstr);
                &error(
                    'ERROR 4321-8 Unable to create PgSQL DBMA_MTA Unique Index. You cannot use this feature unless this is fixed.',
                    @ERROR
                );
            }
            unless ($dbh->commit())
            {
                push(@ERROR, $DBI::errstr);
                &error(
                    'ERROR 4321-9 Unable to create PgSQL  DBMA_MTA Unique Index. You cannot use this feature unless this is fixed.',
                    @ERROR
                );
            }
            $sth->finish() if ($sth);

            $sth =
              $dbh->prepare(
                "SELECT tablename FROM pg_tables WHERE schemaname='public' AND tablename like '%mta%' "
              );
            unless ($sth->execute())
            {
                push(@ERROR, $DBI::errstr);
                &error(
                    'ERROR 4321-9a Unable to select TABLENAME from pg_tables where schemaname=\'public\' Is this a very old PGSQL?. You cannot use this feature unless this is fixed.',
                    @ERROR
                );
            }
            while ((my $table) = $sth->fetchrow_array)
            {
                $table =~ tr/[A-Z]/[a-z]/;
                $str .= "$table\n";
                unless ($str =~ m/dbma_mta_access/i)
                {
                    &CREATE_pgsql_mta_access;
                }
            }
        }

### end PostgreSQL unique

        open(TIMESTAMP, "> $DBMA_TIMESTAMP")
          or die(
            "Please check permissions. chmod 777 $path_determined 
Can't create DBMA_TIMESTAMP file"
                );
        print TIMESTAMP "$date";
        close(TIMESTAMP);
        $sth =
          $dbh->prepare(
                "SELECT alias from $dbmail_aliases_table ORDER by client_idnr");
        unless ($sth->execute())
        {
            print $DBI::errstr;
        }
        while (($alias) = $sth->fetchrow_array)
        {
            &filt($alias);
            $alias =~ s/[0-9a-zA-Z\.\-\_\!\#\$\%\&\'\*\+\/\=\?\^]+\@//g;
            $alias =~ s/\@//g;
            $str7 .= "$alias\n";
            open(DOMAINDATA, "> $DBMA_DATA")
              or die(
                "Please check permissions. chmod 777 $path_determined
Can't create DBMA_DATA.DB file?"
                    );
            print DOMAINDATA "$str7";
            close(DOMAINDATA);
        }
        unlink $DBMA_DATA_MTA_TEMP;
        open(DOMAINDATA, "$DBMA_DATA");
        @data = <DOMAINDATA>;
        foreach $line (@data)
        {
            foreach ($line)
            {
                $count++ unless $seen{$_}++;
            }
        }
        $value = $count - 1;
        foreach $line (sort @data)
        {
            foreach ($line)
            {
                my $uniquedomain .= $line unless ($line{$_}++);
                open(TEMPDATA, ">>$DBMA_DATA_MTA_TEMP")
                  or die("Can't open DBMA_DATA_MTA_TEMP file");
                print TEMPDATA "$uniquedomain" if $uniquedomain;
            }
        }
        close(TEMPDATA);
        close(DOMAINDATA);
        open(TEMPDATA, "$DBMA_DATA_MTA_TEMP");
        @newdata = <TEMPDATA>;
        foreach $line (sort @newdata)
        {
            my $uniquedomain = &filt($line) if $line;
            $sth =
              $dbh->prepare(
                "INSERT INTO DBMA_MTA (mydestination, transport) VALUES ('$uniquedomain', '$transport')"
              );
            $sth->execute();
            $dbh->commit();
        }
        close(TEMPDATA);
        $sth->finish() if ($sth);
        push(
            @INFO,
            "DBMA has succcessfully created database tables and inserted your MTA domains plus default DBMail LMTPD transports. If this is an update, the DBMA_MTA table has been dropped and re-created with default settings. You may add transport configurations or edit the DBMail LMTPD defaults on a per domain basis if you desire. Please read \"help\". Select the \"MTA\" icon which should now appear at the top right \(if \"Use MTA\" is set to \"1\"\) and check your stored MTA domains before switching over your MTA.
	Configuration settings must have \"Use MTA...\" set to \"1\" and your MTA must be configured accordingly.<br /><br />DBMA has also created or checked the existance of the DBMA_MTA_ACCESS \(black \/ white lists\) table. If this an update of your MTA Tables, DBMA did not alter your MTA ACCESS table which likely contains an accumulation of data. If this is the first time you have used this tool, you will need to migrate \(using the DBMA \'migrate\' tool\) into your Access table, or enter from a keyboard, the data you wish the MTA to act upon. Click the \"MTA\" icon at the top right and then select \'Go To MTA Access\'."
            );
        &DBMA_Advisor('Congratulations. This step completed successfully.',
                      @INFO);
    }
}
############################################################## - sub CREATE_pgsql_mta_access
sub CREATE_pgsql_mta_access
{
    {
        no warnings 'redefine';
        $dbh->do("CREATE SEQUENCE dbma_mta_access_myid_seq");
        unless ($dbh->commit())
        {
            push(@ERROR, $DBI::errstr);
            &error(
                'Unable to sequence DBMA_MTA_ACCESS. You cannot use this feature unless this is fixed.',
                @ERROR
            );
        }

        $sth =
          $dbh->prepare(
            "CREATE TABLE DBMA_MTA_ACCESS (myid INT8 DEFAULT nextval('dbma_mta_access_myid_seq'), sender varchar (128) NOT NULL, action varchar (25) NOT NULL)"
          );
        unless ($sth->execute())
        {
            push(@ERROR, $DBI::errstr);
            &error(
                'ERROR 4321-10 Unable to execute PgSQL DBMA_MTA_ACCESS. You cannot use this feature unless this is fixed.',
                @ERROR
            );
        }
        unless ($dbh->commit())
        {
            push(@ERROR, $DBI::errstr);
            &error(
                'Unable to commit PgSQL DBMA_MTA_ACCESS. You cannot use this feature unless this is fixed.',
                @ERROR
            );
        }
        $sth->finish() if ($sth);
        $sth =
          $dbh->prepare(
            "CREATE UNIQUE INDEX sender_DBMA_MTA_ACCESS_ukey ON DBMA_MTA_ACCESS(sender)"
          );
        unless ($sth->execute())
        {
            push(@ERROR, $DBI::errstr);
            &error(
                'ERROR 4321-11 Unable to create PgSQL DBMA_MTA_ACCESS Unique Index. You cannot use this feature unless this is fixed.',
                @ERROR
            );
        }
        unless ($dbh->commit())
        {
            push(@ERROR, $DBI::errstr);
            &error(
                'ERROR 4321-12 Unable to create PgSQL DBMA_MTA_ACCESS Unique Index. You cannot use this feature unless this is fixed.',
                @ERROR
            );
        }
        $sth->finish() if ($sth);
    }
}
############################################################## - sub edit_MTA_Domains
sub edit_MTA_Domains
{
    if ($DBMailOldVersion eq "1") { return 0; }

    &defaults;
    &connect unless ($dbh);
    &update_MTA_data;
    my $newline      = "";
    my $ifline       = "";
    my $printdomains = "";
    my $fetch_mtas   = "";
    $colortellsastory = $colortellsastory || "#E7FAE8";
    $fetch_mtas =
      $dbh->prepare(
        "SELECT DISTINCT mydestination, transport FROM DBMA_MTA ORDER BY DBMA_MTA.mydestination"
      );
    $fetch_mtas->execute();

    while (($_dom, $_transport) = $fetch_mtas->fetchrow_array)
    {
        $mtas          .= "	<option value=\"$_dom\">$_dom</option>";
        $dom_transport .= "
	<div><form method=\"post\" action=\"$mythisscript\"><center>
	<table style=\"background-color:#E7FAE8;width:98%\">
	<tr><td style=\"text-align:left;width:35%\">$_dom</td>
	<td><input type=\"hidden\" name=\"add_MTA\" value=\"$_dom\" />
	<input type=\"text\" title=\"$_dom\" $mouseover value=\"$_transport\" name=\"transport\" size=\"45\" />
	<input type=\"hidden\" name=\"RQT\" value=\"59\" />
	<input type=\"image\" value =\"submit\" alt=\"Type your changes and press Edit\" src=\"images/edit.gif\"
	onmouseover=\"self.status=\'Edit Mail Transport\';return true\"
	onmouseout=\"self.status=\'DBMA\';return true\" style=\"width:22px;height:14px\" />
	</td></tr></table></center></form></div>";

    }
    $fetch_mtas->finish();
    print <<"DBMA";
	<tr><td style="font-family: Arial, sans-serif; font-size: 10pt; color: #000080; background-color: $colortellsastory">
	<span style="color:#005A9C;font-size:110%;font-weight:600">MTA Domains and Transports</span></td>	<td style="font-family: Arial, sans-serif; font-size: 10pt; color: #000080; background-color: $colortellsastory">
	<form method="post" action="$mythisscript"><input type="hidden" value="55" name ="RQT" />
	<input title="Create MTA Domains Table." type="submit" value="Create DBMA_MTA Tables" style="float:right;border-style:solid;background-color:#FFd9d9; color:#6C0000; font-family:arial, sans-serif; font-size:11px; font-weight:normal" onclick="return confirm('This will immediately create MTA database tables for your MTA destination domains, mail transports, and MTA Access. If you have already created MTA_Domains and have entered custom transports and domains for your MTA, they will all be returned to default values after this process has completed. This can be easily edited. The default domains are those within your alias fields. The default transport is the DBMail LMTPD on port 24. Do you wish to proceed?')" /></form></td></tr>
	<tr><td style="font-family: Arial, sans-serif; font-size: 10pt; color: #000080; background-color:$colortellsastory;text-align:left">
	<textarea pre-wrap title="Auto Generated MTA Domains" cols="60" rows="5" class="stats" onmouseover="this.className='statsover';self.status='MTA Domains';return true" onmouseout="this.className='stats';self.status='DBMA';return true">
(MTA Domains Auto-Extracted From Aliases.)
DBMA
    open(MATCHED, "$ALIAS_AND_SQL_MATCH");
    @data = <MATCHED>;

    foreach $line (sort @data)
    {
        print $line;
    }
    close(MATCHED);

    print <<"DBMA";
	</textarea></td>
	<td style="font-family: Arial, sans-serif; font-size: 10pt; color: #000080; background-color:$colortellsastory;text-align:left">
	<textarea pre-wrap title="Manually Added MTA Domains" cols="60" rows="5" class="stats" onmouseover="this.className='statsover';self.status='MTA Domains';return true" onmouseout="this.className='stats';self.status='DBMA';return true">
(MTA Domains Manually Added &amp; Not Among Aliases.)
DBMA
    open(NOTINALIASES, "$Not_Found_In_Aliases")
      or die("Can't yet open DB file?");
    @data = <NOTINALIASES>;

    foreach $newline (sort @data)
    {
        print $newline;
    }
    close(NOTINALIASES);

    print <<"DBMA";
	</textarea></td></tr>
	<tr><td colspan="2" style="width:738px">
	<span class="stats" style="font-size:75%">
	<b>MTA domains</b> are those for which your MTA (i.e.: Postfix) accepts mail. <b>Transports</b> are delivery methods configurable per domain. Read the <a target="_blank" href="DBMA_help.htm#use_DBMA_MTA_Domains">MTA Domains help</a> section to learn how to configure your MTA &amp; use this powerful DBMA feature.
	<br /><b>Notes:</b>
	Should a domain reappear after deleted, user(s) still have alias(es) on the deprecated domain and apparently expect mail. Clean up the old email address(es).
	The default 'transport' is dbmail-lmtpd on port 24. Change this to DBMail SMTP or any anti-virus/SPAM daemon or script. For wholesale changes you can recreate the table as often as needed by pressing the "Create DBMA_MTA Tables" button. This will reconstruct the MTA domains list from all the aliases stored on the system and reset to lmtp:24 all transport settings.
	Please read <a target="_blank" href="DBMA_help.htm#use_DBMA_MTA_Domains">MTA HELP</a>.</span></td></tr>
	<tr><td colspan="2" style="font-family: Arial, sans-serif; font-size: 10pt; color: #000080; text-align:left"><br /><h3>Manipulate MTA Domains (Delete, Add or Edit)</h3></td></tr>
	<tr><td title="Highlight a domain to delete" style="font-family: Arial, sans-serif; font-size: 10pt; color: #000080; background-color: $colortellsastory">
	<span class="gr"><b>Delete</b> Selected MTA Domain</span><br /><form method="post" action="$mythisscript"><input type ="hidden" name ="RQT" value="54" />
	<select style="background-color:$colortellsastory;color:black;" name="delete_MTA" size="4">
DBMA
    print $mtas if ($mtas);
    print <<"DBMA";
	</select>
	<input title="Delete Selected MTA Domain" type="image" value ="submit" src="images/delete.gif" onmouseover="self.status=\'Select MTA Domain to delete.\';return true" onmouseout="self.status=\'DBMA\';return true" style="width:37px;height:14px;vertical-align:bottom" /></form></td>
	<td title="type and add MTA Domain and Transport method" style="font-family: Arial, sans-serif; font-size: 10pt; color: #000080; background-color: $colortellsastory"><form method="post" action="$mythisscript"><input type ="hidden" name ="RQT" value="59" />
	<span class="gr"><b>Add</b> MTA Domain</span><br /><input type="text" $mouseover name="add_MTA" size="30" $changecase /><span class="gr">Domain</span><br />
	<input type="text" $mouseover name="transport" size="30" value="dbmail-lmtp:127.0.0.1:24"/><span class="gr">Transport</span><br />
	<input title="ADD MTA Domain" type="submit" value ="Add MTA Domain" onmouseover="this.className='letsgo';" onmouseout="this.className='c7';" class="c7" /></form></td></tr>
	<tr><td colspan="2"><span class="gr"><b>Edit</b> MTA Domains / Transports</span>
	<span class="gr" style="color:black">  Note:
	If NOT enabled in your MTA, this has NO EFFECT.</span>
DBMA

    print $dom_transport if ($dom_transport);
    print "</td></tr>";
    $dom_transport = "";
    undef $dom_transport;
    undef $mtas;
}
############################################################## - sub GUI_MTA_Domains RQT60
sub GUI_MTA_Domains
{
    &connect unless ($dbh);
    &meta;
    &defaults;
    $colortellsastory = $colortellsastory || "#E7FAE8";
    print <<"DBMA";
<title>DBMA MTA Domains and per-Domain Transports Admin :: Connected to $sqlhost</title>
</head>
	<body>
	<div><center><table>
        <tr><td colspan="3" style="font-size:11px;color:#6a6a95;background:#F8F8FF;width:738px"> $version ($sqltype) on $server $date. Please read <a target="_blank" href="DBMA_help.htm#use_DBMA_MTA_Domains">DBMA MTA HELP</a></td></tr>
	<tr><td style="font-size: 11px; color: #000090; text-align: right" colspan="3">

	<div><center><table style="font-size:11px; color:#000090; font-family:sans-serif" cellspacing="0" cellpadding="0" width="100%" border="0">
	<tr><td colspan="2"><h1>DBMA MTA Admin :: Domains and Transports</h1></td></tr></table></center></div>
	<div><center><table style="background:#d6cfde;font-size:11px; color:#000090" cellspacing="0" cellpadding="0" width="100%" border="0">
	<tr><td style="background-color: #d6cfde; text-align: left"><form action="$mythisscript" method="post"><input type="hidden" name ="RQT" value="61" /> <input onmouseover="this.className='letsgo';" onmouseout="this.className='c7';" class="c7" title="Client Access Table for OKs and REJECTS" type="submit" value="Go to MTA Access" /></form></td>
	<td style="background-color: #d6cfde; text-align: right"><form action="$mythisscript" method="post"><input onmouseover="this.className='letsgo';" onmouseout="this.className='c7';" class="c7" title="Return to Main Menu" type="submit" value="Main" /></form></td></tr>
	</table></center></div></td></tr></table></center></div>
DBMA

    print
      "	<div><center><table style=\"border-style:none;background-color:#E7FAE8\" >\n";
    if ($DBMailOldVersion eq "1") { $use_DBMA_MTA_Domains = 0 }
    &edit_MTA_Domains if $use_DBMA_MTA_Domains eq "1";
    print <<"DBMA";
	<tr><td colspan="2"><hr style="background-color:#E7FAE8; color:#D6CFDE;height:20px" /></td></tr>
	</table></center></div>
DBMA
    $dom_transport = "";
    undef $dom_transport;
    undef $mtas;
    end_HTML;
    exit;
}

############################################################## - sub delete_MTA_Domains
sub delete_MTA_Domains
{
    $sth =
      $dbh->prepare("DELETE FROM DBMA_MTA WHERE mydestination = '$delete_MTA'");
    unless ($sth->execute)
    {
        $errormessage = "Error: Unable to delete MTA Domain $delete_MTA.";
        &DBMA_ConnectStatus;
    }
    unless ($dbh->commit)
    {
        $errormessage =
          "$DBI::errstr <br />Error: commit FAIL for delete MTA Domain";
        &DBMA_ConnectStatus;
    }
    undef $delete_MTA;
    &GUI_MTA_Domains;
}
############################################################## - sub add_MTA_Domains RQT59
sub add_MTA_Domains
{
    &defaults;
    my $_update;
    my $newtransport = $FORM{'transport'} || "dbmail-lmtp:127.0.0.1:24";
    $add_MTA =~ tr/[A-Z]/[a-z]/;
    unless ($add_MTA)
    {
        &GUI_MTA_Domains;
    }

    $sth =
      $dbh->prepare(
         "SELECT mydestination FROM DBMA_MTA WHERE mydestination = '$add_MTA'");
    unless ($sth->execute)
    {
        $errormessage = "Could not check if domain exists $DBI::errstr";
        &DBMA_ConnectStatus;
    }

##- If this is an update

    if (   (($mydestination) = $sth->fetchrow_array)
        && ($mydestination = $add_MTA))
    {
        $_update =
          $dbh->prepare(
            "UPDATE DBMA_MTA SET transport = '$newtransport' WHERE mydestination='$add_MTA'"
          );

        unless ($_update->execute)
        {
            $errormessage =
              "Error: Unable to UPDATE MTA Domain $add_MTA. $DBI::errstr";
            &DBMA_ConnectStatus;
        }

        $dbh->commit();
        $sth->finish()     if ($sth);
        $_update->finish() if ($_update);
    }

##- If this is a new transport letsgodowntown

    else
    {
        $sth =
          $dbh->prepare(
            "INSERT INTO DBMA_MTA (mydestination, transport) VALUES ('$add_MTA', '$newtransport')"
          );
        unless ($sth->execute)
        {
            $errormessage =
              "Error: Unable to ADD MTA Domain $add_MTA. $DBI::errstr";
            &DBMA_ConnectStatus;
        }

        $dbh->commit();

    }
    undef $transport;
    undef $newtransport;
    undef $add_MTA;
    &GUI_MTA_Domains;
}
############################################################## - sub drop_MTA_Table
sub drop_MTA_Table
{
    $sth = $dbh->prepare("DROP TABLE DBMA_MTA");
    $sth->execute();
    $dbh->commit();
    $sth->finish() if ($sth);
}
############################################################## - sub update_MTA_data
sub update_MTA_data
{
    $sth =
      $dbh->prepare(
                "SELECT alias from $dbmail_aliases_table ORDER by client_idnr");
    unless ($sth->execute())
    {
        print
          "Either you have a Configuration Problem or your are upgrading to a new version with different data. Check your configs.";
    }
    while (($alias) = $sth->fetchrow_array)
    {
        &filt($alias);
        $alias =~ s/[0-9a-zA-Z\.\-\_\!\#\$\%\&\'\*\+\/\=\?\^]+\@//g;
        $alias =~ s/\@//g;
        $str7 .= "$alias\n";
        open(DOMAINDATA, "> $DBMA_DATA")
          or die(
            "Please check permissions. chmod 777 $path_determined 
Can't create DBMA_DATA.DB file?"
                );
        print DOMAINDATA "$str7";
        close(DOMAINDATA);
    }
    unlink $DBMA_DATA_MTA_TEMP;
    open(DOMAINDATA, "$DBMA_DATA");
    @data = <DOMAINDATA>;
    foreach $line (sort @data)
    {
        foreach ($line)
        {
            next if /^(\s)*$/;
            my $uniquedomain .= $line unless ($line{$_}++);
            open(TEMPDATA, ">>$DBMA_DATA_MTA_TEMP")
              or die("Can't open DBMA_DATA_MTA_TEMP file");
            print TEMPDATA "$uniquedomain" if $uniquedomain;
        }
    }
    close(TEMPDATA);
    close(DOMAINDATA);
    $sth =
      $dbh->prepare(
          "SELECT mydestination FROM DBMA_MTA ORDER BY DBMA_MTA.mydestination");
    unless ($sth->execute())
    {
        print
          "You are not fully configured yet. Try pressing \"Go!\" twice to re-initiate data files. \n";
    }
    while ((my $mydestination) = $sth->fetchrow_array)
    {
        $str6 .= "$mydestination\n";
    }
    $sth->finish() if ($sth);
    open(SQLDATA, "> $DBMA_SQL_MTA");
    print SQLDATA "$str6";
    close(SQLDATA);
    undef $str6;
    undef $mydestination;
    &MTA_Compare_Alias_and_SQL;
}

############################################################## - sub GUI_MTA_Access RQT61
sub GUI_MTA_Access ()
{
    my $show_list = $FORM{'show_list'} || 0;
    my $myid      = $FORM{'myid'}      || "";
    my $listall   = $listall           || "";
    &connect unless ($dbh);
    &meta;
    &defaults;
    $RQT   = 63               || 0;
    $limit = $FORM{limit}     || 200;
    $LIMIT = ("LIMIT $limit") || 200;
    my $access_search = $FORM{'access_search'} || "";
    my $_sender       = $_sender               || "";
    my $_action       = $_action               || "";

    if (   ($FORM{'access_search'})
        && ($access_search =~ m/[a-z]|[A-Z]|[0-9]/i))
    {
        $sth =
          $dbh->prepare(
            "SELECT myid, sender, action FROM DBMA_MTA_ACCESS WHERE sender LIKE '%$access_search%' LIMIT 20"
          );

        unless ($sth->execute)
        {
            $errormessage = "Failed DBMA_MTA_ACCESS Search $DBI::errstr";
            &DBMA_ConnectStatus;
        }
        $numrows = $sth->rows;

        while (($myid, $_sender, $_action) = $sth->fetchrow_array)
        {
            my $_sender = $_sender || "";
            my $_action = $_action || "";
            $listall .= "
	<div><form action=\"$mythisscript\" method=\"post\"><center><table style=\"font-size:12px;font-family:arial,sans-serif;width:738px;background-color: #E7FAE8\">
	<tr><td style=\"width:30px; color:#6a6a95\">$myid</td><td style=\"width:250px\">$_sender</td>
	<td style=\"width:250px\">$_action</td>
	<td colspan=\"2\"><input type=\"hidden\" value=\"$myid\" name=\"myid\" />
	<input type=\"hidden\" value=\"$_sender\" name=\"sender\" />
	<input type=\"hidden\" name =\"RQT\" value=\"63\" /><input type=\"hidden\" name =\"bypass\" value=\"3\" /><input type=\"hidden\" name =\"show_list\" value=\"1\" />
	<input type=\"image\" value =\"submit\" src=\"images/delete.gif\" onmouseover=\"self.status=\'Delete Access Entry $_sender\';return true\" onmouseout=\"self.status=\'DBMA\';return true\" style=\"width:37px;height:14px\" title=\"Delete number $myid Access entry $_sender\" onclick=\"return confirm(\'DELETE Access entry $_sender?\')\" />
	</td></tr></table></center></form></div>\n";
        }
    }

    print <<"DBMA";
<title>DBMA MTA Access Administration :: Connected to $sqlhost</title>
</head>
	<body>
	<div><center><table>
        <tr><td colspan="3" style="font-size:11px;color:#6a6a95;background:#F8F8FF;width:738px"> $version ($sqltype) on $server $date. Please read <a target="_blank" href="DBMA_help.htm#use_DBMA_MTA_Domains">DBMA MTA HELP</a></td></tr>
	<tr><td style="font-size: 11px; color: #000090; text-align: right" colspan="3">
	<div><center><table style="font-size:11px; color:#000090; font-family: sans-serif, arial, helvetica;" cellspacing="0" cellpadding="0" width="100%" border="0">
	<tr><td colspan="2"><h1>DBMA MTA Admin :: Access</h1></td></tr></table></center></div>
	<div><center><table style="background:#d6cfde;font-size:11px; color: #000090;" cellspacing="0" cellpadding="0" width="100%" border="0">
	<tr><td style="background-color: #d6cfde; text-align: left">
	<form action="$mythisscript" method="post"><input type="hidden" name ="RQT" value="64" /><input onmouseover="this.className='letsgo';" onmouseout="this.className='c7';" class="c7" title="Migrate Tool" type="submit" value="Migrate" /></form></td>
	<td style="background-color: #d6cfde; text-align: left"><form action="$mythisscript" method="post"><input type="hidden" name ="RQT" value="60" /><input onmouseover="this.className='letsgo';" onmouseout="this.className='c7';" class="c7" title="Domains and Transports" type="submit" value="Go to MTA Domains" /></form></td>
	<td style="background-color: #d6cfde; text-align: right"><form action="$mythisscript" method="post"><input onmouseover="this.className='letsgo';" onmouseout="this.className='c7';" class="c7" title="Return to Main Menu" type="submit" value="Main" /></form></td></tr>
	</table></center></div></td></tr></table></center></div>

DBMA
    $colortellsastory = $colortellsastory || "#E7FAE8";
    print <<"DBMA";
	<div><center><table style="width:738px;background-color: #E7FAE8">
	<tr><td><span style="color:#005A9C;font-size:110%;font-weight:600">MTA </span>
	<span style="color: #005A9C; font-size: 110%; font-weight: 600">Access</span><br />
	<span class="stats"><b>A 'Whitelist / Blacklist tool':</b> This is an
	excellent method for fine-grain tuning your MTA access *or* you can rely completely
	on this method for access control in most MTAs, certainly in Postfix and Sendmail.
	Your MTA must be compiled *--with-XXsql* and configured to use MySQL or PostgreSQL.
	If you already use MTA Domains for your destination addresses and or mail transport,
	the appropriate tables for this feature exist.
	If not, please read help and learn how to do this from the configuration window.
	With this tool, you create the 'sender' / 'action' directive for the MTA.
	<br />Please read <a target="_blank" href="DBMA_help.htm#DBMA_MTA_Access">MTA HELP</a>
        </span></td></tr></table></center></div>
	<div><center><table style="font-size:14px;font-family:arial,sans-serif;width:738px;background-color: #E7FAE8"><tr>
DBMA
    my ($OKs, $rejects, $other);
    $sth = $dbh->prepare("SELECT COUNT(*) FROM DBMA_MTA_ACCESS");
    $sth->execute();

    while (($_) = $sth->fetchrow_array)
    {
        print "
	<td style=\"background-color: #FFFFC4\">Currently: $_</td>";
    }

    $sth =
      $dbh->prepare(
        "SELECT COUNT(*) FROM DBMA_MTA_ACCESS WHERE action = 'OK' OR action = 'ok' OR action = 'Ok'"
      );
    $sth->execute();

    while (($OKs) = $sth->fetchrow_array)
    {
        print "
	<td colspan=\"2\" style=\"background-color: #FFFFC4\">Ok = $OKs</td>";
    }

    $sth =
      $dbh->prepare(
        "SELECT COUNT(*) FROM DBMA_MTA_ACCESS WHERE action = 'REJECT' OR action = 'reject' OR action = 'Reject'"
      );
    $sth->execute();
    while (($rejects) = $sth->fetchrow_array)
    {
        print "
	<td colspan=\"2\" style=\"background-color: #FFFFC4\">Rejects = $rejects</td>";
    }

    $sth =
      $dbh->prepare(
        "SELECT COUNT(*) FROM DBMA_MTA_ACCESS WHERE action LIKE '%REJECT_UNVERIFIED_SENDER%' OR action LIKE '%REJECT_UNVERIFIED_SENDER%'"
      );
    $sth->execute();
    while (($other) = $sth->fetchrow_array)
    {
        print "
	<td colspan=\"2\" style=\"background-color: #FFFFC4\">REJECT_UNVERIFIED_SENDER = $other</td>";
    }
    $sth->finish() if ($sth);
    $_sender_ = $_sender || $access_search || $FORM{'access_search'} || "";
    print <<"DBMA";
	</tr></table></center></div>
	<div><form action="$mythisscript" method="post"><center><table style="font-size:11px;font-family:arial,sans-serif;width:738px;background-color: #E7FAE8">
	<tr><td colspan="4"><h4>Action</h4></td><td colspan="2"><h4>Sender</h4></td></tr>
	<tr><td><input type="radio" name="action" value="REJECT" /><small>Reject</small></td>	
	<td colspan="2"><input type="text" style="font-face=arial,sans-serif;font-size:9px;background-color:#E7FAE8" name="action" size="20" />Other
	<input type="reset" onmouseover="this.className='letsgo';" onmouseout="this.className='c7';" class="c7" value="Clear" /></td>
	<td colspan="3"> <input type="text" $mouseover name="sender" value="$_sender_" size="35" />Host or IP</td></tr>
	<tr><td><input type="radio" name="action" value="OK" /><small>OK</small></td>
	<td colspan="2"><input type="radio" name="action" value="REJECT_UNVERIFIED_SENDER" /><small>REJECT_UNVERIFIED_SENDER</small></td>
	<td colspan="3"><input type="hidden" name ="RQT" value="62" />
	<input type="submit" onmouseover="this.className='letsgo';" onmouseout="this.className='c7';" class="c7" value="Add / Update" name="dbma_mta_access" /></td></tr>
	<tr><td colspan="6"><hr style="background-color:#D6CFDE; color:#D6CFDE;height:20px" /></td></tr>
	</table></center></form></div>
	<div><center><table style="font-size:10px;font-family:arial,sans-serif;width:738px;background-color: #E7FAE8">		
	<tr><td colspan="3"><form action="$mythisscript" method="post">Search for:
        <input type ="text" $mouseover size="25" name ="access_search" value="$access_search" />
	<input type="hidden" name ="RQT" value="61" />
	<input type="submit" onmouseover="this.className='letsgo';" onmouseout="this.className='c7';" class="c7" value="Search" name="Search" /></form></td>
	<td colspan="2"><form action="$mythisscript" method="post">
	<input type="hidden" name ="RQT" value="61" /><input type="hidden" name ="show_list" value="1" />
	<input type="submit" onmouseover="this.className='letsgo';" onmouseout="this.className='c7';" class="c7" value="Show List" /> Limit<input type="text" size="4" $mouseover name="limit" value="$limit" /></form></td></tr>
DBMA

    print <<"DBMA";
	<tr><td colspan="6"><hr style="background-color:#D6CFDE; color:#D6CFDE;height:1px" /></td></tr>
	</table></center></div>
DBMA

    if (   ($show_list == 0)
        && ($access_search =~ m/[a-z]|[A-Z]|[0-9]/i))
    {

        print <<"DBMA";
	<div><center><table style="font-size:10px;font-family:arial,sans-serif;width:738px;background-color: #E7FAE8">
	<tr><td style="width:30px">ID</td><td style="width:250px">Sender</td><td style="width:250px">Action</td><td colspan="2">Options</td></tr>
	<tr><td colspan="6"><hr style="background-color:#D6CFDE; color:#D6CFDE;height:1px" /></td></tr>
	</table></center></div>
DBMA
        print "<div>$listall</div>" if ($listall);
    }
    if ($show_list == 1)
    {
        $sth =
          $dbh->prepare(
                "SELECT * FROM DBMA_MTA_ACCESS ORDER BY action, sender $LIMIT");
        unless ($sth->execute)
        {
            $errormessage = "Show List failed $DBI::errstr";
            &DBMA_ConnectStatus;
        }
        while (($myid, $_sender, $_action) = $sth->fetchrow_array)
        {
            $listall .= "
	<div><form action=\"$mythisscript\" method=\"post\"><center><table style=\"font-size:12px;font-family:arial,sans-serif;width:738px;background-color: #E7FAE8\">
	<tr><td style=\"width:30px\; color:#6a6a95\">$myid</td><td style=\"width:250px\">$_sender</td>
	<td style=\"width:250px\">$_action</td>
	<td colspan=\"2\"><input type=\"hidden\" value=\"$myid\" name=\"myid\" />
	<input type=\"hidden\" value=\"$_sender\" name=\"sender\" />
	<input type=\"hidden\" name =\"RQT\" value=\"63\" /><input type=\"hidden\" name =\"bypass\" value=\"3\" /><input type=\"hidden\" name =\"show_list\" value=\"1\" />
	<input type=\"image\" value =\"submit\" src=\"images/delete.gif\" onmouseover=\"self.status=\'Delete Access Entry $_sender\';return true\" onmouseout=\"self.status=\'DBMA\';return true\" style=\"width:37px;height:14px\" title=\"Delete number $myid Access entry $_sender\" onclick=\"return confirm(\'DELETE Access entry $_sender?\')\" />
	</td></tr></table></center></form></div>\n";
        }
        print <<"DBMA";
	<div><center><table style="font-size:10px;font-family:arial,sans-serif;width:738px;background-color: #E7FAE8">
	<tr><td style="width:30px">ID</td><td style="width:250px">Sender</td><td style="width:250px">Action</td><td colspan="2">Options</td></tr>
	<tr><td colspan="6"><hr style="background-color:#D6CFDE; color:#D6CFDE;height:1px" /></td></tr>
	</table></center></div>
DBMA
        print $listall if ($listall);
    }

    $_sender = "";
    $_action = "";
    $listall = "";
    end_HTML;
    exit;
}
############################################################## - sub MTA_Access_SQL RQT62
sub MTA_Access_SQL
{
    &defaults;
    my $access_search = $FORM{'access_search'};
    my $_sender       = "";
    my $_action       = "";
    my $sender        = $FORM{'sender'} || "evilhackers.com";
    my $action        = $FORM{'action'} || "reject";
    my $show_list     = $FORM{'show_list'} || 0;
    $sender =~ tr/[A-Z]/[a-z]/;
    $action =~ tr/[a-z]/[A-Z]/;
    $output = $output || "";

    if ($sender eq " ")
    {
        &GUI_MTA_Access;
        exit;
    }

    $sth =
      $dbh->prepare(
                 "SELECT sender FROM DBMA_MTA_ACCESS WHERE sender = '$sender'");
    unless ($sth->execute)
    {
        $errormessage = "Failed check sender exists $DBI::errstr";
        &DBMA_ConnectStatus;
    }

    if (   (($output) = $sth->fetchrow_array)
        && ($output = $sender))
    {
        my $_update =
          $dbh->prepare(
            "UPDATE DBMA_MTA_ACCESS SET action = '$action' WHERE sender='$sender'"
          );
        unless ($_update->execute)
        {
            $errormessage =
              "Error: Unable to UPDATE MTA Domain $sender $DBI::errstr";
            &DBMA_ConnectStatus;
        }
        $dbh->commit();
        $sth->finish()     if ($sth);
        $_update->finish() if ($_update);
    }
    else
    {
        $sth =
          $dbh->prepare(
            "INSERT INTO DBMA_MTA_ACCESS (sender, action) VALUES ('$sender', '$action')"
          );
        unless ($sth->execute)
        {
            $errormessage =
              "Error: Unable to ADD MTA Access $sender. $DBI::errstr";
            &DBMA_ConnectStatus;
        }
        $dbh->commit();
    }
    undef $action;
    undef $sender;

    if ($show_list == 1)
    {
        &GUI_MTA_Access($show_list);
    }
    &GUI_MTA_Access;
    exit;
}
############################################################## - sub delete_MTA_Access RQT63
sub delete_MTA_Access

{
    my $myid   = $FORM{'myid'};
    my $sender = $FORM{'sender'};
    my $bypass = $FORM{'bypass'};
    if (($FORM{'sender'}) && ($RQT eq "63") && ($bypass eq "3"))
    {
        $sth =
          $dbh->prepare(
            "DELETE FROM DBMA_MTA_ACCESS WHERE sender = '$sender' OR myid = '$myid'"
          );
        unless ($sth->execute)
        {
            $errormessage = "Error: Unable to delete MTA Access $sender.";
            &DBMA_ConnectStatus;
        }
        unless ($dbh->commit)
        {
            $errormessage =
              "$DBI::errstr <br />Error: Unable to delete MTA Access $sender.";
            &DBMA_ConnectStatus;
        }
        undef $sender;
        $sender = "";
        &GUI_MTA_Access;
        $bypass = "";
    }
    exit;
    undef $sender;
    $sender = "";
    $bypass = "";
    &GUI_MTA_Access;
}
############################################################## - sub MTA_Access_Migrate RQT64

sub MTA_Access_Migrate ($)
{
    &meta;
    &defaults;
    my $user     = `whoami`;
    my $filename = $FORM{'filename'} || $filename || "";
    my $_sender  = $FORM{'_sender'} || $_sender || "";
    my $_action  = $FORM{'_action'} || $_action || "";
    my $lines;

    {
        no warnings 'redefine';
        if ($FORM{'filename'})
        {
            unless (-R $filename)
            {
                $perm_error =
                  "<br />ALERT: DBMA cannot read $filename. Please check that it exists or fix permissions.";
                &MTA_Access_Migrate($perm_error);
            }

            &connect unless ($dbh);

            open(DATA, "$filename") or die("Can't open $filename file?");

            @data = <DATA>;
            foreach $line (sort @data)
            {
                my $data .= &filt($line);
                $line =~ s/^(.*[\n\r]+)\1+/$1/mg;
                ($_sender, $_action) = split(/\s+/, $line);
                $lines .= "<tr><td>$_sender  |  $_action</td></tr>\n";
                $dbh->do(
                    "INSERT INTO DBMA_MTA_ACCESS (sender, action) VALUES ('$_sender', '$_action')"
                );

            }

            unless ($dbh->commit())
            {
                print "Something went wrong while adding entries. $DBI::errstr";
            }
            close(DATA);
            &connect unless ($dbh);
        }
    }
    print <<"DBMA";
	<title>DBMA MTA Access Data Migration :: Connected to $sqlhost</title>
	</head><body><div><center><table>
	<tr><td style="font-size: 11px; color: #6a6a95; background-color: #F8F8FF; background-repeat: repeat; background-attachment: scroll; width: 738px; text-align: Left; background-position: 0% 50%">$version ($sqltype $sqlhost) from $server $date. Please read <a target="_blank" href="DBMA_help.htm#use_DBMA_MTA_Domains">DBMA MTA HELP</a></td></tr>
	<tr><td style="font-size: 11px; color: #000090; text-align: right"><div><center><table style="font-size: 11px; color: #000090; font-family: sans-serif, arial, helvetica; cellspacing=" cellpadding="0" width="100%" border="0">
	<tr><td colspan="2" style="text-align: Left"><h1>DBMA MTA Admin :: Access Data Migration</h1></td></tr></table></center></div>
	<div><center><table style="background-color: #d6cfde;font-size: 11px; color: #000090; cellspacing=" cellpadding="0" width="100%" border="0">
	<tr><td style="background-color: #d6cfde; text-align: left"><form action="$mythisscript" method="post"><input type="hidden"name="RQT" value="61" /><input onmouseover="this.className='letsgo';" onmouseout="this.className='c7';" class="c7" title="DBMA MTA Access" type="submit" value="Go To MTA Access" /></form></td>
	<td style="background-color: #d6cfde; text-align: left"><form action="$mythisscript" method="post"><input type="hidden" name="RQT" value="60" /><input onmouseover="this.className='letsgo';" onmouseout="this.className='c7';" class="c7" title="Domains and Transports" type="submit" value="Go to MTA Domains" /></form></td>
	<td style="background-color: #d6cfde; text-align: right"><form action="$mythisscript" method="post"><input onmouseover="this.className='letsgo';" onmouseout="this.className='c7';"class="c7" title="Return to Main Menu" type="submit" value="Main" /></form></td>
	</tr></table></center></div></td></tr></table></center></div>
	<div><center><table style="width:738px;background-color: #E7FAE8">
	<tr><td><span style="color:#005A9C;font-size:110%;font-weight:600">MTA</span>
	<span style="color: #005A9C; font-size: 110%; font-weight: 600">Access Migrate</span><br />
	<span class="stats">This tool enables the migration of text-based mail access files into the DBMA_MTA_ACCESS database table. The format of the file should be</span> 
	<p><span class="stats">"sender" -whitespace- "action" (no quotes in file).</span></p>
	<ul><li><span class="stats">The file must be Readable by</span>
DBMA
    print "	$user" if ($user);
    print <<"DBMA";
	<span class="stats">the user which your HTTPD runs as, and must *not* contain duplicates.</span></li>
	<li><span class="stats">You must type an absolute path to the file.</span></li>
	<li><span class="stats">example: '/etc/postfix/sender_access' </span></li></ul></td></tr></table></center></div>
	<div><center><table style="font-size:14px;font-family:arial,sans-serif;width:738px;background-color: #E7FAE8">
	<tr><td style="background-color: #FFFFC4"><form method="post" action="$mythisscript"><input type="text" name="filename" value="$filename" size="50" /><input onmouseover="this.className='letsgo';" onmouseout="this.className='c7';" 
	class="c7" title="DBMA MTA Access" type="submit" value="Migrate File To Database" /><input type="hidden"name="RQT" value="64" />
	<input type="reset" onmouseover="this.className='letsgo';" onmouseout="this.className='c7';" class="c7" value="Clear" name="clear" /></form></td></tr>
	<tr><td style="background-color: #FFFFC4">Results:
DBMA

    print $perm_error                          if ($perm_error);
    print "Found the following in $filename\n" if ($filename);
    print "	</td></tr>";
    print $lines if ($lines);
    print "</table></center></div>\n";
    end_HTML;
}
############################################################## - sub meta
sub meta
{
    print <<"DBMA";
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="author" content="micheal j. o'brien" />
<link rel="shortcut icon" href="/favicon.ico" />
<link rel="stylesheet" type="text/css" href="DBMA.css" />
DBMA
}
############################################################## - sub header
sub header
{
    $userID =~ s/any//g if $userID;
    &meta;
    print <<"DBMA";
<title>DBMail Administrator (DBMA) connected to $sqlhost from $server</title>
<style type="text/css">
/*<![CDATA[*/
td.c0 a:hover{display: block; margin 0;color:black;text-decoration:underline;background: lime}
td.c0 a{display:block;margin 0}	
td.ad {color:#000090;vertical-align:middle;height:15px;border-radius:4px}	
td{border-style:none;margin-top:0px;text-align:left;vertical-align:top;font-size:11px}
td{margin-top:1px;text-align:left;vertical-align:top}
/*]]>*/
</style></head>
	<body>
DBMA
    &radio_bar;
}
############################################################## - sub menu
sub menu
{
    $userID =~ s/any//g if $userID;
    if (   ($use_DBMA_MTA_Domains eq "1")
        && ($RESTRICTGroupID eq "any"))
    {
        $MTA_GUI =
          "	<a href=\"$mythisscript?MTA\"><img src=\"images/MTA.gif\" style=\"border-style:none;width24px;height:17px\" alt=\"MTA Domains GUI\" /></a>\n";
    }
    if ($RESTRICTGroupID =~ m/[0-9]/i)
    {
        print
          "	<title>$RESTRICTGroupIDName - DBMail Administrator (DBMA) Connected to $sqlhost from $server</title>\n";
    }
    else
    {
        print
          "	<title>DBMail Administrator (DBMA) Connected to $sqlhost from $server</title>\n";
    }
    &defaults;
    $MTA_GUI = $MTA_GUI || "";
    print <<"DBMA";
	</head><body>
	<div><center><table cellspacing="0" cellpadding="0" style="background-color:#F8F8FF;width:738px;font-family:arial;sans-serif;color:#6a6a95;background-color:#F8F8FF;font-size:70%">
	<tr><td style="width:738px">$version ($dbmail_ver $sqltype $sqlhost) from $server $peopledate</td><td style="float:right;width:130px">
	$MTA_GUI
	<a href="DBMA_installation_configuration.htm" rel="external"><img src="images/menu_help.jpg" style="border-style:none;width18px;height:18px" alt="General Help, Installation and Setup." /></a>
	<a target="_blank" href="DBMA_logsearch.cgi"><img src="images/log_search.jpg" style="border-style:none;width18px;height:18px" alt="Log Search" /></a> <a target="_blank" href="http://www.dbma.ca/"><img src="images/DBMA_ico.jpg" style="border-style:none;width18px;height:18px" alt="Updates" /></a>
	<a href="DBMA_help.htm" rel="external"><img src="images/helpico.jpg" style="border-style:none;width18px;height:18px" alt="Menu Help" /></a></td></tr></table></center></div>
DBMA
    &radio_bar;
}
############################################################## - sub radio_bar
sub radio_bar ($)
{

    $loginterval = ($loginterval) || $FORM{'loginterval'} || '4';
    $limit       = ($limit)       || $FORM{'limit'}       || '200';
    $userID      = $userID        || "";
    $str11       = '';
    &connect unless ($dbh);
    $GroupID = ($GroupID) || $FORM{'GroupID'} || $defaultGroup_ID;
    if ($RESTRICTGroupID eq "any")
    {
        $sth =
          $dbh->prepare(
            "SELECT DISTINCT client_idnr from $dbmail_users_table WHERE client_idnr > '0' ORDER BY client_idnr"
          );
        $sth->execute();
        while (($myGroupID) = $sth->fetchrow_array)
        {
            $str11 .= "	<option value=\"$myGroupID\">$myGroupID</option>\n";
        }
        $sth->finish() if ($sth);
        $str11 =~
          s/\<option value\=\"$GroupID\">/\<option selected value\=\"$GroupID\">/g;
        print <<"DBMA";
	<div><center><table style="background-color:#F8F8FF;"><tr><td style="text-align:left;width:40%"><form method="post" action="$mythisscript"><input type="hidden" name="RQT" value="2" />
	<small>User</small> <input onmouseover="this.className='front';self.status='Search for a user and open their Account';return true" onmouseout="this.className='back';self.status='DBMA';return true" type="text" title="Please enter the user ID or name." name="userID" value="$userID" size="10" />
	<input title="Search for user" type="submit" onmouseover="this.className='clear';self.status='Search for a user and open their Account';return true" onmouseout="this.className='letsgo';self.status='DBMA';return true" class="letsgo" value="User Search" /></form></td>
	<td style="text-align:left;width:30%"><form method="post" action="$mythisscript"><input type="hidden" value="all_in_this_group" name="RQT" />
	<select  class="front" onmouseover="this.className='back';self.status='List all the Users for this group.';return true" onmouseout="this.className='letsgo';self.status='DBMA';return true" title="Select the group to display." name ="GroupID">
DBMA
        print "	$str11" if ($str11);
        print <<"DBMA";
	</select>
	<input  class="letsgo" onmouseover="this.className='clear';self.status='List users in this group.';return true" onmouseout="this.className='letsgo';self.status='DBMA';return true" title="List All Users in Group $GroupID" type="submit" value="List Group Users" class="letsgo" /><input type="hidden" name="required" value="GroupID" /></form></td>
	<td style="text-align:left;width:30%"><form method="post" action="$mythisscript">
	<input type="hidden" name="RQT" value="aliases_in_this_group" />
	<select class="front" onmouseover="this.className='back';self.status='List all the Aliases for this group.';return true" onmouseout="this.className='letsgo';self.status='DBMA';return true" title="Select the group to display" name ="GroupID">
DBMA
        print "	$str11" if ($str11);
        print <<"DBMA";
	</select>
	<input title="List aliases in Group $GroupID" type="submit" onmouseover="this.className='clear';self.status='List the aliases for this group.';return true" onmouseout="this.className='letsgo';self.status='DBMA';return true" class="letsgo" value="List Group Aliases" />
	<input type="hidden" name="required" value="GroupID" /></form></td></tr>
	<tr><td colspan="3" width="738px" style="font-family:sans-serif, arial, helvetica;font-size:11px;background-color:#d6cfde;color:#000090;text-align:right;">
	<form method="post" action="$mythisscript"><table border="0" width="100%" cellspacing="0" cellpadding="0" style="width:738px; font-family: sans-serif, arial, helvetica; font-size: 11px; background-color: #d6cfde; color: #000090">
	<tr><td style="color: #FFFFc4; font-size: 10pt; font-weight: bold">Users <a target="_blank" onmouseover="self.status='Help';return true" onmouseout="self.status='DBMA';return true" href="DBMA_help.htm#add_user"><img class="q" src="images/q.gif" alt="help" /></a></td>
	<td style="color: #FFFFc4; font-size: 10pt; font-weight: bold">Alias <a target="_blank" onmouseover="self.status='Help';return true" onmouseout="self.status='DBMA';return true" href="DBMA_help.htm#add_aliases"><img class="q" src="images/q.gif" alt="help" /></a></td>
	<td style="color: #FFFFc4; font-size: 10pt; font-weight: bold">Forward <a target="_blank" onmouseover="self.status='Help';return true" onmouseout="self.status='DBMA';return true" href="DBMA_help.htm#add_forward"><img class="q" src="images/q.gif" alt="help" /></a></td>
	<td style="color: #FFFFc4; font-size: 10pt; font-weight: bold">Special <a target="_blank" onmouseover="self.status='Help';return true" onmouseout="self.status='DBMA';return true" href="DBMA_help.htm#add_auto_notify"><img class="q" src="images/q.gif" alt="help" /></a></td>
	<td style="color: #FFFFc4; font-size: 10pt; font-weight: bold">Global <a target="_blank" onmouseover="self.status='Help';return true" onmouseout="self.status='DBMA';return true" href="DBMA_help.htm#list_all_usrs_all_groups"><img class="q" src="images/q.gif" alt="help" /></a></td></tr>
	<tr><td><input type="radio" name="RQT" value="3" />Add User</td>
	<td><input type="radio" name="RQT" value="7" />Add Aliases</td>
	<td><input type="radio" name="RQT" value="14" />Add Forward</td>
	<td><input type="radio" name="RQT" value="16" />Add Auto Notify</td>
	<td><input type="radio" name="RQT" value="any" />All users all groups</td></tr>
	<tr><td title="Delete Users individually or entire Groups of Users."><input onmouseover="this.className='caution';self.status='This will open a window for deleting users or entire groups.';return true" onmouseout="this.className='c7';self.status='DBMA';return true" type="radio" name="RQT" value="5" />Delete User/Group</td>
	<td><input type="radio" name="RQT" value="8" />Delete Aliases</td>
	<td><input type="radio" name="RQT" value="8" />Delete Forward</td>
	<td><input type="radio" name="RQT" value="18" />Delete Auto Notify</td>
DBMA

        if ($sqltype =~ /pgsql/)
        {
            print <<"DBMA";
	<td title="Fix mismatched Groups in users/aliases. Set status 003 for all mail marked for deletion. Delete unattached mailboxes. Mark for deletion orphaned messages."><input type="radio" name="RQT" value="36" />Database Cleanup</td></tr>
DBMA
        }
        if ($sqltype =~ /mysql/)
        {
            print <<"DBMA";
	<td title="This can take a very long time. Defragments InnoDB tables and indexes, fixes mismatched Groups in users/aliases. Set status 003 for all mail marked for deletion. Delete unattached mailboxes. Mark for deletion orphaned messages.">
	<input onclick="return alert('This can take a long time.\\n\\n1) Defragments InnoDB tables and indexes \(takes the most time\).\\n2) Fixes mismatched Groups in users aliases.\\n3) Sets status 003 for all mail marked for deletion\\n4) Marks for deletion orphaned messages\\n5) Deletes orphaned mailboxes and content\\n\\nIf you are OK with that, press GO button and if not press CLEAR\\n\\n Clicking Ok clears this message.')" type="radio" name="RQT" value="36" />Database Cleanup</td></tr>
DBMA
        }
        print <<"DBMA";
	<tr><td><input onmouseover="this.className='go';" onmouseout="this.className='c7';" type="radio" name="RQT" value="21" />Email a User</td>
	<td><input type="radio" name="RQT" value="19" />List All Aliases</td>
	<td><input type="radio" name="RQT" value="20" />List All Forwards</td>
	<td><input type="radio" name="RQT" value="22" />List Auto Notifications</td>
	<td><input type="radio" name="RQT" value="23" />Logins Last<input type="text" name="loginterval" value="$loginterval" size="1" onmouseover="this.className='sm2';" onmouseout="this.className='sm1';" class="sm1" />hrs</td></tr>
	<tr><td colspan="5" style="text-align:center"><hr style="background-color:#BDB3CA; color:#BDB3CA;height:4px;width:95%" /></td></tr>
	<tr><td><input type="radio" name="RQT" value="24" />Configuration<!--<input type="radio" name="RQT" value="60" />MTA--></td>
	<td><input type="radio" name="RQT" value="26" />Encrypt Help </td><!--DBMA Copyright Mike at dbma.ca-->
	<td><input type="radio" name="RQT" value="44" />ACL<input type="radio" name="RQT" value="43" />ACList</td>
	<td style="text-align:right">Show <input title="Display how many lines&#63; For thousands use &#34;k&#34;" type="text" value="$limit" name="limit" size="3" onmouseover="this.className='sm2';" onmouseout="this.className='sm1';" class="sm1" /> lines. <input type="submit" title="Press to initiate selected tool or to refresh all stats." class="c7" value="Go!" onmouseover="this.className='letsgo';" onmouseout="this.className='c7';" /></td>
	<td style="text-align:center"><a title="Clear All" href="$mythisscript?makeshortform"><img onmouseover="this.className='clear';self.status='DBMA';return true" onmouseout="this.className='clear';self.status='DBMA';return true" src="images/clear.jpg" alt="Clear all selects and stats. &#40;Clear everything&#41;" style="width:47px;height:22px;border-style:none;vertical-align:top" /></a></td></tr></table></form></td></tr></table></center></div>
DBMA
    }
    else
    {
        print <<"DBMA";
	<div><center><table><tr><td style="text-align:left;width:37%"><form method="post" action="$mythisscript"><input type="hidden" name="RQT" value="2" />
	<small>User</small> <input type="text" $mouseover title="Please enter the user ID or name." name="userID" value="$userID" size="12" $changecase />
	<input title="Search for user" type="submit" onmouseover="this.className='clear';" onmouseout="this.className='letsgo';" class="letsgo" value="User Search" /></form></td>
	<td style="text-align:left;width:31%"><form method="post" action="$mythisscript"><input type="hidden" value="all_in_this_group" name="RQT" /><small>Group $RESTRICTGroupID</small><input type="hidden" value="$RESTRICTGroupID" name="GroupID" />
	<input title="All Users in Group $RESTRICTGroupID" type="submit" value="List Users" onmouseover="this.className='clear';" onmouseout="this.className='letsgo';" class="letsgo" /><input type="hidden" name="required" value="GroupID" /></form></td>
	<td style="text-align:left;width:31%"><form method="post" action="$mythisscript"><small>Group $RESTRICTGroupID</small><input type="hidden" value="$RESTRICTGroupID" name="GroupID" size="3" />
	<input type="hidden" name="RQT" value="aliases_in_this_group" /><input title="List aliases in Group $RESTRICTGroupID" type="submit" onmouseover="this.className='clear';" onmouseout="this.className='letsgo';" class="letsgo" value="List Aliases" /><input type="hidden" name="required" value="GroupID" /></form></td></tr>
	<tr><td colspan="3" width="738px" style="font-family:sans-serif, arial, helvetica;font-size:11px;background-color:#d6cfde;color:#000090;text-align:right;">
	<form method="post" action="$mythisscript"><table border="0" width="100%" cellspacing="0" cellpadding="0" style="width:738px; font-family: sans-serif, arial, helvetica; font-size: 11px; background-color: #d6cfde; color: #000090">
	<tr><td style="color: #FFFF99; font-size: 10pt; font-weight: bold">Users</td>
	<td style="color: #FFFF99; font-size: 10pt; font-weight: bold">Aliases</td>
	<td style="color: #FFFF99; font-size: 10pt; font-weight: bold">Forwards</td>
	<td style="color: #FFFF99; font-size: 10pt; font-weight: bold">Special</td>
	<td style="color: #FFFF99; font-size: 10pt; font-weight: bold">Admin</td></tr>
	<tr><td><input type="radio" name="RQT" value="3" />Add User</td>
	<td><input type="radio" name="RQT" value="7" />Add Aliases </td>
	<td><input type="radio" name="RQT" value="14" />Add Forward</td>
	<td><input type="radio" name="RQT" value="16" />Add Auto Notify</td>
	<td><input type="radio" name="RQT" value="21" />Email a User</td></tr>
	<tr><td colspan="5" style="text-align:center">
	<hr style="background-color:#BDB3CA; color:#BDB3CA;height:4px;width:95%" /></td></tr>
	<tr><td class="c16" colspan="5"><big>$RESTRICTGroupIDName Administration </big></td></tr>
	<tr><td class="c16" colspan="5"><a target="_blank" href=\"DBMA_installation_configuration.htm\" onclick=\"return confirm(\'________________$RESTRICTGroupIDName Help_______________________\\n\\nUSER ADMINISTRATION\\nis done from the user account window.\\nDelete, modify, add aliases, change password and more.\\n\\nTO FIND A USER:\\n\\n1 - Type user name at top left and press *Search*.\\n\\n or \\n\\n2 - Select the user name from a list using *List Users* button\\n\\n\\n Click *OK* for more help or *CANCEL* to close.\')\">Help</a></td></tr>
	<tr><td colspan="3" style="text-align:right"></td>
	<td style="text-align:right"><input type="submit" title="Press to initiate selected tool." class="c7" value="Go!" onmouseover="this.className='letsgo';" onmouseout="this.className='c7';" /></td>
	<td style="text-align:center"><a title="Clear All" href="$mythisscript"><img src="images/clear.jpg" alt="Clear. Refresh stats" style="width:47px;height:22px;border-style:none;vertical-align:top" /></a></td></tr></table></form></td></tr></table></center></div>
DBMA
    }
    undef $userID;
}
############################################################## - sub restrict_group_help
sub restrict_group_help
{
    print <<"DBMA";
	<div><center><table style="background-position: top right;background-attachment: fixed; background-repeat: no-repeat;background-image: url(images/bg.jpg);font-size:80%"><tr><td style="width:737px;background:#ffffc4" colspan="2">General Functions for $RESTRICTGroupIDName</td></tr>
	<tr><td width="455"><b>User Search</b></td>
	<td style="width:278px"></td></tr>
	<tr><td style="width:737px" colspan="2">Enter a user ID number, a user name or an email address and search for that specific user to fetch the account window for that user. This function appears throughout the various GUI windows.</td></tr>
	<tr><td style="width:455px"><b>List $RESTRICTGroupIDName Users</b></td><td style="width:278px"></td></tr>
	<tr><td style="width:737px" colspan="2">This is the primary tool for listing users in the RestrictGroup configuration. Enter the group number to list all users in that group. This function appears throughout the various GUI windows in all versions.</td></tr>
	<tr><td style="width:455px"><b>List $RESTRICTGroupIDName Aliases</b></td><td style="width:278px"></td></tr>
	<tr><td width="737" colspan="2">Enter the group number to list all aliases in that group (hard-coded in the Restrict Group configuration. This function appears throughout the various GUI windows.</td></tr>
	<tr><td style="width:737px;background:#ffffc4" colspan="2">Users</td></tr> 
	<tr><td style="width:455px"><b>Add User</b></td><td style="width:278px"></td></tr> 
	<tr><td style="width:737px" colspan="2">Open a user interface for adding users.&nbsp;This function has a number of administratively-set default options which can be configured by your Administrator or service provider. Default presets include auto-generate password, auto-generate alias, group, and password encryption method. FEATURE NOTE: When auto-create alias has been set to &quot;1&quot; in the 'Configuration Options', the 'Add User' interface recycles after typing the user name and pressing &quot;Add New User&quot;.
	In this manner even a large group of users can be populated into the database in minutes. Otherwise, the Add User function causes a proof-reading and modification window to open with the new data set out.</td></tr> 
	<tr><td style="width:455px"><b>Email A User</b></td><td style="width:278px"></td></tr> 
	<tr><td style="width:737px" colspan="2">Send an email to any user. Be careful not to send the user an encrypted password. It won't do them any good. This feature allows a notice to be sent to the user when a mail quota has been reset, a password changed, or any administrative function you may wish to advise the user about.</td></tr> 
	<tr><td style="width:737px;background:#ffffc4" colspan="2">Aliases</td></tr> 
	<tr><td style="width:733px" colspan="2"><b>Add Aliases</b><b><br /></b>Opens a user interface to add an alias for a user. This can also be performed from the Modify User Account Window  or from the Group List. The best place to do this is the User Account Window.</td></tr> 
	<tr><td style="width:737px;background:#ffffc4" colspan="2">Forwards</td></tr>
	<tr><td width="733" colspan="2"><b>Add Forward</b><b><br /></b>Open user interface to add a mail forward. Type the email address to be forwarded and the address to which it should be sent.</td></tr> 
	<tr><td style="width:737px;background:#ffffc4" colspan="2">Mail Notifications</td></tr> 
	<tr><td style="width:733px" colspan="2"><b>Add Auto Notify</b><b><br /></b>Open user interface to add a mail notification for a user.</td></tr></table></center></div>
DBMA
}
############################################################## - end
# Copyright 2004-2008 and supported by Mike O'Brien micheal@e-me.ca
1;
