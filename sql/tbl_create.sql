SET time_zone='-05:00';

create table user(
	username varchar(20) NOT NULL,
	firstname varchar(20) NOT NULL,
	lastname varchar(20) NOT NULL,
	password varchar(20) NOT NULL,
	email varchar(40) NOT NULL,
	PRIMARY KEY (username)
);

create table album(
	albumid BIGINT unsigned NOT NULL,
	title varchar(50) NOT NULL,
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
	lastupdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
	username varchar(20) NOT NULL,
	PRIMARY KEY (albumid),
	FOREIGN KEY (username) REFERENCES user(username)
);

create table photo(
	format char(3) NOT NULL,
    picid varchar(40)  NOT NULL,
	date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
	PRIMARY KEY (picid)
);

create table contain(
	sequencenum BIGINT unsigned NOT NULL,
	albumid BIGINT unsigned NOT NULL,
	picid varchar(40) NOT NULL,
	caption varchar(255) NOT NULL,
	PRIMARY KEY (sequencenum),
	FOREIGN KEY (albumid) REFERENCES album(albumid),
    FOREIGN KEY (picid) REFERENCES photo(picid)
);

