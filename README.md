# mreg (match releases expression generator)

## How to use

```
$ git clone https://github.com/Igglybuff/mreg.git
$ cd mreg
```

### Bash script:

The bash script will dump the expression as a single string to STDOUT.

```
$ ./mreg.sh
Bohemian?Rhapsody*,The?House?with?a?Clock?in?its?Walls*,Venom*,Bad?Times?at?the?El?Royale*,Fantastic?Beasts:?The?Crimes?of?Grindelwald*,Assassination?Nation*,The?Grinch*,Halloween*,Spider-Man:?Into?the?Spider-Verse*,First?Man*,Creed?II*,Hunter?Killer*,A?Star?Is?Born*,Life?Itself*,Ralph?Breaks?the?Internet*,Fahrenheit*,The?Predator*,Instant?Family*,The?Nutcracker?and?the?Four?Realms*,Johnny?English*,Strikes?Again*,Overlord*,McQueen*,A?Simple?Favor*,Peppermint*
```

### Python Flask app:

The flask app will run an HTTP server exposing the expression as text for use with `curl`. It doesn't do any caching, so every time you refresh it will hit dvdsreleasedates.com again.

```
$ pip3 install -r requirements.txt
$ python3 server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

The application will be exposed on `0.0.0.0` at port `5000`. Access it by navigating to http://127.0.0.1:5000/ in your web browser.

### Python CLI tool:

```
$ pip3 install -r requirements.txt
$ pip install .
$ mreg --help
Usage: mreg [OPTIONS]

Options:
  -c, --autodlcfg TEXT  The path to your autodl.cfg file.  [default:
                        ~/.autodl/autodl.cfg]
  -f, --filter TEXT     The name of your autodl-irssi filter for movies.
                        [required]
  --help                Show this message and exit.
$ mreg --autodlcfg "/home/rtorrent/.autodl/autodl.cfg" --filter "filter 1080p/720p Movies IPT"
Your filter was updated successfully!
```

You can use environment variables instead of command line options instead if you prefer:

```
export MREG_AUTODLCFG_PATH=/home/rtorrent/.autodl/autodl.cfg
export MREG_FILTER_NAME="filter 1080p/720p Movies IPT"
```

### Docker

`coming soon`
