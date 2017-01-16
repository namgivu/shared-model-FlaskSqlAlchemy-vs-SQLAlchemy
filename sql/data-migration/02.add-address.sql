CREATE TABLE `addresses` (
  `id`              int AUTO_INCREMENT,
  `street_address`  text NOT NULL,
  PRIMARY KEY (`id`)
);

ALTER TABLE `users` ADD COLUMN billing_address_id  INT;
ALTER TABLE `users` ADD COLUMN shipping_address_id INT;

ALTER TABLE `users` ADD constraint FOREIGN KEY(billing_address_id)   REFERENCES addresses(id);
ALTER TABLE `users` ADD constraint FOREIGN KEY(shipping_address_id)  REFERENCES addresses(id);


set @billingAddress= '122 Soome Street1, Ciity1, Countryy1';
set @shippingAddress='333 Soome Street2, Ciity2, Countryy2';
INSERT INTO `addresses`(street_address) VALUES
  (@billingAddress),
  (@shippingAddress)
;

set @userName='uuserWithAddreess';
set @billingAddressId  = (select id from addresses where street_address=@billingAddress);
set @shippingAddressId = (select id from addresses where street_address=@shippingAddress);
insert into users(user_name, billing_address_id, shipping_address_id) values
                 (@userName, @billingAddressId,  @shippingAddressId)
;
