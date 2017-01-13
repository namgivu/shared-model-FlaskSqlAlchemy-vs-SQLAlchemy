drop database IF EXISTS sandbox_sqlalchemy;
create database sandbox_sqlalchemy;

use sandbox_sqlalchemy;

CREATE TABLE `users` (
  `id`        int AUTO_INCREMENT,
  `user_name` text NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `user_emails` (
  `id`    int AUTO_INCREMENT,
  `email` text NOT NULL,
  `user_id` int NOT NULL,
  FOREIGN KEY(user_id) references users(`id`),
  PRIMARY KEY (`id`)
);

set @user01Name='user1';
set @user02Name='user22';
insert into users(user_name) values
  (@user01Name),
  (@user02Name)
;

set @user01Id=(select id from users where user_name=@user01Name);
set @user02Id=(select id from users where user_name=@user02Name);
insert into user_emails(email, user_id) values
  ('user1-email1@doomain.comm',   @user01Id),
  ('user1-email22@doomain.comm',  @user01Id),
  ('user22-email@doomain.comm',   @user02Id)
;
