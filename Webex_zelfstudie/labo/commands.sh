#!/bin/bash
# commands.sh – run full Webex Teams lab sequence

echo "Testing authentication..."
python3 authentication.py
echo

echo "Listing people..."
python3 list-people.py
echo

echo "Listing rooms..."
python3 list-rooms.py
echo

echo "Creating room..."
python3 create-rooms.py
echo

echo "Getting room details..."
python3 get-room-details.py
echo

echo "Listing memberships..."
python3 list-memberships.py
echo

echo "Creating membership..."
python3 create-membership.py
echo

echo "Sending markdown message..."
python3 create-markdown-message.py
echo
