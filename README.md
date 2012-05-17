# Software Module Loader (sml)

The intend of this software is to replace modules (<http://modules.sf.net>), which is IMO a good piece of software but has some drawbacks:

+ It's written in a mix of C / TCL (newer version is only TCL) -- this is a pure personal opinion, so just skip this point if you're not with me, that's ok
+ The configuration file is too large and too distributed

# Usage

Warning #1: This is pure alpha release and may eat your babies.
Warning #2: Read warning #1, file an issue report when something goes wrong, but don't blame me

1. Copy sml.json.example to ~/.sml.json an edit it, syntax is pure JSON
2. Copy sml.sh and sml.py to a location where you can execute from, e.g. /usr/local/bin
3. Put `alias sml="source sml.sh"` into your .{bash,zsh}rc or wherever it fits
4. Run sml

# Changelog

### 0.1, 2012-05-17

- Support loading and unloading modules
- Installation yet by hand
