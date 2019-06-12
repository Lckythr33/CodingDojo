INSERT INTO `twitter`.`tweets` (`tweet`, `user_id`, `created_at`, `updated_at`) VALUES ('test', '2', '2014-02-01 00:00:01', '2014-02-01 00:00:01');
SELECT * FROM tweets WHERE id=18;
UPDATE `twitter`.`tweets` SET `tweet` = 'change' WHERE (`id` = '18');
DELETE FROM `twitter`.`tweets` WHERE (`id` = '18');
SELECT * FROM tweets;