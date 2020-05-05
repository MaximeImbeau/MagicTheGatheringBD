USE testdb;


CREATE TABLE IF NOT EXISTS Utilisateur(courriel varchar(50), motpasse varchar(64), nom varchar (20), balance float(4, 2) DEFAULT 0.0, PRIMARY KEY (courriel));
INSERT INTO Utilisateur(courriel, motpasse, nom) VALUES("edgeLord@mail.com", "pain", "Bob");

CREATE TABLE IF NOT EXISTS Suivre(email_user varchar(50), email_followed_user varchar(50), FOREIGN KEY (email_user) REFERENCES Utilisateur(courriel), PRIMARY KEY (email_user, email_followed_user), FOREIGN KEY (email_followed_user) REFERENCES Utilisateur(courriel));
INSERT INTO Suivre(email_user, email_followed_user) VALUES("edgeLord@mail.com", "maxime@mai.ca");

CREATE TABLE IF NOT EXISTS cards(name varchar(50), manaCost integer, rarity varchar(15), type varchar(15), imageSource varchar(100), PRIMARY KEY (name));
INSERT INTO cards VALUES ('Air Elemental', 3, 'uncommon', 'creature', 'https://img.scryfall.com/cards/large/front/f/9/f9de2b27-f7d1-4e2d-97b2-2bb236b6fb10.jpg?1562002439'),
('Ifnir Deadlands', 0, 'common', 'land', 'https://img.scryfall.com/cards/large/front/0/b/0b88728b-9b18-40c6-b634-f87f8da83665.jpg?1562788706'),
('Icatian Scout', 1, 'common', 'creature', 'https://img.scryfall.com/cards/large/front/d/b/db63ad7f-6dc4-4249-b360-46ec5569a5a9.jpg?1562935964'),
('Nylea, Keen-Eyed', 3, 'mythic rare', 'creature', 'https://img.scryfall.com/cards/large/front/2/a/2a022e36-5074-4875-ac30-aaa09b7ef421.jpg?1581481404'),
('Bad Moon', 2, 'rare', 'enchantment', 'https://img.scryfall.com/cards/large/front/7/f/7f5eb613-dedc-4b0f-a5f2-32a3821ad923.jpg?1559591581'),
('Ancient Tomb', 0, 'uncommon', 'land', 'https://img.scryfall.com/cards/large/front/3/0/30e401e3-282b-4524-87e1-c6cd50cd6d00.jpg?1562053283'),
('Shinen of Fury''s Fire', 3, 'common', 'creature', 'https://img.scryfall.com/cards/large/front/6/6/66c05acc-7cb2-4a06-9e6f-cb9419298385.jpg?1562494191'),
('Courier Griffin', 4, 'common', 'creature', 'https://img.scryfall.com/cards/large/front/4/d/4d3afc71-f5db-45c3-96b2-8454b7f33542.jpg?1562913062'),
('Waking Nightmare', 3, 'common', 'sorcery', 'https://img.scryfall.com/cards/large/front/1/b/1b892f31-816e-47c0-98b9-d71008bb6af4.jpg?1562757956'),
('Willbender', 2, 'uncommon', 'creature', 'https://img.scryfall.com/cards/large/front/7/c/7c35a94e-4449-4093-9652-5db0ec8b8bdd.jpg?1562844293'),
('Encircling Fissure', 3, 'uncommon', 'instant', 'https://img.scryfall.com/cards/large/front/5/7/575da7cb-6715-43df-a7b4-a4ca00216a1d.jpg?1562915475'),
('White Ward', 1, 'uncommon', 'enchantment', 'https://img.scryfall.com/cards/large/front/1/d/1d8b9830-2b79-44d1-a2f7-964194521d9e.jpg?1559593023'),
('Blue Mana Battery', 4, 'rare', 'artifact', 'https://img.scryfall.com/cards/large/front/c/d/cd2cb84e-c079-486e-87ad-d188fe38bc76.jpg?1559603819'),
('Thornwind Faeries', 3, 'common', 'creature', 'https://img.scryfall.com/cards/large/front/0/5/050280f0-97b2-446e-8166-21f434d06e4d.jpg?1562896031'),
('Sakura-Tribe Elder', 2, 'common', 'creature', 'https://img.scryfall.com/cards/large/front/c/8/c83be2b7-0373-4389-9aa0-523db58f4d2a.jpg?1586298192'),
('Castle Embereth', 0, 'rare', 'land', 'https://img.scryfall.com/cards/large/front/8/b/8bb8512e-6913-4be6-8828-24cfcbec042e.jpg?1572491168'),
('Castle Garenbrig', 0, 'rare', 'land', 'https://img.scryfall.com/cards/large/front/e/3/e3c2c66c-f7f0-41d5-a805-a129aeaf1b75.jpg?1572491176'),
('Castle Vantress', 0, 'rare', 'land', 'https://img.scryfall.com/cards/large/front/0/a/0a8b9d37-e89c-44ad-bd1b-51cb06ec3e0b.jpg?1572491190'),
('Cathedral of Serra', 0, 'uncommon', 'land', 'https://img.scryfall.com/cards/large/front/e/6/e65356e6-0ead-49fd-b069-be1ea9b1c105.jpg?1562861376'),
('Castle Ardenvale', 0, 'rare', 'land', 'https://img.scryfall.com/cards/large/front/7/f/7f910495-8bd7-4134-a281-c16fd666d5cc.jpg?1572491161'),
('Castle Locthwain', 0, 'rare', 'land', 'https://img.scryfall.com/cards/large/front/1/9/195383c1-4723-40b0-ba53-298dfd8e30d0.jpg?1572491183'),
('Coral Atoll', 0, 'uncommon', 'land', 'https://img.scryfall.com/cards/large/front/b/9/b92121b6-b12e-4fe3-9afb-f2c77c2796ac.jpg?1561956168'),
('Desert of the Indomitable', 0, 'common', 'land', 'https://img.scryfall.com/cards/large/front/7/d/7d42aa0c-0408-4b0d-bec5-9861dbcf9ee1.jpg?1562804804'),
('Dormant Volcano', 0, 'uncommon', 'land', 'https://img.scryfall.com/cards/large/front/8/3/83f90da4-9b01-431d-83b1-f54c132efec1.jpg?1562274604'),
('The Flame of Keld', 2, 'uncommon', 'enchantment', 'https://img.scryfall.com/cards/large/front/3/2/324399ed-3d6e-4b4c-8f3d-b7802e2ecadf.jpg?1562733690'),
('Anarchist', 5, 'uncommon', 'creature', 'https://img.scryfall.com/cards/large/front/f/4/f4a989b0-4305-418c-a326-f89958f0c306.jpg?1562744013'),
('Spire Serpent', 5, 'common', 'creature', 'https://img.scryfall.com/cards/large/front/9/a/9a14e2a4-484b-46e4-a5a1-c66cb13be178.jpg?1562613282'),
('Infernal Caretaker', 4, 'common', 'creature', 'https://img.scryfall.com/cards/large/front/8/a/8a028a30-6242-4d87-9501-d1826ecb69b0.jpg?1562922909'),
('Lys Alana Huntmaster', 4, 'common', 'creature', 'https://img.scryfall.com/cards/large/front/1/f/1f0f7367-83ce-4429-b3e9-401390d94eca.jpg?1561935659'),
('Kaervek the Merciless', 7, 'rare', 'creature', 'https://img.scryfall.com/cards/large/front/4/4/444fa5a5-b5b0-4555-bd69-67c1c0cbf317.jpg?1562909155'),
('Harrow', 3, 'common', 'instant', 'https://img.scryfall.com/cards/large/front/e/3/e309c1fc-3a7c-4624-8b48-9b152c2590ae.jpg?1562617636'),
('Mossfire Egg', 1, 'uncommon', 'artifact', 'https://img.scryfall.com/cards/large/front/1/f/1fd66433-b0e9-453d-9a27-ea0efb158dac.jpg?1562900887'),
('Death''s Duet', 3, 'common', 'sorcery', 'https://img.scryfall.com/cards/large/front/6/6/666647e9-afc3-4b04-bad9-b4ce11438ee4.jpg?1562429831'),
('Watchwolf', 2, 'uncommon', 'creature', 'https://img.scryfall.com/cards/large/front/e/c/eca620db-7870-43fb-ba77-eda7f0bc33f0.jpg?1541002946'),
('Defeat', 2, 'common', 'sorcery', 'https://img.scryfall.com/cards/large/front/9/0/9089c86d-c29a-45f3-b826-8cdb81cda990.jpg?1573509345'),
('Wolfkin Bond', 5, 'common', 'enchantment', 'https://img.scryfall.com/cards/large/front/7/4/749e6f1e-5e1f-4b60-a69a-b4ce89628ed4.jpg?1573514861'),
('Fellwar Stone', 2, 'uncommon', 'artifact', 'https://img.scryfall.com/cards/large/front/2/7/2716dacb-4fb7-4fa8-869d-22af82920564.jpg?1562590137'),
('Fiery Temper', 3, 'common', 'instant', 'https://img.scryfall.com/cards/large/front/6/1/61caf82d-e077-4931-a6ad-09fa7f04b36f.jpg?1576384730'),
('Gift of Growth', 2, 'common', 'instant', 'https://img.scryfall.com/cards/large/front/7/a/7a3f8878-5928-47ec-bb31-f4ee24ad982b.jpg?1562738151'),
('Curse of Wizardry', 4, 'rare', 'enchantment', 'https://img.scryfall.com/cards/large/front/d/0/d0f1c170-03d1-42a7-91e4-0ac537af1328.jpg?1562448784'),
('Sorin, Vengeful Bloodlord', 4, 'rare', 'planeswalker', 'https://img.scryfall.com/cards/large/front/2/a/2aadad8a-33e2-4ea3-b923-0fa41f5a92e7.jpg?1570828508'),
('Rootborn Defenses', 3, 'common', 'instant', 'https://img.scryfall.com/cards/large/front/e/c/ecfcf55c-44d8-4585-9722-e91993e41888.jpg?1568003909'),
('Pavel Maliki', 6, 'uncommon', 'creature', 'https://img.scryfall.com/cards/large/front/c/6/c6627e4c-dc84-4ea0-8f69-dea92f55c943.jpg?1562936934'),
('Shell of the Last Kappa', 3, 'rare', 'artifact', 'https://img.scryfall.com/cards/large/front/4/d/4d80f3e7-c3f0-462f-8ae9-8b27a7c15fcd.jpg?1562759886'),
('Three Tragedies', 5, 'uncommon', 'sorcery', 'https://img.scryfall.com/cards/large/front/4/2/42acaa44-15d5-4760-9aa8-b44eda9ed98a.jpg?1562876677'),
('Warleader''s Helix', 4, 'rare', 'instant', 'https://img.scryfall.com/cards/large/front/f/c/fcc1dd23-90fa-4aa4-b0a9-7a92991ad7ec.jpg?1562640152'),
('Bloodstained Mire', 0, 'rare', 'land', 'https://img.scryfall.com/cards/large/front/6/8/68c72226-6f52-4322-8b14-18737293dfa0.jpg?1562919681'),
('Molimo, Maro-Sorcerer', 7, 'rare', 'creature', 'https://img.scryfall.com/cards/large/front/6/9/69072d65-6d1d-48d1-aca0-4273722be79a.jpg?1562483336'),
('Annex', 4, 'uncommon', 'enchantment', 'https://img.scryfall.com/cards/large/front/b/0/b0df72c6-4f54-43ec-a4e0-5733003f4fd7.jpg?1562740318'),
('Notion Rain', 3, 'common', 'sorcery', 'https://img.scryfall.com/cards/large/front/f/4/f4db287e-34c1-459b-882d-3db58f13eade.jpg?1572893773'),
('Kolaghan, the Storm''s Fury', 5, 'rare', 'creature', 'https://img.scryfall.com/cards/large/front/8/5/85b6ec91-0ecc-431c-bf85-220c615e0a80.jpg?1562615351'),
('Virtuous Charge', 3, 'common', 'sorcery', 'https://img.scryfall.com/cards/large/front/7/2/72ad4c79-a85d-4fc6-95ab-5a6d6d667579.jpg?1562257014'),
('Research Assistant', 2, 'common', 'creature', 'https://img.scryfall.com/cards/large/front/4/a/4ac8a7c0-d935-4a60-ac32-dde73f5c75da.jpg?1562786540'),
('Cancel', 3, 'common', 'instant', 'https://img.scryfall.com/cards/large/front/4/7/479f56c2-8256-4325-909a-bf460505dbc5.jpg?1562703421'),
('Flowstone Blade', 1, 'common', 'enchantment', 'https://img.scryfall.com/cards/large/front/0/8/08ffbdce-bf74-4366-a4c5-422e3d5c92b4.jpg?1562864455'),
('Angrath, Minotaur Pirate', 6, 'mythic rare', 'planeswalker', 'https://img.scryfall.com/cards/large/front/f/1/f17103dd-f31b-4f6e-b2ea-4ea91815bdd6.jpg?1555041190'),
('Chandra, Awakened Inferno', 6, 'mythic rare', 'planeswalker', 'https://img.scryfall.com/cards/large/front/4/9/49d2a680-4f3b-4bfa-b77b-d2dfaced9f23.jpg?1563899095'),
('Ajani Unyielding', 6, 'mythic rare', 'planeswalker', 'https://img.scryfall.com/cards/large/front/2/3/23b82ee9-2ac6-4b81-8c64-dd4f47c2d8cb.jpg?1576382099'),
('Jace, the Living Guildpact', 4, 'mythic rare', 'planeswalker', 'https://img.scryfall.com/cards/large/front/9/9/99713bb4-186f-42b6-aa66-e94ec8858e6a.jpg?1562791409'),
('Nissa, Genesis Mage', 7, 'mythic rare', 'planeswalker', 'https://img.scryfall.com/cards/large/front/2/9/2923c85a-4022-4cda-bcbb-bb000137f64f.jpg?1562793463'),
('Akoum Refuge', 0, 'uncommon', 'land', 'https://img.scryfall.com/cards/large/front/1/a/1a30dc5e-9aae-4aea-a2eb-4444a0fe44e3.jpg?1573517610'),
('Arcane Sanctum', 0, 'uncommon', 'land', 'https://img.scryfall.com/cards/large/front/e/d/ed6aced0-6fa7-4881-bc90-f6003be5b05c.jpg?1573517633'),
('Arctic Flats', 0, 'uncommon', 'land', 'https://img.scryfall.com/cards/large/front/6/0/609b15f6-e65b-46d6-95e8-dc39f25d7efa.jpg?1562183944'),
('Botanical Sanctum', 0, 'rare', 'land', 'https://img.scryfall.com/cards/large/front/8/7/8744471b-a528-47d9-84d0-4526273f55e9.jpg?1576383517'),
('Cinder Marsh', 0, 'uncommon', 'land', 'https://img.scryfall.com/cards/large/front/8/c/8c6dc9af-ea7e-41f8-8c1e-22c588312053.jpg?1562430773'),
('Lunarch Mantle', 2, 'common', 'enchantment', 'https://img.scryfall.com/cards/large/front/3/6/360f4759-c178-4ac2-b561-c81e13f67740.jpg?1576383935'),
('Misguided Rage', 3, 'common', 'sorcery', 'https://img.scryfall.com/cards/large/front/7/4/74b5e00a-fef0-4711-9112-2fd067321890.jpg?1562530657'),
('Wall of Roots', 2, 'common', 'creature', 'https://img.scryfall.com/cards/large/front/9/9/999f9e72-97ed-430a-8c1c-26a54f8b7a08.jpg?1562927442'),
('Kami of False Hope', 1, 'common', 'creature', 'https://img.scryfall.com/cards/large/front/4/4/44e4f5e6-935e-429f-89b4-4571376f442e.jpg?1562876719'),
('Orcish Oriflamme', 4, 'common', 'enchantment', 'https://img.scryfall.com/cards/large/front/9/b/9b568475-97db-47be-842c-03305b459fb7.jpg?1580014607'),
('Revealing Wind', 3, 'common', 'instant', 'https://img.scryfall.com/cards/large/front/3/6/36bdd624-e412-4ec8-9929-e1f6b4720e82.jpg?1562784679'),
('Timber Gorge', 0, 'common', 'land', 'https://img.scryfall.com/cards/large/front/0/7/07076412-18fe-4e15-bdb5-17111b4a66db.jpg?1562300278'),
('Mogg Flunkies', 2, 'common', 'creature', 'https://img.scryfall.com/cards/large/front/3/6/364f6774-1a71-40be-918e-4a89a6044443.jpg?1562906452'),
('Dawnstrike Paladin', 5, 'common', 'creature', 'https://img.scryfall.com/cards/large/front/5/4/549ca818-f7bf-47a8-9005-18ddabd3c360.jpg?1562872184'),
('Sorin''s Thirst', 2, 'common', 'instant', 'https://img.scryfall.com/cards/large/front/c/0/c0dacbb2-21e1-4220-bf43-75a0729cdc60.jpg?1563900396'),
('Hot Springs', 2, 'rare', 'enchantment', 'https://img.scryfall.com/cards/large/front/1/d/1d4fe072-81a7-424e-8d21-aaca010d5b1d.jpg?1562900462'),
('Ivory Cup', 1, 'uncommon', 'artifact', 'https://img.scryfall.com/cards/large/front/7/6/76aaff1a-6796-4728-bdb5-bcdc79c9b98c.jpg?1559592236'),
('Serra Paladin', 4, 'common', 'creature', 'https://img.scryfall.com/cards/large/front/7/b/7bd25adf-4d97-4229-abdb-1c060036cfbd.jpg?1562587737'),
('Sengir Vampire', 5, 'uncommon', 'creature', 'https://img.scryfall.com/cards/large/front/c/c/cc232770-2cbb-4fff-95d0-3acad5b79ae6.jpg?1562200908'),
('Priest of Yawgmoth', 2, 'common', 'creature', 'https://img.scryfall.com/cards/large/front/c/9/c9fd4054-42fc-4f95-a6f7-369a5da43dd5.jpg?1562937643'),
('Tolarian Drake', 3, 'common', 'creature', 'https://img.scryfall.com/cards/large/front/e/0/e04bba8a-48ee-4981-adc2-4f82c0f2c1bd.jpg?1562803819'),
('Cinder Hellion', 5, 'common', 'creature', 'https://img.scryfall.com/cards/large/front/5/a/5a069118-42e4-40e3-a2ba-593ac89b9064.jpg?1562913292'),
('Pathbreaker Wurm', 6, 'common', 'creature', 'https://img.scryfall.com/cards/large/front/f/e/fe65eded-37ef-4cf0-b55c-390d34aab7b8.jpg?1561894462'),
('Orcish Spy', 1, 'common', 'creature', 'https://img.scryfall.com/cards/large/front/c/d/cd3890d1-563d-4519-ab8c-913031d71918.jpg?1587910969'),
('Hero of the Games', 3, 'common', 'creature', 'https://img.scryfall.com/cards/large/front/c/d/cdb7c7a6-4e9b-4300-a776-b7e7916950c8.jpg?1581480168'),
('Soaring Seacliff', 0, 'common', 'land', 'https://img.scryfall.com/cards/large/front/f/4/f48608ef-8526-49cc-94a9-c1efc6580a9b.jpg?1581708432'),
('Giant Spider', 4, 'common', 'creature', 'https://img.scryfall.com/cards/large/front/5/2/52ea35ce-8aa1-4818-8ad5-7e462452f10e.jpg?1559591789'),
('Grim Tutor', 3, 'rare', 'sorcery', 'https://img.scryfall.com/cards/large/front/0/7/07077952-8002-4010-904b-447294fd5686.jpg?1562896492'),
('Moment of Heroism', 2, 'common', 'instant', 'https://img.scryfall.com/cards/large/front/4/9/49217b63-0604-4351-b6de-add0e3e1dbc9.jpg?1562864980'),
('Mana Crypt', 0, 'mythic rare', 'artifact', 'https://img.scryfall.com/cards/large/front/7/f/7f361097-129b-4154-aef5-bd29c05bd3e9.jpg?1562920678'),
('Invisibility', 2, 'common', 'enchantment', 'https://img.scryfall.com/cards/large/front/1/8/1858ac51-e6a7-48d7-8759-166070ca13d8.jpg?1559591529'),
('Pikemen', 2, 'common', 'creature', 'https://img.scryfall.com/cards/large/front/b/f/bf2f6936-b50c-4907-9b55-ebf8a3fba8f5.jpg?1562940095'),
('Tectonic Edge', 0, 'uncommon', 'land', 'https://img.scryfall.com/cards/large/front/f/d/fdcf5c0f-9d18-406d-a930-c179a781264f.jpg?1562300216'),
('Crippling Chill', 3, 'common', 'instant', 'https://img.scryfall.com/cards/large/front/7/9/79791bd9-aded-48d9-866d-9f7bd6848905.jpg?1561872390'),
('Wild Mongrel', 2, 'common', 'creature', 'https://img.scryfall.com/cards/large/front/b/c/bc7cca9e-6e07-4826-a782-ed114f45d727.jpg?1561896093'),
('Dark Ritual', 1, 'common', 'instant', 'https://img.scryfall.com/cards/large/front/c/8/c8c774f2-110e-476c-a4ff-cc86d31c6ae7.jpg?1562842886'),
('Icefall', 4, 'common', 'sorcery', 'https://img.scryfall.com/cards/large/front/6/c/6cf90fc3-b08b-4261-a194-d6b06fdd59d8.jpg?1562184668'),
('Seal of Removal', 1, 'common', 'enchantment', 'https://img.scryfall.com/cards/large/front/d/e/de4c651d-e739-4a79-8628-5f681b099ca8.jpg?1562767737'),
('Abzan Charm', 3, 'uncommon', 'instant', 'https://img.scryfall.com/cards/large/front/f/c/fc3478d9-1855-4217-914f-29c284aa7559.jpg?1573514920'),
('Adeliz, the Cinder Wind', 3, 'uncommon', 'creature', 'https://img.scryfall.com/cards/large/front/b/3/b3c950e2-a43b-47f8-9ad6-1909ccc7acbf.jpg?1562741514'),
('Aether Vial', 1, 'uncommon', 'artifact', 'https://img.scryfall.com/cards/large/front/7/4/741c479b-5e92-4837-9673-9bc72aa11d26.jpg?1562637557'),
('Ahn-Crop Champion', 4, 'uncommon', 'creature', 'https://img.scryfall.com/cards/large/front/2/d/2ddda94a-4b2d-47b0-8d2c-3ad70a0d5584.jpg?1543676022'),
('Akki Coalflinger', 3, 'uncommon', 'creature', 'https://img.scryfall.com/cards/large/front/2/c/2c7067f4-8578-4e5e-886a-c9b14729c4b6.jpg?1562904064'),
('Akroan Hoplite', 2, 'uncommon', 'creature', 'https://img.scryfall.com/cards/large/front/7/f/7f82800a-2382-432d-ab85-e19c7b40f736.jpg?1573514942'),
('Anathemancer', 3, 'uncommon', 'creature', 'https://img.scryfall.com/cards/large/front/a/b/ab106855-bd85-4c00-b596-c46d34f8cdd0.jpg?1562643508'),
('Ancient Excavation', 4, 'uncommon', 'instant', 'https://img.scryfall.com/cards/large/front/4/4/442f0af0-b745-49f2-9e95-2688403fc995.jpg?1562273826');


CREATE TABLE IF NOT EXISTS card_colors(name varchar(50), color varchar(10), FOREIGN KEY (name) REFERENCES cards(name), PRIMARY KEY (name, color));
INSERT INTO card_colors VALUES ('Air Elemental', 'blue'), ('Ifnir Deadlands', 'black'), ('Icatian Scout', 'white'),
('Nylea, Keen-Eyed', 'green'), ('Bad Moon', 'black'), ('Ancient Tomb', 'colorless'), ('Shinen of Fury''s Fire', 'red'),
('Courier Griffin', 'white'), ('Waking Nightmare', 'black'), ('Willbender', 'blue'), ('Encircling Fissure', 'white'),
('White Ward', 'white'), ('Blue Mana Battery', 'colorless'), ('Thornwind Faeries', 'blue'), ('Sakura-Tribe Elder', 'green'),
('Castle Embereth', 'red'), ('Castle Garenbrig', 'green'), ('Castle Vantress', 'blue'), ('Cathedral of Serra', 'white'),
('Castle Ardenvale', 'white'), ('Castle Locthwain', 'black'), ('Coral Atoll', 'blue'),
('Desert of the Indomitable', 'green'), ('Dormant Volcano', 'red'), ('The Flame of Keld', 'red'),
('Anarchist', 'red'), ('Spire Serpent', 'blue'), ('Infernal Caretaker', 'black'),
('Lys Alana Huntmaster', 'green'), ('Kaervek the Merciless', 'black'), ('Kaervek the Merciless', 'red'),
('Harrow', 'green'), ('Mossfire Egg', 'colorless'), ('Death''s Duet', 'black'), ('Watchwolf', 'green'), ('Watchwolf', 'white'),
('Defeat', 'black'), ('Wolfkin Bond', 'green'), ('Fellwar Stone', 'colorless'), ('Fiery Temper', 'red'),
('Gift of Growth', 'green'), ('Curse of Wizardry', 'black'), ('Sorin, Vengeful Bloodlord', 'white'),
('Sorin, Vengeful Bloodlord', 'black'), ('Rootborn Defenses', 'white'), ('Pavel Maliki', 'black'),
('Pavel Maliki', 'red'), ('Shell of the Last Kappa', 'colorless'), ('Three Tragedies', 'black'), ('Warleader''s Helix', 'red'),
('Warleader''s Helix', 'white'), ('Bloodstained Mire', 'black'), ('Bloodstained Mire', 'red'),
('Molimo, Maro-Sorcerer', 'green'), ('Annex', 'blue'), ('Notion Rain', 'blue'), ('Notion Rain', 'black'),
('Kolaghan, the Storm''s Fury', 'black'), ('Kolaghan, the Storm''s Fury', 'red'), ('Virtuous Charge', 'white'),
('Research Assistant', 'blue'), ('Cancel', 'blue'), ('Flowstone Blade', 'red'), ('Angrath, Minotaur Pirate', 'black'),
('Angrath, Minotaur Pirate', 'red'), ('Chandra, Awakened Inferno', 'red'), ('Ajani Unyielding', 'green'),
('Ajani Unyielding', 'white'), ('Jace, the Living Guildpact', 'blue'), ('Nissa, Genesis Mage', 'green'),
('Akoum Refuge', 'black'), ('Akoum Refuge', 'red'), ('Arcane Sanctum', 'white'), ('Arcane Sanctum', 'blue'),
('Arcane Sanctum', 'black'), ('Arctic Flats', 'green'), ('Arctic Flats', 'white'), ('Botanical Sanctum', 'green'),
('Botanical Sanctum', 'blue'), ('Cinder Marsh', 'black'), ('Cinder Marsh', 'red'), ('Lunarch Mantle', 'white'),
('Misguided Rage', 'red'), ('Wall of Roots', 'green'), ('Kami of False Hope', 'white'), ('Orcish Oriflamme', 'red'),
('Revealing Wind', 'green'), ('Timber Gorge', 'red'), ('Timber Gorge', 'green'), ('Mogg Flunkies', 'red'),
('Dawnstrike Paladin', 'white'), ('Sorin''s Thirst', 'black'), ('Hot Springs', 'green'), ('Ivory Cup', 'colorless'),
('Serra Paladin', 'white'), ('Sengir Vampire', 'black'), ('Priest of Yawgmoth', 'black'), ('Tolarian Drake', 'blue'),
('Cinder Hellion', 'red'), ('Pathbreaker Wurm', 'green'), ('Orcish Spy', 'red'), ('Hero of the Games', 'red'),
('Soaring Seacliff', 'blue'), ('Giant Spider', 'green'), ('Grim Tutor', 'black'), ('Moment of Heroism', 'white'),
('Mana Crypt', 'colorless'), ('Invisibility', 'blue'), ('Pikemen', 'white'), ('Tectonic Edge', 'colorless'),
('Crippling Chill', 'blue'), ('Wild Mongrel', 'green'), ('Dark Ritual', 'black'), ('Icefall', 'red'),
('Seal of Removal', 'blue'), ('Abzan Charm', 'white'), ('Abzan Charm', 'black'), ('Abzan Charm', 'green'),
('Adeliz, the Cinder Wind', 'blue'), ('Adeliz, the Cinder Wind', 'red'), ('Aether Vial', 'colorless'),
('Ahn-Crop Champion', 'green'), ('Ahn-Crop Champion', 'white'), ('Akki Coalflinger', 'red'), ('Akroan Hoplite', 'red'),
('Akroan Hoplite', 'white'), ('Anathemancer', 'black'), ('Anathemancer', 'red'), ('Ancient Excavation', 'blue'),
('Ancient Excavation', 'white');


CREATE TABLE IF NOT EXISTS Decks(deckId varchar(64), deckName varchar(50), numberOfCards int(3) DEFAULT 0, deckPrice float(4, 2) DEFAULT 0.00 , PRIMARY KEY (deckId));

CREATE TABLE IF NOT EXISTS Decks_content(deckId varchar(64), card_name varchar(50), card_quantity Int(1), FOREIGN KEY (deckId) REFERENCES Decks(deckId), FOREIGN KEY (card_name) REFERENCES Cards(name), PRIMARY KEY (deckId, card_name));

CREATE TABLE IF NOT EXISTS Deck_Owners(deckId varchar(64), owner_email varchar(50), FOREIGN KEY (deckId) REFERENCES Decks(deckId), FOREIGN KEY (owner_email) REFERENCES Utilisateur(courriel));

CREATE TABLE IF NOT EXISTS Contenir(cardName varchar(50), quantity integer, FOREIGN KEY (cardName) REFERENCES cards(name));

CREATE TABLE IF NOT EXISTS Catalog(cardName varchar(50), price integer, FOREIGN KEY (cardName) REFERENCES cards(name));

delimiter //
CREATE TRIGGER addedCardInDeck AFTER INSERT ON Decks_content
	FOR EACH ROW
    BEGIN
		UPDATE Decks SET numberOfCards= numberOfCards+1 WHERE deckId = NEW.deckId;
	END;//
delimiter ;

delimiter //
CREATE TRIGGER updateCardInDeck AFTER UPDATE ON Decks_content
	FOR EACH ROW
    BEGIN
		IF NEW.card_quantity > OLD.card_quantity THEN
		UPDATE Decks SET numberOfCards= numberOfCards+1 WHERE deckId = NEW.deckId;
        ELSE
        UPDATE Decks SET numberOfCards= numberOfCards-1 WHERE deckId = NEW.deckId;
        END IF;
	END;//
delimiter ;

delimiter //
CREATE TRIGGER cardInDeckRemoved BEFORE DELETE ON Decks_content
	FOR EACH ROW
        UPDATE Decks SET numberOfCards= numberOfCards-1 WHERE deckId = DELETED.deckId;
delimiter ;
