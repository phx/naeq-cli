# NAEQ-cli

This is a personal experiment that I have made public to anyone else who is interested in cryptography as well as high strangeness and other weird topics.

Instead of requiring MongoDB or soemthing like that, I have implemented the use of a personal dictionary as a JSON file for saving personal queries.

**Dependencies:** `python3+`

---

## Usage
- `git clone https://github.com/phx/naeq-cli`
- `cd naeq-cli`
- `./naeq.py [WORD/NAME/PHRASE/INTEGER]` or `echo [WORD/NAME/PHRASE/INTEGER] | ./naeq.py`

### Command line flags:

| Parameter | Functionality |
| :---  | :--- |
| `-b`  | *Backup* - backs up your personal database |
| `-d`  | *Delete* - deletes the result from your personal database |
| `-nn` | *No NAEQ* - suppresses NAEQ output and only returns personal database results | 
| `-np` | *No Personal* - suppresses personal database output and only returns NAEQ results |
| `-s`  | *Save* - saves the resulting query in your personal database. |
| `-ss` | *Save Silent* - saves resulting personal query and suppresses NAEQ output |
| `-v`  | *Value* - queries all terms associated with a specific numeric value |
| `-q`  | *Quiet* - suppress all output except for the CEQ value for the query |

Upon running `./naeq.py -s [QUERY]` or `./naeq.py -ss` for the first time, a personal dictionary named `dictionary.json` will be created in the same directory.

Running these commands will save the query into `dictionary.json`.

You can run `./naeq.py -d [QUERY]` do remove the query from `dictionary.json`.

When you start to establish a pretty good size dictionary and want to make sure it stays intact, you may want to periodically back it up using `./naeq.py -b`, which will copy
`dictionary.json` to `dictionary.bak`.

---

Special thanks to [Wren Collier](https://liminalroom.com/) and [Alynne Keith](https://offalynne.neocities.org/), who developed [https://www.naeq.io](https://www.naeq.io/)
and made their project available on [GitHub](https://github.com/misterapol/naeq).  My [`liber_al.json`](liber_al.json) uses the NAEQ dictionary converted straight from their own
[`data.js`](https://raw.githubusercontent.com/misterapol/naeq/master/data.js), which was a *huge* help in the creation of this command line project, as most of the real
work had already been done.

These projects could not have been accomplished without the amazing and interesting work of Allen Greenfield and his book, *Secret Cipher of the UFOnauts*, as well as all
of the amazing and "crazy" individuals who have investigated and worked with this cipher for over a century.

---

Also a special shout out to [Greg and Dana Newkirk](https://weirdhq.com/) and their amazing series [Hellier](https://www.hellier.tv/), where I was first introduced me to this material.

I also could have never done this without the insight of my brother in weird investigations, Devin, who first introduced me to the *Hellier* series.
