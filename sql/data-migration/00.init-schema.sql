drop database IF EXISTS sandbox_sqlalchemy;
create database sandbox_sqlalchemy;

use sandbox_sqlalchemy;

CREATE TABLE `users` (
  `id`        int AUTO_INCREMENT,
  `user_name` text NOT NULL,
  `primary_email_id` int,
  PRIMARY KEY (`id`)
);

CREATE TABLE `user_emails` (
  `id`    int AUTO_INCREMENT,
  `email` text NOT NULL,
  `user_id` int NOT NULL,
  FOREIGN KEY(user_id) references users(`id`),
  PRIMARY KEY (`id`)
);

ALTER TABLE `users` add
  FOREIGN KEY(primary_email_id) references user_emails(`id`)
;

set @user01Name='user1';
set @user02Name='user22';
insert into users(user_name) values
  (@user01Name),
  (@user02Name)
;

set @user01Id=(select id from users where user_name=@user01Name);
set @user02Id=(select id from users where user_name=@user02Name);

set @user1Email1='user1-email1@doomain.comm';
set @user1Email2='user22-email1@doomain.comm';
set @user2Email='user22-email@doomain.comm';

insert into user_emails(email, user_id) values
  (@user1Email1,   @user01Id),
  (@user1Email2,   @user01Id),
  (@user2Email,   @user02Id)
;

update `users`
  set primary_email_id=(select id from user_emails where email=@user1Email1)
  where id=@user01Id
;

update `users`
  set primary_email_id=(select id from user_emails where email=@user2Email)
  where id=@user02Id
;