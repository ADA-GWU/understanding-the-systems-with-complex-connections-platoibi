#!/bin/bash

dir=$(pwd)

osascript <<EOF 
tell application "Terminal"
    do script "python3 \"$dir\"/Server.py"
end tell
EOF
osascript <<EOF 
tell application "Terminal"
    do script "python3 \"$dir\"/Server.py"
end tell
EOF
osascript <<EOF 
tell application "Terminal"
    do script "python3 \"$dir\"/Server.py"
end tell
EOF

osascript <<EOF 
tell application "Terminal"
    do script "python3 \"$dir\"/RequestHandler.py"
end tell
EOF

osascript <<EOF 
tell application "Terminal"
    do script "python3 \"$dir\"/Client.py"
end tell
EOF