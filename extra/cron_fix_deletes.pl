#!/usr/bin/perl
use DBI();
use strict;
use warnings;

# DbMailAdministrator (DBMA) V3.2.x Copyright 2004-2016 **
#      Trouble? Contact: micheal@dbma.ca
#################################################################

# EXAMPLE
#    Example use in crontab
# 1       3       *       *       *       root    /usr/bin/perl /usr/local/www/dbmailadministrator/extra/cron_fix_deletes.pl >> /dev/null 2>&1
# CONFIGURE
############################################### - Configure here please for Postgres or MySQL
my $DBMA_dbname     = "dbmail";
my $DBMA_port       = "3306";
my $DBMA_host       = "localhost";
my $DBMA_user       = "dbmail";
my $DBMA_password   = "dbmail";
my $sqltype         = "mysql"; # or pgsql
###############################################
my ( $message_idnr, $dbh, $sth );    
if ($sqltype eq "pgsql")
    {                                           
unless (                                                                        
    $dbh = DBI->connect(                                                        
"DBI:Pg:user=$DBMA_user;password=$DBMA_password;dbname=$DBMA_dbname;port=$DBMA_port;host=$DBMA_host",                                                           
        "$DBMA_user",                                                           
        "$DBMA_user",                                                           
        { AutoCommit => 1 }                                                     
    )                                                                           
  )                                                                             
{                                                                               
    print "$DBI::errstr";                                                       
    exit;                                                                       
}                                                                               
&fix_deletes;                                                                   
}
elsif ($sqltype =~ /mysql/)
{
unless (
    $dbh = DBI->connect(
"DBI:mysql:user=$DBMA_user;password=$DBMA_password;database=$DBMA_dbname;port=$DBMA_port;host=$DBMA_host",
        "$DBMA_user",
        "$DBMA_user",
        { AutoCommit => 1 }
    )
  )
{
    print "$DBI::errstr";
    exit;
}
&fix_deletes;
}
############################################### - fix_deletes
sub fix_deletes {
## -Phase 1
    $sth =
      $dbh->prepare(
"UPDATE dbmail_messages SET status = '003' where  deleted_flag = '1' OR status >0"
      );
    $sth->execute();
    $sth->finish();
    $sth = $dbh->prepare(
        "SELECT message_idnr from dbmail_messages
JOIN dbmail_mailboxes ON dbmail_messages.mailbox_idnr = dbmail_mailboxes.mailbox_idnr
LEFT JOIN dbmail_users ON dbmail_users.user_idnr = dbmail_mailboxes.owner_idnr
WHERE dbmail_users.user_idnr IS NULL"
    );
    $sth->execute();
## -Phase 2
# And now if we found some orphaned messages we will set their status to 002.
# Why 002? In case you accidentally deleted a user and want to reinstate them in the next few hours or seconds
# as the case may be in terms utility crontab runs.
    while ( ($message_idnr) = $sth->fetchrow_array ) {
        $sth =
          $dbh->prepare(
"UPDATE dbmail_messages SET status = '002', deleted_flag = '1' where  message_idnr = '$message_idnr'"
          );
        $sth->execute();
    }
    $sth->finish();
## -Phase 3
# What follows handles some peculiar event triggered by a wayward web or email client and
# InnoDB cascade breaks on a dbmail-util run and
# leaves the messages alive but deletes the mailboxes when a user is deleted.
# Let's clean this database nicely.
    $sth = $dbh->prepare(
        "UPDATE dbmail_messages
LEFT JOIN dbmail_mailboxes ON dbmail_messages.mailbox_idnr = dbmail_mailboxes.mailbox_idnr
SET dbmail_messages.deleted_flag = '1', status = '001' WHERE dbmail_mailboxes.mailbox_idnr IS NULL"
    );
    $sth->execute();
    $sth->finish();
    print "\nCleanup Success.\n
cron_fix_deletes.pl has run successfully scheduling all rows with \n
deleted_flag=1 to status=003 and orphaned messages to status=002 \n
You have until the next dbmail-util run to review the changes.\n
                                 DbMailAdministrator (DBMA)\n\n";
    exit;
}
