create database books;
use books;

CREATE TABLE `Book_Ratings` (
  `User-ID` int(11) NOT NULL default '0',
  `ISBN` varchar(13) NOT NULL default '',
  `Book-Rating` int(11) NOT NULL default '0',
  PRIMARY KEY  (`User-ID`,`ISBN`)
);

CREATE TABLE `Books` (
  `ISBN` varchar(13) binary NOT NULL default '',
  `Book-Title` varchar(255) default NULL,
  `Book-Author` varchar(255) default NULL,
  `Year-Of-Publication` int(10) unsigned default NULL,
  `Publisher` varchar(255) default NULL,
  `Image-URL-S` varchar(255) binary default NULL,
  `Image-URL-M` varchar(255) binary default NULL,
  `Image-URL-L` varchar(255) binary default NULL,
  PRIMARY KEY  (`ISBN`)
);

CREATE TABLE `Users` (
  `User-ID` int(11) NOT NULL default '0',
  `Location` varchar(250) default NULL,
  `Age` int(11) default NULL,
  PRIMARY KEY  (`User-ID`)
);
