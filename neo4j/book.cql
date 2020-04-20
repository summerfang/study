CREATE (Bart:Reader {name:'Bart Baesens', age:32})
CREATE (Seppe:Reader {name:'Seppe vanden Broucke', age:30})
CREATE (Wilfried:Reader {name:'Wilfried Lemahieu', age:40})
CREATE (Marc:Reader {name:'Marc Markus', age:25})
CREATE (Jenny:Reader {name:'Jenny Jennifers', age:26})
CREATE (Anne:Reader {name:'Anne HatsAway', age:22})
CREATE (Mike:Reader {name:'Mike Smith', age:18})
CREATE (Robert:Reader {name:'Robert Bertoli', age:49})
CREATE (Elvis:Reader {name:'Elvis Presley', age:76})
CREATE (Sandra:Reader {name:'Sandra Mara', age:12})
CREATE (Fantasy:Genre {name:'fantasy'})
CREATE (Education:Genre {name:'education'})
CREATE (Thriller:Genre {name:'thriller'})
CREATE (Humor:Genre {name:'humor'})
CREATE (Romance:Genre {name:'romance'})
CREATE (Detective:Genre {name:'detective'})
CREATE (b01:Book {title:'My First Book'})
CREATE (b02:Book {title:'A Thriller Unleashed'})
CREATE (b03:Book {title:'Database Management'})
CREATE (b04:Book {title:'Laughs, Jokes, and More Jokes'})
CREATE (b05:Book {title:'Where are my Keys?'})
CREATE (b06:Book {title:'A Kiss too Far'})
CREATE (b07:Book {title:'A Wizardly Story'})
CREATE (b08:Book {title:'A Wizardly Story 2: Order of the SQL'})
CREATE (b09:Book {title:'Laughing and Learning'})
CREATE (b10:Book {title:'A Murder in Fantasyville'})
CREATE (b11:Book {title:'Without you I am Nothing'})
CREATE (b12:Book {title:'How to be Romantic: a Guide'})
CREATE (b13:Book {title:'Why Boring is Good'})
CREATE (b14:Book {title:'An Unsolved Problem for Detective
Whiskers'})
CREATE (b15:Book {title:'Mathematics for the Rest of Us'})
CREATE (b16:Book {title:'The Final Book I ever Wrote'})
CREATE (b17:Book {title:'Who Says Love is Outdated?'})
CREATE (b18:Book {title:'A Chainsaw Massacre'})
CREATE
(b01)-[:IS_GENRE]->(Education),
(b02)-[:IS_GENRE]->(Thriller),
(b03)-[:IS_GENRE]->(Education),
(b04)-[:IS_GENRE]->(Humor),
(b05)-[:IS_GENRE]->(Humor), (b05)-[:IS_GENRE]->(Detective),
(b06)-[:IS_GENRE]->(Humor), (b06)-[:IS_GENRE]->(Romance),
(b06)-[:IS_GENRE]->(Thriller),
(b07)-[:IS_GENRE]->(Fantasy),
(b08)-[:IS_GENRE]->(Fantasy), (b08)-[:IS_GENRE]->
(Education),
(b09)-[:IS_GENRE]->(Humor), (b09)-[:IS_GENRE]->(Education),
(b10)-[:IS_GENRE]->(Detective), (b10)-[:IS_GENRE]->(Thriller),
(b10)-[:IS_GENRE]->(Fantasy),
(b11)-[:IS_GENRE]->(Humor), (b11)-[:IS_GENRE]->(Romance),
(b12)-[:IS_GENRE]->(Education), (b12)-[:IS_GENRE]->
(Romance),
(b13)-[:IS_GENRE]->(Humor), (b13)-[:IS_GENRE]->(Education),
(b14)-[:IS_GENRE]->(Humor), (b14)-[:IS_GENRE]->(Detective),
(b15)-[:IS_GENRE]->(Education),
(b16)-[:IS_GENRE]->(Romance),
(b17)-[:IS_GENRE]->(Romance), (b17)-[:IS_GENRE]->(Humor),
(b18)-[:IS_GENRE]->(Thriller)
CREATE
(Bart)-[:FRIEND_OF]->(Seppe),
(Bart)-[:FRIEND_OF]->(Wilfried),
(Bart)-[:FRIEND_OF]->(Jenny),
(Bart)-[:FRIEND_OF]->(Mike),
(Seppe)-[:FRIEND_OF]->(Wilfried),
(Seppe)-[:FRIEND_OF]->(Marc),
(Seppe)-[:FRIEND_OF]->(Robert),
(Seppe)-[:FRIEND_OF]->(Elvis),
(Wilfried)-[:FRIEND_OF]->(Anne),
(Wilfried)-[:FRIEND_OF]->(Mike),
(Marc)-[:FRIEND_OF]->(Mike),
(Jenny)-[:FRIEND_OF]->(Anne),
(Jenny)-[:FRIEND_OF]->(Sandra),
(Anne)-[:FRIEND_OF]->(Mike),
(Anne)-[:FRIEND_OF]->(Elvis),
(Mike)-[:FRIEND_OF]->(Elvis),
(Robert)-[:FRIEND_OF]->(Elvis),
(Robert)-[:FRIEND_OF]->(Sandra)
CREATE
(Bart)-[:LIKES]->(b01), (Bart)-[:LIKES]->(b03), (Bart)-[:LIKES]-
>(b05), (Bart)-[:LIKES]->(b06),
(Seppe)-[:LIKES]->(b01), (Seppe)-[:LIKES]->(b02), (Seppe)-
[:LIKES]->(b03), (Seppe)-[:LIKES]->(b07),
(Wilfried)-[:LIKES]->(b01), (Wilfried)-[:LIKES]->(b05),
(Wilfried)-[:LIKES]->(b06), (Wilfried)-[:LIKES]->(b10),
(Marc)-[:LIKES]->(b03), (Marc)-[:LIKES]->(b11), (Marc)-
[:LIKES]->(b13), (Marc)-[:LIKES]->(b15),
(Jenny)-[:LIKES]->(b08), (Jenny)-[:LIKES]->(b09), (Jenny)-
[:LIKES]->(b12), (Jenny)-[:LIKES]->(b14),
(Anne)-[:LIKES]->(b14), (Anne)-[:LIKES]->(b15), (Anne)-
[:LIKES]->(b17), (Anne)-[:LIKES]->(b18),
(Mike)-[:LIKES]->(b05), (Mike)-[:LIKES]->(b07), (Mike)-
[:LIKES]->(b11), (Mike)-[:LIKES]->(b17),
(Robert)-[:LIKES]->(b04), (Robert)-[:LIKES]->(b10), (Robert)-
[:LIKES]->(b12), (Robert)-[:LIKES]->(b13),
(Elvis)-[:LIKES]->(b03), (Elvis)-[:LIKES]->(b06), (Elvis)-
[:LIKES]->(b14), (Elvis)-[:LIKES]->(b16),
(Sandra)-[:LIKES]->(b03), (Sandra)-[:LIKES]->(b05), (Sandra)-
[:LIKES]->(b07), (Sandra)-[:LIKES]->(b09)