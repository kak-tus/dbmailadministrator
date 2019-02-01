#!/usr/bin/perl

# DbMailAdministrator (DBMA) V3.2.x Copyright 2004-2016 **
#      Trouble? Contact: micheal@dbma.ca
#################################################################
our $dir   = `pwd -P`;
our $clear = "clear";
chop($dir);
our $dir_up = $dir;
$dir_up =~ s/\/dbmailadministrator//g;

&dowork;

sub dowork
{
    our $update          = "http://www.dbma.ca/DBMA_SQL_V3.zip";
    our $DB_CONFIG       = $dir . '/DBMA_CONFIG.DB';
    our $DB_OPTIONS      = $dir . '/DBMA_OPTIONS.DB';
    our $DBMA_DATA       = $dir . '/DBMA_DATA.DB';
    our $DBMA_DATA_MTA   = $dir . '/DBMA_DATA_MTA.DB';
    our $DBMA_SQL_MTA    = $dir . '/DBMA_SQL_MTA.DB';
    our $DBMA_GROUP_DATA = $dir . '/DBMA_GROUP_DATA.DB';
    our $DBMA_STATS      = $dir . '/DBMA_STATS.DB';
    our $DBMA_Matched_SQL_And_Aliases =
      $dir . '/DBMA_Matched_SQL_And_Aliases.DB';
    our $DBMA_Missing_In_SQL_MTA   = $dir . '/DBMA_Missing_In_SQL_MTA.DB';
    our $DBMA_Not_Found_In_Aliases = $dir . '/DBMA_Not_Found_In_Aliases.DB';

    our $DB_TMP      = $dir_up . '/';
    our $OLD_TARBALL = $dir_up . '/DBMA_SQL_V3.zip';

    my $command1 =
      "cp $DBMA_Not_Found_In_Aliases $DB_TMP && cp $DBMA_Missing_In_SQL_MTA $DB_TMP && cp $DBMA_Matched_SQL_And_Aliases $DB_TMP && cp $DBMA_STATS $DB_TMP && cp $DBMA_GROUP_DATA $DB_TMP && cp $DBMA_SQL_MTA $DB_TMP && cp $DBMA_DATA_MTA $DB_TMP && cp $DBMA_DATA $DB_TMP && cp $DB_CONFIG $DB_TMP && cp $DB_OPTIONS $DB_TMP && rm $OLD_TARBALL";
    my $command2 =
      "cd $dir_up && wget $update && tar -xvf DBMA_SQL_V3.tar && rm DBMA_SQL_V3.tar";
    my $command3 =
      "mv $dir_up/DBMA_Not_Found_In_Aliases.DB $dir && mv $dir_up/DBMA_Missing_In_SQL_MTA.DB $dir && mv $dir_up/DBMA_Matched_SQL_And_Aliases.DB $dir && mv $dir_up/DBMA_STATS.DB $dir && mv $dir_up/DBMA_GROUP_DATA.DB $dir && mv $dir_up/DBMA_SQL_MTA.DB $dir && mv $dir_up/DBMA_DATA_MTA.DB $dir && mv $dir_up/DBMA_DATA.DB $dir && mv $dir_up/DBMA_CONFIG.DB $dir && mv $dir_up/DBMA_OPTIONS.DB $dir && chmod 777 $dir && cd $dir && chmod 755 DBMA.cgi && chmod 777 DBMA_TIMESTAMP && chmod 777 *.DB";
    system $command1;
    system $command2;
    system $command3;
    sleep 1;
    system $clear;
    print
      "\n\nDONE If you saw no error messages, it worked. \n\n\n 1) please \"chown -R \<user:group\> $dir\" to the user:group of your HTTPD \n\n\n 2) Then OPEN DBMA and PRESS GO! twice to re-initiated the tmp files\n\n\n\n\n";
    exit;
}
############################################################## - end
# Copyright 2004-2008 and supported by Mike O'Brien http://www.dbma.ca
